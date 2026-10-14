---
name: product-turntable
description: Render an explicitly requested studio product turntable from a saved product blend, with linked materials, automatic full-rotation framing and the saved film stack through native OVRTX.
---

# Product turntable

Run only when the user asks for a turntable. Finishing a model or material does
not invoke this workflow. Delegate to `turntable_specialist` when available;
otherwise pass its saved instructions using `docs/specialists/CONTRACT.md`.

Read current HANDOFF, the specialist contract and
[the execution contract](references/execution.md). Use the Blender product
assembly and Blender MCP workflow skills for live work. The canonical studio is
`blender/studios/product-turntable.blend`: reuse it, never regenerate or overwrite
it for a product. It contains a global camera, scaled softbox rig, matte ground
and a local copy of the accepted KC25 film/compositing graph with packed LUT.

Dispatch includes the saved product `.blend`, explicit asset-only collection,
source SHA256, product slug and requested duration/quality. Preserve linked
geometry, UVs, normals and materials. If that accepted asset is missing, route
preparation to `asset_preparer` through `skills/product-asset-preparation/SKILL.md`
first; it can work offline while rendering is busy. Do not improvise an import
inside the live turntable session. Consume its matching asset-ready receipt.
The collection must be static and
self-contained; uncertain dependencies or render/viewport discrepancies stop
preparation for correction. No material substitutions to improve a studio shot.

Before touching live Blender, the coordinator checks other active chat owners,
transfers sole ownership and verifies no render is active. The runner takes the
same lock as house batches, refuses active render services and checks native
jobs in every scene. Busy means defer with the concrete owner/reason; never
cancel an unrelated render without user authorization. No second renderer or
MCP service is launched.

First make a four-angle low-resolution preview with the same studio and film
stack. Inspect actual front/side/rear/top/foot framing, contact shadows, grain,
reflective highlights and seams. If framing or linked appearance is wrong,
fix the scoped setup/source first. Then run the requested sequence once,
collect native hash-bound receipts and encode the MP4. Camera fit covers the
entire orbit, with padding for saved lens effects; no duplicate wrap frame.

Record exact studio/asset/helper hashes, collection, bounds, frames, FPS,
resolution, samples, native completion and inspected images in the product
checkpoint. A valid file is not visual acceptance. Lost replies reuse native
files/checkpoint, never trigger another capture. Release native ownership and
restore the previous scene; never save/publish the house or mutate the product
source. Return the movie, inspected review evidence, limitations and proposed
knowledge/checkpoint changes for coordinator acceptance.

Turntable movies use 50 frames by default. Retain the saved film/color stack, but set Grain Amount, Distortion and Dispersion to zero in the private studio copy. Four-angle previews remain separate. Do not alter an active capture to apply new defaults.

Before the final orbit, compare accepted native camera matrices with requested poses
and inspect distinct quarter views; planned matrices alone do not prove camera motion.
The Adrian pilot required a temporary capture-order repair that was restored afterward;
see current HANDOFF and its engineering note. Do not assume that fix is installed.
Resolve a reproduced mismatch through the supported capture boundary before final
rendering. Carry detail/finish acceptance separately from movie completion: an orbit
cannot close pending endgrain, edge registration, cavity profile or shader-support gaps.

Runner preflights sibling .asset-ready.json (or --asset-receipt) before live access: accepted stage, current asset/source hashes and collection. Legacy assets require stage coordinator-reviewed-asset with explicit review_evidence; no silent bypass. Historical receipts with changed producer/input hashes require reconciliation, not blind recreation.
