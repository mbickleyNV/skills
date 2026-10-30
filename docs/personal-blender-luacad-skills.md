# Personal LuaCAD and product workflows

The current generalized LuaCAD/product set is published on this fork's `main`
branch under `skills/`. These personal workflows are separate from the inherited
NVIDIA verified/signed catalog; no NVIDIA signature or certification is claimed.

## Current generalized set

| Skill | Purpose |
|---|---|
| [luacad-product-reconstruction](../skills/luacad-product-reconstruction/SKILL.md) | Reference evidence → dimensioned named CAD assemblies |
| [luacad-fidelity-modeling](../skills/luacad-fidelity-modeling/SKILL.md) | Detailed product modeling and source/normal/UV acceptance |
| [luacad-manufactured-details](../skills/luacad-manufactured-details/SKILL.md) | Manufactured edges, pulls, hardware and profiles |
| [luacad-continuous-geometry](../skills/luacad-continuous-geometry/SKILL.md) | Continuous solids, shells, apertures and topology |
| [luacad-2d-to-3d-complexity](../skills/luacad-2d-to-3d-complexity/SKILL.md) | BOSL profiles, offsets, sweeps, skins and placement |
| [product-evidence-extractor](../skills/product-evidence-extractor/SKILL.md) | Variant-specific cited facts from manuals and drawings |
| [product-asset-preparation](../skills/product-asset-preparation/SKILL.md) | Isolated saved product assets and normal/UV/material receipts |
| [product-turntable](../skills/product-turntable/SKILL.md) | Explicitly requested studio product turntables |
| [blender-product-assembly](../skills/blender-product-assembly/SKILL.md) | Product shading, photography and assembly animation |
| [appliance-installation](../skills/appliance-installation/SKILL.md) | Installed appliance envelopes and coordinated cabinet fit |
| [articulated-furniture](../skills/articulated-furniture/SKILL.md) | Furniture mechanisms, simulation and manipulation handoffs |
| [digital-twin-iteration](../skills/digital-twin-iteration/SKILL.md) | Routing mixed reference, CAD, material and preview requests |
| [material-reference-lookdev](../skills/material-reference-lookdev/SKILL.md) | Reference-based finishes and physically scaled PBR maps |
| [image-feedback-to-cad](../skills/image-feedback-to-cad/SKILL.md) | Accepted visual concepts → source-backed integration |
| [cabinetry-refinement](../skills/cabinetry-refinement/SKILL.md) | Existing cabinetry detail under dimensional constraints |
| [existing-asset-refinement](../skills/existing-asset-refinement/SKILL.md) | In-place construction and finish refinement of existing assets |

Start with `digital-twin-iteration` for mixed requests or
`luacad-fidelity-modeling` for modeling. Use focused skills for focused work.
The nine other personal Blender/architectural workflows from the earlier
publication remain available; they are outside this generalized product refresh.

## Portability and dependencies

These 16 directories were refreshed from the current canonical shared catalog
and current project workflow sources, with all their references and bundled
helpers. Generalization removes personal home-directory paths and makes project
adapters explicit rather than assuming a particular remodel, Blender file,
specialist roster, studio or service is installed. The
[source inventory](personal-product-skills-sources.json) records original and
published SHA256 values for every file, distinguishing source updates from edits
made for portability.

Each directory is a skill, not a tooling installer. Install related skills side
by side, or let the agent discover installed siblings by name. References written
as `skills/<name>/...` describe sibling skills in this repository. Supporting
camera, room-rendering and scene-update skills remain in the earlier personal
set. Tile-layout planning is an optional separately installed workflow, not part
of this product bundle.

Only scripts physically inside a skill directory are bundled. Product asset
preparation, turntable capture, articulation/robot adapters, project-specific
imports, canonical scenes, studio templates and renderer binaries are external
integrations. References retain example paths and interface contracts to make
those boundaries inspectable; map them to the active project's maintained
implementation before execution. `/absolute/...` denotes a placeholder, never an
installed path. Missing tooling does not justify inventing support or silently
claiming that a source model is render-ready. A source-only result remains valid
when that is the requested scope.

Use the active project's renderer and save/publication rules. Named specialist
roles describe responsibilities, not an instruction to start agents without
authorization. A sole coordinator can perform those responsibilities; live
Blender always has one owner. Turntables and external publication are separate
requested actions, not automatic consequences of modeling.

## Validation and publication

See the [publication engineering note](engineering-changes/generalized-product-skills.md)
for scope, checks, limitations and rollback. Packaging checks do not establish
fresh LuaCAD, Blender, renderer, simulation or robot behavior. This publication
does not change installed skills, the canonical local catalog or any live scene.
Future updates use a normal fast-forward push; rollback uses a normal revert,
with no force-push or rewriting inherited catalog history.
