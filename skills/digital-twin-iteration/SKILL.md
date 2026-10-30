---
name: digital-twin-iteration
description: Route mixed product or architectural requests from product references or accepted concepts into dimensioned CAD, materials, and fast native previews. Use when coordinating those stages or specialist subagents; simple renders and single-channel edits use their focused skills directly.
---

# Digital twin iteration


For a product-image → editable CAD → detailed image-derived materials → native
turntable request, start with [product-image-to-turntable](../product-image-to-turntable/SKILL.md).
It coordinates the LuaCAD fidelity workflow and ten-skill material bundle with
shared geometry/finish scale, normal/coat ownership and separate fidelity gates.
Focused CAD, finish and preview requests retain the routes below.

## Project adaptation

This is a generalized workflow. Use the active project's source, scene, renderer
and save/publication rules. Names such as `HANDOFF.md`, room XML, specialist
profiles, `blender/tools/`, studio assets and pipeline contracts are integration
examples, not files supplied by this skill. Discover their maintained equivalents
before using them. Only helpers inside this skill directory are bundled. If a
required adapter or asset is absent, report that stage as unavailable and deliver
the supported work; do not invent a command, schema or successful native result.
Use specialist roles only when delegation is authorized and available; otherwise
the coordinator performs the same bounded work. Keep one live Blender owner.


Read the current project handoff and agent instructions, when supplied. Identify the
requested deliverable and the current live Blender owner before choosing work.
Preserve staged intent: research, CAD-only, installation, local save and publication
are distinct actions. A request to model first does not authorize installation.

## Route the actual delta

| Common ask | Load only the relevant workflow |
|---|---|
| Find a product or match a reference | [Product evidence](references/product-evidence.md); research first, no scene mutation |
| Reconstruct a named product or deepen fixture detail | `../luacad-fidelity-modeling/SKILL.md`, which selects the complete LuaCAD toolkit; authorized specialist work uses `luacad_modeler` |
| Prepare frozen standalone CAD/materials as a saved product blend | `../product-asset-preparation/SKILL.md`; `asset_preparer` runs isolated CPU authoring alongside live OVRTX |
| Revise room dimensions or openings | `architecture-drawings-to-3d`, room XML and `house/ROOM-CONTRACT.md` |
| Install an accepted multi-room fixture layout or repeated fixtures with host openings | [Scoped fixture installation](references/scoped-fixture-installation.md); prepare affected parts before live control changes |
| Bring accepted design details into the room | `../image-feedback-to-cad/SKILL.md`; source/import contract only for geometry |
| Change finish, grain, sheen or texture | `../material-reference-lookdev/SKILL.md`; ceramic-specific defects use `skills/tile-finish-lookdev/SKILL.md` |
| Plan tile modules, mixed sizes, trims or ordering | `skills/tile-layout-planning/SKILL.md`; authorized dimensional research uses `tile_layout_planner` |
| Change native camera exposure, pose, optics or movement | `skills/camera-composition/SKILL.md`; no CAD rebuild |
| Tune image grading/exposure compensation, grain or bloom | [Retained-image iteration](references/retained-image-iteration.md), when the retained source and compositor support it |
| Save an alternative or move shared components | `skills/room-variations/SKILL.md` |
| Render saved views or refresh gallery | `skills/ovrtx-room-rendering/SKILL.md` |
| Diagnose slow exporter/native updates | `skills/blender-scene-updates/SKILL.md`; ordinary previews skip this audit |
| Operate doors/drawers or simulate manipulation | `articulated-furniture`; appliance fit uses `appliance-installation` |

Start from the smallest useful affected view. Reuse unchanged geometry, cameras,
materials and evidence. Capture another view only when the requested detail cannot
be judged in that image. Report timings as observations, never projected savings.

## Inspect and apply only the affected scope

For repeated Blender identity/material/bounds queries use
`blender/tools/inspect_remodel.py` through MCP. Pass explicit names, patterns,
collections or a prepared installation receipt; request evaluated geometry only
when needed. Reuse the full baseline for same-query deltas. See
[scoped helper calls](references/scoped-helper-calls.md) for compact invocations,
operation receipt recovery and dependency manifests.

## Delegate useful depth

When delegation is authorized and independent work exists, use
[specialist packets](references/specialist-packets.md). Reference investigation,
source geometry and material analysis can run together with disjoint ownership.
One owner integrates and controls live Blender. A disjoint offline asset preparer
may author its assigned product in the bounded CPU process without taking that
live ownership. Do not spawn a worker merely to
repeat the owner's checks or let multiple workers edit shared XML independently.

Target realism at the least-supported visible features: silhouette, openings,
edge profiles, mating contacts, finish scale and optical behavior. Inspect the
actual resulting image; correct dimensions or a successful USD export alone do
not establish a realistic twin. Label inferred details and native support limits.

Existing dimensioned cabinetry improved from renders/generated concepts routes to
`cabinetry_refiner` and `../cabinetry-refinement/SKILL.md`; reuse existing source
and specialist roles under a numeric dimension lock instead of reconstructing from imagery.

For accepted image-to-existing-furniture refinement, preserve the latest user scope
through specialist handoffs. Route construction/detail tasks as well as finish maps;
finish authorized in-place source/scene replacement rather than returning only a private
pilot. Use cabinetry-refinement fixed/adjustable constraint and delivery-state contracts.

Existing furniture/fixture render → craftsmanship target → source-backed in-place geometry/material refinement routes to existing_asset_refiner and skills/existing-asset-refinement/SKILL.md. Cabinetry uses its specialized extension; render-only input without editable source is concept work, not in-place CAD reconstruction.

High-fidelity product creation includes the material-reference-lookdev production loop:
keep the specialist engaged through actual map/representative-view critique, establish
one reusable finish before broad multiplication, and complete the requested consumer
application. Reuse accepted equivalent finishes/translator evidence; avoid per-variant
validation matrices. Geometry can proceed independently while material reasoning iterates.
