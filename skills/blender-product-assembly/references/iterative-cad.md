# Iterative CAD geometry and native Blender materials

Keep dimensioned geometry, openings, cutouts and placement dependencies upstream.
Use Blender for reusable Material datablocks, texture coordinates, lighting,
cameras and render details. An ordinary room/assembly/object hierarchy plus
stable CAD IDs is usually sufficient; do not add a custom material inheritance
resolver to obtain reusable finishes. Blender parent objects do not automatically
supply materials to child objects.

For a changed CAD part, retain the Blender Object and replace its Mesh datablock.
Use native object-linked material slots when object assignments must outlive mesh
replacement. Preserve the slot count/order in the replacement and verify the
assignments afterward; different slot layouts need explicit reconciliation.
Sharing one Material datablock makes palette changes propagate to its users.
Changing only one user's finish instead requires a distinct material assignment.
Keep material names/IDs independent of display labels and preview mask colors.

Assign critical optical roles from semantic metadata or exact stable part IDs,
not broad name substrings: mirror glass is not window glass, a mirror light panel
is not a mirror pane, and a glass-door hinge is still metal. Validate a short
explicit mapping of these roles before rendering a multi-room batch.

Compare upstream part digests to update only affected geometry. Verify dependent
parts too: a sink-width change may also regenerate its countertop cutout. Retain
parent links, local transforms, modifiers, visibility and scene cameras. This is
not a guarantee for topology-dependent modifiers, face-specific assignments,
painted UVs, newly added/deleted parts or hierarchy edits: inspect the affected
feature when the change crosses one of those boundaries. Prefer reusable texture
coordinates at an explicit physical scale and grain direction over regenerated
bounding-box coordinates that stretch a wood/tile pattern when width changes.

A useful initial proof assigns materials, modifies one upstream dimension,
checks the changed and unchanged parts plus native scene state, then saves,
reopens and verifies again. Run reopen and subsequent inspection in separate MCP
calls so the application can restore its context. Once established, repeat only
the checks invalidated by the current edit; the proof is not a mandatory full
suite for each color adjustment.

Renderer-only cleanup or tiny offsets must remain identifiable downstream
adjustments with a reason, not silently revised CAD dimensions. Check whether
they remain valid after mesh replacement, especially Boolean operands and
coplanar contact surfaces. Report these separately from the material-preservation
proof; later render modifications were not necessarily covered by that test.

For native Blender reuse, collections organize objects; they are not inherited
edit layers. One authoritative file with geometry, cameras and lighting in separate
collections is often sufficient. When independent shot files justify separation,
link the source root collection from a .blend library and keep shot cameras and
lighting local. Append makes detached copies; Library Overrides permit selected
local changes while other properties follow the source. Keep topology edits in
their owning source file and avoid circular library dependencies. A linked-library
split is a separate authoring decision, not an automatic consequence of discussing
inheritance, and must respect any external-datablock loading restrictions.
