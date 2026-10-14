---
name: luacad-fidelity-modeling
description: Build or refine high-fidelity LuaCAD product and fixture models with reference-specific detail, complex profiles, verified exported geometry and explicit render-normal/UV handoffs. Use for dedicated modeling specialists and realism detail passes; research-only and material-only requests use their focused specialists.
---

# LuaCAD fidelity modeling

Read current HANDOFF and AGENTS. Default to close-view product fidelity unless the
user asks for a simplified model. Keep dimensioned geometry in XML/LuaCAD, stable
part IDs and current authoring source. No quiet quality downgrade because a curve,
Boolean or detail is difficult. A blocked detail remains an explicit unresolved item.
Do not promise manufacturing accuracy from inferred construction.

## Use the complete LuaCAD toolkit

Consult all four skills for a modeling assignment; load their deeper references
only for the construction being attempted:

- `luacad-product-reconstruction`: exact variant/evidence, named assembly, dimensions,
  drawing overlays and export. Discover installed entrypoint; canonical shared source
  is `/home/mbickley/agent-skills/skills/luacad-product-reconstruction/SKILL.md`.
- `skills/luacad-manufactured-details/SKILL.md`: edges, lips, pulls, formed hardware
  and panel highlights. Generic radii are inferred fallbacks, not product facts.
- `skills/luacad-continuous-geometry/SKILL.md`: real continuity, shells/apertures,
  mating datums, retired IDs and welded topology distinct from render normals.
- `skills/luacad-2d-to-3d-complexity/SKILL.md`: profiles, offsets, sweeps, skins,
  rounded forms, attachments and efficient repetition; verified installed syntax.

Architectural changes also use room XML/ROOM-CONTRACT and drawing evidence;
installed appliance fit uses `appliance-installation`; articulation uses
`articulated-furniture` when requested. Do not start simulation for ordinary fixtures.
Coordinate with product_detail for disputed references and material_specialist for
surface scale/finish intent when useful and authorized. Share datums rather than
asking each worker to infer them independently.

## Complete the visible detail, then prove it

Use [detail and surface acceptance](references/detail-surface-acceptance.md).
Build a compact feature ledger from the finished views and relevant drawings before
source implementation. Include inner/cavity details that affect view, shadow,
reflection, transmission, attachment or motion, not just the outside envelope.
No invisible filler detail solely to inflate complexity. Express the actual shape
with a reusable profile/path/shell or repeated recipe; higher complexity is appropriate
when the reference demands it. Preserve apertures and section changes as geometry.

Model silhouette/envelope and mating faces, then reference-specific lips, shoulders,
seams, inner reflectors/supports, recesses, cutouts and edge transitions. Revisit each
ledger item at source export and intended view scale. Increase curve/path samples
where silhouette or highlights still facet; planar subdivisions do not add fidelity.
CAD color and smooth preview shading cannot stand in for missing geometry.

Inspect dimensioned named-mesh overlays when drawings exist and close views exposing
remaining detail. A front beauty view cannot prove underside/cavity construction.
Validate changed geometry's bounds, intended connected components, edge incidence,
positive volume, winding and apertures; reconcile stable/retired IDs. Isolate a failing
junction to solve it before repeating across the assembly. Efficiency comes from
reusing validated recipes and unchanged outputs, not deleting requested detail.

## Source owner and integration handoff

The luacad_modeler edits only coordinator-assigned source modules and their build
outputs. Shared XML edits return named snippets unless the worker has sole ownership.
Freeze export digests before import. Never control live Blender, renderer, canonical
scene saves or publication from a parallel CAD worker.

Read `blender/PIPELINE-CONTRACT.md` for a requested Blender handoff. Supply per-part
render-normal and UV intent with material regions, physical scale, grain directions,
seams and delicate surfaces. Native named 3MF does not establish preserved loop UVs
or custom normals. For an authorized standalone product, hand frozen geometry,
surface/normal/metric-UV intent and material recipe to `asset_preparer` using
`skills/product-asset-preparation/SKILL.md`; isolated preparation can run while
OVRTX is busy. Guarded live house imports remain coordinator-owned. The
coordinator owns evaluated/native visual acceptance. Source-only delivery labels that stage
pending; do not claim the model render-ready from topology checks alone.

Return editable source, named export/digests, feature ledger, reference/overlay and
mesh proofs, scoped validation results, normals/UV handoff and remaining limitations.
Mark a partial model partial. Keep task checkpoints and reusable knowledge through
coordinator review in `docs/specialists/`.
