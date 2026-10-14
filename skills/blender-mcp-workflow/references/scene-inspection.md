# On-demand inspection

Resolve `scripts/inspect_scene.py` relative to this skill's installed location.
Run through the existing Blender MCP; it needs Blender's `bpy` and `mathutils`.
No daemon, package install, scene save, rendering, network access or project path
is required. Each call gets fresh state and releases any temporary evaluated mesh.

```python
scope = {"__name__": "scene_inspection"}
exec(open("/absolute/installed/skill/scripts/inspect_scene.py").read(), scope)
scope["emit"](names=["CabinetDoor"], checks=["identity", "appearance", "visibility"])
```

Default checks: identity, geometry, appearance, visibility. `evaluated` explicitly
adds evaluated mesh counts, materials, world bounds and face counts per material
slot. It evaluates the current viewport dependency graph, not a renderer stage
or render-only modifier configuration. Geometry bounds use Blender's object
bounding box transformed into world space; they are not raw CAD source bounds.
Coordinates are Blender units; scene unit scale is included.

Selectors `names`, `patterns` (case-sensitive shell globs), `collections`
(recursive members), and `selected=True` form a union restricted to the active
scene. No selectors means current selection. Missing explicit names/collections
are reported. `limit` defaults to 20, maximum 100; use `offset` and `next_offset`
for pagination. Limit object scope and checks to keep responses small; a single
object with a large node interface may still produce a large record.

`id_properties=["cad_id"]` reports only requested custom properties. A project
adapter supplies its real metadata keys and object selectors; the shared helper
has no assumptions about rooms, ID prefixes, mounting or LuaCAD inventories.
Appearance includes object material slots and Geometry Nodes modifier inputs,
not a full shader graph or a flattened collection-instance mesh.

For before/after inspection, retain the complete `inspect(...)` result in the
calling client and pass it as `baseline` with the same query, page, file, scene,
and view layer. The response includes only changed/new object records plus
removed-from-page names. Paging, membership or selection changes can remove an
object from a page without deleting it. A delta is not a complete baseline for
the next comparison. No snapshots are stored inside Blender. Callers may write
reports to their project scratch area outside the inspector.

## Measure a representative task

Choose the same 5–10 objects, scene revision and checks for both approaches.
Compare an actual historical multi-call discovery sequence with one helper
invocation returning equivalent fields. Keep the scene unchanged between runs.
Record end-to-end time, MCP call count, request/response UTF-8 bytes, and actual
model token usage if available. Bytes are not tokens. Include first-use loading
and any retries; alternate approach order to reduce warm-cache bias. The helper's
`elapsed_ms` measures inspection work only, excluding MCP and model latency.
Check output equivalence before interpreting savings. Do not compare a cheap
metadata query against an evaluated-geometry query or count setup/test calls as
production measurements. Record errors and omitted fields as well as timing.
