## Part and connection model

Translate assembly actions into explicit installed-state constraints: when the
user mates and tightens two parts, their designated mating boundaries should seat
together unless a spacer or designed clearance is shown. Check the actual named
pair (for example shelf rim to leg), not only its screw or intermediate clip.
Derive both mating outlines from shared geometry where possible. Preserve this
contact constraint while adding tool clearance; an internal return cutback must
not silently remove the outer rim or deck's mating boundary.
The converse matters too: restoring exterior contact must not extend an internal
return through a neighboring connector. Inspect the connector's whole exposed
face between its holes, not just the hole centers. Relieve the interfering return
while preserving the separate exterior mating wall and deck outline.

Before refining mesh resolution, resolve the construction. More triangles cannot
repair an incorrect part boundary, mating face, or fold. For ambiguous joints,
make a compact evidence record: visible outline, visible opening, apparent formed
feature, inferred concealed attachment, and the views that support each choice.
Do not promote a plausible interpretation into a measured factory specification.

For punched or folded hardware, inventory negative space before detailing: round
clearance punches, threaded receivers, edge-open reliefs, and elongated features
whose through-cut versus embossed construction may be uncertain. Compare opening
proportions with the drawn screw head as well as the plate outline; do not use the
same diameter for a clearance punch and its threaded receiver by default. Confirm
that each intended opening survives the final union and is not backed by an
uncut mating part. Keep ambiguous emboss/slot interpretations explicitly inferred.
Also record regions that must stay open around the joint, including the ends of
inner walls and return lips. A tiny pointed remnant can be a closed mesh and still
contradict the drawing. Name uncertain construction choices before refining them.

For formed clips, trace both the sheet cross-section (web, bend, return, bearing
surface) and its free-edge outline before building the solid. Distinguish stock
gauge from folded layers and curved edge contours; apparent thickness alone does
not establish a hem. Classify non-round punches explicitly, including square
anti-rotation openings and their matching bolt necks. Preserve reference-visible
folds when solving concealed screw clearance rather than substituting a simpler
outer shape that merely fits.

Read paired contour lines in context: they may describe sheet thickness, a bend,
a pressed bead, an elongated slot, or a leader. A stamped reinforcing rib should
have a corresponding back recess when visible or structurally relevant, not be
represented by a glued-on bar. Model its section and rounded ends; state whether
the gauge is true normal thickness or a vertical-thickness visual approximation.
Use custom profiles, tangent bend sections, and closed polyhedra when boxes and
cylinders are insufficient. Exact stamping/tooling reconstruction needs evidence
that a dimensionless assembly illustration does not provide.
For thin formed shells, nearly coincident outer, inner and rim Boolean surfaces
can create slivers. Test one continuous, closed sampled shell as an alternative;
preserve thickness and rim shape rather than hiding seams with mesh cleanup.

For a disputed repeated joint, validate one isolated prototype in exploded and
seated states before propagation. Keep factory tabs with their parent shelf;
separate only parts the instructions actually show being assembled. An approved
prototype still needs a placement audit: map its local length, width and screw
normal into the final assembly, recalculate hole locations and mating widths,
and check every mirrored copy. Do not merely paste a larger plate onto old rails.

Choose consistent axes and units once, normally millimetres in LuaCAD and metres
in Blender. Put dimensions and repeated feature parameters near the source top.
Give each meaningful component a stable name: posts, shelf assemblies, connectors,
fasteners, washers, feet, and brackets. Preserve identities across revisions.
Include every varying placement index in repeated-part names. Changing a pair
from one side to one end can otherwise produce duplicate names; check unique
identities, not only object count, before replacement import or animation grouping.

Before detailing each distinct joint type, identify both mating surfaces and their
normals in the final-product frame, then record the screw-head side, insertion
axis, shaft length, and destination. A turned flange can be perpendicular to its
parent panel: the panel normal is not automatically the fastening normal.
Check the installed state in the final diagram; the
exploded arrow alone can be ambiguous. Place the head against the accessible
inside lip when shown, and check that the shaft remains within the receiver.
Do not orient screws by a global axis merely because it is convenient. For a
diagonal tube face, derive the insertion direction from its normal.

Validate the connection chain, not only screw orientation: shelf return to
connector web, web to fastening face, fastening face to post. A correctly placed
face plate can still float beside the shelf if its folded web is missing. Model
that web from the mating boundaries. For rear tie panels, resolve both end folds
and their reach onto the shelf rails; do not size the panel only by its silhouette.
Check contact or intended clearance at every repeated joint, using section views
and geometric distances. Closed meshes alone do not prove an attached assembly.
For nested sheet folds, compare the occupied thickness intervals on the mating
normal: contact means adjacent faces, not overlapping sheet volumes. Check the
return lip as well as the fastening web. Place screw heads from the resulting
exposed face, rather than keeping an old coordinate after changing the fold.
Nor does intersection prove the right joint: verify orientation, seating depth,
exposed silhouette and fit. Do not add a protruding ledge simply to close a gap.
For shelf corner clips, establish which return nests under the deck and which
face clamps the post. Keep unverified reinforcement details conservative.

Do not cut arbitrary scallops or access holes merely to rescue an obstructed
screw path. Re-examine the rail termination, corner cutback and fold layout first.
An opening added for clearance is a new geometric assumption requiring evidence
or explicit labeling. Test screw axes through the intended receiving wall, then
separately test head seating, accessible insertion space, and tip clearance from
the opposite wall. Centerline ray tests alone do not prove full-volume clearance.
Give a hole cutter an explicit wall scope: entry wall, intended receiver, or true
through-hole. A long cylinder through hollow stock silently drills the far wall;
do not create that extra exit opening without reference evidence.

Distinguish rounded stock edges from extra flanges. Model tangent rounded profiles
and their inward offsets in CAD when the shape controls the silhouette; do not
rely on render bevels to correct a wrong section. Confirm inner and outer corner
arcs preserve wall thickness and that the connector fits the remaining flat face.

Reconcile supplied hardware counts against joints; distinguish spare parts and
wall-dependent fasteners from product parts. Include screw recesses, washers,
threaded stems, and connector apertures at a detail level appropriate for the
requested views. Describe estimated hardware as an approximation, not certified
manufacturing geometry. Simplify inaccessible thread engagement when warranted.

Keep factory-made subassemblies identifiable. Mesh decks, folded borders, and
welded ribs normally move as one shelf during an assembly animation.
