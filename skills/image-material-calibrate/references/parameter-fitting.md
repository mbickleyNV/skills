# Fit causes, not compensations

## State what the data can identify

Record parameter groups, observed cues, plausible ranges, fixed assumptions and which experiment separates them. One photograph can leave lighting versus albedo, roughness versus emitter size, relief versus refraction, and absorption versus thickness ambiguous. A pleasing fit does not remove that ambiguity. Use visual brackets or measurable controls rather than claiming exact recovered parameters.

| Ambiguity | Useful controlled test |
| --- | --- |
| Reflection width: roughness or light size | Hold geometry and light shape fixed, bracket roughness; then challenge the selected result with a different light size |
| Color: encoding, illumination or intrinsic property | Known-value texture/constant controls, neutral fixture, documented output transform, then a locked-rig property trial |
| Dark region: pigment, cavity or long optical path | Neutral-color relief, altered light direction, or matched clear/absorbing geometry as appropriate |
| Soft detail: roughness, unresolved structure or denoising | Constant roughness/flat-normal interventions and an inspected crop at suitable sampling; keep color/layout fixed |
| Bright or warm edge: interface reflection, thin-region internal transport, pigment or image halo | Inspect reflection and internal-transport controls; vary scattering/thickness with roughness fixed, then roughness with body transport fixed; source color alone does not select the cause |
| Layer influence hidden in beauty | Toggle or perturb the layer with valid energy/coverage semantics, inspect relevant passes and combined appearance |

## Bulk absorption and physical scale

For a homogeneous non-scattering absorbing medium, `T(d) = exp(-sigma_a * d)` per channel. A transmission color `C` specified at positive reference distance `d0` implies `sigma_a = -ln(C) / d0` and `T(d) = C^(d/d0)` under that model. Use linear quantities and matching distance units. Handle zero/one limits explicitly; do not fit displayed RGB values with this equation. A zero-depth shader mode may have different semantics and must be checked in the installed definition.

The observed color depends on optical path length, not merely wall thickness measured normal to the surface. Refraction, internal reflection, scattering, interfaces and the background complicate the image. Do not divide arbitrary beauty images and call the ratio pure absorption. Use matched clear/absorbing controls or simple known-thickness fixtures, exclude clipped/noisy/boundary pixels, and document remaining interface/path confounds. Check approximate multiplicative transmission across known distances before fitting a product.

When thickness is inferred, bracket plausible geometry and absorption together in a controlled study. Changing both `C` and `d0` can describe the same coefficient; do not treat them as independently recovered facts. Select a consistent distance convention and keep it stable. Test a candidate against another thickness or angle while its parameters stay fixed. Report an appearance fit conditional on geometry when thickness is unknown.

Before making absorption extreme to darken a base, inspect its cross-section, rim, interior/outer normals, medium assignments, ray/refraction limits, reflective surroundings and contact lighting. Confirm that a darkening result is physical transport rather than missing paths. Keep pigment, surface tint and bulk absorption distinct.

## Coupled changes and regressions

Record before/after settings, predicted regional changes, observed effect, fixed conditions and affected checks. Multiple simultaneous edits are a new candidate, not a causal isolation. When height remapping, UV repeat or a proxy changes, redo affected scale/profile/normal tests before reusing prior calibration. A new color fit must retain the accepted layout and roughness; a relief revision must retain pigment boundaries and smooth regions.

Inspect source and native at comparable object and feature scale, with exposure/display differences stated. Numerical image errors are appropriate only when registration, encoding and lighting justify them. End with pass/fail/uncertain by defining criterion, not a single unsupported similarity score.

Primary references: [OpenPBR model and parameter meanings](https://academysoftwarefoundation.github.io/OpenPBR/) and [PBRT transmittance](https://www.pbr-book.org/4ed/Volume_Scattering/Transmittance). The equations above describe the stated simple medium; native implementation and complex scenes require validation.

## Interventions must name everything they remove

Describe an intervention by its semantic changes, not only the socket toggled. Disabling a tinted coat may remove both interface reflection and absorption filtering. Neutralizing its tint retains the interface; these are different experiments. A shared parameter can also change energy partition or multiple branches. Record expected downstream changes before rendering and compare the generated study against that exact operation. Do not call the difference a pure additive layer or count a graph toggle as isolating only the effect named in its caption.
