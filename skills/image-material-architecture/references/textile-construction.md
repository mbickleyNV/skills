# Separate topology, population and aggregate response

Read when fibers, yarns, loops, tufts or crossing strands define the source. This
is a construction-analysis route, not a preset for each fabric type. Start with
visible connectivity and scale, then inspect relevant editable exemplars.

## What inspected examples actually teach

- [ASWF OpenPBR velvet](https://github.com/AcademySoftwareFoundation/MaterialX/blob/24c034cc484ebebe01b454e83b40bc2812876eb6/resources/Materials/Examples/OpenPbr/open_pbr_velvet.mtlx)
  has a dark base, rough specular and an independently brighter fuzz layer. It has
  no texture or yarn generator: useful for aggregate angular response, insufficient
  as evidence for resolved pile construction.
- [NVIDIA SimReady v0.2.0](https://github.com/NVIDIA-Omniverse/PhysicalAI-SimReady-Materials/releases/tag/v0.2.0)
  contains editable Carpet and Fabric USD/OpenPBR archives. Inspect the composed
  inherited graph. `Rug_Carpet_Base` drives normal, specular color, roughness and
  anisotropy independently, with zero fuzz. `Fabric_Carpet_Long_Floor_Orange`
  drives reflection weight separately from roughness and normal, also with zero
  fuzz. These graphs contain no pile geometry. `Fabric_Wool_Fuzzy` adds fuzz over
  mapped relief/roughness; `Fabric_Denim` also drives fuzz color from its color map.
  They demonstrate different optical approximations, not proof that those
  settings reconstruct every textile with a similar name.
- The same release's `Fabric_Ripstop_Coated` has zero coat weight and connects a
  file named `glossy_roughness` to specular color. Record actual destination and
  inherited encoding rather than inferring purpose from filename or title. Treat
  suspicious mapping as an inspection question, not a convention to copy.
- [SideFX's braided rug construction](https://www.sidefx.com/tutorials/craftsman-scene-assembly-cops-lighting-lookdev/)
  makes braid paths, deforms them around the rug and creates tube geometry. That
  establishes geometric depth/occlusion; it is not a shader-only rug example.
- [SideFX Karma Hair](https://www.sidefx.com/docs/houdini/nodes/vop/kma_hair.html)
  separates renderer-created curve thickness from fiber scattering, and permits
  MaterialX nodes to drive its parameters. The specialized closure and geometry
  behavior are renderer-specific, not portable OpenPBR support promises.

These are graph/document observations. Verify the chosen behavior in the target
renderer; do not promote a downloaded sample to a native-tested reference.

## Record separate levels before prompting

| Level | Evidence and field decisions |
| --- | --- |
| Overall layout | Regions, borders, raised/cut areas, pile-height transitions; preserve spatial authority |
| Yarn or tuft | Loop versus cut end, bundle width, row/column pitch, packing, twist, connectivity, tilt and height distribution |
| Individual fibers | Finer strand width, curl, local orientation spread, flyaway density and correlation with the parent yarn |
| Unresolved aggregate | Fuzz tint, grazing response, roughness/anisotropy and light redistribution at delivery scale |

Do not use individual-fiber diameter as yarn height. Do not equate total pile
height with the relief contrast visible between adjacent regions. Preserve
uncertainty in physical dimensions; use ratios to a visible bundle/pattern anchor
when scale is unknown. More image pixels or stronger normals cannot fix incorrect
loop connectivity, packing, direction or missing intermediate populations.

## Preserve the population through image generation

Translate the observed hierarchy into concrete source-anchored constraints:
packed rows versus disordered curls, connected U-shaped loop crowns versus cut
tips, distribution of widths/heights, direction changes and quieter areas. Forbid
substitutions that would change this identity, such as rounded beads in place of
strands. Ask for separate population/orientation/coverage fields when needed;
do not infer all of them from one noisy brightness image.

Select morphology with a source-scale detail study. Request numeric maps with
explicit data semantics separately from lit appearance studies. A color-only
intrinsic image should not contain fiber highlights; judge missing geometric
structure in its designated normal/height/population authority, not by demanding
shading in albedo. Reject a grayscale beauty masquerading as height. Keep separate
roughness, reflected-amount and fuzz decisions where the evidence supports them.

Use [the detail pilot](../../image-material-detail-pilot/SKILL.md) to compare source,
field and native crops at similar feature footprints. Check morphology first,
then visibility under front/grazing light and an independent turn. A raw
high-sample view can diagnose filtering; if the population is wrong already,
return to spatial design rather than increasing samples or normal amplitude.

## Decide where geometry earns its cost

Use mapped relief when the required structure is shallow and shading suffices.
Test displacement or explicit supported curves/strands when visible over/under
occlusion, pile silhouettes, open gaps or parallax matter. Keep the standard
shaderball intact and add a separately labeled diagnostic proxy; do not quietly
replace the benchmark with a groom. Exported curves, tube meshes, renderer hair
primitives, displacement and specialized fiber closures each need separate
capability checks. A MaterialX graph alone does not carry the procedural model.

Use [transport diagnostics](../../image-material-diagnostics/SKILL.md) to pair
directional reflection/body observations with fuzz/tangent/normal interventions.
Anisotropy magnitude does not specify local direction; one global tangent cannot
represent crossing yarn populations. Fuzz captures aggregate response, not resolved
loop shapes. Keep the geometry approximation and source-fidelity verdict explicit.

## Distinguish drape from local construction

When reflective cloth becomes veiny or crumpled, use [coherent deformation](../../image-material-spatial-design/references/coherent-deformation.md). Broad folds, yarn crossings and fine tooth need separate morphology and coordinate ownership. A reflective or opaque film can retain broad sheet bending while smoothing yarn-scale relief; assign conformity by scale rather than making every coat globally flat. Keep coherent folds and weave out of stochastic synthesis; route only suitable local residuals to [mapping blends](../../image-material-spatial-design/references/mapping-blends.md).
