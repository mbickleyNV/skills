# Plan-only house context

Use this when the user wants rooms without interior elevations shelled around
existing detailed modules. Read the complete proposed floor plan: enlarged
interior sheets may crop off basements or use a drawing break through a deck.
Register repeated physical anchors between sheets; a crop edge is not a wall.

Create a separate shell module per floor and a stair/circulation module when it
has cross-floor dependencies. Store named spaces, wall endpoints, openings,
floor polygons and voids in XML before CAD. Keep source crop references per space.
Use traced plan topology for the shell and record unshown heights separately.
Preserve the user's existing/new convention; an existing-space label does not
make all proposed partitions inside that space existing.

Detailed modules retain their geometry. Assign the continuous floor to the shell
and suppress local context floor patches only in assembly. Stop adjoining shell
walls at detailed wall faces or assign an explicit shared owner. Preserve doorway
openings at those interfaces. Never fill a stairwell with a convenient floor box.
An overhead skylight outline is distinct from the stair void and the landing.

Tie stair rise to floor datums while labeling inferred tread count and landing
height. Different visible flight lengths in plans can be overhead/under-stair
projections, not conflicting stair designs. Without sections or grade evidence,
exterior stair termination and floor heights remain schematic.

Clarify whether “first flight” is ascending or descending by locating the stated
door/enclosure in the lower plan. Model an under-stair closet as an actual enclosed
cavity with doorway, side/back boundaries and continuous underside; floating tread
blocks alone do not enclose it. Keep the underside below the stepped walking
surfaces. Bind sloping pony-wall and rail heights to the flight pitch, distinguish
rail top from its bottom, and check finished flight edges against the surrounding
guard faces. Do not leave registration slivers as open holes between modules.

Review stair/well corrections in assembled context with adjacent walls, floor layers
and relevant shelves or joinery visible. Bind adjoining lower walls, slab edges and
upper guards to a shared finished-face datum where the evidence calls for continuity.
Check actual exported faces with sections or first-hit rays at representative positions
and heights, including just below and above floor transitions; matching bounding boxes
alone can hide a missing band or stepped face. Assign each transition band and exposed
surface one assembly owner, suppressing redundant local skins only in assembly.
When a wall start is described by a shelf edge, resolve the particular wall and shelf
face from the contextual view before changing their dependent interfaces.

Preview cut height and floor separation are presentation parameters. Keep full
walls in the exported model. Use a readable plan view with room labels alongside
the cutaway: a distant isometric alone hides circulation and spatial omissions.
Verify the stair aperture with a downward ray through the exported floor geometry,
and verify the stair reaches the intended upper datum. Closed parts alone cannot
establish either relationship.

## Exterior enclosure for rendering

First inspect exported wall bounds: a half-height review cut may leave full walls
in the model. Enclosure work then concerns missing ceilings, floor structure,
roof planes and boundary junctions, not automatically extending every wall.
Correlate roof plan with proposed exterior elevations; retain hips, dormers and
skylights as separate elements with inferred dimensions explicitly labeled.
Register sheets with shared anchors and scale, preserving detailed room dimensions.

Give continuous ceilings and floor structure explicit assembly ownership. Preserve
stair voids through every added floor layer. Cut both roof and ceiling for a
skylight, connect them with a shaft, and add glazing at the roof slope. A solid
roof volume or an uncut ceiling defeats interior daylight rendering.
When evidence/user direction identifies a wider open well, distinguish its ceiling
aperture from the smaller glazed roof opening. Line the well to the sloped roof
underside while retaining opaque roof around the skylight; a narrow tube matching
only the glass perimeter does not reproduce that spatial relationship.
Keep the complete exterior preview un-exploded and unclipped, separate from room
cutaways. Check stair and skylight rays, support junctions and representative room
enclosure against exported geometry. Closed component meshes alone do not prove
the assembled building has no light leaks; describe the scope of verification.

For a window audit, reconcile proposed exterior elevations with both existing and
proposed plans. Track presence separately from sill/head accuracy and actual wall
aperture clearance. A generic-height window can pass a presence check while giving
incorrect daylight penetration. If a proposed elevation retains an opening that
the proposed plan omits, record the conflict rather than silently sealing or
restoring it; basement floor changes may also invalidate its old sill datum.

Check the joints between separately authored room perimeters. A wall ending at
the near face of an adjoining partition can leave an open exterior corner across
that partition's thickness. Add a targeted regression for the repaired junction.
Dense directional ray sampling can expose gaps missed by six axis rays, but is
still sampled evidence. Classify intended open exterior doors separately from
unexplained escapes, and omit surrounding ground/neighbor meshes from this test
so they cannot conceal holes in the building enclosure.

Test modifier-evaluated geometry as well as base meshes when a rendered seam is
unexplained. Beveling two wall ends that merely touch along an edge can expose an
exterior slit. Give structural corners full-thickness contact without moving the
room's interior faces, and avoid illustrative bevels on sealed butt-joint edges.
