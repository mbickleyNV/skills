# Room modules and selective house assembly

Read this for multi-room reconstruction or changes that must propagate beyond a
single room. Delegate only when the user authorizes agents (or another applicable
instruction does). Partition at evidence/room boundaries and give each worker one
writer-owned directory, its room packet, a shared units/frame contract and required
build outputs. Do not fork the full house history into every worker.

## Separate authorities

Use a small house XML to reference room-model XML files and their build inputs,
meshes, transforms, aliases and interface ownership. A room owns its detailed
geometry; the house owns placement and shared-boundary decisions. Floors provide
vertical datums. Record uncertain registration separately from printed dimensions.
A useful hierarchy is house → floor → room → named element / finish region.

Declare units, local axes, origin and primary elevation before parallel modeling.
A left-to-right elevation axis is not always plan-right. Use rigid transforms;
never scale a dimensioned room to hide disagreement with a raster plan. A broken
composite elevation requires plan-derived relative placement, not measuring its
graphic gap. Export local meshes unchanged and prefix their IDs when assembling.

Shared walls have one physical owner. Suppress or split the duplicate neighbor
surface while retaining its semantic boundary reference. If two extents disagree,
record the residual and resolve the interface explicitly; do not blindly drop a
whole wall containing an unrelated doorway. Door openings must survive ownership
changes. Floors/slabs may need their own ownership when room patches overlap.

## Splitting a shared elevation into rooms

Room ownership follows the accepted plan boundary, not the extent of an elevation
sheet. Represent an open kitchen/dining transition or stair railing as a semantic
boundary; do not invent a wall to separate module directories. Assign circulation
and shared floors explicitly so splitting a room cannot duplicate them.

When separating an established module, preserve world geometry and stable assembly
part IDs. A retained mesh namespace can differ from the new room ID if each part
has exactly one owner. Update room queries, aliases, selected parameter dependencies,
appearance targets and review links along with build paths. Verify before/after
part IDs and transformed geometry; test disjoint ownership under the shared namespace.
Retain old files only as clearly inactive history, not competing authorities.

## Invalidation and propagation

Hash only declared room inputs: current room XML, authored source and genuine
helper dependencies, including authored preview/export wrappers. Exclude generated
parameter files, generated wrappers, logs, meshes and
previews from the input hash; otherwise builds invalidate themselves. Record the
hash only after a successful build and output validation. Missing outputs invalidate
the cache even if the source hash matches.

A local fixture parameter invalidates its room build and downstream assembly/views.
A placement-only change reuses the room mesh and recomposes the assembly. Shared
interface or floor-datum changes trigger the affected boundary/placements as well.
Do not secretly rewrite every room XML when a global setting changes. Either the
room explicitly inherits that value or it remains an independent parameter.

Use explicit expressions/links for derived parameters and let a user clarification
break the old dependency. Avoid ad hoc generator assignments that overwrite current
XML values. Mark superseded assumptions as history; queries should return current
values before history. Keep role/material intent distinct from preview tint.

## Bounded context and behavioral checks

Provide a query for room/feature aliases that returns only the room XML path, its
sources/crops, transform, relevant shared interfaces and downstream affected
artifacts. `scripts/house_context.py` supports `architecture-assembly/1` house XML.
It reports paths rather than reading every room document into model context.

Verify an unchanged build is a no-op, one room input change rebuilds only that room,
and a placement-only change rebuilds no room meshes. Test missing-output recovery
and failed-build cache behavior when writing the runner. Inspect aggregate unique
IDs, units, transforms and representative shared boundaries. An attractive assembled
view does not certify surveyed alignment, floor heights or un-elevated details.

For cross-module parameter inheritance, hash the selected upstream XML value/node,
not its entire room or house file. Declare the same link in the build and context
query. For example, a ceiling-height edit can affect stairs while a mirror-depth
edit should not. Test both the selected change and an unrelated upstream change.
A path-only dependency list is insufficient if the consumer reads a current value
but its cache never invalidates. Include authored geometry helpers in that cache.

Keep historical regression expectations separate from current-design validation:
a past user-approved numeric value must not permanently block later authorized
changes. Validate dependent dimensions against the current controlling parameter,
and preserve earlier values in the correction history.
