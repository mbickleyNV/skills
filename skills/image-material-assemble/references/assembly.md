# Assembly reference and runtime adapter

## Semantic mapping seeds

These are starting points to verify in the installed NodeDef, not unconditional wiring rules:

| Meaning | Candidate OpenPBR input |
| --- | --- |
| Base coloration / metallic fraction | `base_color` / `base_metalness` |
| Base reflection spread | `specular_roughness` |
| Coat presence / spread | `coat_weight` / `coat_roughness` |
| Transmitting fraction / absorption color and distance | `transmission_weight` / `transmission_color`, `transmission_depth` |
| Base / coat surface orientation | `geometry_normal` / `geometry_coat_normal` |
| Cutout coverage | `geometry_opacity` |

Keep height separate from surface-normal inputs: choose a supported displacement or bump path and verify units. Roughness, coverage and normals are data; color decoding depends on actual encoding. Normal textures require a compatible decoding/basis operation. Never multiply a lit reflection study into reflectivity or use transparency as a substitute for transmission.

Author every connection with source type, processing, destination type, and evidence. A node's existence in a library does not prove the target renderer implements it. Test optional mechanisms in a small controlled scene and mark unsupported behavior explicitly.

Sources: [OpenPBR specification](https://academysoftwarefoundation.github.io/OpenPBR/) and [MaterialX OpenPBR definitions](https://github.com/AcademySoftwareFoundation/MaterialX/blob/main/libraries/bxdf/open_pbr_surface.mtlx). Consult installed definitions first; the linked main branch can change.

## Optional compiled-material capability check

When architecture selects a custom compiled material such as MDL, keep language
and library versions, parameter types/variability, resource resolution and the
renderer integration explicit. A standalone compiler accepting source does not
prove that the renderer's embedded path supports or evaluates it. Keep compile,
load/binding and native influence findings separate. Use one simple typed input
with a predictable visible change to establish the active path before subtle fitting.

Record which changes are argument updates and which require a new module/resource
revision. Verify cache invalidation through the installed official client; do not
import another host's warm-up sequence or runtime workaround as a universal rule.
If the required model is unsupported, return to architecture with the specific gap.
Do not equate MDL, MaterialX/OpenPBR and their parameter conventions or switch the
material representation merely to invoke this optional route. Planning/review-only
work records these probes as pending.

## Standalone OVRTX diagnostics

Use the installed official client and documented stage/material binding flow. Request PathTracing LPE variables with `sourceType=lpe` and the expression as `sourceName`, then include them in the product's `orderedVars`. Current documented categories distinguish rough glossy `G` from ideal delta `S`. Representative broad selections are `E<R[GS]>.*L` and `E<T[GS]>.*L`; `E<RD>.*L` selects diffuse reflection. A selection of only `G` can miss a smooth delta response. These are whole-scene first-event classes unless scoped: with supported uniform geometry token `primvars:omni:label = sample`, candidate specimen selections are `E<R[GS]'sample'>.*L` and `E<T[GS]'sample'>.*L`. Verify label and expression support in the installed SDK with a recognizable background, a labeled specimen, smooth and rough controls, and a known contributing light. Do not interpret an unsupported/black pass as physical absence.

The documentation consulted permits nine LPE variables per product; disable radiance caching for complete path histories (cached radiance can remain in beauty but be missing from LPEs). Preserve raw buffers, expression, labels, integrator, ray depth, sampling/denoise and display conversion. Check finite values and actual spatial scope, not merely file existence. Later-event subsets may overlap their parent classes; do not add them together or label any later glass reflection as necessarily internal without evidence. See [transport semantics](../../image-material-lobe-prompts/references/transport-semantics.md).

Event categories do not automatically isolate a named OpenPBR layer. Use controlled parameter ablations for ambiguous layer behavior and label them accordingly. Cache behavior, denoising, sampling, and display processing can affect comparisons; do not make exact recomposition a condition for this creative workflow.

Source: [OVRTX light path expressions](https://nvidia-omniverse.github.io/ovrtx/sensors/cameras/light_path_expressions.html), consulted 2026-10-27. Recheck against the installed SDK.

## Distinguish runtime failure from material response

A valid document, finite buffers and a converged frame do not prove that the intended material compiled or bound. When a candidate or ablation returns a conspicuous uniform fallback, unexpected flat color or missing contribution, inspect native diagnostics, resolved assets, binding and a known working control before fitting optical parameters. Exclude a fallback image from quality comparisons and numerical ablation deltas; it is a failed execution, not evidence that a layer is undesirable.

Minimize the failing graph or binding while preserving the intended test, using the documented authoring/runtime path. A practical repair such as removing unreachable authoring nodes or using an unambiguous material identity does not establish the compiler root cause. Record the narrow observed failure and workaround without declaring the whole node family unsupported. Restore the intended controlled comparison and verify its actual image before interpreting it.

## Preserve complex graphs during focused revisions

For an existing material or diagnostic ablation, declare the edit surface before
authoring: exact values, connections, texture assets or coordinate transforms that
may change, plus the branches and dependencies that must remain fixed. Snapshot
the source revision, shader identifiers, effective connections, composed binding
and resolved dependency inventory. Work on a separate candidate; do not flatten a
complex layered graph into a convenient base-color/roughness/metalness preset.
Unsupported graph patterns are an explicit adapter limitation, not authorization
to replace the representation. An intentional architecture change gets a named
revision and new validation scope instead of masquerading as a parameter edit.

Reopen the written candidate through the supported reader and inspect its effective
state, including inherited connections, binding and texture resolution. Compare it
to the declared edit surface. A saved scalar cannot override an unexpected connected
input merely because the file contains the new number. Check unchanged branches
and dependency content as well as node count; unchanged topology can still reference
changed textures or defaults. Legitimate path rebasing may change identifiers without
changing meaning, so record semantic equivalence rather than requiring byte identity
of relocated packages. Keep hashes of source assets and declared changed assets. Trace shared upstream textures: changing an image used by both substrate and coat changes both branches. Use a distinct candidate dependency when only one branch should change. Fixed coat inputs can still yield changed path contributions through layer interactions; graph preservation does not imply an unchanged coat-looking event image.

Associate each native capture and AOV with the reopened candidate and its dependency
revision. If a runtime caches assets, verify supported reload/invalidation before
crediting a control. An accidental graph or asset change invalidates its causal
comparison; a successful readback still needs the intended native influence and
source-fidelity checks. Scope this audit to consequential edits rather than creating
a new packaging workflow for every numeric adjustment.

Source-informed adaptation: [representation-preserving refinement](https://github.com/NVIDIA-Omniverse/usd-content-agents/blob/0709377ed35fb066361a0d6735d21984b885fe36/apps/material_agent/docs/material_refinement_and_variation.md) and [saved-candidate quality review](https://github.com/NVIDIA-Omniverse/usd-content-agents/blob/0709377ed35fb066361a0d6735d21984b885fe36/agentic/.agents/skills/content-texture-quality/SKILL.md). These workflow ideas do not establish arbitrary MDL support in the selected renderer.

## Before accepting a material

Check asset resolution, UV orientation/scale, binding, color versus data decoding, normal polarity, real thickness where used, and layer-specific variation. Inspect the reference's defining features in both the diagnostic render and changed lighting. Use [the review skill](../../image-material-review/SKILL.md) for visual acceptance; merely looking plausible under two lights is insufficient when defining features fail. Even a successful visual reconstruction does not establish unique recovery of the original physical material.

## Verify translated texture paths

If an optional texture node validates in the authoring library but the render loses
detail, inspect the actual renderer definitions and generated native shader when
available: resource samplers, active input connections, defaults and translation
diagnostics. Authoring and runtime libraries may differ. A smooth finite frame can
be an omitted sampling path rather than successful texture support. A conspicuous
input substitution plus a matched native control establishes influence; absolute
filenames cannot fix a node that was dropped during translation.

Track graph validation, translation, binding, resource sampling and expected visual
consequence separately. Minimize the failing path before replacing the model. If
architecture selects a supported custom material implementation, preserve the tested
BSDF and qualify a baseline with the old mapping first. Record the adapter-specific
module/version, dependencies, editable controls and portability limit. This is a
material authoring fallback, not permission to patch a runtime or claim universal
MaterialX support. Cold compilation delay alone does not prove unsupported shading.

For independent interfaces, trace each normal/tangent owner and shared upstream
assets. A built-in bump-normal AOV may describe the outer/evaluated interface; it
cannot alone prove a buried substrate normal is correct. Use selected reflections
and matched layer/normal interventions. If authoring a component-off control,
inspect all active paths and child inputs rather than assuming one weight disables
every contribution. An intervention establishes its causal change, not an exact
additive lobe or unique physical decomposition.
