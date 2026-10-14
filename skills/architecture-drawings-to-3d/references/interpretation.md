# Wall, opening and joinery interpretation

## Trace the section profile

Read the sheet legend and the drawing's local conventions. When the supplied
convention identifies heavy black poche as cut interior construction, trace its
connected outline: wall face, floor, ceiling, jamb, lintel/header, return and any
low enclosure. Do not turn every dark mark into a wall: appliance fills, material
patterns and projection conventions still need context.

A short drop from the top boundary beside a doorway can be the entry wall/header
seen in section. Correlate it with the perpendicular wall and opening in plan.
Record which wall terminates at which junction; a full-width backing rectangle
cannot express this relationship. Do not hide the whole entry wall in a cutaway
and then use that view to claim the opening was reconstructed.

Distinguish the fixture dimension chain from the overall room dimension. The start
of a vanity width is not necessarily the left room boundary; an adjacent doorway,
return or wall thickness can fall outside the chain. Do not enlarge or shorten a
room solely to make an elevation crop fit. A cut edge can project in front of a
wall seen beyond; their coincident image location is not a shared depth plane.

If the user corrects a wall extent and the intended plane remains ambiguous,
identify the plane and junction in a small annotated crop or ask a focused question.
Continue independent corrections, preserving the unresolved item explicitly.

## Nested outlines and deep framing

Inventory outer and inner loops around mirror/vanity compositions separately from
cabinet fronts. Consider a continuous millwork surround, side/end panels, top and
bottom rails, recessed mirror backing, and neighboring storage. A thin front-view
line does not establish a thin depth.

When the user identifies wood framing and directs that it share vanity depth,
store wood as semantic intent and depth as a dependency on the vanity parameter.
Use a plain display tone for visibility if materials are deferred. Do not substitute
a metal-looking mirror trim for the architectural surround. Do not assume the mirror
pane itself occupies the full depth or move it flush without supporting evidence.

## Inset fixtures

Read a thick cut edge beside and below a bathtub as potential surrounding
construction, especially when confirmed by the user. Model the insert and enclosure
separately: side wall/apron, deck/rim, backing and actual basin cavity as supported.
A freestanding hollow tub can have the correct width and still be topologically wrong.

Decide whether a printed span measures the fixture or its whole bay. If it measures
the bay, fit insert plus surrounding construction within that span rather than adding
walls outside it. Unspecified enclosure thickness and fixture product remain estimates.
Do not make a full-height shower wall from a low black cut that ends at tub-rim height.

## Corrections as regression checks

When a chase or false wall moves the finished face, move its attached toilet,
flush plate and other fixtures from that face; stop the chase at the evidenced
shelf or cabinet datum. Equal depth is a parameter dependency, not a second
copied number. Check fixtures against the exported support face and top limit.

For shower returns, trace each plan endpoint and identify which side is wet.
Grow solid wall thickness toward the intended side of the glazing boundary,
preserving the printed adjacent fixture bay. Wall thickness must not inherit
glass thickness. Distinguish the full-height door from glass above solid returns,
and bind common glass/joinery top lines to one datum when elevations show them.
Controls and heads need a support wall and an inward-facing direction, not merely
a plausible position within the room.

For a mirror-and-light composition, compare the outer outline with the mirror
pane separately. Confirm whether side panels contain the lights and whether a
ledge spans the whole composition. Move lights onto their panel faces. Do not
reduce the whole surround to thin mirror trim or generalize wood to every outline.

Use semantic checks rather than only a mesh-part count:
- Is the intended doorway actually open, with its header/return represented?
- Does the surround have the directed depth, and is its pane still separate?
- Is the fixture inset within construction while the printed bay stays unchanged?

These are drawing-specific relationships. They are not universal bathroom defaults.

## Door completeness and finish regions

A wall/header silhouette alone does not establish a doorway. Correlate the opening
ends, hinge corner and swing side to the plan arc; model the aperture, jambs/header
and leaf as distinct features. If the user is reviewing the doorway, keep enough
wall and an appropriate leaf pose visible to recognize it. Do not replace it with
a dangling preview header. Arc graphics remain annotations, not geometry.

A visible tile grid identifies a finish coverage region even when individual tile
geometry and materials are deferred. Preserve a named face or thin placement volume
with evidence-linked boundaries, support wall, openings and an explicit thickness
estimate. Do not discard the region merely because textures are out of scope.
A display tint can identify the region without implying a final tile material.

When a user changes an assembly depth, propagate it to surrounds, fronts and fitted
insert geometry. Check overall depth, not only carcass depth. If a fixture must
become a shallow placeholder to fit, state that approximation and avoid leaving
the original basin protruding beyond its resized support.

## Anchors, scope and precedence

Do not automatically center a sink/mirror over the full vanity. Drawer and door
subdivisions can establish an offset sink centerline; sconces follow the mirror
composition. Check each fixture's clearance from wall returns, framing and nearby
panes after placement. A correct overall cabinet width does not catch a light
whose center sits on a boundary.

A correction to “the mirror” should not silently change the lower vanity. Store
assembly-specific parameters and the exact scope of the latest user clarification.
When a formerly shared depth becomes independent, remove or supersede the dependency
in the generator as well as XML; otherwise the next rebuild can undo the correction.

## Classify before extruding

An opening is not automatically a hinged door. Require a matching physical leaf,
hinge corner and swing arc before adding a hinged leaf; the arc itself is never
solid geometry. Long parallel lines can be glazing tracks, and thin closed
rectangles can be joinery fronts or recess outlines. Keep separate classes for
wall, hinged door, sliding/glazed opening, joinery front, recess and annotation.
Do not extrude a reference arrow, leader, dimension extension or swing triangle.

Trace walls from connected faces/poche and their junctions. Review every oblique
segment against the plan: a real angled bay is possible, but a diagonal must not
appear merely because an opening received a default rotated panel. For schematic
context, use a neutral closed pose or omit an unresolved leaf while preserving the
opening. Verify the exported pose, not just the XML label. Distinguish genuine
posed doors from walls in review views.

A built-in drawn in a recess needs three linked quantities: finished wall face,
opening width/height and backing depth. Place the cabinet front on that wall face
and extend its carcass into the recess; cut the adjoining wall opening and retain
back/side construction. Match plan placement to elevation dimensions. Check the
exported front plane, retained printed width, depth direction and clear aperture;
simply moving a cabinet into an uncut wall is not an inset reconstruction.

## Cabinet support types and overlapping glazing

When cabinet outlines are confirmed as wood construction, model the outer box,
finished end panels and the independent door/drawer leaves. A printed end-strip
width belongs to solid material, not an empty margin around an undersized generic
carcass. Fit fronts within the confirmed surround or documented overlay, leaving
only explicitly estimated working reveals. Check the visible front plane as well
as overall width and depth; a recessed thin side can leave a dark void even when
the cabinet's bounding box and dimension chain are correct.

Dark rendered borders need diagnosis before interpretation. Distinguish a real
opening, expected small shadow reveal, missing finished panel, wrong material and
coincident surfaces. A cap/deck/countertop should own its exposed top while the
supporting wall or wood side terminates at its underside. Do not leave both parts
owning the same exposed face, or hide that construction error with a material
change or arbitrary render-only offset. Confirm one representative joint in the
source mesh and then propagate the construction rule to affected modules.

Give cabinet helpers an explicit support type or bottom offset. A base toe-space
must not propagate into a wall-mounted cabinet: check that its bottom panel closes
at the side-panel datum and its doors reach that datum within the intended reveal.
Check the assembled silhouette, not just each panel's closed mesh. Where a continuous
toe kick is confirmed, model one named run beneath the specified bays; do not infer
separate kicks from drawer/carcass boundaries or extend it into unrelated appliances.

Do not give every upper cabinet the same depth by default. An appliance-top cabinet
may align with the appliance front; when confirmed, encode that dependency using
body plus front thickness, and distinguish handle projection from cabinet depth.
Repeated fronts may be separate boxes: preserve each cabinet as a child assembly
with its own carcass and doors instead of one multi-door object.

Trace the complete window perimeter across overlapping joinery before classifying
rectangles as cabinets. A sash-operation symbol can apply only to the lower part
of a continuous window, with fixed glazing above. A shelf crossing the elevation
may sit in front of glass: preserve both depth layers and keep its opaque backing
out of the glazed opening. Store fixed/operable sections and shelf coverage as
separate named features; never extrude the sash-operation graphic.
