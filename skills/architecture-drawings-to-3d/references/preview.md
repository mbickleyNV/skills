# Fast actual-CAD review

Check the installed CLI once. If native `luacad render INPUT.lua OUTPUT.png` is
available, use it for a simple room study. Export named 3MF for durable part identity;
ordinary OBJ export may flatten names. No studio lighting or texture setup is needed.

Use a shared model builder with preview-only visibility/orientation options. Never
bake preview rotations or removed walls into the authoritative room coordinates.
Keep any section geometry explicitly labeled preview-only and verify that its
openings correspond to the full model.

Prefer two complementary checks: an angled cutaway for depth and inset relationships,
and an orthographic view matching the source elevation for silhouette and boundaries.
Side-by-side source crops expose missing returns and surrounds more clearly than
an isolated render. Simple named callouts enable natural-language corrections.

For a request for a “normal render” after mask review, reuse the accepted geometry
with restrained neutral colors and remove mask numbers/legend overlays. Provide a
focused view of the feedback area when a whole-room view makes its details too small.
A presentation-only camera or tint change does not require a geometric house rebuild.
State when a view hides glazing or walls; do not present a diagnostic view as the
complete room. For relationship review, retain both adjoining walls and the full
joinery composition, and inspect the resulting camera view before delivery.
Keep normal previews and segmentation palettes as distinct view modes.

## Local CLI camera behavior

The inspected LuaCAD 1.1.0 native renderer uses a fixed orthographic camera with
azimuth -30 degrees and elevation 30 degrees, CAD-to-display axes Y,Z,X. For a room
whose front view looks along +Y with Z up, the preview-only composition
`shape:rotate(-30,0,0):rotate(0,0,60)` aligns that front elevation to the camera.
Verify this if the installed renderer changes. A darker neutral object tone can
avoid saturation in its default shading. Display tint does not implement glass
transparency or a physical wood material; keep material intent in metadata.

## Relevant validation

Lint the changed Lua, export and inspect named extents. Check connected components
where a part is intended to be one solid. Exact duplicate vertices can be deduplicated
for edge tests; do not move surfaces with broad merge tolerances.

A closed mesh can still be inside-out or contain an unwanted cap. For custom LuaCAD
polyhedra, apply the input-winding and native-export checks in
`luacad-product-reconstruction` before attributing a failure to the Boolean engine.
For sinks, seats and tub basins,
verify an opening geometrically (for example, a vertical ray through the center)
and visually. In one local capped-loft Boolean path, apparent cavities retained
false cap faces. Explicit outer-to-inner ring shells and annular through-frames
resolved that case. Use that fallback after checking orientation and intended face
planarity, then verify the exported opening. Treat this as a local failure mode, not a ban on
Boolean operations or a universal LuaCAD defect.

For an apparent stair/well gap, compare the preview clip and hidden-part settings
with the uncut exported geometry. A sliced floor/roof edge may be presentation-only;
a missing transition band or displaced finished face needs a source correction.
Retain adjacent walls, floors and relevant shelves in a complementary context view
so the isolated opening does not conceal the relationship under review.

Cache unchanged exports if materialization is expensive. Once relevant checks pass,
stop; do not add simulation, manufacturer fixtures or renderer work to a plain study.

## Location-based interior daylight studies

When requested, establish a geographic frame from a bearing basis or north arrow
and record its confidence. Preserve the CAD axes and transform geographic sun
directions into that frame. Resolve date, local time and daylight-saving offset;
city-level coordinates and a provisional survey are not precise site verification.
Do not disclose a drawing's exact street address to an external geocoder merely
because the user supplied a city for the lighting study.

Use one physically based sky/sun source; a sky with an emitting sun disc plus an
extra Sun light can double the direct energy. Verify the installed renderer's
sky rotation convention and altitude units rather than borrowing another engine's
conventions. Change display exposure for readability, not physical sky power, and
record any per-camera exposure differences. Use complete enclosure and distinguish
native dielectric glazing from transparent-shadow approximations. Caustic noise
or missing transport through glass can undermine an otherwise correct sun angle.

Distinguish a physically based clear-sky visualization from calibrated photometry.
Absolute illuminance claims require appropriate source calibration, glazing
transmission, surface reflectances, weather and exterior obstruction evidence.
Unknown site grade or neighbors and generic opening heights remain material limits,
not details that an attractive render resolves.

In Cycles, scene-level refractive caustics alone need not enable the dedicated
World/Light shadow-caustic path. Verify the installed version's light, caster and
receiver settings together. Preserve flat optical normals when applying the smooth
flag required by the solver; averaging normals across a glass box can turn a pane
into a lens. Record energy-altering clamps/filters and any solver limitations.
