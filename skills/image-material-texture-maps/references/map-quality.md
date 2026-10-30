# Multiscale map quality

For a reconstruction dominated by small features, use [detail reconstruction](detail-reconstruction.md) for the early patch-to-native pilot. The checks below apply to each selected map and its later integration.

## Design correlated properties deliberately

For each defining feature, record its spatial authority, scale, relief representation, affected channels, and intentional independence. A groove may require geometry and exposed-substrate coverage without a permanently painted black shadow. Pores may affect orientation more than pigment. Coat wear may change coverage and roughness while revealing a different base. Avoid cloning the same noise into every channel.

Separate macroscopic gradients/coverage from repeating detail when they need independent scale control. Baking a whole-object color gradient and every pore into one texture couples their adjustment: changing UV frequency also moves or repeats the gradient. Plan distinct coordinate fields, masks, or a supported layered construction before generation when this coupling would prevent refinement. Shared-feature alignment still applies within each coordinate field.

Generate competing map interpretations when the selected studies still leave consequential uncertainty. Use contact sheets for relative structure/variation experiments, then generate clean selected maps separately using the same coordinate guide. Do not confuse numeric data maps with lit previews of their effect. Reanalyze the actual output before deciding downstream wiring.

## Inspect spatial fidelity at three scales

- Macro: region shapes, boundaries, layout, UV continuity, bevels and cavities. Measure anchor offsets in pixels relative to narrow feature widths; a small global error can reverse a thin edge mask.
- Meso: chips, pits, cracks, wear islands and grain clusters. Check paired crops/overlays for contour angularity, aspect ratio, rim/profile, size balance, spacing and density; inspect correlated features and deliberate differences. Coincident centers with different outlines fail a shared-boundary contract. A colored halo may intentionally extend beyond a cavity only when its meaning is recorded.
- Micro: grain frequency, orientation, amplitude distribution and sampling. Check at intended render scale and closer; look for blurred noise, aliasing, oversized pebbles and repeated motifs. Resolution alone does not establish fidelity. Separate missing source information from generator resolution limits, UV stretching, geometric undersampling, filtering and denoising. If the generator returns fewer pixels than requested, reassess the smallest defining feature; export/upscale cannot establish recovered detail.

Check physical texel aspect on the actual evaluation mesh. A square image wrapped around a cylinder whose circumference is twice its height stretches pores unless the mapping compensates. Inspect cut faces, caps, poles and UV islands before fitting material parameters; borrowed shader balls can contain unmapped or degenerate regions. Repair the coordinates or use a separately labeled diagnostic specimen, and keep any geometry change explicit. Preserve a user-locked primary benchmark; a diagnostic does not replace it.

For periodic maps inspect a repeated layout and both opposite edges, including derivative continuity for height/normals where relevant. State acceptable discrepancies for the intended view; do not declare seamless from a center crop. For unique maps inspect atlas seams, padding and filtering instead. Preserve registration transforms and invalidate prior checks when the layout changes.

## Verify numbers independently of the prompt

Record actual file format, bit depth, channel meanings, min/max and representative-region distributions. Compare observed values with intended behavior before choosing a remap. Use documented deterministic processing only when supported and allowed by the host. Preserve originals, operation order and a revised artifact ID. Numeric export does not recover lost precision or missing structure.

For generated height, inspect cross-sections through representative features rather than judging a convincing embossed appearance. A declared symmetric depression should descend from the same land height on every side; consistent bright crescents or raised rims can be baked lighting. Test whether values exceed the intended neutral plane and whether nominally flat lands drift. Use asymmetry only when the geometry hypothesis supports it. Request a targeted data-profile correction before wiring a shaded grayscale picture as height.

For roughness, bracket reflection width/contrast under fixed lighting after color/data calibration. Confirm whether the target expects perceptual roughness or a microfacet parameter; do not pre-square a value when the shader already performs its own conversion. Avoid compensating for broad white reflection by desaturating base color.

For generated normals, decode using the declared convention and inspect vector lengths, hemisphere and feature gradients. Compare slopes across known ridges and valleys with height and tangent directions; test both texture axes in a native light response. Positive blue or unit-length vectors do not prove correct orientation. Prefer normals derived from accepted height with physical scale through a permitted deterministic path. If direct normal generation is necessary, keep it provisional until these tests pass. An axis correction requires evidence and reinspection, not a habitual channel flip.

## Keep semantic acceptance separate from numeric validity

Record `identity`, `data_semantics` and `registration` independently for each
consequential generated field. Passing bit depth, range, raw encoding or alignment
cannot turn an attractive lit illustration into a usable parameter map. When
height still resembles a photographed miniature, keep it provisional until
representative profiles and a neutral-color native pilot support its geometry.
Do not clear this finding by narrowing the range or lowering bump strength.

If fields share feature boundaries, inspect local correspondence at the narrowest
consequential feature, not only whole-image overlap. A regenerated high-resolution
patch can move features even when all labels and dimensions match. Re-establish
its authority before wiring it. Where different populations are intentionally
independent, document that relationship instead of forcing correspondence.

Hue-derived coverage is a provisional segmentation, not proof of optical class.
Inspect likely false positives and negatives, retain thin/partial features, and
check whether exposure, oxide color or warm dye would fool the classifier. A
threshold that eliminates elongated ends or converts strands to dots fails even
if the mask's total coverage matches. Route optical ambiguity to analysis and
population ownership to [architecture](../../image-material-architecture/references/population-models.md).

## Verify physical depth in the renderer

Separate macro geometry/displacement from fine normals. Declare patch size and relief amplitude assumptions. If the runtime cannot render required depth, use supported geometry or explicitly mark a defining limitation; increasing bump strength is not a substitute for deep self-shadowing joints. Verify each representation under grazing light and oblique view. Avoid double counting the same height band in both displacement and normals.

Hand off failed checks as failures. A numerically valid image, aligned large motif, or purple normal map does not establish usable final maps.

## Do not erase profile or design while cleaning the map

A smoothstep, clamp, blur or range remap can preserve centers while changing rim width, cavity shape, land flatness and normal slopes. Inspect representative before/after cross-sections and affected native response. Preserve the raw output and record the processed revision. For geometric features, carry physical height and per-axis surface scale through derivatives; see [representation and scale](../../image-material-architecture/references/representation.md).

Separate designed motif fields from stochastic microvariation and broad region masks. Inspect each feature family on the actual proxy at the intended scale before adding fine noise. If required depressions must alter refraction or shadowing, route the accepted height/layout to supported geometry rather than silently declaring a normal-only result complete.

## Orientation fields and fine facets

A plausible purple normal map can have biased mean direction, invalid vector lengths, painted bevels or excessive tilt. Decode numeric channels, inspect mean/distribution and signs, normalize vectors explicitly where needed, and record any justified bias/strength correction. A field of independent flake normals need not be the derivative of a continuous height surface; choose that representation when the source supports oriented particles beneath a smoother interface. Keep coat normals independent and verify the smooth outer reflection survives. Returning a shaded flake picture is not a successful height-map conversion.

For a scalar field that repeatedly becomes a lit miniature object, try an abstract numerical-field prompt with explicit profile and scale after recording the failure. Such a result remains a synthesized hypothesis: inspect its profile and a native neutral-color pilot. Do not claim source microstructure recovery merely because it avoids obvious objects.
