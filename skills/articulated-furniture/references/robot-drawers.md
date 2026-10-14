# Robot manipulation and learned feedback

## Reuse current owners

Start at the checked-out pipeline's fast-path document. On the installed host it
is `/home/mbickley/product-to-3d/spikes/blender-articulation-handoff/PIPELINE-FAST-PATH.md`.
Use `isaac-kitchenette/run_target.sh` for prismatic targets and `run_door.sh` /
`door_run.py` for hinges. `robot_targets.py` derives current body-local targets
and radian hinge coordinates from the saved-Blender USD; never cache joint indices.
Use existing environments, source add-on launcher and validators. Keep Blender,
CPU USD validation and Isaac/Kit in separate processes. Serialize GPU jobs;
parallelize PDF evidence and CAD modules, not runtime qualification.

## Checks before collection

1. **Internal contacts:** per-joint collision flags do not enable adjacent
   parent/child PhysX articulation contacts. Run `contact_topology.inspect` before
   Kit (`--require_contact_siblings`) when case/moving contact is required, then
   verify actual runtime link paths so fixed-link merging cannot invalidate it.
   The implemented saved-Blender migration uses a collisionless fixed support,
   a fixed case child and moving siblings. Preserve meshes, contacts, original
   masses, handles and world joint frames/travel; compare old/new export hashes
   and content with `verify_contact_siblings.py`. Do not apply USD-only repairs.
   A global self-collision flag or robot–handle contact alone is insufficient.
2. **Robot placement:** derive reach from the complete current assembly. If a
   physical pedestal is needed, create its static collision geometry inside the
   environment's scene-setup lifecycle, after the scene exists. Check it remains
   in the loaded scene and supports the declared mount. An earlier spawn may be
   discarded by environment initialization. Keep robot fixtures out of furniture.
3. **Physical gripper range:** derive allowable finger travel from the loaded
   robot. The Panda supports zero closure; a task-imposed positive minimum can
   prevent pinching thin pulls. Preserve the same action convention/clamps in
   teacher and learner; never resize the handle to compensate.
4. **Actual grasp:** use current compiled grip contacts and geometry-derived
   tolerances. Contact force without correct location/opposing sides is not a
   grasp. A body-filtered `contact_pos_w` is an averaged centroid, so it cannot
   identify an individual mounting tab or grip contact. Align post-step contact
   points with next pre-step poses before transforming them into body/hand frames.
   Separate depth, lateral, orientation and tracking errors. A measured robot
   approach/retraction offset belongs in placement/task metadata, not the asset
   or a larger contact tolerance; validate it in a fresh run.

Reuse the proven robot-only differential IK, gravity compensation and accumulated
rate-limited targets. The tested Panda nominal TCP is hand-local [0,0,0.0984] m;
verify geometry when changing robots and do not label a task-specific grasp offset
as universal TCP calibration. Keep the furniture passive throughout operation.

## Admit a useful demonstration immediately

Capture observations before each action and retain actions, post-step measurements,
source target metadata and completed validation together. Use the same acceptance
for teacher collection and final evaluation: sufficient opening and stable mounts,
opposing contact during opening, retained final handle grasp, and signed
contact-supported travel. `door_acceptance.py` implements the current task gate
(final contact plus >=80% signed support); `door_learning.py` requires neighboring
`measurements.json` instead of trusting a `passed` stamp. These thresholds are
explicit task criteria, not universal factory physics. Do not train a run that
briefly grasps, releases and leaves the door open by impact/inertia.

A full-assembly internal-contact diagnostic can use an external probe and a
clearly marked temporary limit overlay, retaining the final asset unchanged.
Compare blockage against the actual contact geometry/clearance, not an invented
near-zero angle. Body poses plus blocked motion are contact inference; label them
separately from direct force measurements. Inspect the first camera frame before
recording. Blender previews use OVRTX; robot recordings use Isaac Sim RTX.

## Learned policy only when requested

Do not turn controller success or low cloning loss into learned-policy success.
Use fresh learner-only feedback with no teacher reference, fallback or baked
trajectory. Keep explicit timed phases accurately labeled. Fresh-process episodes
avoid ambiguous sensor caches; measured reset variation must actually differ.

Before spending more training time after failure, replay the saved checkpoint on
its recorded observations and compare action frames/clamps. Audit held states on
both sides of the goal with consistently rotated handle/hand geometry. Nearly
identical successful trajectories can omit lagged or overshot hold states; longer
fitting does not add that coverage. The demonstrated FJÄLLBO joint-lag augmentation
is opt-in and training-only: actual contact-supported open/hold source rows,
source hinge span/retraction, exact rotated geometry and goal labels, zero-lag
recovery, and normalization over the augmented domain. Do not silently generalize
that product-specific option. If lead-state coverage is needed, implement and
validate it explicitly. Synthetic training states are not physical demonstrations.

Keep training and evaluation provenance separate, including source asset hashes
and any validated topology-only migration. Reuse old observations only when a
concrete invariant report establishes compatibility; fresh evaluation must use
the final asset. Save both failed diagnostics and accepted evidence, but package
only the accepted paths as current.

For speed, batch GPU-to-host observation transfers, reuse immutable contact
geometry, and profile small CPU inference independently of simulator time. The
current loader caps tiny single-observation CPU inference at one thread; training
sets its own thread count. Do not claim this explains whole-episode runtime or
skip physics/contact checks to improve throughput.

For a new supported single-case assembly, create the collisionless support and
case/moving sibling topology during initial Blender authoring, before its first
save/export. Reuse the saved-authoring migration helper and invariant audit;
reserve a separate migration/re-export for existing saved assets. Source-only
re-export must preserve intentional saved Blender edits.
