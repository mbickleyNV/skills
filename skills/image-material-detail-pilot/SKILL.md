---
name: image-material-detail-pilot
description: Test whether defining material microstructure survives source analysis, generated fields and native rendering before expanding the full material. Use when fibers, flakes, pores, facets or other resolved details carry identity, or a plausible shader reads as the wrong kind of surface.
---

# Image Material · Detail pilot

This conditional branch owns the decision to propagate a detail construction.
[Architecture](../image-material-architecture/SKILL.md) chooses candidate
representations; [texture maps](../image-material-texture-maps/SKILL.md) generates
and checks data; this stage tests their combination against visible source
identity. Use it before full-material polish when resolved structure defines the
surface. Skip it for a featureless surface or unrelated optical uncertainty.
Reuse sufficient existing evidence; a review-only request does not authorize new
generation or renders. Planning-only work delivers a proposed pilot with pending
tests, not a passed gate.

## Define a discriminating target

Inspect the source, selected generated field and any native result independently.
Do not let product labels or generated beauty images supply missing observations.
Choose the most consequential feature family and an adjacent quieter region.
Use the [detail procedure](../image-material-texture-maps/references/detail-reconstruction.md)
for sampling, crops and native controls. Record the smallest useful comparison:

`feature/source crop → distinguishing morphology → field revision and meaning →
representation/scale → native crop → verdict → earliest loss → next route`.

Define observable rejection criteria before generation: for example, connected
short strands must not become isolated round grains, mixed widths must not become
identical beads, or buried facets must not deform the outer interface. Preserve
uncertainty about unresolved interiors; do not replace one invented morphology
with another. Use relative feature widths, aspect, spacing and occupancy when
physical scale is unknown. State which of these are visible versus inferred.

## Separate identity, data semantics and rendering

1. **Identity:** compare feature profile, connectivity, size spread, orientation,
   population and quiet space with the source. Judge resemblance before assigning
   shader meaning. A neat weave, dramatic sparkle or extra fuzz can be a failure
   if absent from the source. If morphology already fails, return to spatial
   design/generation before fitting more optical inputs.
2. **Data semantics:** apply [map quality](../image-material-texture-maps/references/map-quality.md).
   A lit grayscale miniature is not accepted height merely because it has raw
   encoding and plausible contrast. Inspect representative profiles under the
   stated geometric hypothesis and test lighting-shaped alternatives. Reject
   unexplained bright caps, shadow troughs or dark contact seams as geometry.
3. **Native consequence:** use a suitable small source-like patch or proxy with
   the intended scale and basis. Compare the selected representation with the
   relevant disabled/neutral control. Preserve the user's primary benchmark;
   a diagnostic patch or added geometry is separately identified. Inspect the
   expected delivery view as well as a resolved detail view.

Compare similar feature footprints, not simply equally sized image panels.
Record crop rectangles, resampling and the width/count of a recognizable feature
used for alignment. Show original context separately. When absolute scale cannot
be recovered, bracket relative scale and label the comparison qualitative;
do not select a convenient crop and claim a physical match. A full swatch next
to a magnified render cannot pass profile or population checks.

## Choose complexity from a failed observation

Read [population and representation decisions](../image-material-architecture/references/population-models.md)
when one set of parameters erases distinct directional or layered responses.
Compare economical representations only where they predict a visible difference:
mapped relief, independently directed surface populations, supported displacement
or explicit strands/particles, and supported aggregate scattering. Prove the
installed renderer can execute the chosen construction. A specialized shader or
geometry is not automatically necessary for every textile or grainy surface.

If a feature survives the map but not the render, check physical scale, filtering,
normal/tangent conversion, masking, sampling and layer attenuation before asking
for more detail. If geometry is needed for visible occlusion or silhouette, route
to architecture; if unavailable, record that specific limit. Do not intensify bump
or brighten glints to disguise a different tactile appearance.

For consequential masked or combined height fields, use the [relief composition control](../image-material-texture-maps/references/relief-composition.md) before accepting their normals. When fine grain could be a rendering artifact, use the [detail-free baseline](../image-material-calibrate/references/controls.md#test-ambiguous-grain-with-a-detail-free-baseline); this diagnoses the source of variation and does not replace the source-fidelity comparison.

## Decision and downstream validity

Record separate `identity`, `data_semantics` and `native_consequence` findings as
pass/fail/uncertain, with evidence. Propagate the construction when defining
criteria pass at the requested scale, or when the user has accepted the stated
approximation. Pending work may proceed provisionally for independent tests, but
does not establish full-material acceptance. A failed defining feature keeps the
material's source-fidelity verdict failed even when graph execution succeeds.

Pass the selected artifact revisions, scale/basis and control settings to assembly.
Changing layout, feature population, map conversion, coordinate scale or the
representation invalidates the affected pilot. Optical-only edits need not repeat
unrelated morphology checks unless they hide the feature. Review final integration
for regression; a successful patch does not certify the final material.

Route source ambiguity to [analysis](../image-material-analyze/SKILL.md), wrong
shape/population to [spatial design](../image-material-spatial-design/SKILL.md),
invalid fields to [texture maps](../image-material-texture-maps/SKILL.md), missing
physical effects to architecture, and optical calibration to
[calibration](../image-material-calibrate/SKILL.md). Keep failed constructions and
their lessons; do not turn the pilot into another attractive but unused sheet.

When detail has a hierarchy of bundles and finer strands, use [textile construction](../image-material-architecture/references/textile-construction.md). Keep bundle dimensions/packing, fiber scale and aggregate sheen distinct. Diagnose the designated structure field before faulting a properly unlit intrinsic color map.

For an approved hypothesis that becomes flat or weak in the native material, use [detail retention](references/detail-retention.md) to inspect effective graph values, scale populations and independent interface response before promoting the result.
