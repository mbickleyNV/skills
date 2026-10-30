# Plan controllable surface complexity

Read this for surfaces with multiple color sources, coatings, wear, inclusions, or interacting scales. Build complexity from visible relationships and useful independent controls. A single photograph can support a layered working model without proving its composition.

## Distinguish three kinds of structure

| Structure | What it means | What to preserve |
| --- | --- | --- |
| Color composition | Several pigment fields, stains, motifs or inclusions contribute to intrinsic color within a body | Separate colors, coverage, spatial scales and mixing intent where they need independent adjustment |
| Physical layer stack | A coating, film, fiber layer or other optical interface sits above a substrate | Order, coverage, optical response, normals, thickness/absorption assumptions and interactions |
| Spatial regions | Neighboring or exposed materials occupy different parts of the surface | Boundary/transition structure, material assignments or supported mixtures, and transitions in relief/roughness |

These are not interchangeable. A clearcoat does not make a flattened color texture into a multi-component pigment construction. Several mixed color maps do not establish several physical optical layers. A dark region does not automatically require metalness, cutout or absorption.

## Assess subtle coatings without equating matte with bare

When a finish could be coated, retain a thin conformal or rough coating as a rival to an uncoated interface even when no sharp clearcoat highlight is visible. A coating may follow grain, soften only its smallest scales, pool locally, or have a matte microsurface. Lack of a broad smooth highlight is not evidence of absence. Conversely, grazing bright edges alone do not prove coating: curvature, Fresnel response, subsurface transport, and illumination remain alternatives.

Inspect highlight continuity across pigment boundaries, response on ridge tops versus recesses, local smoothing or bridging of texture, coverage transitions/wear, and whether a single rough interface can explain the observed angular response. State which cues are visible and which are unavailable; do not claim chemical glaze or measured thickness from appearance alone.

Compare plausible bare, thin-conformal and partially smoothing coating hypotheses with the same pigment, accepted substrate relief, light, exposure and camera. Avoid using a thick wet clearcoat as the only coated alternative. Carry the actual hypothesis into imagegen: describe layer order, conformity, coating roughness/coverage, intended base-versus-coat normal relationship and preserved fine structure. A coating can be uniform; require maps only for supported spatial variation.

Test native coat removal and a relevant base/coat normal or roughness control. Inspect reflection and beauty, including coupled body attenuation, under the established rig and a separately labeled revealing angle if needed. Select for source fidelity, retain unresolved alternatives, and record whether the installed coat model approximates a real stack or only its visible response. See [finish fields](../../image-material-texture-maps/references/finish-fields.md) for separate spread and strength tests.

## Author a layer plan before requesting maps

Give each meaningful component a stable layer ID. Record evidence, role, above/below or neighboring relationships, coverage authority, owned properties, geometry relation, coordinate field, scale band, independent controls, uncertainty and a native test. Route unsupported physical interpretations back to analysis.

Choose enough components to make defining features controllable. Depending on evidence, these might include broad body coloration, finer pigment variation, sparse inclusions, localized staining, exposed substrate, coating coverage and fine surface orientation. These are possibilities, not a required stack or a fixed channel count. An evidence-supported simple surface can remain simple.

Separate broad gradients from repeatable detail when tuning one must not move the other. Keep independent pigment-only variation separate from relief. Where actual cavities have distinct local pigmentation, share a feature/layout authority but keep pigmentation and cavity depth independently adjustable. Do not paint geometric shadow into color just to make a cavity legible.

For each interaction ask:

- Does an upper layer conform to, smooth, bridge, pool in, or break around the lower structure? What observed cue supports that choice?
- Does wear remove coating, expose another body, deform geometry, or merely alter gloss? Which effects share a mask and which need distinct boundaries?
- Does color vary because of pigment, coverage, illumination, or potentially thickness-dependent absorption? Which interpretation can be tested?
- Which properties covary, and which must remain independently adjustable? Reusing one noise field everywhere creates false correlation.

## Specify mask meaning and combination explicitly

A mask has an owner, polarity, coordinate field, layout revision and semantic meaning. Material coverage, pigment concentration, coat amount, depth, and cutout opacity are different quantities. Record which feature IDs generate or constrain it and which other masks share or intentionally differ from its boundary.

State the combination operation and ordering. A linear-light color mix, multiplicative tint, coverage blend of materials, and physical layer composition produce different behavior. Choose the operation from the intended meaning and document approximation; do not default to multiplying every map. Do not normalize masks for unrelated stacked phenomena as though they were exclusive neighboring regions. For exclusive mixtures, validate coverage/overlap and the supported mixing model.

Use supported shader/BSDF layering or material assignments for distinct optical behavior when available. Check the installed definitions and renderer support before choosing nodes. Do not implement a purported optical stack by blindly adding reflected energy or by averaging all parameters. A simpler approximation is acceptable only when its lost behavior is explicit and the requested fidelity permits it.

## Generate components, then prove their interaction

Ask imagegen for registered component maps or masks tied to the shared authority, with irrelevant features excluded. A full-color study can guide the target while editable components build it. Retain generated originals and document any permitted extraction or physically defined derivation. An imagegen mask is an uncalibrated candidate until inspected.

When a composite is sufficient, record why independent controls add no useful distinction. When the workflow needs independent controls but they cannot be recovered, keep the composite provisional rather than labeling it layered. Baking for delivery can follow validation; retain the editable construction and document what the bake loses.

In assembly, expose meaningful controls for component color/coverage/scale and layer roughness/normal response. Test a component disabled, exaggerated or isolated in a diagnostic preview to confirm where it acts; restore the candidate afterward. Check that adjusting a macro gradient does not unintentionally resize pores, and changing pore depth does not repaint pigment. Native layer toggles show causal influence, not additive isolated energy.

Review both component and combined results. A component can be plausible alone but become hidden, overly correlated or physically inconsistent when combined. Declare how many color components, physical layers and spatial materials were actually implemented; name any collapsed or unsupported part of the planned model.

## Preserve the relationship between interfaces

For consequential layer interactions, name what each interface inherits and what it changes. A conformal outer layer may inherit substrate slopes; a smoothing layer may attenuate only selected scales; its own microtexture can remain independent. Describe that relationship in the generated study and the map/graph contract rather than asking generically for a second normal map. Keep layer coverage, slope smoothing and microsurface roughness separately controllable when the evidence distinguishes them.

Inspect the interface alone through an appropriate ablation and then in the combined construction. A smoothing change can hide substrate detail; changing coverage can alter both reflection and body attenuation. Choose a control that tests the disputed relationship without simultaneously changing pigment, unrelated slope amplitudes and illumination. Additional layers count as useful complexity only when their intended interactions survive the combined render.


## Distinguish finishing processes from additional optical interfaces

A polished region can be the same exposed conductor with a different slope distribution; it does not establish a dielectric coating. Compare rough recesses and smoother upper regions with a transparent-interface hypothesis when the evidence is ambiguous. Preserve independent roughness and normal ownership in either construction. An opaque metallic film may hide an underlying textile's visible weave while inheriting its crinkles: do not expose coarse yarn topology simply because the product is called fabric. Keep large drape/silhouette folds in the geometry contract.

A bright substrate may make a valid low-reflectivity outer interface subtle in the combined view. Inspect both the intervention and the combined image; do not inflate IOR merely to advertise layering. Test a compound mixture with both endpoint controls in the native renderer. Black finite output at both endpoints is failed execution evidence, even if the document validates and the renderer reports convergence. Retain the failure and a separately validated candidate; do not silently substitute parameter interpolation and call it the same optical construction.
