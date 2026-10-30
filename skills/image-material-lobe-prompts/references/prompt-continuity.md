# Keep generation tied to the evidence

Use the case's [feature record](../../image-material-analyze/references/feature-preservation.md) and [layer plan](../../image-material-analyze/references/layer-architecture.md) for both appearance studies and map prompts. This protocol applies to every consequential generation, including revisions of a previously attractive output.

## Compile a small prompt contract

Before submission record:

1. **Purpose:** the one question or component this image should resolve; mechanism/layer/feature IDs.
2. **Inputs and precedence:** actual image attachments, exact roles, source identity versus layout authority, and the current accepted revision. Explicitly limit rejected examples to illustrating the defect.
3. **Preserve:** concrete shapes, edge profiles, feature proportions, population/spacing, region boundaries and cross-property relationships relevant to this output. Include important absences. Translate IDs into visible descriptions.
4. **Change:** the intended variable, allowed variation, or missing component to generate. For a path-selected study, state which paths are excluded and which later interactions remain; for an ablation state the physical intervention. Do not replace this distinction with “remove highlights.”
5. **Output semantics:** use the [output type and transport contract](transport-semantics.md); distinguish angular illustration, path radiance, ablation, beauty and intrinsic data. Record coordinate field, channel polarity and supported size/format intent where relevant. Numeric calibration remains a later check.
6. **Review:** source crops and representative anchors to inspect, defining drift that rejects the candidate, and native test if generation cannot resolve the distinction.

Use concrete positive constraints as well as exclusions. “No polygonal holes” is weaker than a source-grounded description of contour irregularity, roundness, rim softness and population. Do not generalize a rounded reference into a rule that all materials have rounded features.

For layer studies, describe component relationships and expected visible changes under the declared lights. For a map, carry the same morphology but remove the lighting cues that do not belong in the property. Do not transfer highlights or relief shading from a lobe study into intrinsic color. Do not turn every visible dark mark into height.

## Audit the request after prompt assembly

When a tool wrapper, template or adapter rewrites prompts, check the final exposed
request against the feature contract, including exclusions and attachment roles.
Record the submitted prompt and any observable rewrite; if backend rewriting is
not exposed, mark it unknown instead of claiming the model received identical text.
Do not adopt a blanket surface-only filter that removes required pores, cavities,
strand crossings or seams merely because the same words can describe object geometry.
Assign each feature to geometry, surface fields or excluded scene content first.
For example, excluding the product silhouette can coexist with preserving observed
surface pits; excluding a modeled joint must not erase an accepted weave structure.

Flag contradictions between positive detail instructions and appended negatives
before generation. Resolve them with concrete scale and ownership descriptions,
then inspect the returned feature crop. A clean prompt is a necessary handoff,
not evidence that generation complied. Apply this audit to maps as well as lobe
studies; lighting exclusions suitable for intrinsic data would invalidate a requested
lit radiance study.

Source-informed caution: the optional [surface-only policy](https://github.com/NVIDIA-Omniverse/usd-content-agents/blob/0709377ed35fb066361a0d6735d21984b885fe36/apps/texture_agent/texture_agent/functions/detail_policy.py) demonstrates why adapter exclusions must be checked against feature ownership. Its filter is not adopted here.

## Review before another generation consumes the result

Inspect each contact-sheet cell against its intended control and preserved features. Record partial successes per cell: a useful gloss bracket may still fail morphology and must not become the layout guide. Split dense grids or produce detail studies when the defining structure is too small to judge.

At full-resolution selection and at the study-to-map boundary, repeat the relevant feature checks. The selected cell's visual quality does not guarantee the new generation kept its details. Keep the original source/crops and accepted layout in the next request, not just the latest generated image.

When a multi-reference or multi-panel request copies beauty into a selected contribution, reduce the conflict: edit one actual native contribution directly, use the source only for explicitly limited morphology, and omit the beauty reference if the pass itself already fixes geometry and framing. Name a few decisive preserved/excluded regions. Reinspect; fewer attachments do not guarantee compliance. Never repair the label instead of the image.

Use a targeted correction with changed/locked fields: describe the observed defect, the desired local correction, and the accepted structure to retain. Avoid broad requests to “increase quality” or “add complexity.” If multiple attempts repeat the same defect, change the experiment: simplify the requested component, use a clearer shape/layout guide, or defer the optical question to a native control. Record unresolved features rather than treating a more dramatic image as progress.

The exact submitted prompt and inputs are the reproducibility artifact. Summaries in the case must not replace them. Save a compact feature-to-prompt coverage record so the next agent can see which details were carried, intentionally omitted as irrelevant, or still unresolved.

## Bind studies to the construction plan

Load the architecture's input audit and representation plan. Give each proposed physical interaction a study purpose and a native follow-up: for example, a smooth upper interface over patterned relief, exposed neighboring materials, or attenuation through different path lengths. Use the actual relevant input families in reasoning, but prompt imagegen with visible outcomes rather than unsupported numerical shader promises.

Compile the [feature packet](../../image-material-analyze/references/feature-preservation.md) into literal instructions. Describe the designed distribution and empty/smooth regions, not merely “complex detailed texture.” State which marks belong to the front surface and which may be seen through another surface. For each selected study, explain which property it constrains and which it cannot establish. Good optical behavior with wrong motifs can be a behavior reference, but cannot become map/layout authority.

A contact sheet should buy distinct, inspectable experiments. Split sheets when small cells hide defining profiles or layer boundaries. Keep selected full-resolution successors tied to source crops and the same construction plan. Review any reinterpretation before asking for maps.

## Do not let a failed illustration eliminate a physical rival

Keep the hypothesis verdict separate from the generated cell verdict. If a requested thin rough conformal layer becomes a thick glossy layer, the generation failed its intervention; it did not test the intended physical explanation. Retain any still source-supported rival and use a more constrained generation or a native comparison. Likewise, body-color leakage into a requested reflection-only image is a semantic failure, not evidence for colored reflection. Only the valid aspects of a partially useful image may guide later maps, with their allowed role stated explicitly.

## Protect coherent structure during texture revisions

For folds/drape, translate [coherent-deformation descriptors](../../image-material-spatial-design/references/coherent-deformation.md) into explicit prompt text: shoulder/trough widths, continuity, endpoints, spacing and quiet areas, separately from weave or fine grain. Carry each family's owner and scale through appearance studies and map requests. A rejected veiny example supplies a defect to remove, not new layout authority. Do not ask stochastic tiling to preserve an organized field by implication; freeze that field and generate only the declared local residual. Review the submitted prompt and returned crop for this separation before propagation.
