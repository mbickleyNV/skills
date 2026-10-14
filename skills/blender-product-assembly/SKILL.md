---
name: blender-product-assembly
description: Shade, light, render, and animate named CAD product assemblies in Blender, including assembly-sequence mockups and OVRTX product photography. Applies to scene work, not Blender or MCP infrastructure setup.
---

# Blender product assemblies

Use the available Blender control workflow for scene operations. Preserve the
requested renderer and use existing project assets. This skill covers scene and
model decisions; it does not configure render services or transport infrastructure.

## Preserve the CAD contract

Import the named component assembly with verified axes and units. For millimetre
sources, the final world-space conversion is 0.001 metres per source unit; do not
apply that factor twice. Verify world bounds and component counts after import.
Keep the CAD identity in object names or metadata so revisions and animation
groups can be rebuilt deterministically.

Check relevant close-up joints as well as the hero silhouette: closed tube ends,
inside screw heads, concealed tips, bracket holes, washers, and panel connections.
Use small topology cleanup tolerances appropriate to the thinnest strand. Preserve
holes and document inferred geometry instead of presenting it as measured CAD.

Judge the final pose against the designated finished-product view before accepting
construction close-ups. Contact checks do not validate clip orientation or visible
overhang. Inspect thin extrusions with modifiers disabled: broad bevels and smooth
normals can make a closed tube look flanged or swollen. Preserve CAD-rounded
profiles, avoid a second large bevel, and keep planar stock faces visually planar.
Before changing proportions from a reference comparison, match view direction,
elevation and perspective strength using rim slopes and visible top/side areas.
Keep a reference-comparison camera separate from the beauty camera. Camera tilt
and perspective can masquerade as wrong basket depth, spacing or base clearance.
Use the overview to select one detail proof of the least-supported visible part
family, not only the joint most recently edited; this replaces a redundant audit.

For repeated CAD dimensions, palettes and room-style revisions, read
[references/iterative-cad.md](references/iterative-cad.md).

## Geometry review views

Use a close-up with the same assembly relationship as the instruction inset to
review a disputed joint, plus a seated view with the display offsets removed.
Choose the camera so both receiving holes and relevant formed features are
visible; a whole-product hero cannot verify these details. Keep enough adjacent
geometry to establish orientation. Label cropped coupons and inferred sections;
never propagate their artificial crop boundaries into the product.
For formed clamps, make the existing joint proof reveal the free edge, return
bend and tube-bearing region together. If the bolt hides a disputed punch, use
an explicitly exploded copy to reveal its shape; retain a seated occurrence.
This is a choice of proof framing, not an additional full audit.

When a render shows a stray strip or obstruction, trace the visible feature to its
named CAD part and face before editing. A targeted view ray or section can separate
actual interference from foreground occlusion. Fix geometric defects in the CAD;
moving the camera or hiding the offending object does not resolve them. Afterward,
use a reference-matched view to show the required open region, not only hole centers.

After integrating a prototype, render its actual occurrence in the complete
model as well as the final-product silhouette. A good-looking isolated connector
does not establish that mirrored joints fit their rails or that its width matches
the post's available flat face. Preserve the prior assembly as a separate revision.

If a planar CAD face looks rippled, inspect geometry and shading separately.
In one OVRTX export path, smooth/flat flags and custom normals alone left diagonal
patches; splitting coincident vertices at planar/curved boundaries in render-only
meshes resolved them. Use this only after inspection, retain closed source solids,
and do not claim index-split render meshes retain the source's welded topology.
Gentle bead-to-flat transitions can still produce long needle-like highlights
after angle-based splitting. A tested fallback is fully unshared triangle vertices
and flat shading on the offending render-only part; proof-render it and inspect
the curved silhouette for faceting before acceptance. This resolved a formed-tab
case without moving surface points or changing its CAD construction.

## Powder coating and studio contrast

Coated steel is a dielectric painted surface over metal; it does not require a
fully metallic Principled shader. Start with low metallic, moderate roughness,
and a restrained coat layer. Tune against rendered highlight width and color.
Keep the underlying green or other pigment visible in lit areas and shadows.
Do not force a color change solely by increasing saturation or lowering roughness.
Convert sRGB reference colors to linear values when assigning shader inputs.

Build the lighting hierarchy deliberately: one broad key, a weaker fill, and a
rim/back light that separates the outline. A key-to-fill power ratio around 4:1
is a starting point, not a fixed rule; distances, sizes, and incidence change the
effective ratio. Avoid three equally strong softboxes, which flatten shape.
Control the world/background contribution and use a neutral sweep. Inspect the
highlighted top surface as well as the darkest structural face before choosing
exposure. Use coat and light size to make a slightly shiny finish without white
clipped panels. A gray-looking color under excess illumination is a lighting
problem as well as a possible shader problem.

Render a cheap proof, inspect it, then change the material/light balance before
the final image. Preserve framing while comparing lighting versions. Supplement
the hero with a useful hardware or section close-up when corrections are subtle.

## Task-sized verification

For a local correction, inspect the affected contact boundary in CAD and in one
in-context proof. Reuse established cameras, materials and checks; rerun only
checks invalidated by the change. Do not repeat source, exporter and Blender
checks that establish the same fact, or request a second full audit by default.
Batch skill edits and validate/deploy once after the content is settled.

Acceptance starts with construction, not mesh statistics. For each disputed joint
type, compare one matching detail and its assembly overview with the reference:
part boundaries, required empty space, bends, mating surfaces, and fastening action.
Use technical mesh checks to support that comparison, not replace it. Stop when
the depicted relationship and relevant invariants pass; do not add a second audit
or a larger sampling count merely to increase confidence in an unproven reading.

A tight installed joint is not verified by connector contact alone. Show the
actual shelf-rim-to-leg seam in a view where a gap would be visible; do not use
framing or an oversized hidden connector to conceal a missing mating surface.

For animations or instruction-step contact sheets, also read
[references/animation.md](references/animation.md).

For a physical drop after an authored reveal, read
[references/physics-handoff.md](references/physics-handoff.md). Physics attributes
alone do not establish that the requested solver ran.

## OVRTX-specific observations and delivery

The observed OVRTX Blender 5.1 installation supports simple Principled base color,
roughness, and metallic materials. Test extra coat/texture inputs in a proof rather
than assuming every Blender shader node is translated. A 65 mm perspective camera
worked where orthographic export failed in one installation; prefer a tested camera
path without treating that local failure as a universal OVRTX limitation.

For multi-shot OVRTX rendering or a stalled render call, read the short
[batch-render observations](references/ovrtx-batch.md). These describe a tested
local workaround, not a general engine requirement or permission to alter services.

For still delivery, check the saved scene, requested renderer and output file
once, then stage through the established media workflow. Keep the validated CAD
source distinct from render-only mesh treatment.
