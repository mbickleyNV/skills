---
name: luacad-2d-to-3d-complexity
description: Turn controlled 2D outlines, regions, and paths into complex native LuaCAD solids using BOSL sweeps, skins, offsets, rounded profiles, attachments, and distributors. Use when geometry should be driven by compact profiles rather than primitive piles; not for Blender shading, articulation, or evidence interpretation.
---

# LuaCAD 2D-to-3D complexity

## Project adaptation

This is a generalized workflow. Use the active project's source, scene, renderer
and save/publication rules. Names such as `HANDOFF.md`, room XML, specialist
profiles, `blender/tools/`, studio assets and pipeline contracts are integration
examples, not files supplied by this skill. Discover their maintained equivalents
before using them. Only helpers inside this skill directory are bundled. If a
required adapter or asset is absent, report that stage as unavailable and deliver
the supported work; do not invent a command, schema or successful native result.
Use specialist roles only when delegation is authorized and available; otherwise
the coordinator performs the same bounded work. Keep one live Blender owner.


Drive complexity from the smallest stable representation: a closed region for planar coverage, one profile plus a path for constant-section bends, or corresponding profiles for changing sections. Prefer native `bosl.*` geometry because LuaCAD 1.1 previews and meshes it without OpenSCAD.

## Choose the construction deliberately

| Intent | Construction | Reject when |
|---|---|---|
| Constant section along Z, optionally twisted/scaled | `bosl.linear_sweep` | the section changes independently at intermediate stations |
| Bent rod, trim, duct, cable, or lever | `bosl.path_sweep` | the path self-intersects or section correspondence must change |
| Controlled transition among several sections | `bosl.skin` | profiles lack deliberate vertex correspondence or winding |
| Planar shell, inset, border, or machining allowance | sketch `:offset`, `:offsetradius`, `bosl.shell2d`, or `bosl.offset`; use sketch `:linear_extrude` for holes | an inward offset folds over or erases narrow features |
| End-rounded/chamfered extrusion | `bosl.offset_sweep` or `bosl.rounded_prism` | rounding would cross thin walls or small apertures |
| Tapered rectangular solid | `bosl.prismoid` | a freeform loft is required |
| Edge/corner-rounded box | `bosl.cuboid` | the object is not box-like enough for edge selectors |
| Datum-based placement | `bosl.attach` / `bosl.align` | source geometry lacks meaningful attachment descriptors |
| Repeated layout with spacing derived from sizes | distributors such as `bosl.xdistribute` | each copy needs a stable exported part identity |

Read [verified LuaCAD 1.1 syntax](references/verified-syntax.md) when selecting or debugging one of these constructors.

## Preserve geometry authority

Keep dimensions, paths, profile samples, winding, station order, and mating datums explicit. Round or smooth only after the envelope, apertures, and contacts are correct. Do not fuse distinct materials, operable bodies, fasteners, glazing, or intentional construction joints merely to reduce object count.

Attachments place the child; they do not implicitly return the parent-plus-child assembly. Union the placed child with its parent only when that joint is physically continuous. Distributors are efficient layout tools but can export one named object containing several disconnected components; emit separate top-level named shapes when downstream identity matters.

## Validate at the representation boundary

For each production solid:

1. lint the Lua source and inspect `luacad info`;
2. convert to named 3MF with the native Manifold backend;
3. verify expected bounds, closed edges, one connected component when continuity is intended, positive signed volume, and no collapsed triangles after exact-coordinate deduplication;
4. sample profile/path stations for section size, tread or bend datums, openings, and mating planes;
5. render a native preview from a direction that exposes the transition or cavity.

Debug helpers such as `bosl.show_anchors`, `bosl.show_int`, and `bosl.debug_region` are visual diagnostics, not production solids. Keep them in a diagnostic render or exclude them from export; their arrows and markers are intentionally disconnected.
