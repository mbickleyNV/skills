# RTPT material capabilities and qualified evidence

Separate source authoring, translator output, native renderer consumption and
appearance. A successful USD export or material-change acknowledgement does not
establish the last two. Preserve the user's requested renderer mode.

## What distilling changes

NVIDIA describes RTPT/Real-Time 2.0 as automatic material distilling to a constrained
multilobe structure, compared with full MDL evaluation in Interactive PT. The
public MDL SDK 2026.0.2 `ovrtx` target is derived from rule blocks also used by
`rtx_distiller`. It has separate coat, glossy and base normal carriers. Some rules
standardize glossy families to GGX V-cavities, merge metallic lobes and average
normal directions, or remove thin-film/coat-absorption modifiers. Do not assume
every nested Blender closure retains an independently sampled reflection lobe.

The public target is not proven byte-identical to an installed `rtx_distiller`.
Distilling can retain compiled procedural input expressions; optional texture
baking and the authoring-time UsdPreviewSurface Distill and Bake extension are
separate operations. Do not automatically bake hex/triplanar input fields.

RTPT caching, roughness thresholds and firefly filtering can also change highlights.
Read the installed runtime's native settings when diagnosis requires them. A UI
DLSS toggle does not prove which reconstruction passes run; device/driver runtime
availability matters. Disabling distilling is not established as a full-MDL RTPT
mode. Alternate target names or structure-print settings need supported API and
material-recompilation evidence before they become a workflow recommendation.

## Bounded validation record (2026-11-01)

ARM64 GB10, Blender5.2.2, SHM base71706012 plus local material repairs; installed
package SHA256 e91ee4256920b7c407d29db23b96eb4adbcecd9743917c544fa5501814309cf4.
Public OVRTX0.6.0.1791947691, loaded MDL SDK2026.0.2 build391700.2276. Native stage
readback: mdlDistillingtrue, target `rtx_distiller`, splitClearcoattrue. This
identifies the tested environment, not a universal minimum or required pin.

| Mechanism | Evidence and limits |
| --- | --- |
| Hex scalar field, procedural flake population and BOX/triplanar scalar field | Editable Blender graphs translated and rendered in Cycles and OVRTX. Exact stochastic hash locations/filtering can differ. |
| Independent Principled mixtures, coat, substrate/coat normals | PT showed independent normal influence and restoration after UV derivative, source Mikk-frame and closure translation repairs. |
| Whole-expression UV Bump | PT relief control passed in this UV route. This does not establish arbitrary 3D/object-space finite differences. Inspect newly introduced coordinate routes. |
| Metallic tangent normals in RTPT | A constant-tilt metallic control changed PT strongly but RTPT only at noise level. Full paint RTPT retained coat/scratches but reduced oriented flake sparkle to flatter speckles. Exact distiller versus downstream consumption remains unresolved. |
| Typed numeric controls | Scalar/color inputs updated while retaining accepted shader paths; controls/restoration passed in PT. Structural graph changes use a separate update path. |
| Thin film, measured BSDF, arbitrary multilayer closures, displacement, volumes and temporal stability | Not qualified by that paint study. Discover and validate the actual requested mechanism; do not infer blanket absence or support. |

The tested explicit source-frame producer requires a modifier-free Mesh without
shape keys and the active render UV set; it carries source corner normal plus
Mikk tangent/sign. Named nonactive UV routes are rejected by that producer.
These are route-specific admission limits, not blanket restrictions on Blender
geometry or all add-on material paths. Use the complete source frame to form a
tangent-map normal, then transform it once (inverse-transpose under nonuniform
scale). Qualify evaluated/modifier routes separately.

## Efficient diagnosis and acceptance

Start from the existing finish's question. For a disputed normal use the same
simple material with geometric versus constant tilted normal before debugging
tiny stochastic flakes. Trace source MDL and distilled glossy-normal expressions
where diagnostic access exists: lost tilt points toward rewriting; preserved tilt
with no response points toward consumption. Existing stage readback alone cannot
make that distinction. Then isolate the flake mixture or coat if needed.

For a new material prefer one matched mechanism control and restored candidate;
do not rerun a historical matrix for known unchanged paths. Hold camera, lighting,
exposure, display and unrelated shader inputs fixed. A nonzero pixel delta proves
neither intended morphology nor independent lobe ownership. Inspect actual images.

Allow native warm-up and compilation to complete. Recover persisted capture
receipts after a lost reply. PT convergence and RTPT stopping criteria differ:
RTPT may report convergedfalse while a requested completed capture is valid.
Worker steps are not necessarily nativeSPP. Separate cold activation, preparation,
submitted edits and image completion; a cold capture is not a frame-rate benchmark.

Sources: [OVRTX RTPT settings](https://nvidia-omniverse.github.io/ovrtx/sensors/cameras/render_modes/real_time_path_tracing.html),
[renderer comparison](https://nvidia-omniverse.github.io/omniverse-performance/skill-tree/reference/render-settings.html),
[pinned MDL distiller rules](https://github.com/NVIDIA/MDL-SDK/blob/1b9592c1b086b691b44d1a30eee4827d1ff55b8c/src/shaders/plugin/mdl_distiller/dist_rules_ovrtx.mdltl),
[distiller API contract](https://github.com/NVIDIA/MDL-SDK/blob/1b9592c1b086b691b44d1a30eee4827d1ff55b8c/include/mi/neuraylib/imdl_distiller_api.h).
