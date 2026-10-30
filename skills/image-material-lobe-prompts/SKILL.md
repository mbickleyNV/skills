---
name: image-material-lobe-prompts
description: Turn image-based material hypotheses into detailed image-generation prompts for approximate lobe appearance, then inspect and revise the generated studies. Use after reference analysis and before deriving texture maps.
---

# Image Material · 3 · Prompt and inspect lobes

Read the analysis brief and [shared handoff](../image-material-analyze/references/handoff.md). Inspect the reference yourself; do not rely solely on another agent's caption. If evidence, layer order, or feature anchors are missing, return to [analysis](../image-material-analyze/SKILL.md). For explicit observation-only planning, use attributed user observations without claiming image inspection. Author executable text-only hypothesis prompts with declared synthetic specimen/layout choices; mark source correspondence untested and revisit them when an image becomes available. Do not refer to attachments that do not exist.

## Define the output and its physical meaning

Read [transport semantics](references/transport-semantics.md) before authoring contribution studies. Choose beauty, angular illustration, path-selected radiance, ablation or intrinsic data explicitly. For a radiance hypothesis compile a transport contract: selected first event/object, retained later interactions, excluded paths, complete scene, native behavior reference and visual falsifiers. Inspect real renderer examples when available; attach the relevant one as behavior guidance while keeping the source photograph as identity authority. A polished silhouette on black does not establish isolation.

## Cover the mechanisms and competing explanations

Treat studies as predicted appearances under a declared camera, geometry, and lighting setup. They help reason about a material; they are not measured lobes, numerical inversions, or renderer ground truth. Predict what the active mechanisms should contribute and why before generating images.

Read the analysis mechanism inventory and [architecture](../image-material-architecture/SKILL.md) input/representation plan. Resolve missing consequential decisions before treating a study as a production target. For each active mechanism and consequential uncertain mechanism, assign an actual generated study or controlled variant and a review criterion. Select the output type by causal meaning: absorption needs matched attenuation controls, not an invented additive lobe; physical layer tests need verified labels or ablations. A diffuse/glossy pair alone does not establish coverage of coats, anisotropy, subsurface behavior, fibers, transmission, or interacting layers. Map each mechanism to its study cells; track missing coverage explicitly. Unsupported mechanisms need a documented reason, not a ceremonial black image. Do not invent layers to fill cells.

For complex or high-fidelity work, read [contact-sheet exploration](references/contact-sheets.md). Use multiple controlled hypotheses and targeted refinements: first compare interpretations, then explore the uncertain response of the promising interpretations, then regenerate selected studies at useful inspection resolution. Two generic lobe pictures and one beauty are insufficient if important questions remain. Even an opaque surface with only body and reflection responses may need substantial studies of multiscale relief, roughness, edge structure, and coating alternatives.

Keep the reference crop/geometry, camera, light positions and shapes, background, exposure, display intent, and feature anchors consistent across comparable studies. If the scene is reinterpreted on a shader ball, record that it is a material-response study, not spatial correspondence to the original object. Transmission studies need an explicit thickness and background assumption.


When finish variation matters, follow [spatial finish studies](../image-material-texture-maps/references/finish-fields.md): predict and generate controlled alternatives for highlight spread versus reflection strength/coverage with accepted normals and lighting locked. Treat parameter maps and radiance studies as different outputs. Carry selected regional predictions into map prompts and native tests.

When coating is consequential but uncertain, compare credible uncoated, thin-conformal and partially smoothing hypotheses from [layer analysis](../image-material-analyze/references/layer-architecture.md). Do not make the sole coated candidate artificially thick or wet. Preserve substrate features and state the separate coat roughness, coverage and normal relationship.

## Protect identity from appearance-study drift

When resolved structure carries identity, start with a source-led closeup or
material patch whose prompt states visible morphology and scale anchors. Use
neutral, simple lighting to select structure before elaborate shaderball lighting.
Avoid leading with a guessed product category that replaces the observed texture
with a stereotype. Then use the accepted morphology in mechanism studies, retaining
the source as identity authority. This ordering is conditional; transmission or
thickness uncertainty may require an optical probe first.

In each consequential prompt, expand feature IDs into concrete instructions:
shape/connectivity, size spread, orientation, density/quiet areas, layer relationship,
allowed change and forbidden substitution. For instance, if the source shows
interrupted thin strands, do not request generic glitter or dense round beads.
Contact sheets explore alternatives; a selected cell does not certify a production
field. Route a plausible-looking but identity-drifted result to the
[detail pilot](../image-material-detail-pilot/SKILL.md) before deriving other maps.

## Carry the details through generation

Use [prompt continuity](references/prompt-continuity.md) to turn the feature record and layer plan into a concrete contract for each generation. Reattach source identity and accepted layout at stage boundaries. Record attachment precedence, preserved details, permitted changes and rejection criteria. Never promote a failed isolate or a morphology-drifted study into spatial authority merely because its lighting looks convincing.

For defining fine structure, carry the [detail targets and patch scale](../image-material-texture-maps/references/detail-reconstruction.md) into a dedicated closeup study. Do not let a whole-object lobe sheet substitute for a resolved morphology study. Bright or warm edges need rival optical explanations; preserve uncertainty rather than turning them automatically into polish, coat, pigment or an emissive rim.

## Compose and run the prompt

Read [the prompt specification](references/prompt-spec.md). Write a complete prompt with concrete visual descriptions and region relationships. State what each attached image is for, which features must remain fixed, what may change, the optical mechanism being studied, and what a successful image would reveal. Avoid unexplained shorthand such as “make a specular map.”

Use the host's available image-generation tool and applicable imagegen instructions. For edits, attach the actual reference/layout images through the tool's supported mechanism; text descriptions do not substitute for image attachments. If only prompt authoring was requested, stop with executable prompts and mark studies ungenerated.

Store the exact submitted prompt, parent images and roles, settings if available, resulting files, and a compact hypothesis-to-prompt rationale. Do not claim control over unavailable seeds, bit depth, calibration, or shared generation state.

## Inspect before accepting

View the generated result. Compare it against both the reference and the predicted behavior:

- Did it preserve the intended features, coverage, relative scale, and layer relationships?
- Are highlights consistent with the declared lights and surface curvature? Did it invent pigment, relief, opacity, or new motifs?
- Does the study distinguish the rival explanations, or merely repeat the beauty image?
- Does the output honor its path selection, including allowed later interactions and object scope? Does it pass its positive and negative visual tests? A transmitted highlight may be legitimate; a beauty cutout is not proof of separation. Should the distinction be tested in the renderer?

Record concrete discrepancies and issue a targeted edit, retaining anchors. Include the defect and the intended discriminating change in the next prompt; do not merely request “more realistic.” Do not treat a visually persuasive generation as new evidence about the real object's hidden structure. If generation cannot isolate a mechanism convincingly after meaningful revised attempts, mark the study unresolved and carry the competing hypotheses into renderer tests. Record what was attempted and why rendering is the better test; this is not a shortcut to skip imagegen exploration.

Hand the coverage ledger, inspected contact sheets, selected full-size studies, rejected alternatives and reasons, explicit optical predictions, and unresolved questions to [texture-map reasoning](../image-material-texture-maps/SKILL.md). Keep the original reference as the primary evidence. A requested planning-only deliverable may stop at authored prompts; a full reconstruction must actually generate and inspect the studies.

Use the [diagnostic plan](../image-material-diagnostics/SKILL.md) to choose contact-sheet cells before generation. Include direct/indirect, directional/light-selected or relevant transmission observations when they discriminate hypotheses; compare parameter interventions in the same selected path family. Do not substitute unrelated empty passes for mechanism coverage or invent layer-specific LPE labels.

Carry intermediate feature counts and within-feature detail into the downstream map contract. When native results flatten an approved study, route to [detail retention](../image-material-detail-pilot/references/detail-retention.md); do not silently shrink its defining structures or replace the target with a smoother interpretation.
