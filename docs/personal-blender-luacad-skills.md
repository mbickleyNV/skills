# Personal Blender and LuaCAD workflows

This personal fork includes 24 Blender/LuaCAD workflow skills used for product
reconstruction, architectural modeling, materials, camera composition, native
OVRTX rendering and scene-update engineering. These are personal workflow
snapshots, separate from the inherited NVIDIA verified/signed catalog. No NVIDIA
signature, certification or benchmark claim is made for these additions.

## Sources and snapshot rules

Shared workflows come from the local `agent-skills/skills` catalog. Remodel
workflows come from the current `63rd-remodel/skills` tree; their room-rendering
and scene-update entrypoints take precedence over the generic shared versions.
The architectural reconstruction entrypoint includes the installed continuous-wall
guidance missing from its older catalog copy. Its other references and helpers
remain from the canonical catalog.

Complete skill references, agent metadata and five Python helpers are included.
Backups, Python bytecode/cache directories and empty directories are excluded.
The scene-update skill includes the current routing document and knowledgebase
inside its own `references/` directory, with its two links adjusted accordingly.

## Use and dependencies

Read each `skills/<name>/SKILL.md` when its task applies, or install the specific
skill directory into your agent's skills location. Start with
`digital-twin-iteration` for mixed requests and `luacad-fidelity-modeling` for
modeling; focused rendering and appearance work use their focused skills.

Project workflows expect the project's current HANDOFF, AGENTS, room XML,
contracts, tools and specialist profiles. Those dependencies and local machine
paths remain explicit; this snapshot does not bundle the remodel project,
Blender scene, service configuration, credentials or renderer binaries.
An installed MCP/runtime and the active project backend contract are required
for live work. Installing these instructions alone does not install the tooling.

## Validation and recovery

The publication was checked with the existing skill fleet catalog validator,
its 18 unit checks, Python parsing of all five helpers, a credential-pattern scan,
and the pinned Nix flake packaging check on an isolated catalog containing only
these 24 skills. These checks establish skill packaging, not fresh Blender,
LuaCAD or native renderer behavior. No scene or runtime was changed.

This is a source publication only. Existing Codex/Hermes installations and the
canonical local catalog are unchanged. Future publication should compare with
the current personal repository head and use a normal fast-forward push.
Rollback is a normal revert of the publication commit; do not reset unrelated
inherited catalog history or force-push.
