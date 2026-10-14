# LuaCAD capability selection

Read this reference when a continuous form would otherwise require custom
polyhedron code or a long primitive/Boolean chain. Confirm the installed LuaCAD
version and API before relying on a particular BOSL function.

## Highest-value capabilities for architectural modeling

- **Path sweeps and Bézier/NURBS paths:** curved faucets, shower arms, lever handles,
  grab bars, rails, conduits, and profiled trim. Derive visual and hollow-wall
  sections from shared parameters; validate bend orientation and end ports.
- **Skin/loft and prismoids:** tapered hoods, basins, sanitaryware, transition pieces,
  sloped curbs, and irregular surrounds. Use when section change is real rather than
  approximating it with stacked cylinders or boxes.
- **Rounded/chamfered manufactured primitives:** cabinet corners, solid-surface edges,
  appliance bodies, hardware plates, and trim. Radius must come from evidence or an
  explicit design assumption.
- **Attachment anchors and tagged booleans:** place repeated hinges, pulls, fasteners,
  and subtractive cutters from named mating datums instead of repeating world-space
  arithmetic. Keep moving bodies and material changes separate.
- **2D offsets and regions:** wall finish coverage, gaskets, frame profiles, countertop
  reveals, and consistent inner/outer rings. Offset in the profile plane before
  extrusion; do not fake thickness with scaled 3D copies.
- **Distributors and path placement:** repeated slats, nozzles, shelf pins, and fasteners
  when repetition is genuine. Keep an array as one source recipe while preserving
  separate named parts if downstream interaction or materials require them.
- **Mesh/SVG import:** reuse manufacturer outlines or verified profiles as editable
  Boolean/extrusion inputs. Imports drop material and texture data, so geometry alone
  is authoritative.
- **watch, Studio, 2D preview, and debug/background modifiers:** shorten profile and
  aperture iteration before producing named 3MF exports. These are review aids, not
  final geometry or validation.

## Selection boundary

Use these capabilities to improve shape authority, editability, or robustness—not to
increase detail indiscriminately. Core boxes, cylinders, profile extrusions, and direct
CSG remain preferable for simple exact architecture. Prototype unfamiliar helpers on
one representative part and inspect the native exported mesh before propagating them.
