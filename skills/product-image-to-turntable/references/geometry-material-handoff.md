# Geometry and material handoff

Use a compact case record, not a second asset or renderer schema. Map these fields
to the active project's maintained packets and receipts. Missing fields remain
explicitly inferred or pending. Do not fabricate support for an example interface.

| Field | What it protects |
|---|---|
| Source image identity and region/crop anchors | Geometry and maps refer to the same product, finish and visual authority |
| Known dimensions, units, axes, scale anchor and inferred ranges | CAD, UV extent, relief, wall thickness and scattering distances agree |
| Stable part/surface IDs and material-case IDs | Export/import does not silently assign one finish to every part |
| Surface role, boundaries, continuity and grain direction | Broad faces, edges, cavities and different materials keep their intended treatment |
| Wall/solid construction and thickness assumptions | Thin-edge warmth and attenuation are tested on actual geometry rather than painted edges |
| Source topology, winding, flat/smooth/crease and render-normal intent | Geometric normals, smooth normals and texture normals stay separate |
| UV set or object/rest projection frame; texture physical extent | Fine detail retains scale and orientation through transforms and export |
| Macro/meso/micro ownership | Shape, displacement, bump/normal and roughness are selected by visible effect and sampling |
| Base/coat interfaces, normal ownership and graph hash | A smooth outer film can preserve broad form while suppressing buried fine scratches |
| Channel meaning, encoding, range/units, map hash and actual consuming input | No sRGB decoding of scalar data, double color conversion or disconnected generated field |
| Native support/influence findings and diagnostics | Authored nodes and input definitions are distinguished from demonstrated runtime behavior |
| Saved asset or stage hash, dependencies, renderer and studio identity | The reviewed material is the material in the final movie |

For each critical feature, record its source footprint, intended physical width,
texture sampling and final image footprint. Increase resolution or representation
only when that feature needs it; a nominally large texture can still undersample
a small UV chart. Test silhouette-bearing folds/fibers as geometry when required.
Keep real relief distinct from blurred photographic shading.

For the coordinate contract, specify each feature family's carrier, transforms
and periodicity. Shared fields use registered sampling. Test normal basis under
rotated/scaled parts, projection boundaries and grazing light when those change.
For rest/object mapping, verify the frame moves with the rotating product so the
surface does not swim. Stochastic offsets/rotations must not break a coherent
motif, fold or brushing direction. Treat blur, seam coverage and repetition as
separate acceptance questions.

For translucent solids, carry geometric units into transport units. Keep true
thickness, reflection, absorption, scattering and roughness independently editable.
Use matched thickness/background or transport controls for ambiguous edges; do not
force bright/warm boundaries into base-color or gloss masks. Any shadow policy
that changes physical transport is a project-specific approximation, not a universal
glass requirement; record its effect and do not call it source evidence.

The minimal review receipt states input revisions, route (saved Blender asset or
maintained native USD), actual material bindings, representative inspected images,
separate fidelity/support/delivery findings and the next focused correction. A
packaging pass does not establish new LuaCAD, Blender or native renderer behavior.
