---
name: image-feedback-to-cad
description: Iterate accepted image details into this remodel's CAD and Blender scene, with a quick OVRTX preview and changed-part updates.
---

# Image feedback to CAD

When the requested design is a recallable alternative, use
`skills/room-variations/SKILL.md` for ownership, draft/commit/save and rendering.
Separate shared component placement from variation appearance before editing.

Get one useful picture quickly. Start with the short `HANDOFF.md`; read only the
instructions relevant to the delta. Material/camera work needs no room XML, CAD
build or architecture audit. For geometry, read the affected room XML and the
source/import contracts; for tile coverage also read `blender/tile-layout/README.md`.
For marked protrusions, dark seams or narrow wood fillers, read
[marked repair diagnosis](references/marked-repairs.md) to identify the owning
source and separate geometry, shading and UV defects before editing.

- Preserve XML dimensions, opening boundaries and stable part IDs. Generated
  imagery supplies detail intent, not measurement. Record new assumptions in
  the room XML; use existing Lua helpers for physical details.
- Update changed geometry and its dependent finish only. Use the guarded
  `blender/prepare-ovrtx-source.py --detail-room <room-id>` entrypoint after that
  room's geometry-only build. Laundry/kitchen use `house/rooms/<room-id>/build.py
  --geometry-only`; downstairs uses `downstairs-bathroom/rebuild.py --geometry-only`. The importer compares
  stored part digests, preserves unchanged meshes/materials, and checks selected
  assignments and bounds. Full house exports/atlases are not routine look-dev steps.
- For a local repair, add `--parts id1,id2` (or a quoted prefix glob) to the
  guarded preparer. Include affected mating/dependent parts. This shrinks the MCP
  payload, not just the eventual import. Omit the filter for initial setup or when
  dependency scope is unclear; do not reread/send all meshes for a two-part edit.
- Treat `house.blend` as persistent authored state: native room/assembly collections,
  shared Material/node-group datablocks, saved cameras and lighting. Replace Mesh
  data under stable Objects; do not reconstruct the scene or append duplicate assets.
  Read the native reuse section in `blender/PIPELINE-CONTRACT.md` only when changing
  ownership or introducing linked .blend libraries.
- Get the requested view rendering before documentation/tool polish; use render
  accumulation time for that work. Reuse its saved camera and skip unrelated tile
  synchronization. A contact failure needs mating-boundary evidence, not more samples.
- Keep checks in tools and scoped to the delta: material/normal/bounds gates stay;
  deep topology checks apply to new or changed geometry. Glass policy checks only
  imported/edited objects, with mesh evaluation only where material mixing or
  modifiers require it. No repeated whole-room, USD or shader audit for ordinary
  edits. Inspect the resulting image; no extra tile tests.
- For beveled cabinet doors, drawer fronts, fillers, scribes and panels, preserve constant
  normals on broad planar faces and smooth normals only on the bevel bands.
  Blanket smooth shading produces false bowed highlights even when the geometry
  is flat. The guarded full and scoped importers own this repair and must reapply
  it on cache hits; do not patch the render by changing lights or roughness.
- Reuse `blender/materials/` for metric textures, grain direction and light
  assumptions. Do not rebuild existing material graphs or reset lights on every
  import. Keep one documented accepted appearance entrypoint/order per room;
  baseline material setup must not silently revert an accepted finish. Geometry-only
  imports reuse existing materials and bind new parts to the accepted palette.
- Use `blender/tools/render_feedback_mcp.py` for one affected view. Low-resolution
  64–128 samples is a useful preview default; final quality and additional cameras
  depend on the request and visible convergence, not mandatory numbers. Preserve
  transport depth when reducing preview resolution/samples.
- Set frame, then camera, then update, then capture serially. Native accumulation
  completion is the wait condition; add no fixed sleep afterward. Save/reopen only
  when a preview or error shows stale export state. Recovery details belong in
  `skills/ovrtx-room-rendering/references/recovery.md`, loaded only on failure.
- Store exposure in Camera data's native `ovrtx_exposure` settings, with per-shot
  brightness targets or explicit scene defaults. Do not restore retired manual
  meter/EV-offset workflows. Keep aspect, frame, native clip range and output
  metadata with each saved shot for controlled comparisons.
- Follow `AGENTS.md` for local scene saves and explicit OVStorage publication.
  Importing or rendering does not authorize publication. Replace the affected named
  JPG under the room's `renders/<room>/primary/` or `diagnostic/` category.
  Scratch holds proofs and intermediates. Refresh a
  contact sheet when useful, not as a required second deliverable. No new manifests.

Only one owner touches live Blender. Delegate source work only when authorized
and genuinely parallel; no automatic second verifier. Use this project's installed
public SDK/OVStream add-on; follow the active backend contract in `AGENTS.md`.


## Load detail for the affected work

- Mating profiles, accent lights, delegated source integration or an explicit
  continuity sweep: [detailed integration](references/detailed-integration.md).
- Wood color, roughness, texture scale or stale UVs:
  [texture workflow](references/texture-workflow.md).
- Finish-only generated concepts: [concept boundaries](references/finish-concepts.md).
- Mixed product/model/material requests and specialist briefs:
  `skills/digital-twin-iteration/SKILL.md`.
- General finish matching: `skills/material-reference-lookdev/SKILL.md`.
