---
name: image-material-analyze
description: Analyze an input image into evidence, competing material hypotheses, and a reconstruction brief. Start here for an image-to-material workflow that continues through generated lobe studies, coordinated texture maps, and MaterialX/OpenPBR assembly.
---

# Image Material · 1 · Analyze

Infer a plausible material from visible evidence. A photograph does not uniquely determine its shader. Keep observations, assumptions, and experimental choices distinct; do not turn a familiar material name into a recipe.


For regional highlight differences or a complaint of uniform finish, use [spatial finish reasoning](../image-material-texture-maps/references/finish-fields.md). Record separate evidence and map/uniform/unresolved decisions for normal structure, roughness spread, and reflected amount/coverage. Do not infer these fields from brightness alone.

When the user chooses a generated hypothesis as the appearance target, record that authority explicitly and route a flat/weak native result through [detail retention](../image-material-detail-pilot/references/detail-retention.md). Continue tracking original-photo fidelity separately. A request to recover the richness of a generated study does not by itself approve its invented topology or material identity. When the user points back to the source photograph, re-anchor the identity contract before retaining details from that study.

## Start and route

Inspect the actual image with an available image-viewing tool before interpreting it. If it is unavailable, request it and stop image-dependent analysis. If the user explicitly requests planning from supplied observations without an image, proceed using those observations as attributed text evidence; do not invent visual inspection, coordinates, unseen detail or an exact layout. Mark image-dependent decisions pending and any illustrative layout synthetic. Read [the handoff contract](references/handoff.md), and create a task-owned case directory following the host's artifact policy. Keep case data outside the skill folders.

For a full reconstruction, use these sibling stages as a dependency map, carrying the same case record:

1. This skill: evidence and hypotheses.
2. [image-material-architecture](../image-material-architecture/SKILL.md): select representations, editable layers and complete input coverage.
3. [image-material-lobe-prompts](../image-material-lobe-prompts/SKILL.md): synthesize and critique appearance studies.
4. [image-material-texture-maps](../image-material-texture-maps/SKILL.md): derive and inspect coordinated property maps.
5. [image-material-calibrate](../image-material-calibrate/SKILL.md): establish response conventions and discriminate uncertain parameters; revisit during assembly.
6. [image-material-assemble](../image-material-assemble/SKILL.md): build and verify the selected construction in the native renderer.
7. [image-material-review](../image-material-review/SKILL.md): compare source, generated studies, and native results; resolve defining failures and loop back.

For regional finish, multiscale populations or organized motifs, the eighth skill, [spatial design](../image-material-spatial-design/SKILL.md), branches from architecture before production maps.

For identity-defining fine structure or a reconstruction that reads as the wrong
surface, route architecture/spatial design through [detail pilot](../image-material-detail-pilot/SKILL.md)
before full-material polish. This ninth skill accepts or rejects a construction
using source, field and native evidence; it can return directly to morphology or
representation design. Uniform surfaces do not need this branch.

This is a dependency route, not a rigid sequence: run cheap geometry/capability/calibration probes early when they change the study or map plan.

Honor narrower requests such as analysis only or prompts only. Do not invoke generation or rendering for those requests. If a required tool is unavailable, deliver the completed upstream artifacts and name the missing capability; never invent a generated image or successful render.

For a narrow repair, reuse accepted case state and investigate the reported delta. A changed projection routes first to [normal-path probes](../image-material-spatial-design/references/coordinate-transfer.md#qualify-a-changed-normal-path-with-simple-probes); suspected masked height to [relief composition](../image-material-texture-maps/references/relief-composition.md); ambiguous grain to [the detail-free baseline](../image-material-calibrate/references/controls.md#test-ambiguous-grain-with-a-detail-free-baseline). Select only relevant checks; a repair plan does not require rebuilding the full mechanism inventory.

## Ask questions of the evidence

Use [the question guide](references/questions.md) selectively. Answer with compact evidence and decision summaries, not a transcript of private reasoning. Ask the user only for missing information that would change a consequential choice and cannot be resolved by inspection or a cheap experiment. Proceed with labeled assumptions for reversible choices.

- Establish the target surface: which regions belong to it, and which are background, neighboring materials, cast shadows, or objects seen through it? Record region coordinates on the source image.
- Separate object shape from surface structure. What affects the silhouette, what deforms a reflected highlight, and what only changes color? Identify macro, meso, and micro features and their likely physical scale.
- Separate illumination from material. Examine highlight shape, shadow direction, perspective, exposure, compression, and white balance. Mark saturated or occluded regions as missing information.
- Infer candidate layers and their order. For each, identify evidence for pigment, dielectric/metal reflection, coating, transmission, subsurface scattering, fibers, or emission. An attractive explanation is still a hypothesis. For plausible coatings, assess [subtle conformal or rough layers](references/layer-architecture.md), not only smooth glossy clearcoat; matte appearance alone cannot rule them out.
- Test rival explanations for ambiguous cues. A bright streak could be pigment, relief, or a reflection. State what observation or render variation would distinguish them. Retain alternatives only when they would change maps or graph structure.
- Decide representation: geometry, spatial map, scalar parameter, or unresolved. Favor spatial variation only where evidence supports it. Do not generate a map for every available shader input.

Read [mechanism coverage and fidelity planning](references/coverage.md). Complete the mechanism inventory before choosing studies; diffuse and glossy are event categories, not an adequate default description of a complex material. Mark each mechanism active, uncertain, or unsupported in the working model with evidence and a test. Missing evidence is not proof of physical absence.

For ambiguous optical evidence, add a causal row: observation → competing mechanisms → expected change under controlled light/background/thickness → representation → falsifier. Distinguish sharp displaced detail from blur, and volume attenuation from surface coloration. Read [transport semantics](../image-material-lobe-prompts/references/transport-semantics.md) when defining the required optical studies.

Record evidence IDs, hypotheses with confidence and counterevidence, feature positions, layer relationships, unknown scale assumptions, and discriminating tests. Give each major accepted hypothesis a reason and a revision trigger. Do not report numerical IOR, roughness, thickness, or chemical composition as measured from a single photograph.

Before the first generation, write a short visual identity contract: the few
features whose loss would make this a different surface, a source crop for each,
and concrete forbidden substitutions. Describe connectivity, width/length spread,
orientation and occupied/quiet areas where visible. Keep product labels and
inferred manufacturing categories separate from these observations. A generated
beauty cannot redefine the contract; a revision needs source evidence or explicit
user steering.

Set the requested fidelity and viewing conditions explicitly. For a high-quality reconstruction, list defining features that must survive a hero view, close inspection, and revealing light. Rank them by perceptual importance. Plan enough generation and native experiments to resolve those features; do not silently downgrade to a quick game-material prototype. Complexity follows the evidence and layer interactions, not node count.

## Preserve details and plan the construction

Read [feature preservation](references/feature-preservation.md) when small structures define identity. Record shape, edge profile, population, scale and cross-property relationships with source anchors; carry these as explicit prompt constraints and check them after each generation. Matching feature centers is insufficient when contours or rims change.

When fine detail defines identity, use the [detail reconstruction procedure](../image-material-texture-maps/references/detail-reconstruction.md) to select source crops, estimate actual texture/render sampling, and plan an early native detail pilot. Keep that pilot ahead of full-material polish so failed morphology is corrected before it spreads through the graph.

For multiple color sources or interacting layers, read [layer architecture](references/layer-architecture.md). Plan independently controllable color components, physical interfaces and spatial regions before maps are requested. Keep their meanings distinct. Record which features share a mask, which intentionally differ, and what an edit must leave unchanged.

## Ready for the next stage

Provide a concise reconstruction brief identifying the chosen working hypothesis, alternatives still worth testing, the feature/layout anchors that must survive generation, and the intended output (unique patch, tileable surface, or supplied UV atlas). If the target is curved or partially hidden, distinguish visible reconstruction from synthesized coverage.

Proceed when the brief can constrain a prompt without unstated guesses about the target region, coordinate layout, or meaning of the proposed layers. An observation-only plan may use an explicitly synthetic layout; source correspondence stays pending. Low-confidence parameter values may remain provisional and be bracketed later. The first skill can be complete even when later generation is unavailable.

## Portable bundle

Version 0.15.0. Move all ten sibling `image-material-*` directories together and preserve their names. Relative links and the shared handoff then continue to resolve. Load this file as the entry point in a new host; register/discover the ten skills according to that host's skill mechanism. No renderer, imagegen service, sample asset, or repository installation is bundled. See [bundle metadata](references/bundle.json) for the member list, provenance, and dependency contract.

For multiscale populations, organized motifs or nonuniform wear, route from architecture through [spatial design](../image-material-spatial-design/SKILL.md) before production maps. Keep one source photograph per case when testing single-image reconstruction; research can inform hypotheses but additional views, source shaders and supplied material maps would change the experiment.

For complex contribution studies or disputed lobe coverage, route through [transport diagnostics](../image-material-diagnostics/SKILL.md) after architecture and before lobe prompting. This conditional tenth skill owns the hypothesis-to-observable plan, built-in AOV/LPE selection and matched interventions; it does not replace calibration or the official renderer.

For seam removal, repeated-patch suppression or mapping blur, route through [mapping blends](../image-material-spatial-design/references/mapping-blends.md); these are distinct problems. For coherent folds becoming branching ridges, route through [deformation morphology](../image-material-spatial-design/references/coherent-deformation.md) before more texture generation. Preserve the source/user-selected target and the established benchmark while revising only the responsible feature or coordinate family.
