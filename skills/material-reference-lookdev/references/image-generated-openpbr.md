# Product photographs → generated maps → OpenPBR appearance

Use for an authorized new material or finish creation task. The material specialist
owns analysis, prompt design and proposed recipe; the coordinator owns image generation,
asset assembly and live integration. A research-only assignment returns proposals
and does not automatically generate assets or mutate Blender. Load the imagegen
skill when actually generating; use the built-in tool, not an unsolicited API runner.

## Reference packet and target

Inspect the actual input images. Identify exact product finish and distinct material
regions. Assign each image a role: full-product silhouette/context, finish color,
macro texture, or sheen/lighting reference. Prefer a clean, high-resolution surface
crop; perspective and specular highlights are lighting evidence, not raw albedo.
Record known dimensions or an inferred physical patch extent with confidence.
Keep paint, exposed metal, glass, fabric and edge hardware separate where physical
construction requires it. Use intended close-up and product-view scale to allocate
texture detail. No unrelated dirt, wear, embossing or fictitious pores for realism.

## Generate the visual contact sheet

Use the supplied finish crop as primary texture evidence. Request a flat orthographic
material study, with a clean unlabeled map area and gutters separating optional
labels/previews. State patch extent, grain direction, color family, pattern density,
and invariants. Ask for seamless borders, neutral diffuse base color without baked
highlights, shadows, perspective or object contours. Include a repeated-tile preview
and plausible roughness/relief views only where justified by the physical finish.

Example prompt brief (adapt, never treat as a fixed tool schema):

> From the supplied product finish close-up, reconstruct a flat seamless surface
> patch representing [extent] mm. Preserve [color, grain, pore/speckle scale and
> direction]. Produce a review sheet showing the proposed base-color patch and
> coherent roughness/relief interpretation, with a repeated-tile preview. Keep all
> texture regions square, separate from labels, without product edges or lighting
> baked into base color. Relief is [absent / restrained and justified by reference].
> Do not invent wear or increase grain size for drama.

Inspect the generated sheet against the actual reference. Reject architecture/product
drift, lighting contamination, invented relief and obvious repeated motifs. Refine
one visible discrepancy at a time. A generated lit sphere is an appearance concept,
not evidence that any native shader supports the recipe.

## Build a coherent map set

The review sheet is not automatically a shader-ready set. Preserve an approved master
surface pattern and derive or register other channels to it. Use existing deterministic
asset helpers for extraction, normalization, normal construction and sheet assembly;
image editing/generation itself follows imagegen. Do not independently regenerate
every channel and assume feature correspondence. A pigment speckle may belong only
in color; dark color does not establish a depression or high roughness.

For every delivered channel record crop/bounds, resolution, physical extent, color
space, direction, provenance, transform and interpretation. Inspect repeat borders
in a tiled preview, channel alignment and fine pattern density at actual resolution.
Normal maps need an explicit tangent convention, plausible numeric direction and
strength, checked on a lit native surface. Scalar height needs a documented physical
amplitude and reference level before displacement; if not justified, omit displacement.
Use constant scalar channels when they represent the material better than invented
textures. No mandatory all-channel package: add transmission, coat or fuzz only when
the real surface and target shader need them. AO stays separate from base color.

## Describe the OpenPBR material and translator boundary

OpenPBR is a surface model, not a contact-sheet file format. Reference specification:
https://academysoftwarefoundation.github.io/OpenPBR/ . Describe the intended physical
layers and fields, such as base_color/base_metalness, specular_roughness/specular_ior,
coat_weight/coat_roughness, transmission_weight, subsurface_weight and fuzz_weight,
only as applicable. Mark every inferred value; avoid arbitrary layer stacking.
Opaque powder coating is dielectric even over metal; a clear finish over exposed
metal or wood is a different construction. Anisotropy needs real directional evidence.

Map that intent to the installed Blender/USD/native path. Record fields supported,
approximated or unavailable; do not assume a Principled or UsdPreviewSurface shader
is an exact OpenPBR implementation, or switch backend to obtain one. If only a subset
is supported, deliver the reusable OpenPBR-intent recipe plus the validated native
approximation and its limitations. Explicit MaterialX/MDL authoring needs an actual
supported authoring/import path, not an invented graph contract.

For established project precedents and version-dependent translator findings, read
[prior material lessons](prior-material-lessons.md) only for the affected material.
This project already has a MaterialX/OpenPBR translator; verify its exact admitted
channel/coordinate path instead of assuming generic USD export capabilities.

## Native appearance acceptance and durable delivery

Generate and inspect the material swatch/contact sheet before extracting coherent maps.
For native review, use the first representative product/detail view with useful grazing
highlights. A separate flat/curved rendered study is conditional: use it only when that
view cannot expose an uncertain appearance-critical response.
Reuse the saved scene and sparse material update path when integrating. Keep camera,
exposure, color management and light fixed for comparisons. Change color/pattern,
roughness and relief separately when diagnosing. Judge highlight width/rolloff,
grazing response, pattern scale, repetition and contact appearance, not just color.
No added tile tests and no automatic house batch. Respect live owner availability.

Deliver the visual sheet, usable maps/constants, recipe/UV extent and inspected native
image evidence when rendering is authorized. Candidates, generated sheets and proofs
stay in scratch. Accepted texture assets use the existing material-library organization;
approved rendered diagnostics follow AGENTS. Save/publish only within authorized scope.
Store the accepted reference/prompt, recipe, source hashes, map transforms, backend
identity, known approximations and inspection result through coordinator review in
specialist knowledge. Never label inferred textures a measured product scan.

## Physical pattern scale receipt

Image-generated maps require a scale_receipt in the product material packet. Record
patch_extent_m, confidence (measured or inferred), reference_evidence and
generated_review_evidence, plus features with axis (0=U, 1=V), target_size_m,
observed_fraction and relative_tolerance. Infer target feature spacing against a
known product dimension using a rectified same-plane crop; label perspective and
finish uncertainty. Specify both patch dimensions and feature size/density in the
generation prompt. Inspect the actual output: physical feature size equals patch
extent on that axis times observed fractional image span. A generated label or
prompt dimension is not calibration. Choose justified tolerance before reviewing.

Record crop/resize transforms and hashes with the map provenance. All channels share
one patch and registration. A 300 mm patch with a feature spanning 10% represents
30 mm, irrespective of resolution. Do not resize UVs per part bounding box. Surface
recipes use that same extent and declare grain_direction. End grain and distinct
construction need their own evidence/recipe. Explicit complex UVs require a metric
validation adapter; until then report that acceptance gap rather than claiming scale.

Before a full turntable, review a fixed-lighting product view and close-up for scale,
direction and repetition. Where reference scale is inferred, compare a small set of
labeled candidates while keeping sheen/exposure fixed. Coordinator records the
accepted candidate and native evidence; numerical scale receipt acceptance alone
does not prove the photograph match. Reuse completed previews; do not rerender an
active sequence automatically.

## Multi-material fidelity and review coverage

Build a region ledger covering face grain, exposed end grain, slab top/edges,
ceramic, coated layers and metal finish. Each visible region needs reference evidence,
implemented recipe/UVs and a comparable native crop. A scalar endgrain color or
unregistered slab edge remains a candidate approximation when visible at the target
scale; do not close the fidelity item solely because it is disclosed. Develop the
missing directional map or shared slab-space mapping when the reference requires it.
Photographic evidence supports grain/brush orientation and pore filling; add those
contributions only where observed and admitted by the installed native path.

Check pattern at multiple scales: broad figure/vein distribution, principal bands,
and resolvable fine pores/hairlines. Measure several representative locations rather
than selecting one favorable line. Fix tolerances before generation; wide inferred
tolerances describe uncertainty, not high fidelity. Compare generated pattern layout,
contrast and density with the reference even when numeric sizes pass. If pixels cannot
resolve intended microfeatures, report texel size and omit the unsupported claim;
upsampling cannot add evidence. Crop/registration and repeat continuity must be checked
on actual part extents, including small panel wraps. A seamless prompt is not proof.

Inspect neutral color/pattern and grazing sheen separately with fixed exposure and
lighting. Keep scalar channels where evidence supports uniform response; do not force
invented roughness/normal maps. Record actual exported/native shader schema and visible
response. OpenPBR intent preserved in JSON does not establish OpenPBR rendering. For
appearance-critical unsupported coat/anisotropy, run a bounded native A/B when rendering
is authorized, or retain the limitation and avoid accepting it as verified.

Native acceptance records capture mode (still/timeline/etc.), effective material presentation and required native material layer evidence alongside backend/translator identity. Reuse only when these match; valid image hashes without required presentation remain unverified. Use existing native receipts rather than adding a per-variant matrix.
# Small wood parts and shared finishes

When a wood finish looks weak on a small part, calculate physical texel size for
each channel (patch extent divided by pixel count), then inspect resolved grain
and pores at the intended view scale. A high-resolution scan can still be too
coarse for a handle. Pixel resizing does not create detail or change physical
extent. For nearly flat normals, inspect source bit depth and numeric slopes;
an 8-bit preview of a 16-bit map can conceal valid variation.

Review facegrain and endgrain together on the assembled part after changing a
master. Their anatomy and orientation differ, but the same finish should retain
coherent pigment and coating response. A stale endgrain grade can make a newly
upgraded face look unfinished. If only color is wrong, retain accepted normal
and roughness channels rather than rebuilding them without cause.

On an observed weak response, check the actual consumer, composed normal route,
UV channel and map identity before increasing relief. If native consumption is
uncertain, use one fixed-lighting comparison with other channels held constant.
Keep both images and their matching native receipts before reusing a capture
helper's output path; overwritten evidence cannot support a retained proof.

Share materials by actual recipe equivalence, not by product or material name:
species/anatomy, finish, surface orientation, map content, shader response,
physical mapping extent, color/data interpretation and normal/sampling settings.
Shared anatomy can support distinct finished, raw and stained recipes without
collapsing their surface response. Grain direction and phase remain per-part
mapping. A new patch extent needs a corresponding metric UV adjustment to
preserve physical coordinates. Portable packed product libraries may reuse a
common recipe without acquiring an external dependency on its master blend.

For the bounded hardware example and its acceptance limits, read
[the shared-wood lesson](prior-material-lessons.md#shared-hardware-woods).
