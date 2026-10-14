# Blender scene update routing

Use the saved scene directly for ordinary renders. This reference is for edit
propagation; the [capability knowledgebase](scene-update-knowledgebase.md) records
current implementation and consumer limits. The active backend is the installed
public SDK/OVStream build; newer API documentation does not authorize an upgrade.

## Choose the route by evaluated output

| Change | Current route | Guard |
|---|---|---|
| Existing camera, active product, resolution or supported quality | Direct typed attributes/relationship | Existing mapped targets and supported fields |
| Existing Object/parent pose | Direct native transform/reset writes | Stable hierarchy; cached descendant/evaluated dependency closure |
| Light values, dimensions, inherited scale | Direct shared light conversion | Same form/schema; recompute normalized emitter area |
| Canonical flat/HDR World | Direct supported Dome values/resource selection | Stable supported graph; narrow Mapping Z contract; dirty same-path assets fall back |
| Material constants | Direct existing PreviewSurface/OpenPBR inputs | Same active graph and accepted schema |
| Simple uniform binding | Direct existing material target | Effective Object slots, shared aliases, modifiers and precedence checked |
| Uniform mesh deformation/connectivity/normals/primvars | Direct evaluated mesh arrays | Supported existing schema, bounds and consumer channels; UV texture image proof remains pending |
| Mesh-only Geometry Nodes | Direct evaluated mesh arrays | No curves, volume, point-cloud or instance components |
| GeomSubset/material-face changes | Population fallback | Native subset indices accepted but assignment image wrong; route blocked |
| Existing mesh/light hide-render | One current inline visibility opinion sent to OVStage | Stable mapped owners; derived visibility updates and direct values preserved |
| Graph, membership, parent/schema or physics changes | Established scoped/full population | Explicit consumer/dependency closure; no silent omission |
| Native create/clone/delete/PointInstancer/new graph connections | Experimental or blocked | Not automatic production admission; new-parent propagation failed, instancer probe crashed, graph consumption unproven |

The direct compiler currently applies only to **native camera-sequence capture**.
F12/viewport retain their established paths and reconstruct directly changed
current owners before switching consumers.

## One edit batch, one current projection

Preserve original ID identity, evaluation context and tri-state geometry,
transform and shading flags. Evaluate at the existing frame/edit boundary and
sample nominated owners once. Shared-data and ancestor dependency indices are
captured at bootstrap and refreshed when population changes. Unknown edits
retain a concrete fallback reason.

Write `omni:xform` with an intentional reset boundary and row-vector conversion;
never author derived worldMatrix. Group typed updates, wait for native completion
and invalidate accumulation for affected consumers. Storage acceptance is not
proof that an image or a physics shape updated correctly.

The ACK index retains one current version per attribute. Same population plus
no pending edits is an O(1) no-op; changed owners select only pending rows. New
worker/population identity replays the current projection. Failed/incomplete
writes do not acknowledge it. Runtime values represent the current Blender
scene, not a growing design ledger.

Before population fallback, include all resolved directly changed owners so
stale bootstrap USD cannot restore their older state. Unsupported routes do not
justify a whole-house rescan, history review or save/reopen proof before every
render.

## Primary contracts

[Blender dependency graph](https://docs.blender.org/api/5.1/bpy.types.Depsgraph.html)
provides evaluated output and update notifications.
[OVStage typed writes](https://github.com/NVIDIA-Omniverse/ovstage/blob/71f917ad449d104fb062c6149221cda13417814b/docs/scene/writing_attributes.rst),
[transforms](https://github.com/NVIDIA-Omniverse/ovstage/blob/71f917ad449d104fb062c6149221cda13417814b/docs/scene/transforms.rst)
and [async completion](https://github.com/NVIDIA-Omniverse/ovstage/blob/71f917ad449d104fb062c6149221cda13417814b/docs/concepts/async_model.rst)
separate native storage, hierarchy and acknowledgment.
[OVRTX attributes](https://nvidia-omniverse.github.io/ovrtx/scene/attributes.html)
and [material binding](https://nvidia-omniverse.github.io/ovrtx/materials/material_binding.html)
document renderer-facing updates. Installed code and actual images determine
which documented features this adapter currently admits.
