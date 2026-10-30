---
name: image-material-assemble
description: Interpret texture-channel contracts, assemble a validated MaterialX/OpenPBR material, and use renders to diagnose image-reconstruction errors. Use after map analysis to select shader connections, conversions, layer behavior, and targeted corrections; supports standalone OVRTX validation.
---

# Image Material · 6 · Assemble, render, and revise

Read the case record, architecture/input audit, calibration results, actual maps, and [shared handoff](../image-material-analyze/references/handoff.md). Build from physical meanings, not filenames or generic channel presets. Keep the workflow renderer-independent until choosing the target adapter; begin with standalone MaterialX/OpenPBR and OVRTX when available. Blender is optional.

For a planning-only request, use the available evidence and proposed channel contracts even if maps or a runtime are absent. Produce a provisional connection table, expected conversions, and the checks needed at execution time. Installed-runtime discovery, graph authoring, and render validation may remain pending; do not present guessed sockets as verified or request unavailable maps merely to draft a plan.

For a narrow revision of an existing material, reuse accepted state and start with the [declared edit surface and readback](references/assembly.md#preserve-complex-graphs-during-focused-revisions). Revisit only invalidated decisions; a roughness edit does not require new coat maps, a full architecture redesign or a new study sheet.

## Resolve the target and graph

Use [architecture](../image-material-architecture/SKILL.md) to inventory the installed MaterialX/OpenPBR definitions and choose representations; discover renderer capabilities using documented interfaces. Verify node/input names, types, defaults, units, supported texture operations, and output/binding conventions against that installation. Read [assembly and diagnostic guidance](references/assembly.md) for the questions to resolve and public reference sources. Do not assume the newest web specification matches the runtime.

For every channel contract, decide:

- Which physical layer and parameter should it drive? Is it coverage, roughness, color, direction, surface orientation, or volume behavior?
- Is the input directly meaningful, or does it require channel extraction, decoding, remapping, unit conversion, or a normal/bump operation?
- Which UV set, transform, tangent basis, sampler behavior, and file encoding apply? Will a color transform corrupt scalar/vector data?
- Does another connection already represent the same feature? Are base and coat normals intentionally shared or distinct?
- Does the intended behavior require geometry, thickness, displacement support, or a separate material assignment instead of another socket?

Write an explicit source → operations → destination table with types, ranges, units, rationale, evidence IDs, and any unavailable capability before authoring the graph. Resolve ambiguity rather than wiring a map speculatively and forgetting it. Choose scalar values for unsupported spatial claims; record why inactive lobes remain inactive.

Reconcile every planned active input with the actual graph, binding and rendered influence. Track declared support separately from working response. Geometry, medium boundaries, displacement and tangent fields are part of the construction, even when they are outside the surface node.

For the default MaterialX/OpenPBR route, author an editable MaterialX material with resolvable asset paths, unique node identifiers, compatible definitions, and a valid surface output. Bind it explicitly to the intended geometry. Keep texture paths relative within a delivered material package where supported; record any external dependency. Validate the document and inspect the resulting connections and material binding. A validator pass establishes graph consistency, not renderer feature support. If architecture explicitly chose another supported representation, preserve it and use its adapter validation contract; do not convert merely to follow the MaterialX example.

## Preserve the planned layer controls

Implement the approved [layer architecture](../image-material-analyze/references/layer-architecture.md), including meaningful independent color, coverage and scale controls. Map each planned component to actual nodes, masks or material assignments and record approximations. Verify mask semantics and mixing order; color compositing is not physical optical layering. Test component influence and independence in native renders, then restore the final candidate. State which components were actually implemented and which were collapsed.

Use a neutral-color relief render and a flat or diffuse color diagnostic to separate painted contour errors from geometry. Verify UV aspect, geometric sampling and filtering before blaming a shader. For projection changes or animated/reusable materials, follow [coordinate transfer](../image-material-spatial-design/references/coordinate-transfer.md) before accepting mapping and layer-normal behavior. Choose geometry and texture sampling from the smallest defining feature at the intended view, rather than assuming a large triangle count or image dimension is sufficient.

For unresolved defining detail, use the [detail pilot](../image-material-detail-pilot/SKILL.md) before promoting the full material as source-faithful. A narrowly requested graph assembly can finish with that quality finding pending. Keep its geometry/profile and actual scale visible in a closeup, with a control that isolates the disputed channel. Distinguish a connected input from detail proven to survive that input; a noisy numerical image delta is not proof of the intended morphology.

For focused edits or ablations of an existing material, use [graph-preserving revisions](references/assembly.md#preserve-complex-graphs-during-focused-revisions): declare allowed changes, reopen the authored candidate, and verify the effective graph and dependencies before comparing native output.

When wiring interacting relief or coverage-driven thickness, use [relief composition](../image-material-texture-maps/references/relief-composition.md). Verify the operation and affected interface; a shared mask alone does not establish coherent edge normals.

## Calibrate and render controlled experiments

Use the host's official runtime client/runbook and supported authoring path. This skill does not supply a bridge, native binary, runtime patch, or replacement transport. Record versions and actual unsupported features; do not silently substitute a simpler material and claim the intended graph rendered.

Before artistic tuning, use [calibration](../image-material-calibrate/SKILL.md) for color/data interpretation, display, lighting, physical scale and parameter fitting. Carry its tested conventions and unresolved confounds into the graph; do not compensate for untested conditions through color or roughness.

Use a surface resembling the target to assess layout and scale, and a proper shader ball when curvature/grazing response helps diagnose the layers. Reuse an established user-selected benchmark across trials: record asset and UV hashes, transforms, camera, lights, environment, exposure and display. Inspect UV quality; do not silently replace the specimen with a custom mesh or tune its rig for one material. Declare any necessary repair and preserve geometry when the repair concerns UVs. Introduce separately labeled diagnostic fixtures/lights as needed while retaining the primary comparison setup. Inspect beauty and all relevant supported native lobe passes without waiting for the user to ask. Test active mechanisms that cannot be separated by LPE using controlled layer/map ablations. Change lighting or view to challenge the interpretation; include closeups and grazing/backlit conditions when relevant.

Native lobe passes, generated lobe studies, and display previews must remain separately identified. Approximate appearance is the goal; exact LPE-to-beauty recomposition is not an acceptance gate. A layer-toggle comparison is a causal experiment, not an isolated additive lobe.


Apply the [native finish-field gate](../image-material-texture-maps/references/finish-fields.md) when normals, roughness or reflection-strength variation is defining or disputed. Prove normal ON/OFF in neutral color at final resolution, then test roughness and strength/coverage independently with reflection passes and fixed unrelated inputs. Graph validation does not establish active derivatives or mapped influence; preserve a failed capability finding and test a supported representation.

## Diagnose and route corrections

Check mapping and connection correctness before changing the material hypothesis. Use a conspicuous temporary scalar or diagnostic texture if needed to establish that a socket and binding are active; restore the candidate afterward.

| Observed mismatch | First checks and route |
| --- | --- |
| Features drift between channels | Layout revision, UVs, transforms, alignment → map skill |
| Highlight location/shape is wrong | Light geometry, object shape, normals, then roughness/anisotropy → assembly or map skill |
| Pattern stays bright/dark under changed light | Baked illumination versus real pigment → maps or analysis |
| Relief is inverted or too strong | Normal convention, height sign, physical amplitude, duplicate detail → assembly/maps |
| Coat hides or follows the wrong detail | Layer order, coverage, separate normals, roughness → assembly or analysis |
| Color/transmission changes implausibly | Encoding, exposure, volume/thickness, absorption interpretation → assembly or analysis |
| Candidate looks good but contradicts the source | Invented structure or false interpretation → analysis/lobe prompts |

Keep alternative causes explicit and choose a discriminating experiment. Inspect the render, record what actually happened, and update the case graph. Promote only supported conditional lessons; do not create a new skill for each material encountered.

## Finish

Route actual renders, buffers, rig settings and the connection table through [image-material-review](../image-material-review/SKILL.md) before declaring visual completion. A graph validation pass, finite buffers, convergence, or an attractive ball does not establish reference fidelity. Deliver the editable graph, map inventory, one representative render and the review verdict. If generation or rendering could not run, label the deliverable a plan/graph candidate, not a completed material. State how to try it and the requested decision (Try it, Keep it, Fix it, Drop it, or Blocked).

Execute the [hypothesis-driven diagnostic plan](../image-material-diagnostics/SKILL.md), including relevant built-in AOVs and batched LPE selections. Verify returned buffers, labels, raw channel semantics and exact frozen artifact revisions. Capture the same selected pass under consequential layer/map interventions, not only intervention beauty.

When an accepted appearance study loses surface complexity in assembly, use [detail retention](../image-material-detail-pilot/references/detail-retention.md). Compare effective scalar distributions and normal slopes after every transform, plus base/coat interventions; connected maps alone do not close the finding.
