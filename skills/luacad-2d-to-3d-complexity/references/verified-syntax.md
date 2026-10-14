# Verified LuaCAD 1.1 BOSL syntax

These calls were linted, converted to 3MF, and rendered with the installed LuaCAD 1.1.0 native backend. Runnable coupons are under `../../coupons/`.

## Regions and offsets

```lua
local plate = bosl.rect { {44, 28}, rounding = 5 }
local ring = bosl.shell2d { thickness = -3, p = plate }
local solid = ring:linear_extrude(8) -- preserves the shell hole

local delta = plate:offset(3)          -- mitered sketch offset
local round = plate:offsetradius(3)    -- rounded sketch offset
local points = bosl.offset {
  path = {{-12,-7},{12,-7},{12,7},{-12,7}}, r = 3
}                                       -- returns a Lua point list
```

Use `delta = value, chamfer = true` with `bosl.offset` for straight-cut corners. Negative offsets can fail when narrow features fold over; treat that error as a profile problem, not a reason to disable validity checks. Sketch offsets remain sketches and support `:linear_extrude`; `bosl.offset` returns points suitable for `bosl.linear_sweep`. In the installed 1.1.0 build, passing a hole-bearing `shell2d` sketch through `bosl.linear_sweep { region=... }` retained only the outer outline and filled the hole. Use the sketch method `:linear_extrude(height)` for 2D CSG with holes, then verify the cavity in the mesh and preview.

## Path sweep

```lua
local section = {{-3,-2},{3,-2},{3,2},{-3,2}}
local path = {{0,0,0},{0,0,24},{18,0,34},{34,12,34}}
local solid = bosl.path_sweep {
  shape = section, path = path, method = "incremental"
}
```

Keep a consistent closed-section winding and remove repeated path stations. Inspect frame rotation at tight 3D bends; `incremental` is useful for ordinary open paths but is not proof against twist or self-intersection. Use `closed`, `twist`, `scale`, `normal`, or `last_normal` only when the path’s framing requires them.

## Skin / loft

```lua
local a={{-12,-8,0},{12,-8,0},{12,8,0},{-12,8,0}}
local b={{-8,-5,16},{8,-5,16},{8,5,16},{-8,5,16}}
local c={{-4,-9,34},{4,-9,34},{4,9,34},{-4,9,34}}
local solid = bosl.skin({a,b,c}, 0)
```

The positional `0` is the verified `slices` argument. Equal point counts make correspondence explicit. For unequal profiles, decide whether `refine`, `sampling`, or an explicit resample represents the design; do not accept an automatic vertex association without inspecting seam placement and signed volume.

## Rounded, chamfered, and tapered solids

```lua
local box = bosl.cuboid { {34,24,10}, rounding = 3 }
local taper = bosl.prismoid {
  size1 = {28,20}, size2 = {18,12}, h = 18, rounding = 2
}
local rounded = bosl.rounded_prism {
  bottom = {{-14,-10},{14,-10},{14,10},{-14,10}},
  height = 14, joint_top = 2, joint_bot = 2
}
local softened = bosl.offset_sweep {
  path = {{-10,-10},{10,-10},{10,10},{-10,10}},
  height = 10, r = 2
}
```

`bosl.cuboid` uses BOSL anchors and has no `center` parameter; LuaCAD rejects unknown names. Use `edges` and `except` only after testing a representative selector. Check thin walls and small apertures after any rounding/chamfer because end treatments can consume them.

## Attachments and distributors

```lua
local body = bosl.cuboid { {34,24,10}, rounding = 3 }
local boss = bosl.attach(body, bosl.cyl { d=10, h=14 }, bosl.TOP)
local assembly = body + boss

local arranged = bosl.xdistribute {
  spacing = 10, p = {assembly, taper, rounded}
}
```

`bosl.attach(parent, child, from)` returns the placed child. Add the parent explicitly. Use `overlap` when a fixed union needs genuine in-stock contact. The tested distributor produces one geometry object with three disconnected components; it is appropriate for previews or one grouped export, not stable per-part identity. `line_copies`, `grid_copies`, `rot_copies`, `arc_copies`, and `path_copies` follow the same `p = shape-or-list` value model.

## Debug and preview

```lua
render(body + bosl.show_anchors { desc=body, s=5 })
render(bosl.show_int { shapes={body, other} })
-- Region-only diagnostic:
render(bosl.debug_region { region=my_region, vertices=true, edges=true })
```

Run the cheapest useful loop:

```text
luacad lint model.lua
luacad info model.lua
luacad convert model.lua model.3mf
luacad render model.lua preview.png
```

The default converter is native Manifold; `--via-manifold` is a no-op. `--smooth` changes the preview shading, not the exported tessellation. Keep diagnostic arrows/intersections out of production 3MF.
