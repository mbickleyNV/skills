# Generalized LuaCAD and product skill publication

## Problem and resulting behavior

The personal skills snapshot on `mbickleyNV/skills` main at `b3f18b0` omitted
product-evidence-extractor and lagged current product UV, material production,
curved-surface fidelity and integration guidance. It also presented personal
machine paths and project integration files as local prerequisites.

Refresh 16 LuaCAD/product workflow directories (50 files including two Python
helpers), add the missing evidence extractor, and preserve current source lessons.
Generalize personal absolute paths into explicit placeholders; use sibling skill
references; state project/tool/scene dependencies and authorized specialist
fallback in each entrypoint. Keep studio selection project-owned, preserve the
requested renderer, and distinguish historical adapters from installed support.
The index lists the exact scope. Nine earlier personal support skills and the
inherited NVIDIA catalog remain outside this refresh.

## Changed source, revision and data contracts

Destination: https://github.com/mbickleyNV/skills on main. The publication commit
containing this note identifies the exact revision; its parent is `b3f18b0`.
Source selection: canonical shared `agent-skills/skills` for shared workflows;
current project `skills` for project-developed product workflows. Do not author
into installed Codex/Hermes projections. Original and publication SHA256 values
for every scoped file are in `docs/personal-product-skills-sources.json`.

Preserve named CAD identities, units, source topology versus render normals,
metric UV and physical-scale evidence, source/asset receipt hashes and explicit
native acceptance stages. Preserve product-source-packet/1 and product-evidence/1
helper interfaces. No runtime/API implementation changed. Packet/turntable and
robot interfaces described in references belong to optional external adapters;
this publication does not supply or certify those adapters.

## Validation and observed results

Validated an isolated catalog at `/tmp/product-skills-validation`, containing
only these 16 published directories and the canonical fleet validation tooling:

- `python3 scripts/skill_fleet.py validate`: all 16 valid after removing an empty
  source reference directory (empty directories are not portable or Git content).
- `python3 -m unittest discover -s tests -v`: 18 existing checks passed.
- `scripts/nix-flake flake check`: passed using the canonical pinned container
  and flake lock. Upstream informational warnings: unknown flake outputs
  skillsSrc, skillNames and allSkillSources.
- The existing skill-creator `quick_validate.py`: all 16 entrypoints passed.
- Both bundled Python helpers parsed; drawing-overlay CLI loaded successfully.
- Evidence extraction smoke check prepared a temporary text-source packet,
  accepted an exact cited quote and rejected a fabricated quote.
- Published file hashes matched the complete scoped inventory. Relative Markdown
  file links resolved; a naive link scan's two matches inside Python code were
  inspected as code, not links. No personal home-directory paths remain in scope.
- Credential-pattern scan found no private keys or recognizable GitHub/AWS/OpenAI
  token patterns. `git diff --check` passed.

No LuaCAD generation, Blender process, native renderer, simulation or robot was
run. These checks establish packaging and helper behavior, not new visual or
native-runtime validation. No render was needed for this instructions-only update.

## Deployment, limitations and recovery

Source publication only: no installed skill, fleet state, local canonical catalog,
scene, renderer or service changed. External helper paths, specialist contracts,
studio assets and pipeline examples require a maintained project equivalent;
`/absolute/...` is explicitly a placeholder. The product workflow is reusable
but is not a standalone Blender/robot toolchain installer. Historical native
observations retain their bounded evidence status.

Reproduce by checking out this publication revision, installing the selected
skill directories side by side and running the checks above in an isolated fleet
catalog. Use the source inventory to compare future source updates without
silently overwriting the generalized edition. Roll back with a normal revert of
this publication commit. Do not force-push or reset inherited catalog history.
