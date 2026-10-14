# OVRTX still batches: local Blender 5.1 observations

Prefer the existing geometry and saved camera/pose states. Camera-only shots need
only a camera change; assembly steps also change part transforms or visibility.
Do not rebuild geometry, reload the file, or restart the worker between healthy
renders. Give inactive shot scenes fake users before saving so they survive reload.

In one tested twelve-shot batch, viewport drawing and final rendering interfered:
Blender's main thread waited on its GPU drawing mutex while a render job waited
on a Python semaphore. `INVOKE_DEFAULT` did not fix it. After normal recovery,
changing VIEW_3D areas to CONSOLE and using sequential blocking
`bpy.ops.render.render(write_still=True)` completed the remaining nine OVRTX
shots; the first took about 20 seconds including tool overhead. Keep this as a
version-specific fallback, not proof of a fixed underlying add-on defect. Capture
the prior UI types if they should be restored after the batch.

A tool call once remained pending after its PNG had been saved. Before calling a
render stalled, check the expected file's freshness/completeness and the current
render status when responsive. An old file is not evidence of a new render; GPU
activity alone is not progress, either. Avoid queuing duplicate render requests.
Use output/log progress for bounded waits and preserve completed frames. Process
or service repair needs appropriate task authority; do not blindly kill workers.

A later camera-only edit produced a fresh PNG with the old view. A fresh scene
copy using the same objects and the updated camera refreshed the rendered pixels.
Use this only when the image is demonstrably stale; a new timestamp or changed
camera transform is not enough to verify that the intended view rendered.

After one geometry import, `CreateSimulation ALREADY_EXISTS` persisted through
a scene copy. Saving the task-owned .blend and reopening it with `load_ui=False,
use_scripts=False`, then selecting the scene and rendering in a separate MCP call,
resolved that collision without service changes. Immediately after reopening,
`bpy.context.window` may be None; use an available window from
`bpy.context.window_manager.windows` in the subsequent call. Disable rendered
viewports again before retrying. This is a bounded local recovery, not a reason
to reload between healthy frames. If it fails, preserve outputs and report the
blocker rather than repeating unchanged retries.

The exposed `simulation_reset_token` controls the OVPhysX demo, not an OVRTX
render-session reset. Do not increment it to repair stale imagery or collisions.

MCP safe mode in this installation rejects `time` imports, computed `getattr`,
lambdas, and timers/handlers. Use straightforward `bpy` calls and sorted name lists;
measure elapsed time outside Blender. Do not weaken safe mode for a render batch.

## Render-only physics opinions

In the inspected add-on, both `APPLY` and `REMOVE` physics schema opinions trigger
USD override authoring. Setting every render-only copy to `REMOVE` is therefore
not a cheap way to disable simulation. For ordinary exported mesh copies with no
inherited USD physics schemas, use `INHERIT` on rigid-body/collision opinions and
the render scene's physics opinion; preserve `APPLY` on the prepared simulation
source. If referenced USD already contains physics, `INHERIT` will not remove it:
inspect that path and use explicit removal where needed.

A local 548-part replay benchmark dropped from roughly 23 to 18–20 seconds per
frame after neutralizing render-copy opinions and clearing copy-only physics
metadata. Treat this as a measured combined optimization, not a universal timing
promise. Benchmark a warm frame and check its pixels before committing the batch.
