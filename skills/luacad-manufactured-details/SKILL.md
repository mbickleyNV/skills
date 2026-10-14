---
name: luacad-manufactured-details
description: Build and refine pulls, handles, cranks, frames, moulding, cabinet fronts, and other manufactured architectural details in LuaCAD. Use when replacing box-built hardware, adding physically plausible small edge radii, consolidating tangent trim or frames, or auditing a room for detail geometry quality without changing architectural datums.
---

# LuaCAD Manufactured Details

Use this skill after architectural dimensions and openings are established. Pair it with `luacad-continuous-geometry` for topology decisions and `luacad-2d-to-3d-complexity` for profile and sweep syntax.

Honor the assigned stage and live owner. A CAD-only worker uses native LuaCAD
previews and returns source/export plus normal/UV intent. Blender import,
room-context captures and canonical scene changes are coordinator-owned and
deferred until authorized and the live owner is available.

Use product drawings and visible edge profiles before generic detail defaults.
The radii below are inferred visual starting points when evidence is absent,
not manufacturer specifications. Respect stock thickness and the finished envelope.
Choose genuine in-stock overlap for the actual junction; the example 0.5 mm is
not a universal tolerance.

## Working model

Classify the part before modeling it:

1. **Panel or front**: keep one solid and add a 0.75-1.25 mm physical radius. Preserve exact installed bounds, reveals, thickness, and stable ID.
2. **Hand hardware**: use a 2-3 mm edge radius for rectangular pulls. Use `bosl.path_sweep` for round or curved handles. Join rail and feet only when the manufactured item is one rigid casting or extrusion; overlap members by about 0.5 mm so the union is topologically connected.
3. **Frame or casing**: make a closed 2D ring or U profile and extrude it. Use subtraction or a profile with an opening. Do not assemble a continuous frame from tangent boxes.
4. **Moulding or baseboard**: draw the complete section once and `linear_extrude` it along the run. Keep intentional room corners and installation joints separate.
5. **Crank, stay, or hinge**: preserve articulation. Sweep each bent link as one member, but keep pins, plates, gaskets, and independently moving links as separate named parts.
6. **Shell or finish**: do not use this skill to fuse distinct materials, construction layers, service gaps, moving parts, or cross-room ownership boundaries.

## Radius policy

- 0.75-1.25 mm: cabinet doors, drawer faces, appliance panels, and painted millwork.
- 2-3 mm: pulls, lever members, knobs with rectangular sections, small metal plates.
- Larger radii: only when supported by a product reference or a recorded design decision.

The radius is real geometry. Do not fake missing edge treatment with smooth shading or bevel modifiers in Blender.

## Preferred LuaCAD patterns

For a soft rectangular solid:

```lua
local function softbox(x,y,z,w,d,h,r)
 return bosl.cuboid{{w,d,h},rounding=math.min(r,w/2,d/2,h/2)}
   :translate(x+w/2,y+d/2,z+h/2)
end
```

For a continuous frame, create the outer 2D profile minus its opening, then extrude. For a three-sided door frame, use one U-shaped polygon. For profiled trim, make one closed section and extrude the full run. For curved round stock, sweep a circular profile along a continuous path.

## Audit workflow

1. Read the room XML and identify immutable datums, stable IDs, materials, movement, and ownership.
2. Search source for repeated `box` or `cube` unions used to imitate one manufactured item.
3. Inspect panels and fronts for perfectly sharp render-facing edges.
4. Rank candidates: visible close-up hardware and fronts first; hidden carcass construction last.
5. Prototype one representative instance and render it before propagating the helper.
6. Apply the helper by semantic class, not by a global blanket replacement.
7. Rebuild only affected rooms and use narrow part filters for Blender synchronization.

## Validation contract

For every changed part:

- preserve the documented envelope unless the design explicitly changes;
- require a closed mesh, zero nonmanifold edges, positive volume, and the intended component count;
- check a welded topology report separately from render normals;
- verify reveals and moving clearances after rounding;
- compare object count before and after when consolidation is a goal;
- inspect one affected room-context proof; add a close-up only when the detail cannot be judged there.

A higher triangle count is acceptable when it creates a real small radius or sweep. Never spend triangles on hidden edges that cannot affect silhouette, highlight, or contact shadow.

## Project handoff

Keep durable geometry in XML/LuaCAD and stable objects in `blender/house.blend`. Replace Mesh data on existing Blender objects, retain materials and transforms, and save only current named room renders. Record exceptions when a construction joint or moving interface must remain separate.
