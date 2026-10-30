---
name: image-material-diagnostics
description: Design and verify hypothesis-driven material diagnostics using native light-path selections, light groups and matched parameter interventions. Use before complex lobe studies, when aggregate diffuse/reflection passes hide a disputed mechanism, or when reviewing diagnostic coverage; does not own a renderer bridge.
---

# Image Material · Transport diagnostics

Turn the case's consequential hypotheses into observable tests. Route here from
[architecture](../image-material-architecture/SKILL.md) before contribution prompts,
and revisit during assembly or disputed review. For planning-only work, author the
plan and mark native support and results pending. Reuse sufficient existing tests;
a narrow repair does not require a complete new material reconstruction.

## Choose observations before output names

Read the mechanism inventory and [transport meanings](../image-material-lobe-prompts/references/transport-semantics.md).
For each active or consequential uncertain mechanism, make a compact row:

`evidence/hypothesis → rival explanation → observable/path selection → revealing
fixture/light/view → parameter intervention → positive/negative prediction →
native support and result → remaining ambiguity`.

Every claimed mechanism needs an observed discriminating test or an explicit
unresolved limitation. An aggregate parent pass, connected input, or empty buffer
does not close that row. Do not use the same fixed channel list for every material.
Choose additional outputs when they distinguish a live hypothesis; file count is
not complexity. Preserve the user's primary shaderball and rig, and label added
diagnostic fixtures or illumination separately.

Read [selection strategies](references/selection-strategies.md) for finish, fibers,
translucency, flakes and layer interactions. Keep four different meanings clear:

- Physical/model components: base, coat, fuzz, medium, particle populations.
- Path selections: reflection/transmission, event mode, depth, source light, geometry.
- Intrinsic data: roughness, normal, tangent, coverage, coefficients and color.
- Interventions: the changed coupled response after disabling or flattening one input.

A shader component can contribute to multiple path sets; multiple components can
share one event bin. Named geometry/light labels do not imply addressable coat,
fuzz or subsurface labels. Absorption is attenuation, not an additive radiance lobe.

## Resolve the renderer adapter

For OVRTX, read [the LPE adapter](references/ovrtx-lpe.md). For another renderer,
resolve its documented syntax, produced event classifications, layer labels,
output limits and cache behavior independently. Track `documented`, `authored`, `returned`,
`positive_contribution`, `controlled_semantics` and `unresolved` separately. A parser accepting a token does not
prove that the integrator emits it. Renderer version changes can invalidate these
capability findings without invalidating the physical hypothesis.

Split required selections into supported batches with the same frozen graph,
textures, camera, lights, settings and raw baseline output. Include relevant built-in material-data and transport AOVs
from the adapter; LPEs are only one diagnostic tool. Use the host's official
runtime/client through [assembly](../image-material-assemble/SKILL.md); do not add
a bridge or renderer implementation to this bundle. Check actual returned buffers,
not just authored RenderVars. Preserve exact expressions and label bindings.

## Pair selected passes with interventions

For a claimed coat, fuzz, film or mapped finish effect, compare the original and
controlled material in the **same selected path output**, as well as beauty. For
example, direct key-light reflection before/after flattening coat roughness can
reveal a change hidden by combined lighting. The difference is a causal effect,
not a recovered additive coat image. Keep baseline revisions matched; an old
control cannot establish influence in a newer graph/map revision.

Freeze texture dependencies before capture. Preserve the effective graph except
declared edits, including inherited connections. If a tiny near-off value avoids
unnecessary recompilation, state the value and verify residual energy is negligible
for the claim; do not call it exactly zero. Do not change a physical experiment to
optimize compilation if that changes the question being tested.

Before interpreting a black selection, check produced-event support, labels,
geometry/path topology, ray depth, light eligibility and a known positive fixture.
Small effects require enough samples or a repeat baseline to bound Monte Carlo
variation. An output can be correctly empty for this scene while support remains
unverified. Subsurface shading need not appear as explicit volume events.

## Drive generation and review from the same plan

Send the selected observables to [lobe prompts](../image-material-lobe-prompts/SKILL.md).
Each generated cell states the actual allowed path content or changed parameter,
fixed scene, source morphology, prediction and falsifier. Use native behavior
guides when available. Keep generated pictures qualitative; do not force imagegen
to fabricate a precise event isolate it repeatedly fails to represent. Retain the
attempt and test the physical hypothesis natively.

Review source → generated prediction → fields/graph → selected native response →
beauty. Use common exposure for comparable passes; if a boosted preview helps see
weak contributions, retain the original and label the gain. Overlapping path sets
must not be added or scored as an exclusive decomposition. Simple disjoint
partition checks can catch capture errors, but exact beauty recomposition is not
a material-fidelity gate.

Handoff `diagnostic_plan` rows with expressions, labels, batch IDs, dependencies,
controls, predictions, observations and support status to calibration/assembly and
[review](../image-material-review/SKILL.md). Uncovered consequential mechanisms keep
coverage pending, even if the beauty looks plausible. Source fidelity remains a
separate verdict from diagnostic execution and measured influence.

For doubled or softened detail after projection/hex edits, use [mapping-blend controls](../image-material-spatial-design/references/mapping-blends.md) beneath the same interface before refitting roughness. Verify finite values in every claimed returned buffer, not beauty alone. Built-in bump-normal output may describe an outer interface; use matched layer/normal interventions to test buried structure.
