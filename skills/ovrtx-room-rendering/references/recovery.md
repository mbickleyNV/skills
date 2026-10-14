# OVRTX bounded recovery

Classify the error before acting. This reference is not a routine render checklist.

Use the public SDK/OVStream backend named in `AGENTS.md` and current `HANDOFF.md`.
Archived SIL packages, bridge ports and custom runtime pins are not recovery paths.

## Dead MCP connection

An expired tool call or terminated client does not prove Blender stopped its
script. Before replaying work, check the expected frame outputs and establish
completion through a reconnected read-only scene/status call. Outputs alone may
represent only the first shots of an in-flight batch. Do not submit another
render or scene mutation while the original execution may still be running.
Keep completed images that pass camera, frame, dimensions and visual checks;
resume only missing captures. Reduce subsequent per-call batch size to fit the
observed client deadline. Do not turn one observed timeout into a universal
renderer limit.

A host batch client can terminate while Blender continues its current shot.
Before retrying, verify that Blender is idle, then check the staged capture's
camera, frame, resolution, image, and semantic files. Promote a complete,
verified capture to its canonical gallery path with the batch helper; rerender
only missing or incomplete shots. For a client deadline shorter than a room
batch, run one shot per bounded command while keeping the same live service.

"Session terminated" alone is not a renderer or scene failure. Read `HANDOFF.md`
and check the managed MCP service state. If it was intentionally stopped and the
current user has authorized Blender restoration or authoring, start that existing
service with `systemctl --user start blender-gym-mcp.service` and verify it is
active. An old app tool proxy may still report
`Transport closed`; use a fresh session through the project's existing
authenticated, TLS-verified MCP client. The project's
`blender/tools/render_primary_batch.py` shows the client URL, CA and token lookup;
reuse that configuration without printing the token. This is the same managed service, not a
second daemon or a headless bypass. Keep safe mode and credentials intact. Make
a read-only live-scene check before opening the canonical scene or replaying an
import; check active jobs and preserve unsaved work. A failed partial import may
be discarded by reopening the saved scene only when no other unsaved authoring
would be lost. If the idle session ended, open only the canonical scene and wait
for that call to finish before the next call.

Preserve live unsaved authoring. Do not reopen a saved file to repair transport.
`bpy.data.is_dirty == False` alone does not establish that scripted edits were
saved; use the known authoring/save history and project handoff. A request to
render or reconnect is not authorization to save or publish.

## Stale Blender export state

Symptoms include:

- `final_render: unsupported affected Blender object session_uid ...`
- a camera, frame, topology, or engine change immediately preceding the failure
- a completed capture retains old grain/material appearance although stored UVs,
  render UV layer, and material image links show the intended update

Recovery:

1. Preserve intended authoring changes and restore durable camera/render settings.
   Follow the project's manual save/publish authorization before saving anything.
   If this recovery would discard live work and saving is not authorized, stop
   before reopening and explain the required save/reopen action. Do not save
   diagnostic poses, fallback engines, or preview settings over accepted state.
2. Reopen that scene with `bpy.ops.wm.open_mainfile(...)` in a separate MCP call.
3. End the open call; inspect in the next call, then run one low-resolution proof
   using the intended engine, frame and camera.
4. Continue only after that proof succeeds.

Do not restart the worker for this error before trying the clean reopen. Do not
save transient fallback-engine or preview settings over the main scene.

## Stale renderer simulation

Symptoms include `CreateSimulation ... ALREADY_EXISTS` for an OVRTX simulation.
This is renderer lifecycle state, not evidence of bad geometry or materials.

After one clean scene reopen reproduces it, stop repeated render/reset attempts.
With user authorization and sole live-Blender ownership, inspect the installed
add-on's runtime diagnostics and task-owned public SDK worker. Use its supported
`Restart OVRTX Worker` action only for confirmed stale renderer state. Verify
runtime preflight and one low-resolution proof before batching. Do not start a
SIL service or use a physics reset as renderer recovery.

For this remodel, the user's 2026-09-24 instruction authorizes that supported
restart without another question when the scene is saved, no render is active,
and one batch owns Blender. The primary batch takes an exclusive process lock,
checks the saved scene and idle render state, attempts one worker restart on a
known stale-worker error, and verifies a small proof before resuming. If the
proof fails or the same error repeats, stop instead of cycling worker restarts.

## Compound semantic labels after reparenting

An unknown semantic class such as `kitchen/cabinet-fronts, kitchen/cabinet-hardware`
can be one comma-joined inherited label, not two missing registry entries.
Inspect the failed capture's native ID map and the affected objects' parent chains.
OVRTX can union semantic labels through ancestry when labeled hardware is parented
beneath a differently labeled front mesh. Use an unlabeled component Empty with
front and mount as siblings and labels on geometry leaves. Preserve world placement
and local style bindings. Audit the affected ancestry, refresh the live scene with
owners/mounts included, then retry only failed captures. A restart alone cannot
repair this hierarchy error. Do not submit repair mutations during an active capture.

## Export/material failures

First inspect only the affected object's live/evaluated assignment. An inactive
binding or old appearance despite correct live materials can be stale incremental
export state: use the bounded saved-scene refresh above, not repeated material
edits. Incorrect assignments, duplicate identities, missing markers or unsupported
shaders need scoped source/material repair, not a worker restart.
Preserve hidden dependency markers as viewport-evaluable and use
`hide_render` rather than viewport hiding where the project contract requires it.

## Stop conditions

Perform at most one clean reopen and one authorized worker recovery for the same
failure. If the identical error persists, preserve logs and outputs, report the
exact blocker, and do not substitute another renderer without explicit approval.

## After add-on build/install only

Verify the relevant installed files against the tested package once per install,
not before each render. Package the active add-on with its public
`scripts/build_public_sdk_packages.py` builder and use Blender's normal extension
installer. Retain the verified public SDK runtime unless its dependencies changed;
check the add-on preflight after installation. Do not use archived research/SIL
materializers or custom runtime pins.
A successful packaging receipt alone is not proof the installed fix is present.
Keep runtime integrity checks. Run focused feature tests and one live smoke check
after a renderer change; routine material/camera edits need neither a rebuild
nor the full add-on test suite. Broader tests belong to release/integration work.
