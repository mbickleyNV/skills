---
name: image-material-review
description: Compare a reconstructed material against its source, generated lobe hypotheses and native render passes; diagnose fidelity failures and drive targeted revisions. Use before accepting an image-derived material or when its color, roughness, relief or layers look wrong.
---

# Image Material · 7 · Compare and refine

Read the [shared case contract](../image-material-analyze/references/handoff.md), fidelity target, mechanism inventory and actual source/generated/native images. Verify what was executed. A caption, graph validator or reported convergence cannot replace viewing the results. For review-only requests, diagnose available evidence and identify missing experiments; do not fabricate them.

## Establish a fair comparison

Read [comparison and acceptance](references/comparison.md). For visual comparison, use available source crops, generated hypotheses, native beauty and passes/ablations in a compact sheet or comparison view. Include revealing closeups when available. In a narrow review, identify missing evidence without inventing cells or generating new assets outside the requested scope. Keep source, generated, native and display-preview roles explicit.

Compare the original source first for identity, color family, structure and scale. Then compare generated predictions to native behavior. A generated lobe is a hypothesis and may be wrong; do not improve its match by making the actual material less faithful to the source. Diffuse response includes illumination and relief shading; it is not unlit base color. LPE event categories are not independent physical layers.

Classify comparisons as controlled numeric, matched qualitative, or unmatched qualitative. Document geometry, camera, feature scale, light, exposure and display differences. Use numerical image deltas only when correspondence and encoding make them meaningful; otherwise describe localized visual deltas and propose a controlled experiment. Never normalize each pass independently to make it look convincing.

## Decide source fidelity before crediting mechanism coverage

Inspect source and native result before reading the case's success claims. Use
comparable feature footprints and original context; apply the
[detail pilot](../image-material-detail-pilot/SKILL.md) to defining fine structures.
A differently magnified field/native crop beside a complete source swatch is not
sufficient for morphology or density acceptance.

Report `execution`, `mechanism_influence` and `source_fidelity` separately.
Connected inputs, visible glints, successful ablations and many generated images
can establish useful technical progress while source fidelity fails. A failed
identity-defining criterion is a veto on overall material acceptance; do not
average it away with other successes or call it merely a polish limitation.
“Plausible member of the material family” and “faithful to this source” are
separate findings. Put the strongest defining failure first and route the earliest
loss. Additional complexity must address that observed loss.

## Check optical semantics before judging resemblance

Read [transport semantics](../image-material-lobe-prompts/references/transport-semantics.md) for radiance comparisons. Check the actual expression, object scope, retained later events and renderer settings against the generated contract. Apply its scene-specific falsifiers. Background distortion, retained internal structure and exclusion of camera-first reflections matter more than a generic “glassy” appearance. Highlight presence alone does not reject transmission. A matched clear/absorbing pair tests attenuation; an absorption-colored panel cannot be added as another lobe. Reject mislabeled or uncontrolled studies before their appearance becomes a shader target.

## Audit coverage and fidelity

Check the mechanism ledger and per-input audit against the actual graph, generated studies and native evidence. Unassessed active inputs, missing representations and untested claimed layer controls remain explicit gaps. Every active and consequential uncertain mechanism needs an inspected study/test or a concrete unresolved limitation. Do not count two event-class images as coverage of all physical layers. Check each defining feature at macro, meso and micro scale, including interactions between layers.

Use pass/fail/uncertain findings tied to image regions and evidence. Judge identity and layout; color/contrast; highlight width and angular response; layer/coverage behavior; physical depth; grain scale and detail; alignment/seams; and changed-light robustness where relevant. One beautiful hero view cannot cancel a failed defining feature. Mark quality acceptance separately from technical validity.

## Audit preservation and layered control

Read [feature preservation](../image-material-analyze/references/feature-preservation.md). Compare source, last accepted candidate and current output at the same meaningful detail scale. Check contours and rim profiles as well as positions, feature populations and optical response. Verify the prompt actually carried the details that drifted. Inspect color-only and neutral-color relief controls when painted boundaries and physical shape disagree.

For defining fine structure, review the [detail targets, sampling checks and native pilots](../image-material-texture-maps/references/detail-reconstruction.md). Require a source/selected-field/native crop chain at comparable feature scale. Report presence, morphology and rendered visibility separately: a fleck mask can be present while its profile is wrong or the final feature is unresolved. A hero image alone cannot close that finding.

Audit the planned [layer architecture](../image-material-analyze/references/layer-architecture.md) against the actual graph. Confirm independent controls and intended mask relationships, and inspect combined interactions. Do not accept a flattened color composite as fulfillment of a multi-component construction. Keep approximation and missing support visible.

Record revisions and downstream invalidation. An old alignment, color or ablation result applies only to its tested artifacts and conditions. Recheck affected behavior after changes, without repeating unrelated tests. Preserve the strongest accepted candidate when a revision fixes one property but regresses another.


For uniform-looking reflection or disputed normal detail, require the [finish-field comparison](../image-material-texture-maps/references/finish-fields.md): source → generated prediction → field → graph remap → native reflection/beauty, with matched normal, roughness and strength/coverage controls for consequential properties. A detailed normal map cannot close an untested roughness or reflected-amount finding. Distinguish field existence, native influence and source consistency.

## Turn deltas into the next experiment

For each consequential failure record: source observation, generated prediction, actual native behavior, confounders, likely cause plus plausible alternative, discriminating test, and destination skill. Locate the earliest inspected artifact or conversion where the defining cue is lost. If a motif exists in the map but disappears in the render, test mapping, scale, profile conversion, representation and sampling before replacing the map. Conversely, downstream parameter tuning cannot restore a feature absent from the spatial authority. Prioritize the defining discrepancy with greatest perceptual impact. Hold unrelated variables fixed when diagnosing it.

- Unsupported interpretation or invented features → [analysis](../image-material-analyze/SKILL.md).
- Missing coverage, ambiguous layer response or failed generated controls → [lobe prompts](../image-material-lobe-prompts/SKILL.md), using a focused contact sheet or edit.
- Wrong spatial structure, frequency, correlations or numeric data → [texture maps](../image-material-texture-maps/SKILL.md).
- Wrong representation, collapsed layers or missing defining depth → [architecture](../image-material-architecture/SKILL.md).
- Encoding, light/display, thickness-dependent color or confounded parameter fits → [calibration](../image-material-calibrate/SKILL.md).
- Wiring, binding, basis, units or ignored inputs → [assembly](../image-material-assemble/SKILL.md).

After a correction, inspect the affected pass and beauty and recheck previously accepted defining features. Preserve candidates and record rejected changes; do not repeatedly regenerate without a new testable distinction. Add only conditional, evidence-backed lessons to the case knowledge graph.

## Completion

For full reconstruction, continue while important failures have actionable tests and authorized resources remain. Do not self-impose a one-correction limit or silently lower a high-fidelity target. Stop when defining criteria pass under the agreed views/lights, the user's budget/scope ends, or a concrete missing capability/input prevents meaningful progress. In the latter cases report a prototype or blocked component, not a finished material. An explicit preview request can complete with unresolved quality findings clearly labeled.

Deliver the artifacts appropriate to the requested stage: for reconstruction, one representative image, a linked comparison, and editable material/maps; for review-only work, available evidence and actionable findings. Include the most important remaining uncertainty, how to try the next step, and a human decision: Try it, Keep it, Fix it, Drop it, or Blocked. Exact LPE recomposition is not required. A review pass establishes the declared visual target, not unique recovery of the real material.

Review local morphology and global distribution separately. Route correct shapes with incorrect placement, missing intermediate-scale populations, or accidental correlation of different properties to [spatial design](../image-material-spatial-design/SKILL.md). A passing closeup pilot can coexist with a failing hero distribution. If an effect is absent in native output, retain the declared-versus-observed capability gap instead of crediting the connected socket.

For curved transfer or turntables, review the [coordinate-transfer views](../image-material-spatial-design/references/coordinate-transfer.md) before promoting a front-view success. A fallback or failed material execution is excluded from optical deltas; return it to assembly. Keep a failed generated illustration distinct from rejection of the physical hypothesis it was meant to test.

Audit the [diagnostic plan](../image-material-diagnostics/SKILL.md) row by row. Distinguish documented, returned, positive contribution and controlled semantic verification. Match original/control versions in both the selected pass and beauty; aggregate diffuse/reflection or empty unrelated outputs cannot close unresolved mechanism rows. Source fidelity remains separate.

When the user selects a generated hypothesis as the visual target, assess that explicit target separately from source-photo fidelity. Use [detail retention](../image-material-detail-pilot/references/detail-retention.md) for target/field/effective-graph/native comparisons and retain unresolved detail failures.

For hex/triplanar revisions, apply [mapping-blend review](../image-material-spatial-design/references/mapping-blends.md): inspect structured and production textures, transitions and continuous motion. Separate less ghosting from sharper boundary artifacts; still-only improvements remain provisional. If cloth reads as veins, inspect [coherent deformation](../image-material-spatial-design/references/coherent-deformation.md) and locate the first wrong morphology before increasing normal strength or gloss.
