# Finish coverage topology

A visible elevation grid establishes one surface, not a complete surround. For
a user-confirmed wrap, enumerate supporting walls in plan and retain the original
region ID while adding perpendicular regions. Derive their common top/bottom and
footprint from existing parameters; record unprinted depth as an estimate rather
than promoting it to a drawing dimension.

Store coverage, inward normal, source identity, corner ownership and aperture
exclusions. Keep source reservation thickness distinct from installed finish
thickness. Check the final finish buildup at internal corners, not only touching
placeholder volumes. A preview of the outside of a U-shaped region can conceal
its cavity: inspect the wet side with both end walls in frame.

Tile in a niche means the back, both jambs, top and bottom when confirmed by the
user. Derive these planes from the clear liner interior. Keep the mouth open,
but let the surrounding finish cover a substrate flange unless exposed trim was
specified. Retain projecting sills and cut their occupied volume where needed.
Recess-return finish and tile on a window reveal are different scope decisions;
do not infer an unrequested reveal finish from the word surround.

A downstream procedural consumer must use the actual aperture-bearing marker,
not merely its bounding box. Source updates alone do not update that consumer:
explicitly sync the changed markers, refresh finish geometry and inspect a
matching interior view. Keep individual finish units downstream when authorized;
don't duplicate their geometry in both CAD and Blender.

For local iteration, provide a geometry-only room build (lint/export/current mesh
checks) separately from review-atlas generation. Run full review packaging only
when it is the deliverable; do not regenerate masks and historical proof views for
each finish adjustment. Keep current state in a compact project handoff, with
general rules here and customer dimensions, colors and render settings there.
