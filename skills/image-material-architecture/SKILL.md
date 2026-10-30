---
name: image-material-architecture
description: Plan evidence-supported material layers, input coverage, spatial controls and geometry representations before generating maps or wiring a shader. Use for complex image-derived materials or when a reconstruction loses defining surface behavior.
---

# Image Material · 2 · Architecture

Turn the [analysis](../image-material-analyze/SKILL.md) into an executable construction plan. Read the case's evidence, defining features and [shared handoff](../image-material-analyze/references/handoff.md). In planning-only work, propose the plan from available observations and mark inspection/runtime checks pending. Keep this workflow general across material types.

## Account for inputs without manufacturing effects

For a narrow repair, reuse the accepted input inventory and inspect affected inputs,
parents and effective connections only. Rebuild the full inventory when the shader
definition or architecture changed, or when full reconstruction is requested.

Read [input coverage](references/input-coverage.md). Inventory the installed shader definition rather than assuming a remembered socket list. The optional [inventory helper](scripts/inventory_inputs.py) exports active inherited inputs, defaults and version metadata from MaterialX; it does not test renderer support. Resolve the helper link against this skill directory, then run that script in the host's MaterialX environment with `--output` pointing to a new JSON file in the case directory.

The output belongs in the case directory. If the runtime is unavailable, use a family-level provisional inventory and defer exact sockets. For each input assign a disposition, evidence/component owner, expected influence and validation status. Group inactive child inputs under a justified inactive parent when that preserves complete accounting. Distinguish absent visual evidence, a rejected hypothesis, unavailable runtime support and an untested input.

For each active mechanism, map evidence → component → representation/control → relevant inputs → generated study → native test. Conversely, every active input needs a physical role or a declared artistic approximation. Discover neglected controls, but do not add coat, fuzz, scattering or dispersion merely to raise the count. Maximum fidelity means preserving the observed complexity and its interactions.

## Design independently editable structure

Use [layer architecture](../image-material-analyze/references/layer-architecture.md) to distinguish pigment composition, vertical optical layers and neighboring material regions. Record each component's order, coverage, coordinate field, property ownership and combination operation. A single OpenPBR node has a particular layer structure; arbitrary nested coats, inclusions or volumes may require supported composition, separate surfaces or a different shader. Record the gap rather than promising that extra masks can represent any stack.

Plan the relationships that make the surface distinctive: a finish smooths some underlying relief; wear reveals a different substrate; isolated grains change color without changing height; wet regions alter reflection while retaining the underlying pattern. Use separate controls where those properties must vary independently, and shared feature authority where boundaries should coincide. Require a native influence test for important controls and an interaction test for consequential combinations. An AOV containing glossy reflection does not prove that both coat and base respond correctly.

## Choose spatial construction before optical fitting

Read [representation and scale](references/representation.md) for relief, transmission, repeating motifs, or multiple scales. Identify what the shader can represent and what requires geometry. Give defining feature families explicit distribution and profile targets, including intentional sparse/empty areas. Record whether the design is stochastic, arranged, periodic, or unique. Do not convert an organized motif into generic noise.

Keep a stable response benchmark and a separately identified source-like proxy when geometry or layout changes appearance. Preserve the user's established shader ball. Fit physical scale and layout on the proxy; challenge angular response on the benchmark. A solid ball cannot establish a hollow object's absorption fit.


For spatially varied finish, apply the [finish-field contract](../image-material-texture-maps/references/finish-fields.md) before choosing maps. Give normal structure, roughness and reflection strength/coverage separate owners and influence tests; retain physically coherent IOR when appropriate. A shared pore mask does not account for independent broad finish variation.

For distinct directions, particles, yarns or overlapping responses, use
[population models](references/population-models.md). Select additional components
because they predict a missing visible behavior, not because unused sockets
remain. One height field plus one tangent can be inadequate; that is a hypothesis
to test, not a reason to force geometry onto every material.

For defining resolved detail, make the [detail pilot](../image-material-detail-pilot/SKILL.md)
an early branch before production-map expansion. A failed source identity or data
semantics finding routes back immediately; a valid graph is not a substitute.

## Hand off a construction plan

Deliver `input_audit`, `layer_plan`, `representation_plan`, and `experiment_plan` in the case. Each defining feature must reach an implementable control or an explicit unresolved limitation. Rank uncertainties by their effect on the target appearance. Route morphology/identity uncertainty to analysis, appearance alternatives to [lobe prompts](../image-material-lobe-prompts/SKILL.md), and response/units uncertainty to [calibration](../image-material-calibrate/SKILL.md). Resolve critical representation questions before generating production maps; do not block independent studies on unrelated unknowns.

In a full reconstruction, proceed to generation and inspection. A complete plan is not proof that the shader, maps or final material work.

For separate feature populations, region-dependent finishes or organized motifs, delegate field design to [spatial design](../image-material-spatial-design/SKILL.md). Keep its morphology, distribution and property ownership explicit. Do not represent a requested physical stack merely by interpolating one set of surface parameters.

For fibers, flakes, pile or organized grooves, read [structured scattering](references/structured-scattering.md). Inspect a technical exemplar only when field/mapping review leaves an unresolved representation or renderer-behavior question and research is in scope; keep it separate from identity evidence.

For research into complex authored examples or a suspected representation ceiling, use [exemplar research and mechanism transfer](references/exemplar-research.md). Trace active graph relationships, test native responses, and turn findings into evidence-tagged mechanism records before borrowing them for a new image.

Before generating contribution studies, use [transport diagnostics](../image-material-diagnostics/SKILL.md) to assign each consequential mechanism an observable and discriminating control. For resolved yarn, loops or pile, read [textile construction](references/textile-construction.md) to separate population geometry from aggregate fuzz and mapped finish; this route also applies to analogous hierarchical strands.

For built-up surface response, inspect [complete exemplar constructions](references/built-up-exemplars.md), including composed scalar values, normal ownership, masks and actual base/coat connections. Follow the live graph rather than material labels.
