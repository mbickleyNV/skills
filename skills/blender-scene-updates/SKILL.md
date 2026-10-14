---
name: blender-scene-updates
description: Optimize Blender-to-USD-to-OVStage/OVRTX edit propagation and diagnose slow scene refreshes. Use for exporter/adapter/runtime performance engineering, not ordinary authoring or rendering.
---

# Blender scene updates

Read the project's active backend contract and current state. Keep the installed
backend; upstream documentation is evidence, not authorization to upgrade.
Leave a running native capture with its current owner. Review files/receipts
without live Blender calls; activate runtime changes at an idle boundary.

Use [change routing](references/blender-scene-update-routing.md) for API contracts and candidate
routes. It covers Blender provenance/evaluation, shared data/instances, USD
population versus typed values, and native completion. Check installed versions
before relying on newer documentation.

Classify the actual affected output, not just the user's edit intent. Preserve
original ID identity, geometry/transform/shading flags including unknown,
evaluation context, bindings and dependent owners. Coalesce notifications before
reconciliation. Route proven value changes without geometry export; export only
changed geometry and affected consumers. Unknown/unsupported changes retain a
reasoned fallback. No room-name or product-name special cases.

Measure one representative warm edit at matching render settings. Report
end-to-end latency plus preparation, generation, delta, native population and
accumulation. Nested timings are inclusive. Distinguish process/session reuse,
scoped population and full replacement; a Stage ID alone proves none of these.
Acknowledge existing receipts after lost replies instead of rerendering.

Keep validation proportional: changed-source/material/normal guards, focused
regressions for the routing change, and one affected image. Historical audits,
full scene inventories and save/reopen proofs are not routine render steps.
The saved Blender scene is authoring authority; update caches retain current
projection state, not a living record of past design decisions.

For this adapter, use [project knowledgebase](references/scene-update-knowledgebase.md). Routine captures remain in `skills/ovrtx-room-rendering/SKILL.md`.
