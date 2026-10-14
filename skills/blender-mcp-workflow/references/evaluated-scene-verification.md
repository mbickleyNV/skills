# Evaluated scene verification

Use this for procedural geometry, modifier stacks, imports, material assignments,
and render discrepancies. Apply the checks that match the reported defect; a
scene-wide audit is unnecessary for a local edit.

## Establish ownership before editing

Identify the source of the visible boundary and the path that rebuilds it:
source mesh or CAD, node group, host object, modifiers, materials, and exporter.
State which source is authoritative for dimensions and which stage owns the
generated result. Put the repair in that replayable path; a live scene patch is
complete only if a fresh build would reproduce it. Keep generated coverage on
the actual source shape, including openings and nonrectangular cuts. Bounds are
enough only when the source region really is rectangular.

Trace the active node output and modifier order before changing a branch. In
particular, inspect multi-input links, duplicate streams, old backing geometry,
Boolean operands, deleted-face selectors, and geometry that remains connected
but hidden behind another surface. A graph can be connected and still emit an
unwanted second surface. Confirm that shared groups and host overrides resolve
to the intended material datablocks and current parameters.

## Check the evaluated result

Inspect one affected evaluated object at a time. Use a small set of checks tied
to the defect: world-space bounds and boundary vertices, face counts and normals
by material, material-slot validity, UVs where relevant, and first-hit rays at
the reported image location. For a recessed or layered finish, check the front
surface height and material in both the field and the gap, plus a point just
outside the intended boundary. When an image has an annotation, use its exact
region as a check target rather than inferring coverage from a broad camera.

Keep geometric correctness and appearance separate. If two surfaces should use
one material, compare their actual datablock identities before changing color;
lighting, normal direction, exposure, and transparency may explain different
pixels. Conversely, a correct material assignment does not prove the surface
is visible or that the renderer exported it as intended.

## Prove the result in the intended view

Render a low-cost frame that includes the entire reported boundary and enough
detail to see the defect. Check the actual pixels, not only a successful render
call or the mesh statistics. A close-up can prove joints or surface detail, while
a wider view proves the complete cut or room relationship; use both only when
one view cannot answer the request. Reject a proof if its camera crops or
occludes the reported area. If evaluated data and the image disagree, check
renderer translation or stale state with the project's supported recovery path
before making another geometry or material change.

After correcting a failed proof, replace or discard it. Save and verify durable
scene changes under the project's ownership rules, then report what the image
shows and any part that was established only by a mesh or ray check.
