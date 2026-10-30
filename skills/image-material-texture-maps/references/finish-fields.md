# Spatial finish: normals, roughness and reflection strength

Use this reference when reconstructing a spatially varied finish, when highlights look uniform despite detailed color/normal maps, or when a user questions roughness or specular variation. It is a cross-stage check, not a demand to make every material patchy or enable every lobe.

## Establish what the image supports

For each relevant layer and region, assess these separately:

| Property | Observable question | Candidate control | Important confounder |
| --- | --- | --- | --- |
| Surface orientation | Do highlights fragment, tilt, or form rims around relief? | Normal, bump or geometry | Painted bright/dark edges and local curvature |
| Microsurface spread | Does reflection broaden or lose local coherence across comparable patches? | Base/coat roughness; anisotropy only if directional evidence supports it | Normal variation, source size, focus and camera blur |
| Reflected amount | Do comparable patches change reflection strength after spread/orientation are accounted for? | Interface coverage, material mixture, physically justified IOR, or a declared reflectance-weight approximation | Roughness changes peak brightness too; Fresnel angle and illumination also change it |
| Reflection color | Is color in interface reflection, the underlying body, or attenuation through a layer? | Layer-specific optical color/absorption where supported | A colored environment or body contribution in beauty |

A roughness map and a specular-amount map are parameter fields, not separate additive lobes. A reflection LPE generally contains their combined effects. Do not label a grayscale parameter sheet as a radiance isolate.

Record evidence/counterevidence, confidence, scale bands, ownership and a map/uniform/unresolved disposition for each applicable property. A uniform choice needs a reason. Do not mark all properties covered because diffuse and reflection images exist. Conversely, a single photograph rarely establishes a unique roughness or reflectance field: keep competing explanations and reject invented polish or coating that contradicts the source.

For a homogeneous dielectric, normally keep IOR physically coherent. Do not turn source luminance into an arbitrary IOR, metalness or specular-weight texture. If patchy glaze, varnish, contamination or wear is supported, separate its coverage from its own roughness. If an artistic specular-weight approximation is needed, name it as an approximation, bound it, and verify its angular behavior. Inspect installed input definitions and native influence rather than assuming universal socket semantics. Distinguish literal fractional area coverage, a renderer's coat-weight model, and an artistic specular-weight adjustment; connecting a mask to coat weight does not by itself prove a physical area mixture. Record the selected meaning and approximation.

## Generate discriminating appearance studies

Carry the source crops, accepted morphology, material scale and fixed specimen/lighting into the prompt. For unresolved finish, use a compact contact sheet that tests the plausible causes independently. Useful cells are a uniform-finish control, spatial roughness with strength held fixed, spatial strength/coverage with roughness held fixed, and the combined candidate. Keep normals, pigment, light shape/position, exposure and camera unchanged. Include a reflection-only prediction or paired beauty/reflection studies where it helps distinguish the causes.

Describe the expected visual difference in concrete terms: which regions have broader/less coherent reflections; which have reduced coverage or weaker reflection at similar spread; where the finish remains smooth and uniform; and which boundaries are shared with relief or pigment. A request for “more complex specular” is insufficient. Avoid generating a new random mottled layout in every cell. Inspect whether the generator actually preserved the locked factors; reject or mark uncontrolled cells rather than treating persuasive highlights as evidence.

Use the generator to make independent intrinsic field candidates from the accepted layout and selected hypotheses. Request roughness and strength/coverage separately when a sheet would compromise alignment or resolution. Do not accept a beauty crop, reflection isolate, or inverted height as either field. A height correlation can be physically justified locally, but is not a substitute for independent finish variation at other supported scales.

## Define and inspect field contracts

For each field record:

- Layer/property meaning and exact source evidence; generated parent/layout IDs and preserved anchors.
- Macro, intermediate and fine populations, including deliberate uniform regions; physical patch size or relative scale uncertainty.
- Polarity and scalar channel; measured encoding/bit depth; raw-data treatment; calibrated range and remap. Requested precision is not actual precision.
- Correlations that should exist and those that should not: pore interiors may share boundaries while broad finish patches remain independent of pigment and pore noise.
- Separate controls for field amplitude, frequency, offset and coverage; avoid one overloaded grayscale mask driving every property identically.
- Exact source-to-socket path, neutral/constant comparison value, intended visible influence and rejection criteria.

Inspect the field at feature scale and in a native preview. Nearly uniform remaps can erase a visually rich generated field; excessive contrast can invent a damaged or wet finish. Record final ranges and spatial distribution after all graph operations, not only original image histograms. Check for baked lighting, directional bright edges, tiling, unmotivated anticorrelation and loss of intermediate-scale structure. Strong correlation is neither proof of registration nor of correct physical causality.

## Prove that the fields work

Use immutable candidate files and fixed geometry, light, exposure, display and all unrelated inputs. For consequential finish controls, inspect:

1. Neutral-color normal ON/OFF with the same roughness and strength. Show the defining relief at final display resolution and a useful closeup. A connected bump socket or purple texture alone does not pass. If a valid derivative-based bump has no native influence, test a supported explicit normal representation and its basis; record the capability gap instead of hiding it with pigment.
2. Spatial roughness versus a declared constant roughness, holding normals and strength/coverage fixed. Inspect the native reflection pass and beauty for the predicted regional spread/coherence change.
3. Spatial strength/coverage versus its declared constant, holding normals and roughness fixed. Inspect the predicted reflection change and any coupled body attenuation. Coat coverage changes can have coupled effects; do not pretend they are a pure additive intensity knob.
4. The combined candidate, checking that one field has not erased another. Where both fields are consequential, a four-cell uniform/roughness-only/strength-only/combined ablation is useful. Do not require redundant cells for properties justifiably uniform.

Use exact parameter constants or declared field averages as controls, not per-pass exposure normalization. Averages are only controls, not claims of energy equivalence through nonlinear shading. Reflection peak brightness alone cannot identify strength: roughness, normals and masking also affect it. Compare local profile/footprint and relative or integrated response on matched patches; if geometry confounds the comparison, use a separately labeled planar or curved diagnostic specimen. Retain the user's standard ball and rig for the primary result.

Keep linear native data for meaningful numeric comparisons and use one display treatment across comparable previews. Inspect both direct appearance and image differences; a nonzero delta caused by noise does not prove the intended effect. For final-size detail, compare actual output sampling and denoising, not only a supersized closeup.

## Compare the prediction with native reflection

Place source crop, generated finish prediction, actual field previews, and native reflection/ablation crops together. Mark comparisons controlled, matched qualitative or unmatched qualitative. List the predicted region/behavior and the observed delta: missing contrast, incorrect highlight width, wrong patch scale, strength/width confusion, overcoating, normal suppression, or invented source structure. Route the earliest failure to analysis, prompting, field generation, calibration or wiring.

Record each field as generated-unreviewed, mapped-unproven, influence-proven, source-consistent/provisional, or rejected as appropriate. These are different claims. Do not promote a full reconstruction while defining finish variation remains unassessed, its map is absent, its final graph remap suppresses it, or its generated prediction has never been checked against native behavior. Preserve honest uncertainty when a single source cannot distinguish mechanisms.

## Check correlations at the scale where they have meaning

State the expected relation separately for broad finish regions and local feature boundaries. For example, a hypothesis may predict greater coating amount over smoother broad regions while permitting independent fine variation. A whole-image correlation can conceal a wrong broad relation behind aligned fine noise. Inspect matched regional averages or low-frequency previews and representative shared boundaries; use numbers as supporting diagnostics, not as proof of causality. Do not impose a correlation just because it makes a stronger image.

If the generated field reverses a justified polarity, keep the rejected original and choose a targeted regeneration or a documented numeric remap when that fully preserves the accepted semantics. Verify endpoint meanings, effective range, intermediate values and the native response after the correction. Inversion cannot repair different boundaries, invented structure or a wrong physical hypothesis. Record the operation in the source-to-socket path so the next agent does not invert it again.
