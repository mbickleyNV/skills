# Lessons from prior project material work

## Shared hardware woods

Coordinator-reviewed 2026-10-07 evidence:
`blender/docs/engineering-changes/shared-oak-hardware-lookdev.md` and
`blender/docs/engineering-changes/shared-hardware-wood-materials.md`.
The earlier 1 m oak scan provided roughly 0.244 mm color and 0.488 mm normal
texels. It passed persistence checks but looked weak at handle scale. The revised
2172×724, 300×100 mm generated master resolved inferred 2–3 pixel pores; its
dimensions and anatomy are artistic estimates, not measured manufacturer data.
An endgrain color correction restored continuity while retaining accepted endgrain
normal/roughness. A fixed-lighting black-stain normal comparison established
visible native response; final inferred relief was 40 µm. These numbers are this
recipe's choices, not defaults for other woods. The comparison image survived,
but its reused native output path did not retain a complete comparison receipt;
the final six Frankie captures do have matching native evidence.

Recipe/content-based sharing reduced 156 bindings across 78 wood variants to ten
actual materials. Numeric shader defaults were normalized recursively so 0 and
0.0 did not create false recipe differences. Cross-family Material identity,
source geometry/normals/UV preservation and unchanged Mesh identity were checked
in isolated save/reopen exercises. Portable assets remained packed. Six refreshed
Frankie gallery views were reviewed; the other 44 updated assets reused accepted
recipes without separate native review. The paused bathroom consumer was not
updated. Catalogue, gallery and room installation remain separate stages.

These are reusable workflow findings, not permission to replay archived proofs or
restore old backends. Check current source/installed identity before relying on a
translator finding. Historical images/results are evidence at their recorded stage.

## Heath LM5 / Basalt Gunmetal generated atlas

Sources: `blender/materials/textures/tile/heath-lm5/imagegen-source.json`,
`openpbr-inputs.json`, `blender/materials/prepare_heath_lm5_textures.py` and
`heath_lm5.py`. Built-in image generation produced a four-column variant atlas with
rows for albedo, concave height and roughness. The documented patch was 100 mm;
normal preparation used inferred 0.12 mm peak-to-valley relief and metric gradients.
Those values are this finish's artistic interpretation, not universal ceramic values.

- Registration across channels matters more than generating four attractive
  unrelated images. Inspect actual alignment; a prompt requesting registration
  does not prove it occurred. Keep palette variants within one reference family.
- Deriving tangent normals from a scalar field with documented physical extent
  gives explicit slope/amplitude control. Keep the height reference out of shader
  displacement unless that channel is intended and supported.
- The preparer cropped panel borders and blended the outer eight pixels for periodic
  edges. This is an implementation precedent, not proof of seamless tiling for a new
  surface; inspect repetition and preserve important pattern features.
- Stable shade and UV-phase fields can vary appearance without making new physical
  tile definitions. `exact-tile-map-palette-primvars.md` documents exact map selection
  and normal Strength retention in the later MaterialX/OpenPBR path. Reuse existing
  graphs/maps and sparse appearance updates rather than cloning material families.

## User-supplied white oak PBR sheet

Sources: `blender/materials/main_floor_white_oak.py` and the 2026-09-24 main-floor
entry in `docs/handoff-session-history.md`. It sampled aligned color, normal and
roughness panels directly through matching UV regions without resampling the sheet.
Color and data copies had distinct sRGB/Non-Color interpretations; board width was
physical and grain direction followed the accepted layout.

- Direct atlas sampling is valid when channel coordinates and translator support
  are verified; extraction is not mandatory. Use the same pattern/offset for all
  channels and avoid losing map resolution to ornamental sheet labels.
- Metric scale persists across different panel sizes; object bounding-box mapping
  silently changes grain size. Rotate/offset samples per stable part identity while
  preserving intentional grain direction and shared random phase across channels.
- The living-room EEVEE proof used cooler lighting than the OVRTX kitchen/dining
  proofs. It was layout evidence, not a reliable stain-color comparison. Cross-engine
  pictures need explicit color/exposure context before adjusting albedo.

## Ceramic relief and translator changes

Source: 2026-09-24 upstairs channel-audit entries in
`docs/handoff-session-history.md`, `skills/tile-finish-lookdev/SKILL.md`, and later
`blender/docs/engineering-changes/exact-tile-map-palette-primvars.md`.

- Grayscale height accidentally connected as normal produced dirty false shading;
  other procedural Bump nodes did not export their intended relief. Diagnose the
  actual channel/coordinate route before adding stronger noise or changing lights.
- Near-flat normal pixels can hide relief regardless of the thumbnail. Inspect
  numeric range and rendered scale; some intended grain disappears below one pixel.
- Earlier stock USD paths dropped Normal Map Strength; encoded restrained slopes
  plus Strength 1 were a workaround there. Later shared OpenPBR palette conversion
  explicitly preserves Strength. Select a current-path remedy; do not multiply
  encoded slope and preserved strength twice or infer current defects from old notes.
- Coat Weight and Coat Roughness support changed independently. Read the exact
  `materialx-coat-weight-texture.md` and `exact-coat-roughness-palette.md` contracts
  if needed: scalar channel selection, active/named UV and single-versus-palette
  lowering have distinct admission rules. A working coat constant is not proof that
  every coat texture chain works. Source-only acceptance is not native validation.

## Oak grading, Marmoleum and coated furniture

`skills/image-feedback-to-cad/references/texture-workflow.md` records an oak float-save
round-trip that brightened color and reduced contrast. Grade from untouched input,
keep an explicit color-space path and use absolute transforms so recalls/imports do
not compound tint. The matcha Marmoleum history records generated reference maps and
an initially dark proof; a ceiling slab blocked lighting and temporary white-point
changes differed from saved settings. Material refinement needs the actual light and
geometry context. Deck furniture work used distinct powder coat, wood and grey paint
with per-part grain direction; preserve that construction separation.

Review scope: recent chats "Research Geo Nodes interaction ideas", "Simplify bathroom
vanity", "Model deck and furniture in LuaCAD" and "Create matcha orange laundry
variant", plus the older durable session history and maintained material sources.
The original LM5 image-generation conversation was not recovered in this sample;
its retained prompt/input metadata and executable preparation are the evidence.
