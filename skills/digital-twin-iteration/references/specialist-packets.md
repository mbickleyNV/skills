# Specialist packets and integration

Project adapter note: paths and commands outside this skill directory describe
optional integration examples. They are not bundled dependencies. Locate a
maintained equivalent and verify its interface before execution; no historical
helper, local service or schema is assumed to be installed.

For repeated product-detail or material work, reuse `.codex/agents/product_detail.toml`
or `.codex/agents/material_specialist.toml` and `docs/specialists/CONTRACT.md`.
For implementing high-fidelity CAD source, use `.codex/agents/luacad_modeler.toml`
with `../../luacad-fidelity-modeling/SKILL.md`; include required detail ledger,
assigned modules and per-part normals/UV handoff in the packet.
Attach the relevant knowledge entries and a named task checkpoint. The coordinator
merges proposed durable findings after review; workers do not promote their own
assumptions. Use the documented explicit-brief fallback when profile selection is
unavailable, and report how the worker was instantiated.

Extend the interface ownership approach in `luacad-product-reconstruction`'s
`references/large-assemblies.md`; do not create competing dimension records.
Share only the affected pages/crops and current view, not the entire chat or blend.

Each task brief contains:

- Exact ask, deliverable stage, intended viewing scale and acceptance view.
- Allowed files or source sections; coordinating owner and neighboring dependencies.
- Reference paths/URLs/pages; specified versus inferred values and unresolved questions.
- Units/axes, controlling parameter names, stable part IDs, source digest and finished
  mating planes. Identify fixed, moving, removable and continuously finished parts.
- Current image/camera and known material/renderer limits when relevant; a read-only
  worker gets no live Blender ownership.
- Return changed files/IDs, assumptions, reusable recipe, scoped validation evidence
  and remaining uncertainty. Shared XML changes return named-element snippets for
  the owner to merge. Freeze exports and report their digest before integration.

Useful independent assignments:

**Tile layout planner:** for mixed formats, trim or order quantities, supply affected
room XML/LuaCAD and existing planning/catalog paths, fixed finish planes, candidate
sizes and quantity assumptions. Reuse `tile_layout_planner` and
`skills/tile-layout-planning/SKILL.md`; receive proposed named-element deltas, repeat
cell/cut math and per-line-item costs. It does not write source or control Blender.

**Reference/detail investigator:** inspect manufacturer drawings and close images;
return variant, measured envelope, missing visible details and uncertainty. Investigate
the disputed feature rather than collecting unrelated product options.

**Geometry owner:** implement one bounded module against shared datums; return named
source and export, interface/bounds checks and a CAD proof. A new repeated lattice
or Boolean recipe should pass on one representative junction before full export.

**Material investigator:** analyze finish references and existing maps; return physical
scale, channel/color-space recipe, grain direction, native compatibility questions
and reference-backed appearance bounds. Do not independently change room lighting
or shared material graphs.

The coordinating owner resolves interface conflicts, applies shared XML snippets,
imports frozen changed parts once, checks evaluated assignments and inspects one
native affected preview. Check live-owner availability before integration; while
a batch or another owner holds Blender, defer imports, material/light changes and
captures until that owner releases it. Source-only work can continue. A late
worker change becomes a new explicit delta. Use
render accumulation for documentation or remaining read-only research. Do not make
every small edit a three-worker task; startup and merge costs can exceed useful work.
