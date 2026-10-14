# Specialized OVRTX captures

Read only the section relevant to the requested diagnostic or capture. The active project contract overrides older backend examples.


This project uses the installed public SDK/OVStream add-on. Read the active
backend contract in `AGENTS.md` and the current top of `HANDOFF.md`; archived
research-build/SIL notes are evidence, never install or recovery instructions.

Default and saved-variation room and whole-house batches MUST use `blender/tools/render_timeline_batch.py`
or the supervised `blender/tools/start_primary_render_service.py` launcher, which
routes to that timeline runner. This is the validated session-reusing path.
`render_primary_batch.py` is the standalone still fallback;
do not use it for ordinary whole-house refreshes. The older
`render_ovrtx_camera_batch.py` projection restrictions do not describe the native
timeline workflow. Preserve the current `--refresh-after` checkpoint when
resuming so completed RGB/semantic bundles are kept. Verify actual promoted
images and camera-retarget receipts, not merely a live process or simulation ID.
The supervised timeline service does not auto-restart after failure: a lost
client can leave a native timeline active; inspect Blender before resuming.

For live draft captures, refresh the renderer once after source or appearance
edits. Repeat captures of the unchanged draft should render directly in the same
view layer. `room_looks.refresh_renderer()` now admits actual deferred native edits
against the add-on's accepted generation; it retains `ViewLayer` and does not force
World dirty or create a fresh study cache. Keep the
native timeline for camera batches. An on-demand scene-inspector call does not
refresh that cache.

Monitor a live capture without queuing Blender work by using
`blender/tools/inspect_native_render.py --output <exact-frame.jpg> --log
<pinned-worker.log> --started-after <launch-epoch> --camera <camera-name>
--log-offset <worker-log-byte-size-before-launch>`.
It verifies the native receipt, camera, current file and hash, and reports native
failure events only after the pinned launch offset. Pin the actual
worker log before launch; do not discover it from filename recency. A `waiting`
result, idle GPU, or MCP status timeout does not establish deadlock: cold house
preparation has taken roughly four minutes while warm captures take about a
minute. Do not repeatedly queue status requests during preparation. Before any
recovery, check exact native completion again and preserve the unpublished draft;
a transport timeout alone does not authorize restarting Blender. Use existing
bounded recovery guidance only after independent evidence of an actual failure.

For committed variations or shared placement changes, read
`skills/room-variations/SKILL.md`. The batch renders Default at requested times
and variants only in morning, verifies both style and shared-placement revisions,
and restores the live Default. Kitchen committed looks and the saved laundry
Matcha Orange study have explicit recall adapters. Queue variations behind an
active Default service using `--variants-only --wait-for-batch` on the supervised
launcher, with an explicit canonical `--scene` when local work is unpublished. Refresh only the requested views and report stale
views accurately; do not expand a two-view inheritance check into a full room batch.

For camera framing or reframing, route first through the project
`camera-composition` skill, then return here for OVRTX proof and final capture.

Use the canonical scene from `HANDOFF.md` and `OVRTX_EXAMPLE`. Preserve unrelated
geometry, materials, lighting and cameras. Reuse the existing capture helper
`blender/tools/render_feedback_mcp.py` rather than rewriting render setup.

For interactive shots, prefer `start_feedback_shot(...)`. It starts the native
session-reusing timeline and returns promptly; save its returned ticket path.
The ticket is also written beside the staging image before launch, so a lost
control reply can be recovered without rerendering. Wait on the exact native
`.sequence.json` file outside Blender, then call `complete_feedback_shot(ticket)`
to verify/copy the existing JPEG and restore the previous camera/render settings.
It preserves the saved scene's exposure, view transform and white balance. Final
outputs default to the room's `diagnostic/` folder; use `primary/` only for an
already approved primary view. The blocking `render_feedback_shot` remains for
callers that explicitly require a synchronous HDR still.

Optimize time to the first useful image. Reuse the saved scene and requested
camera; do not rebuild CAD for appearance/camera-only work. For a changed look,
inspect one representative cheap preview, then capture the requested views.
Preview each newly composed camera, but do not require a preview per unchanged
camera in a batch. The helper restores saved resolution/aspect/sample defaults;
explicit arguments override them, and previews preserve aspect at reduced size.
Keep transport depth while reducing preview resolution/samples.

Routine imports apply the glass policy only to imported objects. Run
`blender/materials/glass_visibility.py` then
`apply_glass_shadow_policy(objects=affected_objects)` after direct glass edits.
This uses assigned materials, not names such as "sea-glass tile", and preserves
opaque frames. Every LuaCAD-to-Blender import path that can create or replace
glass must invoke this policy after material reconciliation. The saved
`Object.visible_shadow=False` becomes OVRTX `primvars:doNotCastShadows`; assigning
a transparent material alone is insufficient. No recurring whole-house audit, USD traversal, repeated save/reopen
proof, shader inventory or add-on suite is needed for ordinary room iterations.
Reserve those checks for an explicit audit, changed exporter/runtime, or evidence
of wrong output. Keep scoped material/normal import gates and inspect the images.

For thin shower panes, use a dedicated transmissive Principled material when
other objects share the architectural glass material. The installed add-on's
opt-in `material['ovrtx_thin_walled'] = True` authors OpenPBR
`geometry_thin_walled`; verify that exported input once when introducing the
material. It is separate from `visible_shadow`, and it may leave a dark object
behind glass unchanged. To diagnose that symptom, compare the same camera with
glass present and temporarily hidden, restore the panes, and inspect the actual
captures before changing cabinet normals, lighting, or trace depth. Keep a
thin-glass visual result distinct from proof that the exporter wrote the flag.

Set frame first, explicitly assign the camera, update the view layer, then render.
Capture cameras serially in the same live scene. Size each execution to fit the
shortest client, tool, or wrapper deadline, not just the backend timeout. When
that budget is uncertain or a batch has outlived its caller, use one camera per
call; separate calls can reuse the open Blender scene without reopening it.
Standalone final-render calls may still create and tear down an OVRTX worker
session for each image. Do not infer persistent renderer reuse from a persistent
Blender process.
Record each shot's native elapsed time rather
than treating batch wall time as one render. Native accumulation completion is sufficient; do not
sleep an additional fixed interval afterward. Use each camera data-block’s `ovrtx_exposure` settings (or explicit scene
defaults) for native OVRTX auto exposure. Brightness target is direct white-point
scale: lower is brighter. Never restore `ovrtx_exposure_ev` or use the retired
Blender median meter. The add-on enforces Blender exposure0/gamma1/curvesoff;
Filmic and per-shot white balance are explicit display choices. Save JPG
with the display transform applied once. If Render Result is absent after a
successful native capture, use the helper's exact frame-specific display PNG;
do not rerender solely to recover the transient image datablock.

Before a swatch comparison, read the active scene white-balance value and use
the same value in both captures. Blender's `view_settings.white_balance_temperature`
is scene-wide in the saved `.blend`; a request phrased as a camera white point
can therefore affect other saved views unless the capture path has an explicit
per-shot override. Record that scope when saving a new value.

For a targeted explicit camera-list capture outside routine room/variation
batches, `blender/tools/render_ovrtx_camera_batch.py` is the Blender-side helper.
Normal batches still use the timeline runner and service launcher above. The add-on owns the
persistent OVRTX session and ordered render results; this project-side `bpy`
helper owns camera names, frames, output paths and formats.
Group only cameras with identical projection, lens, shift and clipping settings.

For batch performance work, inspect `render_timeline_batch.py` native sequence
receipts: `total_ms`, `native_timings`, and `runtime.session_reuse`. Compare
worker PID, runtime epoch, native stage ID and load count across scene changes.
Recall, export and population can dominate wall time even when native capture
is fast. Do not add nested timers together or attribute their difference to USD
export without an export-specific measurement. Preserve image and semantic
verification while investigating performance.

Inspect the actual image. A successful call cannot rule out stale geometry or a
wrong camera. Only when evidence indicates stale state, save/reopen in separate
calls. Read [recovery](references/recovery.md) only on failure; don't preemptively
restart workers or change engines. Keep the installed public SDK/OVStream backend.

Keep primary JPGs in `renders/<room>/primary/` and diagnostics in `diagnostic/`;
temporary PNG/EXR and proofs belong in `scratch/`. A render request does not
authorize saving the scene: follow `AGENTS.md` and the manual OVStorage
save/publish contract. Report which
shots were refreshed; do not imply old detail images or contact sheets are new.
Build sheets only when useful/requested, from the intended current JPGs.
If the project render path is outside Blender media staging's allowed root, keep
the project JPG as source of truth, checksum-copy the verified file into a stable
task folder under the Blender output root, and stage that exact copy. Do not
rerender solely to obtain an attachable path.

## Saved cutaway cameras

Read [near-plane framing](references/near-plane-framing.md) for cabinet-centered
views through a wall. Increase the near plane after framing; millimetre clips do
not remove foreground walls. Use native Camera clip_start/clip_end and lens.
Reuse laundry camera66 from house.blend as a worked example. Read its actual
native clip/lens/pose and review aspect; prose values age as the design changes.
Do not reset a saved camera from an older example.

Inspect each final contact-sheet panel; omit failed proofs.

The installed add-on uses the public SDK and OVStream backend. Use its runtime
preflight and diagnostic/recovery path; retain runtime integrity checks. Preview
cost is best reduced via samples and resolution, retaining sufficient transport
depth. Batch scene changes must retain the renderer session; verify reuse from
native capture receipts rather than assuming it from a successful image.

For light/glass A/Bs, unchanged auto-exposure settings do not mean locked exposure.
Use qualitative comparisons unless exposure is actually fixed for both captures;
never infer lux or percentage illumination from auto-exposed review JPGs.
