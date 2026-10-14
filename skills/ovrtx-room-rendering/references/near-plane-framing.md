# Head-on room elevations through an intervening wall

Use a camera near plane to omit foreground obstructions from the camera view
without deleting walls or changing their contribution to the scene lighting.
This is a view cutaway, not a geometry edit. Check the actual renderer: viewport
clipping alone is not evidence that a rendered image respects the near plane.

## Fit first, clip second

1. Measure the target assembly using evaluated world-space bounding-box corners
   (`object.matrix_world @ Vector(corner)`). Mesh origins may all be zero.
2. Aim square to the cabinet faces. Center the camera on the cabinet run's
   horizontal midpoint and its full vertical extent, including the toe/platform.
3. Back the camera away along that normal until the whole target fits with a
   small margin in the intended aspect ratio. The camera may enter another room.
   Use all projected corners for the fit; include cabinet depth and lens shift.
4. A normal near plane can now show the intervening room/wall. INCREASE
   `camera.data.clip_start` until the plane lies beyond those obstructions.
   Decreasing it to millimetres exposes more foreground; it does not cut a wall away.
5. Keep the plane before the nearest part of the target. In camera coordinates,
   forward depth is `-(camera.matrix_world.inverted() @ world_point).z`.
   Choose `obstruction_max_depth + clearance < clip_start < target_min_depth`.
   Near distance is along the view axis, not radial distance to a corner.
   If there is no interval, change framing; do not hide parts or crop the target.
6. Inspect a small actual render. Increase the plane in measured increments only
   if foreground remains. Confirm every cabinet edge and fixture is intact, then
   render the requested final quality once. Stop sweeping once the view is good.

For a level perspective camera with vertical field of view V and aspect A,
the fitting distance is at least max(H/(2*tan(V/2)), W/(2*A*tan(V/2))) from
the nearest target plane, with a framing margin. Blender sensor fit, shift and
non-square pixels can alter this; projected bounds are the final check.

## Reuse the saved camera

Native Camera data already owns `clip_start`, `clip_end`, `lens`, `sensor_fit`,
`shift_x` and `shift_y`; the camera Object owns the pose. These persist in the
blend file and OVRTX exports the clip range. Use these fields rather than an
extra add-on near-clip override. Give independent shots independent Camera
datablocks so changing one clip does not change another shot.

Record the matching frame/marker, aspect ratio and output path as well as pose.
Use project per-camera `review_width`, `review_height`, `review_samples` and
`review_output` metadata when available. Restore width/height when reusing a shot;
Blender render dimensions are otherwise scene-wide. Keep exposure in native
`camera.data.ovrtx_exposure`; do not use legacy manual EV metadata.
Optional intent notes/target coordinates can be custom properties, but the
native clip/lens/pose are authoritative. Save to the project's canonical blend.

Set frame, assign camera, update, render. Inspect the image; inspect evaluated
materials only if the appearance is wrong or material assignment changed. A new-camera `unsupported affected ...
session_uid` error can need the project's bounded save/reopen recovery; do not
misdiagnose it as a bad near plane. Wait for native render completion, not an
extra fixed settle sleep. Preserve light-transport depth when reducing preview
resolution/samples.

