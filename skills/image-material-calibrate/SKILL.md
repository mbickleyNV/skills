---
name: image-material-calibrate
description: Diagnose color, thickness, roughness, scale and lighting confounds with controlled renderer experiments before fitting an image-derived material. Use when a plausible shader looks wrong or a fit must transfer between a benchmark and product geometry.
---

# Image Material · 5 · Calibrate and fit

Make parameter changes interpretable. Read the case's accepted artifacts, architecture, runtime capabilities and [shared handoff](../image-material-analyze/references/handoff.md). Use the installed official rendering path. This skill provides experiment design, not a runtime client. Planning-only work can deliver an experiment plan with all executions pending.


For ambiguous or spatially varied highlights, use [finish-field controls](../image-material-texture-maps/references/finish-fields.md). Calibrate roughness spread separately from reflection strength/coverage with normal structure fixed; account for peak-brightness coupling, Fresnel angle and source shape. Report the final field range and visible response, not only input image statistics.

## Establish the comparison conditions

Read [calibration controls](references/controls.md) to separate texture interpretation, display and illumination. Record scene units, physical geometry, lights, exposure, working/output encodings and display transform. Unknown settings stay unknown. Reuse controls while their dependencies remain unchanged. A major color mismatch is a reason to test the pipeline, not to apply an assumed inverse gamma or arbitrary saturation multiplier.

Preserve the established shader-ball benchmark. For spatial layout, transmission or subsurface targets, add a source-like proxy with explicit thickness/geometry assumptions. Use both fixtures for different questions. Record any geometric, material, UV, light or display change between trials. Matching a product proxy does not retroactively validate the shader ball, or vice versa.

## Separate uncertain causes

Read [parameter fitting](references/parameter-fitting.md) when color depends on thickness, several parameters can explain one cue, or artistic tuning improves only one view. List a small set of competing causes, predict their different responses, and choose a revealing experiment. Test decisive controls before broad parameter sweeps. Use contact sheets to compare controlled native brackets; imagegen studies remain qualitative predictions.

Fit the coarsest defining errors first: geometry/scale and layout, then broad optical behavior, then layer interactions and fine response. This is an adaptive order, not a mandatory full rebuild. Do not tune microsurface roughness to hide an incorrect feature population or absorption to hide a wrong base cross-section. Preserve the best candidate while rejecting compensating fits.

## Verify controls and transfer

For important inputs, prove native influence under a revealing light or view and restore the candidate. For interacting layers, compare the combined result and meaningful interventions; an ablation is causal evidence rather than an additive lobe. Check unsupported paths and inactive branches before changing values aggressively. Test the suspected input at a useful scale; a near-zero difference may reflect sampling rather than ignored wiring.

Evaluate a selected candidate under an independent condition capable of exposing the disputed cause: a different thickness, grazing angle, light angular size, patterned background or layer toggle. Keep material parameters fixed during that check. Select conditions by the hypothesis; do not render every possible permutation. State residual mismatch and non-identifiability when available evidence cannot determine a unique solution.

## Handoff

Write tested controls, chosen parameters with units/conventions, fixed versus inferred quantities, support/limitations, dependencies and invalidation triggers into `calibration` and `experiment_plan`. Record whether a change is physically motivated, an artistic fit, or a workaround with lost behavior. A fit to a single uncalibrated photograph is not a measured material.

Return verified conventions and selected brackets to [assembly](../image-material-assemble/SKILL.md), representation failures to [architecture](../image-material-architecture/SKILL.md), and unresolved visual failures to [review](../image-material-review/SKILL.md). Proceed with independent work if one control is unavailable, while leaving affected acceptance claims pending.

For disappearing glints or flat-looking cloth, apply [detail-survival controls](../image-material-architecture/references/structured-scattering.md). Test final-size filtering and an independent fiber tint/angular response before increasing every normal amplitude or roughness.

For ambiguous mechanism attribution, use [transport diagnostics](../image-material-diagnostics/SKILL.md) to separate direct/indirect, light direction, relevant path topology and built-in material fields. Calibrate only after verifying output semantics; a black output or tiny stochastic delta is not by itself a physical conclusion.
