"""On-demand, read-only Blender inspection. No scene writes or persistent cache."""
import fnmatch
import json
import time

VERSION = 1
CHECKS = {"identity", "geometry", "appearance", "visibility", "evaluated"}


def _vector(value):
    return [round(float(x), 6) for x in value]


def _bounds(obj):
    from mathutils import Vector
    if obj.type not in {"MESH", "CURVE", "SURFACE", "FONT", "META", "VOLUME"}:
        return None
    points = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
    return {"min": _vector([min(p[i] for p in points) for i in range(3)]),
            "max": _vector([max(p[i] for p in points) for i in range(3)])}


def _materials(obj):
    return [{"slot": i, "material": slot.material.name if slot.material else None,
             "link": slot.link} for i, slot in enumerate(obj.material_slots)]


def _value(value):
    if value is None or isinstance(value, (str, bool, int, float)):
        return value
    if hasattr(value, "name"):
        return {"name": value.name, "type": type(value).__name__}
    try:
        return list(value)
    except TypeError:
        return str(value)


def _nodes(obj):
    groups = []
    for modifier in obj.modifiers:
        group = getattr(modifier, "node_group", None)
        if modifier.type != "NODES" or not group:
            continue
        inputs = {}
        for socket in group.interface.items_tree:
            if socket.item_type == "SOCKET" and socket.in_out == "INPUT":
                if socket.identifier in modifier:
                    inputs[socket.name] = _value(modifier[socket.identifier])
        groups.append({"modifier": modifier.name, "group": group.name, "inputs": inputs})
    return groups


def inspect(names=None, patterns=None, collections=None, selected=False,
            checks=None, limit=20, offset=0, id_properties=None, baseline=None):
    """Selectors are a union, intersected with active scene membership.

    No selector means current selection, never an implicit whole-scene dump.
    `evaluated` is opt-in and returns counts/face-material usage, not mesh data.
    Baseline compares the same query/page only; snapshots remain caller-owned.
    """
    import bpy
    started = time.perf_counter()
    checks = sorted(set(checks if checks is not None else
                        ["identity", "geometry", "appearance", "visibility"]))
    if set(checks) - CHECKS:
        raise ValueError("Unknown checks: " + str(set(checks) - CHECKS))
    if not isinstance(limit, int) or not 1 <= limit <= 100:
        raise ValueError("limit must be 1..100")
    if not isinstance(offset, int) or offset < 0:
        raise ValueError("offset must be nonnegative")
    for value in (names, patterns, collections, id_properties):
        if value is not None and (not isinstance(value, (list, tuple)) or
                                  not all(isinstance(x, str) for x in value)):
            raise ValueError("selectors and id_properties must be lists of strings")
    names, patterns, collections = names or [], patterns or [], collections or []
    scene = bpy.context.scene
    active = {obj.name: obj for obj in scene.objects}
    hits = {name for name in names if name in active}
    missing = {"objects": [name for name in names if name not in active], "collections": []}
    for name in collections:
        collection = bpy.data.collections.get(name)
        if collection is None:
            missing["collections"].append(name)
        else:
            hits.update(obj.name for obj in collection.all_objects if obj.name in active)
    if patterns:
        hits.update(name for name in active if any(fnmatch.fnmatchcase(name, p) for p in patterns))
    if selected or not (names or patterns or collections):
        hits.update(obj.name for obj in bpy.context.selected_objects if obj.name in active)
    query = {"names": list(names), "patterns": list(patterns), "collections": list(collections),
             "selected": selected, "checks": checks, "limit": limit, "offset": offset,
             "id_properties": list(id_properties or [])}
    ordered = sorted(hits)
    depsgraph = bpy.context.evaluated_depsgraph_get() if "evaluated" in checks else None
    objects, errors = {}, []
    for name in ordered[offset:offset + limit]:
        obj = active[name]
        record = {"type": obj.type}
        objects[name] = record
        try:
            if "identity" in checks:
                record["identity"] = {"data": obj.data.name if obj.data else None,
                    "parent": obj.parent.name if obj.parent else None,
                    "collections": sorted(c.name for c in obj.users_collection),
                    "library": obj.library.filepath if obj.library else None,
                    "source": {key: _value(obj.get(key)) for key in id_properties or []}}
            if "geometry" in checks:
                record["geometry"] = {"bounds_world": _bounds(obj),
                    "matrix_world": [_vector(row) for row in obj.matrix_world],
                    "modifiers": [{"name": m.name, "type": m.type,
                        "viewport": m.show_viewport, "render": m.show_render} for m in obj.modifiers]}
            if "appearance" in checks:
                record["appearance"] = {"materials": _materials(obj), "nodes": _nodes(obj)}
            if "visibility" in checks:
                record["visibility"] = {"hide_render": obj.hide_render,
                    "hide_viewport": obj.hide_viewport, "hide_layer": obj.hide_get(),
                    "visible_view_layer": obj.visible_get(), "instance_type": obj.instance_type,
                    "instance_collection": obj.instance_collection.name if obj.instance_collection else None}
            if depsgraph is not None and obj.type == "MESH":
                evaluated = obj.evaluated_get(depsgraph)
                mesh = evaluated.to_mesh()
                try:
                    usage = {}
                    for polygon in mesh.polygons:
                        slot = str(polygon.material_index)
                        usage[slot] = usage.get(slot, 0) + 1
                    record["evaluated"] = {"bounds_world": _bounds(evaluated),
                        "vertices": len(mesh.vertices), "faces": len(mesh.polygons),
                        "materials": _materials(evaluated), "faces_by_slot": usage}
                finally:
                    evaluated.to_mesh_clear()
        except Exception as exc:
            errors.append({"object": name, "error": str(exc)})
    camera = scene.camera
    scene_info = {"file": bpy.data.filepath, "dirty": bpy.data.is_dirty,
        "scene": scene.name, "view_layer": bpy.context.view_layer.name,
        "frame": scene.frame_current, "engine": scene.render.engine,
        "units": {"system": scene.unit_settings.system, "scale_length": scene.unit_settings.scale_length},
        "camera": None if camera is None else {"name": camera.name, "lens": camera.data.lens,
            "clip": [camera.data.clip_start, camera.data.clip_end]}}
    report = {"version": VERSION, "query": query, "scene": scene_info,
              "matched": len(ordered), "returned": len(objects),
              "next_offset": offset + limit if offset + limit < len(ordered) else None,
              "missing": missing, "objects": objects, "errors": errors}
    if baseline is not None:
        if baseline.get("version") != VERSION or baseline.get("query") != query:
            raise ValueError("Baseline must use the same version, query and page")
        if any(baseline["scene"][k] != scene_info[k] for k in ("file", "scene", "view_layer")):
            raise ValueError("Baseline belongs to another scene or view layer")
        previous = baseline.get("objects", {})
        report["objects"] = {name: value for name, value in objects.items() if previous.get(name) != value}
        report["delta"] = {"added": sorted(set(objects) - set(previous)),
            "removed_from_page": sorted(set(previous) - set(objects)),
            "changed": sorted(name for name in objects.keys() & previous.keys() if objects[name] != previous[name]),
            "scene_changed": baseline["scene"] != scene_info,
            "note": "Page differences are not proof of object deletion."}
    report["elapsed_ms"] = round((time.perf_counter() - started) * 1000, 3)
    return report


def emit(**query):
    """Print exactly one JSON report; no scene mutation or filesystem output."""
    report = inspect(**query)
    print(json.dumps(report, separators=(",", ":"), default=str))
    return report
