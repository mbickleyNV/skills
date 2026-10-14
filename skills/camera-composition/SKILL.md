---
name: camera-composition
description: Place and refine editable Blender architectural cameras using legal room footprints, world transforms, semantic shot purposes, field of view, and occlusion-aware previews. Use for room camera seeding or reframing, without changing structural geometry.
---

# Camera composition

Compose cameras from the existing architecture. Camera-only work skips CAD
rebuilds and does not authorize structural geometry, furniture, door-pose,
material, or visibility changes. Pair actual Blender operations with
`blender-mcp-workflow` and OVRTX captures with the project's
`skills/ovrtx-room-rendering/SKILL.md`.

## Establish coordinates before choosing positions

Read `HANDOFF.md`, `house/ROOM-CONTRACT.md`, `house/house.xml`, and the relevant
room XML or `house/shell/{upper,lower}-shell.xml`. Inspect existing native camera
Objects, camera data, parent transforms, constraints, animation and timeline
markers before creating or changing anything. Reuse matching shot identities;
do not overwrite unrelated accepted cameras.

Resolve the complete source-to-world transform, including units, plan origin,
axis signs, room placement, floor elevation and Blender import/parent transforms.
Room-local axes need not match house axes. Plan pixels typically increase downward
while house Y increases upward; verify the builder's conversion rather than
assuming a sign. XML millimeters are not automatically Blender world units.
If one Blender unit represents `s` meters, a physical height `h` meters is `h/s`
world units. Check import scaling as well as scene unit settings against a known
dimension and floor point; do not apply conversion or floor translation twice.
For imported geometry, use evaluated `matrix_world` and evaluated mesh vertices
(or all eight transformed bounding-box corners), never untransformed dimensions.

Record each room's finished floor world Z. Place eye height relative to that
floor, not world zero, slab bottom, or the midpoint of the room's Z bounds.
For example, a floor at 3.0 m and eye height 1.55 m gives world Z 4.55 m in a
meter-based scene. Start ordinary standing views around 1.4–1.65 m above floor;
use a different height only when the shot purpose calls for it. Room midheight
is useful for subject extent calculations, not as an automatic eye height.

## Derive a legal footprint, not a bounding-box rectangle

A space's `bbox-px` is a search envelope or label extent, not proof of occupancy.
In the upper shell, `entry` overlaps `front-bedroom`; a camera inside the entry
box can actually be in the bedroom or entry closet. Neither box-center targeting
nor shrinking the box by a fixed margin resolves this topology.

1. Trace the room's interior finished faces, returns, partitions and real door
   apertures from source topology; reconcile them with existing evaluated geometry.
   Inspect the builder before converting traces to finished-face clearances:
   confirm centerline versus face placement, wall and panel thickness, and aperture
   offset units, origin and direction along the segment. Traces may be wall
   centerlines, panels may use separate thin stock, and opening offsets may run
   from endpoint A toward B; XML alone may not specify these semantics.
   Shared boundaries may belong to a neighboring detailed room. Use the actual
   polygon, including concavities, rather than a convex hull or whole-floor slab.
2. Exclude adjacent rooms, closets/storage interiors, built-ins, wall thickness,
   posts and stair voids. Closet fronts are boundaries even when represented as
   thin panels. Source shell examples include `entry_closet_*`,
   `rear_bedroom_closet_*` and lower `bedroom_closet_*`. A floor beneath a closet
   does not make it a legal room viewpoint.
3. Where a doorway connects rooms, retain semantic room membership; do not let a
   flood fill through every aperture classify the entire floor as one room.
   Doorway views must use a real opening and its current leaf pose. A recess,
   window or closed door is not a passage for the camera.
4. Build candidate points inside the resulting footprint with clearance from
   finished surfaces and obstacles. Start with 0.25–0.40 m clearance, a composition
   heuristic rather than a building-code requirement. Measure nearest-boundary
   distance, including concave returns, not just distance to box edges. Verify
   floor support below and headroom above the eye. Never place the eye inside a
   wall, closet, furnishing, stair void or neighboring room to gain distance.

For ambiguous topology, use the clearly supported interior region and report
uncertainty. Do not invent missing architecture to make a camera fit.

## Seed distinct purposes for the requested rooms

Resolve requested room identities against current source IDs and honor the
requested shot counts and purposes. Do not substitute arbitrary `<space>` entries
to meet a count. When several views are requested without a count or purposes,
default to three distinct views: overview, reverse and feature. Adapt this set
to explicit counts or purposes rather than adding unrequested cameras. Retain
unspecified room usage labels. Seeding is camera placement; it does not imply
approved renders or permission to build out an empty shell.

| Shot | Position and aim | Required visual information |
| --- | --- | --- |
| `overview` | Near a legal entry-side or perimeter candidate, looking diagonally into the main usable volume | Room depth, two meaningful boundaries, floor context and a principal opening where feasible |
| `reverse` | In a different legal region, generally toward the opposite end, looking back | Entry/circulation and boundaries omitted by overview; not a small yaw or lens variant of overview |
| `feature` | At a legal stand-off facing an existing window bay, opening, wall or other defining feature | Feature plus enough adjoining architecture to locate it; no invented furnishing as subject |

Name cameras by room and purpose, such as `<room>-overview`, `<room>-reverse`
and `<room>-feature`, unless an established shot identity already serves the purpose. For each purpose, choose
required visible landmarks before aiming. Aim at their useful visual center,
not the room box center. The target need not be an editable Empty or new geometry.

Generate several candidates from inset corners, entry-side positions and usable
perimeter segments; reject illegal ones first. Among survivors, prefer visible
required landmarks, useful coverage and wall clearance, then distinctness from
other shots and moderate lens distortion. When candidates are similar, prefer
more clearance and a longer lens. In narrow circulation, compose along the
actual corridor or bend rather than across neighboring rooms. A set of complementary shots
may cover an irregular room collectively; no single shot must show everything.

## Fit lens and aspect together

Start landscape room views around 24–35 mm on a 36 mm horizontal sensor; feature
views often benefit from 35–50 mm. These are starting points, not fixed settings.
Choose output aspect before fitting. Move within the legal region or narrow the
subject before resorting to an extreme wide angle.

For a perspective camera with explicit horizontal sensor fit, sensor width `S`
and focal length `f` in the same units, and pixel-corrected aspect
`A = (resolution_x * pixel_aspect_x) / (resolution_y * pixel_aspect_y)`:

- `hFOV = 2 * atan(S / (2*f))`
- `vFOV = 2 * atan(tan(hFOV/2) / A)`
- At forward depth `d`, visible width is `2*d*tan(hFOV/2)` and height is
  `2*d*tan(vFOV/2)`.
- A centered, front-parallel target of width `W` and height `H` needs at least
  `max(W/(2*tan(hFOV/2)), H/(2*tan(vFOV/2)))` stand-off, plus framing margin.

Example: 36 mm sensor, 28 mm lens and 3:2 aspect give about 65.5° horizontal and
46.4° vertical FOV; at 3 m the frame spans about 3.86 × 2.57 m. This explains
why ceiling and floor coverage can fail despite adequate horizontal coverage.
Do not apply these horizontal-fit equations blindly to AUTO/vertical sensor fit,
orthographic cameras or shifted frames. Use the evaluated camera projection for
those cases and for final fitting. For oblique rooms, project required landmark
and extent points individually: depth varies, so a single width/distance estimate
is only a seed. Leave roughly 5–10% frame margin around required features.

For tall-feature shots, include the base/toe and header/top as must-have landmarks.
Project all feature bounds, especially the nearest oblique corners; reasonable
center stand-off and eye-level aim do not guarantee full-height coverage. If
cropped, choose a pullback within verified free space or native lens shift that
preserves verticals, then reproject all bounds before previewing.

Blender cameras look along local -Z with local +Y up. Keep roll zero and start
level for architectural verticals; aim at eye-height world Z for a level view.
Use modest native lens shift to include more floor or ceiling while preserving
verticals, then recheck projected coverage. Confirm that shift actually changes
the selected renderer's image; Blender projection alone does not prove renderer
support. If shift is ineffective, reset it to zero and use a verified legal
camera position, height or lens alternative, then reproject and inspect a new
preview. A lower level viewpoint can suit tall-object features: measure height
from the finished floor and keep the target at the same Z to preserve verticals.
Actual images decide acceptance; do not record shift as successful from projection
checks alone. Do not tilt toward a room midpoint
by default or rely on postprocessing to repair extreme perspective.

## Reject obstruction and clipping before preview

Test the evaluated scene at the intended frame and render visibility state.
Cast rays from the eye toward each required landmark's center and representative
edges/corners. Compare the first hit's identity and distance with the intended
surface using a scale-appropriate tolerance; a wall hit before the target is an
obstruction. A single clear center ray does not prove that a window, doorway or
whole room is visible. Do not require every room corner to be visible when the
shot purpose does not need it.

Also sample a frame grid (for example 5×5 rays, including borders) to detect
nearby walls or jambs dominating the image. Interpret hits semantically: the far
wall is expected, an immediate side-wall hit across most of the frame is not.
Include partitions, door leaves, closet fronts and furniture in these checks.
A geometric glass hit is not automatically opaque; verify actual evaluated
material assignments and inspect the preview for transmission or reflections.
Ray tests are a rejection aid, not evidence that a render looks correct.

`clip_start` must be **closer to the eye than every intended visible surface**,
with a safety margin. It must never be beyond the nearest intended surface.
Clipping uses camera-forward depth, not radial ray distance: for a visible point
`P`, compare against `dot(P-eye, forward)`. A modest physical near clip such as
0.01–0.05 m is a starting range, converted to scene units. Set `clip_end` beyond
the farthest intended visible depth with modest margin.

Never increase near clip to see through a wall, closed door, or closet front.
Never hide walls or move the eye outside the room to fake an interior view.
If obstructed, change position, aim, subject coverage or lens within the legal
footprint. An explicitly requested cutaway is a separate diagnostic task, not
an implicit exception for overview/reverse/feature seeding.

## Preview, adjust and preserve editable cameras

Set the timeline frame first, then assign the camera. Verify the evaluated active
camera because markers, constraints and animation can override the intended
transform or `scene.camera`. Use native camera Objects and editable Camera data;
avoid unintended linked lens edits across shots. Preserve useful existing room
or renderer collection membership and mapping.

Place new/unapproved shots in `REMODEL_CAMERAS/Diagnostic`; accepted primary
views belong in `REMODEL_CAMERAS/Primary`. The name `overview` alone does not
promote a newly seeded shot. Retain existing approved categories and promote
only when the corresponding view is accepted by the user.

Render a low-resolution, low-sample preview at the intended aspect and inspect
actual pixels for purpose, coverage, eye height, obstructed regions, wall/near-plane
cuts, stretched edges and verticals. If poor, identify the cause, make a focused
correction, and preview again. A correction is not verified until its new image
is inspected. After a few unsuccessful adjustments, report the concrete limit
instead of widening indefinitely or modifying architecture. Once composition is
verified, render once at requested final quality, if rendering was requested.

Distinguish exposure from composition: a well-framed room can remain nearly
black beside a bright window. Confirm the active native per-camera exposure
override and its native autoexposure target, then judge the actual preview;
enabling autoexposure alone does not guarantee a usable interior. Adjust within
native supported limits for this shot, not to a universal target. Review exposure
per shot; do not copy a room-wide target from a window-facing overview to a
reverse view without that window. Compare exposure adjustments at consistent
sample counts. Low-sample autoexposure previews can misrepresent saved-quality
brightness; if preview and final brightness differ materially, validate the
affected shot's exposure at its intended capture sample count and inspect the
result before acceptance. Brightening
the interior can sacrifice window detail; inspect that tradeoff before accepting
the image. Do not change lighting or materials solely to compensate for exposure.

Keep previews in `scratch/`. Durable current JPGs use
`renders/<room>/primary/<shot>.jpg` or `renders/<room>/diagnostic/<shot>.jpg`;
replace the corresponding current image rather than timestamping versions.
Keep shot aspect/output settings with the native camera using project conventions.
Report separately which cameras were merely seeded, geometrically checked,
previewed, visually accepted, or saved/published. Never claim evaluated geometry,
materials or image quality that you have not actually inspected.

## Physical optics and camera moves

For native OVRTX depth of field, validate the authored camera against the actual
USD stage units. USD focal length and filmback are tenths of a stage unit:
millimeters convert as `mm * 0.01 / metersPerUnit`. F-stop is dimensionless;
focus distance and clipping use stage units. Orthographic gates already expressed
in scene units need their own conversion. Matching field of view alone cannot
validate these units because equally wrong lens and filmback preserve their ratio.
See `blender/docs/engineering-changes/camera-physical-units-audit.md` for the
known installed producer defect and the bounded native comparison; do not assume
the temporary movie workaround is a deployed fix.

Choose the visible subject and focus surface together. Check the closest visible
foreground surfaces before changing f-stop to compensate for unexpected blur.
For an animation, review first/middle/last frames at the intended aspect and
quality. Check what the movement reveals, the changing foreground overlap, and
whether it adds useful visual information before committing to a long sequence.
Retiring a rejected shot removes only its camera, camera markers and unreferenced
animation/data; preserve accepted room cameras and unrelated actions.

## Ownership and save authorization

Follow the project's [AGENTS.md](../../AGENTS.md) authoring contract and
[HANDOFF.md](../../HANDOFF.md) for exclusive Blender ownership, canonical-scene
sync, and authorized save/publish with revision verification. Camera placement
does not itself authorize saving or publishing; keep native cameras editable
without saving during normal iteration. Do not initiate shutdown merely to
obtain a save exception.

If OVRTX cannot map a camera, inspect mapping or use an appropriate existing
mapped camera within scope. Save/reopen is not an automatic recovery permission:
preserve unsaved work and respect the same save/publish authorization boundary.
