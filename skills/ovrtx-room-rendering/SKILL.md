---
name: ovrtx-room-rendering
description: Render saved remodel cameras and room/house batches through the session-reusing OVRTX pipeline. Use for stills and batches; use scene-update guidance for exporter/runtime engineering.
---

# OVRTX room rendering

Read current `HANDOFF.md` and the active backend contract in `AGENTS.md`.
Use the saved canonical scene directly. Ordinary captures do not require CAD
rebuilds, old proofs, whole-house inventories, save/reopen audits, or publication.
One owner controls live Blender; leave an existing native job alone.

## Choose the capture

- Saved-camera feedback: use `start_feedback_shot` and `complete_feedback_shot`
  in `blender/tools/render_feedback_mcp.py`. Keep the persisted ticket; a lost
  reply does not justify another capture. Inspect the completed affected image.
- Room/house batches: use `start_primary_render_service.py`, which runs
  `render_timeline_batch.py`. Keep its refresh checkpoint on resume. The
  standalone `render_primary_batch.py` is for targeted stills, not normal batches.
- New/reframed camera: use `skills/camera-composition/SKILL.md`; check one cheap
  preview before one final capture. Existing approved cameras need no new preview.
- Saved variations/shared placement: use `skills/room-variations/SKILL.md`.

Choose compositing explicitly: `CAMERA` follows each camera's RAW/SCENE choice,
`RAW` bypasses the saved nodes, and `SCENE` applies the enabled saved stack to
the requested batch. A request to grade the whole house overrides camera opt-in
for that batch; it does not establish a universal policy for future diagnostics.
Use an explicit `--scene blender/house.blend` for unpublished local authoring
changes; the service's unattended default resolves the published OVStorage leaf.
For an intentional fresh batch, create one `--refresh-after` epoch and retain it
on recovery instead of changing it and recapturing completed views.

Gallery renders default to RGB only; pass `--semantic-masks` when region maps
are requested. When included, semantic masks must align spatially with composited
RGB. Color grading,
grain and bloom do not belong in label images. Lens warps require nearest-neighbor
label resampling with the same spatial mapping; reject unknown mappings rather
than attaching raw masks to changed pixels. See the gallery compositing contract
in `blender/docs/engineering-changes/house-gallery-compositing.md`.

Set frame before camera and evaluate the view layer. Use saved camera native
exposure and color settings. Sample/bounce changes alone need no restart.
Keep JPGs in the established room `primary/` or `diagnostic/` path; intermediate
PNG/EXR and proofs belong in `scratch/`. Do not promote diagnostics implicitly.
Save/publish only under the project's manual authoring contract.

## Observe completion cheaply

Inspect exact native receipts/files outside Blender while rendering. Do not
queue live status calls during preparation. Native accumulation completion
requires no extra settle sleep. Confirm sequence retirement before switching
lighting or starting another owner; keep checkpoints after a controller failure.
A waiting result, idle GPU or lost reply does not establish native failure.
Verify native product/runtime quality tokens when cached controller diagnostics
disagree; a stale DLSS Boolean does not establish the accepted reconstruction mode.
Use `python3 blender/tools/inspect_native_render.py --ticket <ticket.json>`
for compact offline completion/timing output; add `--timings` only for diagnosis.
Without a ticket, use the exact output/start epoch and pinned worker log.

## Read details only when needed

- Actual failure: [bounded recovery](references/recovery.md).
- Blocked cabinet view: [near-plane framing](references/near-plane-framing.md).
- Glass diagnosis, exposure/color comparisons, HDR/media delivery, saved
  variations, or targeted camera groups:
  [specialized captures](references/specialized-captures.md).
- Exporter/runtime optimization: `skills/blender-scene-updates/SKILL.md` and
  `blender/docs/scene-update-knowledgebase.md`; performance review is not a
  prerequisite for routine rendering. Timers are nested; do not sum parent
  totals with their children or infer native cost from batch wall time.
