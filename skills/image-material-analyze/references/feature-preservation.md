# Preserve observed detail across stages

Use this record when identity depends on small features or a revision risks changing previously accepted structure. Keep it in the case, not in a material-specific skill. Read the source at the intended viewing scale and in representative closeups before choosing descriptive words.

## Describe morphology, not just a material label

For each defining feature family, assign a stable feature ID and record:

- **Evidence and location:** source/crop IDs, representative anchors, region, visibility limits, confidence. Include a typical instance and a meaningful exception; do not extrapolate from one attractive patch.
- **Shape:** roundness versus angularity, elongation, direction, irregularity, branching, continuity, and connected versus separate marks. Preserve what is visible; do not make every pore circular or every scratch straight.
- **Boundary and profile:** sharp or softly rolled edge, rim width relative to feature width, depression/raised/flat interpretation, and whether a colored halo is pigment, reflection, or unresolved. A dark center is not sufficient evidence of a cavity.
- **Population:** relative size range, small-to-large balance, spacing, clustering, density changes, overlap and empty areas. Prefer ratios to nearby features when physical size is unknown. Do not invent measured distributions from prose.
- **Appearance and relationships:** color family, local contrast, which features interrupt reflections, which are pigment-only, and which boundaries should coincide across properties. State deliberate offsets, such as a stain extending beyond a recess.
- **Scale and representation:** macro/meso/micro band, coordinate field, provisional units if needed, geometry/map/scalar decision, affected layer and channel IDs.
- **Preservation:** features locked for this experiment, permitted changes, specific drift to reject, inspection view/crop, and a tolerance justified by visible feature width and intended output scale. Leave numerical tolerances unset when unsupported.

A useful statement is “isolated shallow depressions with rounded but uneven outlines and narrow soft rims, interspersed with much smaller flat pigment dots.” “Highly detailed porous surface” discards the distinctions the next stage needs. This example does not prescribe pore morphology for other references.

Record negative evidence selectively: a region has no visible crack network, directional scratches, or large raised grains where a generator is likely to invent them. Negative constraints should prevent an observed or plausible drift, not become a generic list of everything absent.

## Give evidence and synthesized structure different authority

The source determines visible identity and morphology. A selected layout guide determines downstream coordinates for synthesized or rectified coverage. An accepted study constrains only the behavior it successfully demonstrated. A rejected output illustrates a defect; it is never a replacement identity reference.

Use explicit priorities if attachments conflict. Reattach the original source or relevant source crop at generation boundaries, especially when deriving maps from studies or revising a previous map. A long chain that references only the latest output can amplify its mistakes. If a source crop has different perspective from the layout, use it for shape/statistics only; preserve coordinates from the layout guide.

Fix feature family, proportions and distributions even where exact unseen coordinates must be synthesized. Once a synthesized layout is accepted, use that revision consistently for shared features. Source morphology and pixel registration are distinct checks; matching centers does not establish matching contours or correct physical meaning.

## Carry constraints into every handoff

For each prompt, select the relevant feature IDs and write their concrete visible constraints into the submitted text. IDs alone have no meaning to imagegen. Store the evidence-to-prompt mapping and exact attachment roles in `prompt_contracts`.

After generation, add a `feature_checks` record for every selected defining feature: artifact/version, inspection crop or view, preserved/changed/lost/unassessed finding, relation to source, and next action. Evaluate a generation on these observations, not on the quality of the prompt. Failed defining features cannot be silently promoted to spatial authority.

Distinguish alignment from morphology. Sample matched contours, rim widths and aspect ratios as well as centers; compare population statistics and detail at actual output scale. Use measurement only where segmentation, perspective and sampling justify it. Otherwise record a concrete visual finding. Tiny contact-sheet cells cannot establish subpixel or microdetail preservation.

## Revisions must not trade one failure for another

Before requesting “sharper,” “richer,” or “more complex,” identify the property to change and the accepted properties to lock. Sharpening must not introduce angular contours, halos, embossed grain, or extra cracks. Increasing color richness must not alter roughness or invent a tinted coating.

Compare each successor against both the source and the last accepted candidate. Record regressions even if one feature improved. A defect seen in the color map may dominate the apparent shape of otherwise rounded geometry: compare height, intrinsic color and neutral-color rendered relief separately before increasing tessellation or changing roughness.

Keep a `revision_log` entry with changed/locked features, rejected defect, selected artifact IDs, and downstream artifacts/checks invalidated by the revision. Reinspect affected layers and re-render affected behavior. Preserve historical results as historical; a check of an older palette or layout does not certify its successor. If a layout changes, update all consumers or explicitly mark incompatible revisions.

## Compile a feature packet that can survive a handoff

For each identity-defining family, attach a representative source crop and write a concrete constraint with shape/profile, relative size, arrangement, smooth surrounding area and affected properties. Include a contrasting family or exception when it changes interpretation. In transparent objects, flag possible back-wall images before treating overlapping marks as one surface's population. Give a crop role and visible region, not a bare feature ID.

Carry the packet into both appearance and data prompts. Verify its clauses in the exact submitted prompt and inspect them again in the result. If detail is too small in a sheet, request a dedicated closeup. A source anchor omitted by an attachment limit must remain an explicit unresolved constraint, with a focused follow-up generation when consequential. Do not silently drop it.

Compare arranged motifs by their design relationships as well as their contours. Scale adjustments that make circles round can still alter counts, repeat rhythm or neighboring symbol families. A feature packet can be complete while its generated realization fails; keep those statuses separate.
