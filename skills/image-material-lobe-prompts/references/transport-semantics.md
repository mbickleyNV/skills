# Define the image before calling it a lobe

Read this when prompting or reviewing optical contribution studies. Translate the relevant semantics into the submitted prompt; attaching this document or naming a pass is insufficient.

## Choose the output type

| Output | Meaning | Consequence for prompting |
| --- | --- | --- |
| Angular BSDF illustration | Directional scattering at an interaction | A directional diagram is not an object appearance or texture |
| Path-selected radiance hypothesis | Complete light paths selected by event, object or verified label | Describe both the selection and the later interactions it retains |
| Material/layer ablation | Render after changing one material property or layer | Compare against a matched control; removing a layer changes other paths |
| Intrinsic parameter/data image | Color, orientation, coefficient, coverage or geometry data | Remove lighting; define coordinates, encoding, units and polarity |
| Beauty hypothesis | Combined visible response | Useful for identity and interaction, insufficient evidence of isolation |

A physical layer is a material construction, not an output category. One dielectric interface produces reflection and transmission. A coat changes the response beneath it. Neither first-event class automatically isolates a layer. [OpenPBR](https://academysoftwarefoundation.github.io/OpenPBR/) defines material layering; [PBRT](https://www.pbr-book.org/4ed/Reflection_Models) describes angular scattering.

## Compile a transport contract

For each radiance study record:

- Output type and qualitative status; generated studies have **no additive or calibrated-AOV claim**.
- Target object/region and camera-first event, or another explicitly defined path selection. Record executable LPE only when verified in the target renderer; plain-language path notation is otherwise sufficient.
- Allowed later events and endpoints; separate these from excluded paths.
- Complete scene: specimen geometry/thickness, background geometry, environment, lights, camera, exposure/display intent. Explain which scene elements remain physically present but invisible outside the selected contribution.
- Actual behavior reference: a documented native pass, preferably a control from the same renderer and benchmark. Record source, expression, settings and inspection. If unavailable, mark behavior guidance missing and require native corroboration before accepting isolation.
- Positive and negative visual tests, comparison limits, and any separately introduced diagnostic intervention.

Give attachments distinct jobs: source photo supplies material identity/morphology; accepted layout supplies coordinates; benchmark supplies specimen/camera/rig; native pass supplies transport behavior. Do not copy another reference's geometry, tint, material details or exposure merely because its path behavior is useful. A clear native control may establish path structure while leaving the target's relief and absorption to be inferred.

## Camera-first does not mean only one interaction

These sequences are explanatory notation, not portable executable LPE syntax:

| Complete path from camera | First-event class | Visible implication |
| --- | --- | --- |
| E → T → T → D(background) → L | Transmission | A lit background remains visible, refracted through glass |
| E → T → R → T → L | Transmission | Later internal reflection and bright refracted light shapes survive |
| E → R → D(scene) → L | Reflection | Reflected illuminated scenery survives |
| E → D(floor) → T → T → L | Diffuse receiver first | A floor caustic is not the glass's transmission-first image |
| E → L outside specimen | Directly seen light | Excluded from a specimen-scoped R/T study |

For transmission-first, exclude paths whose **first** interaction is reflection. Do not say “remove all reflections/highlights”: that removes legitimate later interactions. For reflection-first, retain later transmissions when the path selection permits them. Black unselected pixels mean an output selection; they do not mean deleting the background or switching off the environment.

Inspect the [official SideFX transmission example](https://www.sidefx.com/docs/houdini/images/solaris/support/lpe_transmission.jpg) alongside its [documented selection](https://www.sidefx.com/docs/houdini/solaris/support/lpe.html#transmission): the isolated glass retains structured surroundings and white light shapes. The [caustics example](https://www.sidefx.com/docs/houdini/images/solaris/support/lpe_caustics.jpg) shows receiving-surface contributions. Do not assign a path to a bright pixel from appearance alone. A cropped beauty still mixes path classes inside the silhouette.

## Choose causal controls, not imaginary additive layers

| Observation | Competing causes | Controlled test and falsifier |
| --- | --- | --- |
| Darker, more saturated thick regions | Bulk absorption, opaque pigment, lighting or geometry | Compare absorbing/zero-absorption versions at fixed geometry, then known thicknesses. A painted gradient cannot establish distance-dependent extinction |
| Blurred background | Microsurface roughness, volume scattering, defocus or unresolved relief | Hold camera/focus fixed; vary one cause. Sharp but displaced/split lines favor coherent relief over broad roughness |
| Bright molded rims | Interface orientation, thickness/lensing, pigment | Use neutral-color relief and structured-background transmission; fixed painted bands fail directional response |
| Milky interior | Scattering versus rough interface | Compare supported volume-scattering and rough-interface controls; do not add haze by default |

Absorption attenuates throughput: homogeneous non-scattering transmittance is `T(d) = exp(-sigma_a * d)`, accumulating interior path length. It is not a positive additive lobe. Use matched clear/absorbing controls; any difference or ratio needs a defined direction, common exposure and valid native data. OpenPBR's positive `transmission_depth` sets a distance for `transmission_color`; zero depth is an artistic distance-independent mode. Verify the installed implementation and distance units before interpreting a number. [Transmittance](https://www.pbr-book.org/4ed/Volume_Scattering/Transmittance), [OpenPBR translucent base](https://academysoftwarefoundation.github.io/OpenPBR/).

For ordinary bulk-tinted dielectric glass, direct interface reflection mainly follows incident illumination; bulk tint affects paths through the medium. Grazing reflectance increases, but a bright outline is not guaranteed against a dark reflected environment. Total internal reflection may occur later along a transmission-first path. [Dielectric reflection and transmission](https://www.pbr-book.org/4ed/Reflection_Models/Specular_Reflection_and_Transmission).

Coherent mesoscopic relief bends or splits recognizable light/background structures. Microsurface roughness broadens angular response. Bump/normal mapping changes shading orientation, not true wall thickness, silhouette or geometric parallax. Escalate to geometry when those effects define the target, while retaining any user-locked benchmark as a separate comparison. [MaterialX PBR specification](https://materialx.org/assets/MaterialX.v1.38.PBRSpec.pdf).

## Reject semantic failures before evaluating polish

- A transmission study with a declared patterned background must contain plausibly transformed background structure. A flat colored fill fails; highlights alone do not.
- A reflection study under neutral illumination should not contain opaque tinted body fill unless the hypothesis supplies a physical reason. Do not apply this ordinary-glass criterion to conductor reflection or all later paths through tinted media.
- Check whole-scene versus specimen-only scope. Black exterior pixels cannot by themselves prove isolation; examine what survives inside.
- Reject a control that changes geometry, light, exposure and a parameter simultaneously when it claims to isolate that parameter.
- Reject unsupported absorption-as-additive, scattering-as-opacity, or normal-as-thickness interpretations.
- Do not force every unknown into more imagegen cells. Use a native test when generation repeatedly fails the relevant semantics, preserving the failed attempts and unresolved hypothesis.

Generalize by cause: conductor spectral reflection is not glass pigment; subsurface radiance is not an unlit color map; fiber response needs directional evidence; a coat requires verified layer labels or a named ablation. For each material choose the appropriate path contract and causal tests rather than a fixed diffuse/specular checklist.

## Renderer-specific meanings must be checked

Pass names and letters are not universal. [Arnold](https://help.autodesk.com/cloudhelp/ENU/AR-Core/files/ac-output-aovs/arnold_user_guide_ac_output_aovs_ac_expression_aovs_html.html), [Karma](https://www.sidefx.com/docs/houdini/solaris/support/lpe.html) and [OVRTX](https://nvidia-omniverse.github.io/ovrtx/sensors/cameras/light_path_expressions.html) use different conventions. Settings that pass underlying-object AOVs through glass also alter interpretation. Preserve integrator, ray-depth, labels, cache, denoise and display settings with native examples. Follow the [installed-runtime adapter](../../image-material-assemble/references/assembly.md); a black pass can indicate unsupported selection or exhausted paths rather than physical absence.
