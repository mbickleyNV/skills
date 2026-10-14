# Authored animation to physical release

Preserve the approved animation. Evaluate its final held pose and copy world
matrices into a separate simulation scene; remove inherited animation, parenting
and constraints that would compete with physics. The release begins from that
pose, not the original assembled matrices or a generic radial explosion. Release
with zero velocity after a stationary hold unless the user requests an impulse.

Distinguish rigid-body ownership from CAD identity. Follow the user's requested
granularity, noting when individually releasing factory-joined pieces represents
a construction reveal rather than realistic breakage. Store stable identities
through solver export and returned poses.

Estimate mass from enclosed CAD volume and an explicitly inferred material
density, not bounding-box volume for hollow parts. Check units and transform
scale once. Friction and restitution are physical-material properties, distinct
from the visual shader. Use low bounce for cabinet boards and hardware unless
evidence suggests otherwise. Record assumptions rather than implying measured
properties. Give the floor a static collision volume with its top aligned to the
visible floor; a render plane does not automatically collide.

Choose collision approximations by shape and scale. Convex hulls fill sink bowls,
rings and other cavities; disclose this and use supported compound/decomposed
colliders when those openings affect the requested result. Check initial collider
overlaps and thin-part contact/timestep settings before a full drop. A watertight
visual mesh does not prove a stable collision model. Do not invent unsupported
CCD or solver fields, or silently inflate tiny hardware to make it behave.

## Installed OV integration boundary

Inspect the installed integration before selecting SimReady or native authoring.
One inspected OVRTX Blender add-on exposes `obj.ov.physics.rigid_body` (schema
opinion and mass), `obj.ov.physics.collision` (convex hull or analytic sphere),
physics materials under `material.ov.physics`, and gravity under
`scene.ov.physics_scene`. These compile USD physics opinions; they are not proof
of successful runtime simulation. SimReady is optional only when the installed
native path can express the required properties; do not assume arbitrary SimReady
collections or custom property names translate.

Prove the requested solver with one falling body and the intended floor before
the full assembly. The inspected viewport path requires an active camera even
for a physics test. Build the complete test before activating its viewport to
avoid publishing partial scene state. Confirm actual displacement/contact and
solver evidence, not merely a playing timeline. Do not substitute Bullet or
hand-authored falling keys for requested OVPhysX results.

Keep physics stepping, pose capture and final rendering serialized. Capture
first/middle/last from the same run with simulation timestamps; preserve returned
poses for later rendering instead of restarting the solver independently per shot.
Use bounded recovery only after a diagnosed failure. If the integration cannot
advance even the coupon, preserve the prepared scene, report that no simulation
proof exists, and obtain authority before changing the add-on or service.

## Capture once, render the captured motion

If viewport playback fails but the installed add-on exposes a supported native
runtime client, a bounded capture through that client can establish real OVPhysX
motion without repairing viewport playback. This is not permission to bypass
Blender control policy or change services. Keep the exported source immutable;
record its hash, solver identity, timestep, timestamps and CAD-to-prim mapping.
Check `metersPerUnit` and `upAxis` on the actual composed USD root: stage metadata
does not inherit from sublayers. Correct Blender bounds alone do not prove the
solver sees the same units. Report a mismatch before running the full simulation.

Separate solver rate from movie rate. One successful run used ten 240 Hz steps
per 24 fps output sample; choose rates for the actual contact scale, not as fixed
defaults. Capture translation, quaternion and linear/angular velocity, with one
found, finite state per expected identity at each sample. Save frame-sized pose
records and a compact manifest rather than sending the entire run through MCP.
Replay these returned poses into render-only copies; retain the prepared physics
scene separately. Baked native results are not hand-authored substitute physics.

For an appended fall, compare sample zero with the approved animation endpoint,
including camera, lights, world and resolution. Reuse compatible intro frames;
append samples after zero so the seam does not add an unintended duplicate hold.
Keep the editable Blender timeline consistent with this playback mapping.

Do not infer solver failure solely because a board remains upright. Check its
support/contact and residual motion before diagnosing it; do not add an unrequested
impulse to force a more dramatic ending. Distinguish visually quiet large panels
from small-hardware jitter, and describe the last frame as a timed observation
unless settling has actually been established.
