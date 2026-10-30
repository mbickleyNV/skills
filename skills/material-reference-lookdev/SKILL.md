---
name: material-reference-lookdev
description: Create or refine reference-based product finishes, including image-generated PBR contact sheets, aligned maps and OpenPBR recipes for native visual review. Use for wood, coatings, ceramic, glass and fabric appearance; tile layout defects stay with tile-finish-lookdev and geometry stays in CAD.
---

# Material reference look development

## Project adaptation

This is a generalized workflow. Use the active project's source, scene, renderer
and save/publication rules. Names such as `HANDOFF.md`, room XML, specialist
profiles, `blender/tools/`, studio assets and pipeline contracts are integration
examples, not files supplied by this skill. Discover their maintained equivalents
before using them. Only helpers inside this skill directory are bundled. If a
required adapter or asset is absent, report that stage as unavailable and deliver
the supported work; do not invent a command, schema or successful native result.
Use specialist roles only when delegation is authorized and available; otherwise
the coordinator performs the same bounded work. Keep one live Blender owner.


Read current `HANDOFF.md` and follow `AGENTS.md` for live ownership and saves.
Identify the frontmost visible object and evaluated assignment before changing a
material. Classify geometry/contact, UV scale/direction, texture channels, translator
support, lighting/exposure or compositing as the likely cause. Avoid compensating
for a bad mating surface or bowed planar normals by changing roughness.

## Reference and physical recipe

- Identify exact finish variant and source provenance. Sample swatch interiors away
  from glare/shadow; product photography includes lighting and is not pure albedo.
  Generated flat references can approximate hidden patterns, not verify them.
- For named color alternatives, inspect actual manufacturer swatches together
  before ranking similarity. Compare lightness, hue and saturation separately
  from glaze character; a similar gloss or variation range cannot make dark brown
  a match for pale green-white. Keep the comparison light/white point fixed and
  label room renders as appearance studies when photography is uncalibrated.
- Require the physical pattern scale receipt and generated-feature review in
  `references/image-generated-openpbr.md` for image-generated product maps.
- Record texture extent in physical units and orient grain per part. Keep albedo,
  roughness and normal aligned. Use sRGB for color and Non-Color for data channels.
  Preserve repeated-pattern scale and textile direction, including the actual rug
  dimensions; do not bake photographed highlights or folds into a flat finish.
- Separate tile/part color variation from fine surface grain. Match amplitude to
  reference and viewing scale. Powder coat is a coated dielectric surface; visible
  substrate or wear needs supporting evidence. Do not add generalized dirt/aging
  to every asset to make it realistic.
- When sample and installation photos disagree, compare them side by side before
  choosing the color center. A brighter installation board is not inherently a
  better albedo reference than darker product samples. Preserve the discrepancy
  and give the user's latest image and color correction priority over an earlier
  photographic interpretation or specialist acceptance.
- Judge lightness, chroma and hue separately in the actual fixed-lighting render.
  Source RGB agreement alone can still produce an overly bright/saturated finish
  after room illumination and the saved film grade. For a reported saturation or
  brightness mismatch, adjust only the affected material/instance color, then
  inspect one representative native preview before repeating a gallery batch.
  Keep the palette's stable IDs and relative variation; do not shift room lighting
  to repair one finish.
- Treat a noted photographic cast as uncertainty, not permission to erase the
  reference's dark or muted character. Use unclipped, plausibly neutral surfaces
  only as a cautious cast check; colored bounce and mixed lighting are not global
  white-balance evidence. Avoid sampling grout, glare and deep shadows as tile
  albedo. A small blue cast does not by itself justify brighter/oranger tile.
- Physical lips, gaps, perforations and visible textile thickness belong to geometry
  when they affect silhouette/contact/shadows. Shader normals cannot replace them.
  Label unsourced small radii, roughness values and fabric construction as estimates.

## Native compatibility and bounded iteration

For a new product finish from input photographs, or an explicitly requested
image-generated PBR contact sheet, use
[image-generated OpenPBR workflow](references/image-generated-openpbr.md).
Use clearly labeled inferred parameters to make a strong candidate when calibrated
measurements are unavailable; improve through visual review rather than blocking
all progress on a physical sample. Separate appearance fidelity from measured accuracy.

Reuse artist materials and existing helpers in `blender/materials/`. Change only
affected materials and their intended consumers; a shared name is not permission
to alter other rooms. Geometry-only imports retain accepted finish assignments.

Verify active render UVs and exported channels only when a mismatch makes that
inspection useful. Blender node connectivity or USD authoring does not establish
native support. Confirm translator-sensitive normal strength, bump, coat or texture
mix behavior in the installed backend before adopting a recipe. Bake only the
unsupported requested contribution, with physical scale and provenance retained.

Keep camera, exposure, white point, lighting and grading fixed for comparison.
Inspect one representative affected view; add a close-up when grain or micro-sheen
cannot be resolved there. Avoid full-house rendering for one material. Record the
actual image result and any limitations; no added tile look-development tests.

Load existing specialized detail only when needed:

- Ceramic/grout/GN UV and mottling: `skills/tile-finish-lookdev/SKILL.md`.
- Wood maps, grain and stale UV diagnosis:
  `../image-feedback-to-cad/references/texture-workflow.md`. Read its wood-edge
  section for cabinet lipping, edge banding or smeared bevels; verify evaluated
  edge charts separately from accepted broad faces before changing the finish.
- Pure grade/bloom/grain changes:
  `../digital-twin-iteration/references/retained-image-iteration.md`.
- Native captures: `skills/ovrtx-room-rendering/SKILL.md`; failure recovery only
  after a concrete failure. Source/export performance investigations use
  `skills/blender-scene-updates/SKILL.md`.

## Product-to-material production loop

For small wood parts or cross-product finish sharing, use the resolution,
face/endgrain continuity and recipe-equivalence guidance in
[image-generated-openpbr.md](references/image-generated-openpbr.md#small-wood-parts-and-shared-finishes).

For high-fidelity asset creation, keep material_specialist responsible for appearance
reasoning through reference analysis, proposed recipe, actual generated-map review and
critique of the first representative asset view. Reuse/follow up the same specialist;
a prompt or audit alone is not finish delivery. Coordinator owns generation/integration
and native tools. Research-only assignments retain their narrower scope.

Choose the smallest representative asset/surface that exercises the requested finish
at its intended viewing scale. Develop and review it before multiplying recipes across
sizes/products. Reuse an accepted finish when reference, scale, mapping and renderer path
remain equivalent; new size alone does not require another material study. Independent
geometry work can proceed in parallel. Offline-only scope may produce reusable masters
and candidates; do not call their appearance accepted or start unauthorized rendering.

Judge reference fidelity: anatomy/pattern, physical scale, direction, seams, color and
surface response. Add channels only when evidence and visible response justify them;
OpenPBR intent is not a feature-count target. Use existing map/UV/source checks. Inspect
actual shader translation on the first new path or a demonstrated mismatch, then reuse
that finding while identity/support remains unchanged. A novel or uncertain appearance-
critical channel needs one bounded comparison; known unchanged channels don't need a
new test matrix. Fold pattern and sheen review into the first useful product/detail view
when possible, rather than creating mandatory separate swatch batches.

Carry a compact handoff with reference/recipe/map identities, physical extent, admitted
shader path and destination. Report stages separately: authored candidate, applied to
requested asset/scene, appearance-reviewed, saved/delivered. Confirm the requested
consumer actually selects the new recipe/library before calling an upgrade complete.
A candidate file or gallery preview does not imply another scene was updated. Complete
authorized application/delivery; keep research-only/offline candidates clearly bounded.
