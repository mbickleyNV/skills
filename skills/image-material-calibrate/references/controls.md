# Calibration before artistic tuning

Establish what the installed pipeline actually does. Record scene units, light shapes/intensities, camera/exposure, working primaries, texture encodings, native output encoding, display/view transform and denoising. Unknown is an acceptable record; it is not evidence for an assumed conversion. Reuse verified controls only while their dependencies remain unchanged.

## Separate three problems

1. **Texture interpretation:** compare a known encoded color patch through the texture path against its correctly decoded linear shader constant under identical geometry/light. Test a raw scalar/vector path against known data values. Use identical material settings, neutral color corrections and finite linear buffers. Match coordinate regions and compare local variation/noise. Agreement establishes only the paths tested, not every node or format.
2. **Display:** compare the renderer's display output with the documented conversion of its linear output, where available. Avoid double decoding, double tone mapping, per-pass auto exposure and mixing view transforms. Preserve HDR buffers. Treat imagegen/source encoding as unknown unless established; generated pictures are not radiometrically calibrated targets.
3. **Scene illumination:** check neutral gray and color patches and highlight clipping under the diagnostic rig. Do not inherit extreme illumination from a different material specimen and compensate through albedo. Lock the rig before material comparisons. The photograph's unknown white balance/exposure remains a separate uncertainty.

Known-value fixtures can be tiny numerical assets created with supported authoring tools; they are controls, not AI edits of source imagery. Record actual values, results and tolerances justified by noise/precision. Diagnose non-finite output before claiming that pass supports a measurement.

## Disentangle reflection, color and geometry

Render fixed-color roughness brackets under fixed lighting, followed by fixed-roughness relief brackets if needed. Inspect both body response and reflection. Roughness changes can change the apparent color by redistributing reflection; that does not justify arbitrary saturation compensation. Confirm the installed roughness convention before remapping. Document any artistic color adjustment after calibration and tie it to a source discrepancy.

Use neutral/flat-normal, constant-roughness, constant-albedo and layer-off controls to prove important maps affect the intended result. For complex materials choose controls that isolate the disputed mechanism; do not render every permutation mechanically. A tiny normal perturbation can be lost at the chosen distance or sampling, while albedo grain can falsely suggest working relief. Judge normal action in reflection and under changing light.

Check UV coverage, tangent basis, both axes, feature frequency and real geometry scale. If a required input is ignored by the renderer, investigate the supported path or substitute a declared equivalent only after verifying its behavior. An unconnected height asset is not rendered displacement. Preserve the material candidate and restore diagnostic overrides after each test.

## Preserve the benchmark while diagnosing its illumination

If the established benchmark compresses color or detail, retain it unchanged and create a separately named diagnostic varying one illumination/exposure control. Keep material, geometry, UVs and display fixed; record which light intensities changed and by what factor. Judge whether the mismatch is illumination-dependent before retuning intrinsic color. A darker diagnostic is not a replacement benchmark or a matched source comparison.

A creative revision may change several variables to improve appearance, but cannot identify their individual causes. Use matched one-variable interventions for claims about layer influence, internal transport or roughness. A narrow bright edge can contain both neutral Fresnel reflection and warm internal response; do not replace one unsupported universal explanation with another.

## Revalidate new paths and added controls

Switching from authored constants to color textures invalidates the relevant encoding check even if the renderer version is unchanged. Compare a known encoded patch to its decoded constant and include a deliberately raw negative control. If the correctly tagged texture agrees, record that rejected gamma hypothesis; do not apply an extra inverse transform to improve appearance.

If color remains pale, bracket newly enabled transport inputs individually while holding the input color, exposure and lights fixed. Diffuse roughness, glossy roughness and fuzz roughness describe different mechanisms; do not enable them together as a generic material-complexity upgrade. Check local linear RGB/chroma as well as the displayed beauty. Record a surprising runtime-specific response with a minimal constant-color control and version; do not convert it into a universal rule to disable that parameter. Keep the physically supported candidate or a named workaround, and retain the failing control for future runtime comparison.

## Qualify the evidence before crediting influence

For a small quantitative delta, establish a repeat-baseline/noise comparison or
other justified uncertainty bound before attributing it to an input. Keep the
qualitative visual finding when precision is insufficient. A changed beauty proves
only the tested intervention, not all parameters in its component.

Track validity per output channel. A non-finite diagnostic AOV cannot support a
measurement, even if beauty is finite; finite beauty need not be discarded for an
independent visual inspection. Preserve raw failures and channel-specific status.
Do not silently sanitize invalid values or promote technical influence into a
source-fidelity pass.

## Test ambiguous grain with a detail-free baseline

When fine grain could be authored detail or a rendering artifact, make a separate
control that disables the disputed fine-scale pigment, roughness, relief and other
microvariation together. Keep geometry, broad spatial regions, lighting, exposure
and the intended base scattering model fixed. Record the replacement constants
and any variance change; removing roughness variation cannot preserve every
angular response exactly. This joint intervention locates residual variation; it
does not isolate a single input or supply an additive lobe.

Compare at equivalent verified capture settings. Inspect effective accumulation
limits, sample count when exposed, convergence and denoising state through the
documented native client. More update calls or a longer wait need not yield more
samples after a limit is reached. If effective sample counts cannot be observed,
state that limit instead of claiming a measured convergence improvement.

Residual grain may come from transport noise, geometry, structured reflections,
filtering or capture processing. Test the relevant alternative rather than calling
all residual variation noise. Restore feature families separately when needed,
and require spatially anchored detail with plausible light/view response. Judge
raw and denoised results where available; denoiser-off speckle is not automatically
real microstructure. Preserve the primary benchmark and use this branch only for
an unresolved detail question.
