# Distinct populations need distinct response hypotheses

Use when a material has overlapping directional structures, mixed particle sizes,
separate optical populations or a defining structure that one surface response
fails to express. This is a representation branch, not a material-type recipe.

## Describe what is visible before choosing components

For each consequential population record shape/connectivity, width and length
spread, spacing/coverage, orientation spread, interruptions, layer/depth and quiet
regions. Choose a few descriptors that discriminate the actual candidates rather
than filling every field. For unresolved fine texture use aggregate observations;
do not infer exact fiber cross-sections or chemistry from a product label.

For a directional surface, check whether it contains one direction, crossing
directions, curved bundles, interrupted segments or locally disordered structure.
Do not replace that observation with a single global tangent just because the
shader offers one. For grains, inspect whether the highlight belongs to a flat
facet, rounded bump, rim or internal inclusion. Sparse bright marks alone do not
establish metal, relief or low roughness.

## Select a supported representation

| Visible requirement | Candidate construction | What must be tested |
| --- | --- | --- |
| One resolved shallow structure without depth-dependent occlusion | Independent height/normal field and appropriate finish | Profile and aggregate response survive final sampling |
| Distinct directions or optical populations | Region-specific tangent/material fields where resolved; supported BSDF mixture for unresolved populations | Mixing actual responses differs from averaging roughness, metalness or tangents; no accidental direction cancellation |
| Over/under relationships, cavities, loose silhouettes or parallax | Supported displacement, separate surfaces, strands or particle geometry on a labeled proxy | Depth and shadow behavior improve the source match at the delivery scale |
| Subpixel microstructure | Supported aggregate/fiber/microflake response with scale-aware statistics | Resolved-to-unresolved transition retains appropriate sheen/glint distribution rather than becoming smooth or noisy |
| A smooth finish above structured substrate | Separate base/coat normal and finish controls within supported layer composition | Substrate detail survives while the outer interface remains appropriately smooth |

These are hypotheses to test, not a mandatory escalation ladder. Use the smallest
construction that reproduces the visible requirement. Keep benchmark geometry
unchanged when requested; a geometry-rich diagnostic must not quietly replace it.
If the installed MaterialX/renderer path cannot express a required mixture or
geometry, name that capability gap and the approximation it forces.

For opposing tangent directions, remember that an axis is not a directed arrow;
naive vector averaging can cancel equivalent orientations. For crossing
populations, one average tangent can erase two response peaks. Conversely, two
different spatial colors do not necessarily require two BSDFs. Choose separate
responses only for a consequential observed or tested distinction.

Keep population ownership coherent. A metallic strand region may own color,
roughness, normal/tangent and reflected amount together. Replacing it is a
population intervention, not an isolated metalness test. A hue-derived mask is
only a segmentation hypothesis: warm dye, patina, illumination and metallic
reflection may overlap in RGB. Check false positives/negatives on selected source
and layout features, including shaded and neutral regions. Do not let thresholding
turn elongated features into pinholes or assign an entire optical class by hue.

## Verify tactile identity before adding more lobes

Use the [detail pilot](../../image-material-detail-pilot/SKILL.md) to compare
representations at similar feature footprints. Ask what the surface reads as
without its title: soft tangled structure, hard grains, cut grooves, smooth glaze,
or another appearance supported by the reference. Use this as a falsifier, not a
replacement for concrete evidence. A flexible textile that reads as pebbled
rubber still fails even if fuzz, anisotropy and gold glints are demonstrably active.

The [OpenPBR specification](https://academysoftwarefoundation.github.io/OpenPBR/)
defines a particular base/coat/fuzz structure and explicitly leaves some high-end
cloth, hair and volume needs to specialized or bespoke models. This is permission
to test a richer supported representation when evidence calls for it, not evidence
that a particular reconstruction requires one. Its fuzz layer models aggregate
reflection; it does not construct resolved strands. For angular parameter
interpretation, consult the [OpenPBR fuzz documentation](https://help.autodesk.com/cloudhelp/ENU/AR-Core/files/ac-shading/ac-surface-shaders/ac-openpbr-surface/arnold_user_guide_ac_openpbr_fuzz_html.html)
and then verify the installed implementation rather than borrowing another
renderer’s AOV names or assuming matching native support.
