# Shared case contract · version 3

Use one case record, structured as JSON/YAML or equivalently explicit Markdown, plus referenced files. Start from [case-template.json](case-template.json) when useful. Populate only the current stage; empty future sections mean pending, not successful. All case-local paths are relative to the case root. Record external sources with stable identifiers or URLs and their usage rights. Copying skills must not require copying any case assets. Make the case handoff usable by a fresh agent without prior chat: include the current accepted artifact set, source/crop roles, preservation constraints, pending failures and superseded revisions.

## Keep the decision view compact

For planning or a narrow review, one table can carry `evidence/feature IDs | competing cause | proposed control/representation | next discriminating test | status`. Reuse these IDs in prompts and input audits instead of repeating the same prose in every section. Populate only executed or requested stages; leave future fields pending. Put complete per-input accounting in a linked appendix when needed, grouping inactive child rationales. This reduces duplicate bookkeeping without reducing the coverage or inspection required for a full high-fidelity reconstruction.

For an explicitly observation-only plan, source-image inspection, pixel regions and correspondence remain pending; carry attributed observations instead. The stage table below does not require invented assets or coordinates to complete that plan.

## Required handoffs

| Stage | Required output for the executed stage |
| --- | --- |
| Analysis | Source image and target regions; evidence IDs; feature morphology and preservation constraints; coordinate/scale assumptions; competing hypotheses; editable layer plan; confidence and distinguishing tests |
| Architecture | Installed input dispositions or provisional families; editable layer construction; representation/scale plan; consequential capability gaps and experiments |
| Lobe studies | Mechanism-to-study coverage ledger; cell manifest, alternatives and full-resolution selections; exact submitted prompt, feature coverage and input precedence; lighting/camera/layout contract; generated artifact IDs; appearance predictions; inspection findings; accepted/rejected/provisional status |
| Texture maps | Shared layout revision; one channel contract per map or scalar; exact prompts and inputs; raw outputs and processing; contour/profile/population checks and cross-map inspection; encoding, range, units, seams and orientation |
| Calibration | Tested color/data/display conventions; geometry/scale assumptions; controlled parameter trials; influence and transfer checks with limitations |
| Assembly | Calibration controls; target versions/capabilities; explicit source-to-socket table including operations; graph and binding; validation result; scene/lighting/view transform; render evidence and routed corrections |
| Review | Source/generated/native comparison; comparability limits; defining-feature findings; routed experiments; visual acceptance separate from technical validity |

A conditional detail pilot hands off selected feature/source/field/native crop
IDs, crop scaling, data-semantic findings, representation/basis, changed/fixed
variables, separate identity/data/native verdicts, earliest loss and routed next
action. Use `detail_pilots` already in the case; avoid duplicating feature records.
Its status is pending until inspected, even if the full graph rendered.

## Stage status examples

Use explicit stage statuses such as `pending`, `analysis_complete`, `prompts_authored_ungenerated`, `studies_generated_unreviewed`, `studies_reviewed`, `contracts_and_prompts_only`, `maps_generated_unreviewed`, `maps_reviewed`, `provisional_plan_only`, `graph_validated_unrendered`, `render_reviewed`, or `blocked`. Equivalent clear wording is acceptable; this is not a closed enum. Keep artifact acceptance (usable/provisional/rejected) separate from stage completion. In a planning request, completing the plan does not advance generation or rendering status.

Keep `quality_verdicts.execution`, `quality_verdicts.mechanism_influence` and
`quality_verdicts.source_fidelity` independent. A defining feature failure vetoes
source-fidelity acceptance; technical completion and a prototype deliverable can
still be reported. Store identity constraints on existing feature IDs and preserve
superseded verdicts in revision history.

## Record conventions

- `fidelity_target`: requested quality, intended views/scale/lights, defining criteria with evidence, and explicit user budget if any.
- `mechanism_inventory`: ID, physical mechanism/layer/regions, active/uncertain/unsupported status, evidence/counterevidence, generated cell IDs, native test IDs, and unresolved limitations.
- `transport_contracts`: study ID, output type, target scope, first-event/other selection, retained later events, excluded paths, complete scene, native behavior reference/provenance/settings, exposure/display, additive claim (none for generation), positive/negative visual tests, observed result and limits. See [transport semantics](../../image-material-lobe-prompts/references/transport-semantics.md).
- `benchmark`: accepted specimen/UV asset IDs and hashes, geometry transforms, camera, lights/environment, exposure/display and separately labeled diagnostic variants. Preserve the user's established setup across trials.
- `study_cells`: ID, sheet artifact and row/column, hypothesis IDs, changed/locked variables, prediction, actual inspection, selection/rejection reason, and full-resolution successor.
- `calibration`: tested path, known inputs, rig/display settings, native outputs, result, limits and invalidation conditions.
- `quality_acceptance`: pending/prototype/accepted/blocked status, criterion findings, blocking deltas and next experiments.
- `evidence`: id, source artifact, normalized region or feature location, visible observation, limitations.
- `hypotheses`: id, evidence IDs, proposed explanation, alternatives, confidence (low/medium/high with reason), counterevidence, chosen/provisional/rejected, distinguishing test.
- `features`: id, evidence/crop IDs, region/anchors, morphology (contour, edge/profile, topology, orientation), population (size ratios/range, density, spacing/clustering), scale band, confidence/visibility limits, physical interpretation, affected layer/channel IDs, shared versus independent boundaries, locked traits, allowed changes, forbidden drift, and inspection/tolerance basis. See [feature preservation](feature-preservation.md).
- `layer_plan`: status, components (stable IDs, evidence, color-composition/physical-interface/spatial-region role, order/adjacency, owned properties, coverage/mask authority, coordinate field and scale, independent controls, uncertainty, intended native tests), relationships, combination operations and known approximations. See [layer architecture](layer-architecture.md).
- `prompt_contracts`: id, exact prompt ID, feature/layer IDs, input artifact IDs and precedence, concrete preserved constraints, permitted changes, output semantics and review criteria. Record intentionally omitted irrelevant features; IDs alone are not submitted visual instructions.
- `feature_checks`: feature ID, artifact/version, inspected crop/view, morphology/profile/population/relationship findings, preserved/changed/lost/unassessed verdict, measurement or visual evidence, and correction route. Distinguish correspondence to source from consistency with synthesized layout.
- `revision_log`: id, parent and successor artifact IDs, intended change, locked features, observed regressions, selection/rejection, invalidated downstream artifacts/checks, and revalidation results. Never rewrite historical evidence to appear current.
- `artifacts`: id, path, role, provenance, parent IDs, layout revision, status, and inspection result. Preserve original output and create a new revision when processing changes values or layout.
- `channel_contracts`: id, physical property, layer, map/scalar/geometry decision and reason, input artifact/channel, encoding, intended numeric range, units, UV/UDIM/tiling, value polarity, normal convention if relevant, processing, uncertainty.
- `connections`: channel contract ID, source node/output, operations in order, destination node/input/type, fallback or unavailable capability, validation evidence.
- `reviews`: hypothesis tested, artifact IDs, observed discrepancy, likely cause and alternatives, next experiment, route, outcome.

Prompts must contain actual descriptions drawn from the inspected image, or attributed user observations for an explicitly requested observation-only plan. In that mode, distinguish synthetic specimen/layout choices from evidence and leave image inspection/correspondence pending. Template placeholders are authoring aids, never finished deliverables. Save generator/model identity and settings only if exposed; use unknown otherwise. Distinguish generated candidates, processed assets, native render outputs, and display previews. A generated picture of a lobe is not a native AOV.

## Small knowledge graph

Keep `knowledge.nodes` and `knowledge.edges` in the case record; no graph database is required. Nodes reference existing evidence, hypothesis, feature, layer/component, input, representation, experiment, prompt, artifact, channel, connection, and review IDs. Use unambiguous IDs across the case. Edges use explicit verbs such as supports, contradicts, tests, constrains, generated-from, drives, or revises. Each edge carries a short rationale and evidence IDs where available.

Example directed edges: E1 supports H1; H1 constrains P1; A1 generated-from P1; C1 describes A1; C1 drives W1; R1 tests H1. Here E/H/P/A/C/W/R identify evidence, hypothesis, prompt, artifact, channel, connection, and review records. Each ID must resolve to an actual record; use multiple edges when a result depends on several inputs. Add feature → constrains → prompt, component → owns → channel, and review → invalidates → artifact/check relationships where relevant. Add feature → represented-by → representation, component → controls → input, and experiment → tests → input/hypothesis edges when those records exist. Keep causal explanations attached to edges; a connectivity graph alone cannot explain why two maps should share a boundary.

Promote a rule to reusable knowledge only after a rendered test supports it. Store its conditions, supporting and conflicting cases, confidence, and correction route. Keep material-specific cases outside the skills; a single success does not establish a universal rule. Rejected hypotheses remain useful counterexamples.

## Iteration and stopping

For each mismatch, identify the earliest responsible stage. Change one meaningful cause at a time when practical. Preserve the best candidate and rejected experiments with their reasons. For complex/high-fidelity work, explore competing interpretations, refine useful studies, and test actual maps and rendered behavior. Do not impose a small candidate quota or stop after one correction while defining failures have actionable tests. Use the user's stated budget; when none is specified, continue evidence-driven corrections without repeatedly rerunning an uninformative experiment. Ask for direction only when a consequential ambiguity or resource limit cannot be resolved independently.

Finish when the requested stage is complete. A full material requires coherent maps, validated connections, and the visual acceptance review in [image-material-review](../../image-material-review/SKILL.md). A technically successful render with missing defining features remains a prototype. A user-requested preview or plan can finish without full-material acceptance; mark later stages pending. Exact additive reconstruction of beauty from LPEs is not required. Report untested claims and unavailable capabilities explicitly. Migrate v1/v2 case records by adding layer_plan, prompt_contracts, feature_checks and revision_log as pending/unassessed, extending feature records only from available evidence. Add optional v0.4 `transport_contracts` and `benchmark` records as pending to older v3 cases; this is an additive extension, not evidence that earlier studies passed these checks. Keep older validations tied to their original artifacts; never invent completed checks.

## v0.5 construction and fitting records

- `input_audit`: definition/package/renderer versions and provenance; each available input's type/default, disposition, component/feature owner, evidence/rationale, channel/value, capability state and influence test. Include external geometry/volume controls. Group inactive child rationale without hiding inputs.
- `representation_plan`: feature IDs, geometry/displacement/normal/roughness/color/volume decision, coordinate field, physical scale and uncertainty, ownership of frequency bands, optical/thickness consequences, native check and unsupported behavior.
- `experiment_plan`: question, competing causes, changed/locked variables, predicted regional response, specimen and settings, generated/native artifact IDs, observed result, confounders, selection and invalidated checks. Distinguish proposed from executed experiments.
- `feature_packets`: source crop IDs and roles, defining family, literal morphology/profile/population constraints, smooth/empty regions, channel effects, submitted prompt IDs and per-output findings.

Architecture outputs the input audit, editable layer construction and representation plan. Calibration outputs tested conventions and a parameter fit with assumptions and transfer checks. Add these fields as pending/empty to older v3 cases; do not invent historical passes. Keep all ten skill directories together. Cross-stage routes are dependencies and may loop when a test changes the physical interpretation.

## v0.6 fine-detail records

Use these only when fine structure is consequential; compact rows or linked artifacts suffice. See [detail reconstruction](../../image-material-texture-maps/references/detail-reconstruction.md).

- `detail_targets`: source crop and feature ID; shape/profile and population constraints; physical or relative scale with uncertainty; likely properties and alternatives; expected closeup/hero visibility; acceptance observation.
- `sampling_checks`: actual returned dimensions/bit depth, patch coverage and local UV span, estimated feature texels in both axes, projected render pixels, filtering/denoising considerations, and action if unresolved. Requested size is not actual resolution.
- `detail_pilots`: accepted source/field revisions, actual scale/mapping, diagnostic specimen/view/light, changed/fixed variables and sampling, native closeups, observed morphology/visibility, pass/fail/uncertain, earliest loss and correction route.

Add these empty to older records without inventing retrospective validation. Preserve the primary benchmark while adding separately identified diagnostic views. A passed optical study does not imply a passed morphology pilot.

For spatially complex cases include `spatial_plan`: independently identified feature families, source anchors, regional controls, coordinate/scale assumptions, property ownership, overlap rules and defaults on other geometry. Record actual generated encoding and any rejected literal edit constraints. Keep source identity, research facts and generated hypotheses distinguishable in the evidence ledger.

## v0.8 spatial finish records

When finish varies or is disputed, add `finish_fields`: property/layer and evidence IDs; map/uniform/unresolved decision; morphology and scale; independent/shared authority; generated study/map IDs; measured encoding and calibrated final range; exact graph connection; normal/roughness/strength control artifacts; predicted versus native behavior; final-size visibility; acceptance and uncertainty. Follow [spatial finish](../../image-material-texture-maps/references/finish-fields.md). Add this as pending to older cases; do not infer historical passes.

## v0.9 conditional transfer evidence

For projection changes, curved transfer or animation, add `coordinate_transfer` with the field frames and scale, mapping tradeoffs, normal basis, required attributes/defaults, accepted artifact IDs, angular tests and invalidated checks described in [coordinate transfer](../../image-material-spatial-design/references/coordinate-transfer.md). Leave it pending when not executed. Reuse `study_cells` and `hypotheses` to distinguish a failed illustration from a tested physical rival; reuse `reviews` to exclude runtime fallback images from optical comparisons. No new universal per-material checklist is required.

## Diagnostic coverage

Use `diagnostic_plan` for the conditional diagnostics stage: hypothesis/evidence IDs,
competing causes, output kind, expression or built-in name, target/light labels,
fixed fixture and artifact revisions, batch ID, matched intervention, positive and
negative predictions, documented/returned/positive/controlled-semantic status,
actual observations and unresolved limits. Link existing mechanism and study IDs;
do not duplicate their records. Add this as pending to older cases, never infer
retrospective diagnostic coverage.

## v0.15 conditional mapping and deformation evidence

Extend `coordinate_transfer` only when relevant: per-family coherent versus
stochastic classification; shared tile identity/rotation/weight policy; actual
projection and synthesis equations/settings; native translation/sampling evidence;
structured/production and layer/normal controls; all-buffer finite findings;
transition and continuous-motion verdicts. Leave unexecuted checks pending.

Use existing `features`, `spatial_plan` and `detail_pilots` for broad fold shoulder,
trough, continuity and quiet-land constraints, construction scale and local residual
ownership. Record the earliest source/appearance/field/native morphology loss.
Store trial settings with implementation and case conditions; never promote a
single sharpness/gain combination to an unconditional preset.
