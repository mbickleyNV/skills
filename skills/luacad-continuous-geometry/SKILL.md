---
name: luacad-continuous-geometry
description: Audit and repair LuaCAD geometry that should read as continuous, using extrusions, sweeps, unions, and aperture-cut shells while preserving real joints, materials, and articulation. Use for room or product models with excessive tangent primitives, visible seams, disconnected exports, or inflated part counts.
---

# LuaCAD continuous geometry

Reduce false fragmentation, not semantics. One manufactured solid or uninterrupted
finish should normally export as one connected mesh. Keep material changes,
construction joints, operable bodies, removable hardware, glazing, and intentional
finish breaks separate even when they touch.

## Prevent coincident geometry at the source

Declare one owner for each rendered surface before modeling neighboring parts.
Derive adjoining solids from shared wall, slab, ceiling and roof datums rather
than repeating measured coordinates in separate modules. For a framed opening,
distinguish clear passage from the rough cut: subtract the frame envelope from
the wall while preserving the specified clear width. For layered floors and
roofs, name structural top, finish top, ceiling top and deck top explicitly;
do not infer structural elevations from a finish recess or a convenient mesh z.
Model dormer cheeks and similar closures from the mating deck surface so they
terminate at their owner rather than passing through it.

Treat part identity as part of the source assembly. A source rename or removal
must emit a retired-ID delta for Blender at build time; replacing Mesh data for
current IDs alone cannot retire older Objects. Use stable names that round-trip
through the Blender importer, including names ending in numbers with decimal
points. Keep non-rendered source members visibly distinct in the viewport so
authors do not mistake them for a second finish layer.

## Classify before rebuilding

Audit named parts by visual function and topology, then choose the smallest repair:

- Use a 2D profile extrusion for a constant-section casing, rail, panel, countertop,
  or wall outline.
- Use one outer solid minus apertures for a continuous wall or cabinet shell. Do not
  surround a door or window with tangent jamb, header, and sill boxes when the wall
  is meant to be uninterrupted.
- Use a sweep for a bent rod, lever, pull, faucet, tube, cable, or trim path. A sweep
  may vary section orientation or scale, but it should not be approximated by a chain
  of intersecting spheres or cylinders when the silhouette is continuous.
- Use a loft or controlled polyhedron when the cross-section changes materially and
  a sweep cannot describe the form faithfully.
- For stairs, stepped plinths, raked enclosures, and other exact prismatic forms,
  build one closed 2D side profile and extrude it across the constant width. This
  preserves every tread or edge datum while eliminating tangent boxes and separate
  soffits. Prefer this over a Boolean union when the input pieces meet only face to
  face; the union can remain non-manifold even when the preview looks correct.
- Use overlapping-stock unions for fixed assemblies whose seams are not real. Tangent
  contact alone does not establish one exported component.

Do not fuse merely to lower the object count. Preserve stable IDs for meaningful
parts, and record every retired primitive ID so downstream Blender objects can be
removed explicitly.

When the installed LuaCAD provides a maintained BOSL implementation, prefer its
profile/path operations over new one-off mesh generators when they express the form
directly. Useful candidates include path sweeps for plumbing and handles, rounded or
chamfered cuboids for manufactured casework, prismoids and skin/loft operations for
tapered bodies, and attachment anchors for repeated hardware. Keep a small native
export coupon until winding, bounds, section orientation, and hollow-wall thickness
pass; availability of a helper does not replace export validation. Read
[capability selection](references/capability-selection.md) when choosing beyond core
primitives and CSG.

For profile-, region-, path-, or section-driven authoring, also use
`luacad-2d-to-3d-complexity` and its verified LuaCAD 1.1 syntax. In this build,
hole-bearing `bosl.shell2d` sketches must use the sketch's `:linear_extrude()` path;
`bosl.linear_sweep` can retain only the outer loop and silently fill the cavity.
Treat attachments as transformed-child placement and distributors as layout helpers,
not proof of fused topology or stable per-copy identity.

## Treat finish junctions as datums

Continuous appearance does not require one mesh across different materials. Keep a
countertop, metal upstand, tile backsplash, and painted wall separate, then derive
their mating faces from shared parameters. Check the actual relationships: top meets
start height, front meets back plane, and lateral extents agree where the design calls
for a flush junction. Do not conceal a source gap with smooth shading, coincident
render patches, or arbitrary offsets.

For cross-room wall finishes, follow the project's finish-group ownership contract.
For procedural finishes, keep the source coverage marker aligned with the evaluated
render geometry and validate both bounds.

## Validate the exported result

For each changed part, verify:

1. expected world bounds and silhouette;
2. one connected component when the part is intended to be continuous;
3. closed edge incidence and positive signed volume;
4. no collapsed triangles or unintended coincident faces;
5. aperture dimensions and all shared-datum contacts;
6. named-part count and the explicit set of retired IDs.

Do not use a minimum total-part assertion as a regression gate: a valid consolidation
should reduce that number. Assert required stable IDs, forbidden retired IDs, and the
topology/datum invariants instead. Reconcile every parallel identity record—generated
inventory, XML part list, object hierarchy, assembly include/suppress rules, and
Blender objects—not only the emitted 3MF.

## Audit coincident surfaces across the house

For one reported overlap, inspect the owning source and affected dependencies first.
Expand to other owners when evidence identifies the same shared cause. Inspect the
entire active scene for an explicit house-wide cleanup, not every local repair.
Compare current LuaCAD inventory IDs, per-part digests and world bounds with active
Blender Objects; archive or remove obsolete rendered CAD IDs. A scoped mesh update
does not establish that other rooms are current, so run the guarded full-model
preparation/import before delivering a house-wide cleanup. Imported numeric ID
suffixes need identity-safe matching: Blender can reinterpret a source name such
as `hinge_1054.8` as a collision suffix.

Screen visible meshes for identical world-space faces with matching outward normals,
and for sizable partial coplanar intersections. Keep opposing-normal contacts,
trim backing, tile/grout undersides and intentional construction joints separate
from exposed duplicate front faces. Inspect procedural finishes as evaluated meshes;
their source markers and Boolean output can disagree. Report the scan scope and
remaining candidate classes, rather than claiming a zero-overlap guarantee from
one thresholded check. Repair an exposed overlap in its owning LuaCAD profile,
aperture, slab or roof datum, then rebuild and repeat the screen after import.

Test one representative sweep or Boolean junction before propagating a repeated
pattern. Prefer exact-coordinate deduplication over a broad merge distance, which can
erase thin stock. Keep render normals separate from welded source topology.

## Sync and review narrowly

Regenerate the LuaCAD room or product, then replace only affected Blender Mesh data
on existing named Objects. Preserve object identity, materials, cameras, and unrelated
artist work. Delete only explicitly retired IDs. A new fused mesh does not remove its
predecessors automatically.

Use a native LuaCAD render for fast silhouette and opening checks. When Blender review
is requested, make one inexpensive proof from an affected saved camera, inspect the
actual image, then update only the current approved shots. A clean render is supporting
evidence; it does not replace component, manifold, volume, and datum checks.

If deleting several Blender objects causes the live renderer to retain stale stage
bindings, save and reopen the canonical scene once, then retry one proof. When a
generated delta contains unrelated historical changes, extract or import only the
reviewed retained IDs and delete only the explicit retired set.
