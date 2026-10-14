## Assembly animation

Derive ordered groups from the assembly instructions, not object list order.
Keep factory-built subassemblies together. Move fasteners after their mating parts
arrive; animate screw translation along its insertion axis and optional rotation
about the same axis. Move brackets and washers in their final installed orientation
or show the rotation explicitly. Do not use arbitrary radial explosions for a
sequence intended to explain the assembly.
Choose which threaded member actually rotates: a square-neck carriage bolt stays
indexed while its nut turns. A construction reveal may separate factory assemblies
for clarity, but keep their welded/internal parts together and label the distinction
from literal assembly order. Test withdrawal clearance before adding vertical spread.

Keep inventory groups separate from motion ownership: a hinge's mounting plate,
door cup and articulating links cannot all move rigidly with the door. Use the CAD
ownership map and original assembled matrices. Approved exploded stills validate
layout, not the paths between them; release fasteners and withdraw interlocking
parts before spreading them. Label a construction reveal that is not literal
reverse assembly, and disclose unsolved linkage motion.

For deliberately softer motion, use explicit ease-in/ease-out with zero endpoint
velocity (and preferably acceleration, such as quintic smootherstep), stagger
subassemblies and retain readable holds. Longer duration alone does not improve
easing. Benchmark a warm render batch before selecting unique motion-frame rate;
prefer reducing duration/resolution to repeating frames when smoothness matters.
Check framing at motion extrema, including forward drawers, low feet and high
panels. An assembled hero camera may crop the middle of an explosion.

For instruction-matched stills, identify the operation's visible evidence before
choosing the camera: moving part, fastening face, clearance opening, receiving
opening, and head/washer side. A detail that hides the fastener does not explain
fastening, even if the geometry is present elsewhere in the scene. Use a short
coaxial separation only where the reference calls for it; show an installed joint
seated when the reference does. Do not preserve an old shot's clearance workaround
after updating CAD. Re-derive affected offsets from the new mating faces.

Review the completed contact sheet against the relevant PDF insets once before
delivery. First-shot approval does not validate unrelated later operations. Fix
only mismatched panels; a successful file write or complete panel count is not
evidence that the depicted assembly action matches the drawing.

An upright explanatory mockup may make connections clearer than the document's
laid-down working pose. State that simplification. Use staged holds and a final
assembled hold, gentle interpolation, and stable camera framing. Avoid having
waiting parts cross the assembled product; preview early, intermediate, hardware,
and final frames before rendering the full sequence.

Set origins/pivots from component geometry deliberately: imported vertices may
already be in assembly coordinates while every object origin remains at zero.
Use offsets from recorded final transforms and restore the exact assembled pose
at the final frame. Parent factory assemblies to appropriate pivots or animate
their members consistently. Check the final animation bounds against the CAD.
New parent transforms may not yet be evaluated when assigning a child's world
matrix. Use an explicit inverse from the known seated parent transform, or update
the dependency graph first, and compare seated world matrices with their originals.
Plausible object locations alone can hide a double-offset of assembly-coordinate CAD.

When shortening a preview, retime every action and its keyframe handles before
changing the frame range. Merely reducing `frame_end` truncates later assembly
steps. Blender 5 actions may expose curves through layers, strips, and channel
bags rather than the older flat action F-curve interface. Inspect the current
action structure and confirm that every component's final key moved. Reserve a
brief assembled hold so the viewer can understand the result.

Test changed object transforms and visibility on representative animation frames
before a long render. Runtime scene translation may differ between still and live
updates. In the observed installation, keyframed Blender transforms evaluated
correctly while OVRTX still reused the assembled scene. Inspect rendered pixels
as well as transform values; successful render calls alone do not prove animation.

## Tested OVRTX frame-render workflow

When ordinary keyframed renders reuse stale poses, preserve the authored scene
and evaluate each required frame there. Copy evaluated world matrices into
independent, unanimated objects in a fresh scene identity, sharing unchanged mesh
data. Retain the evaluated camera, world, lights and OVRTX settings. Disable
VIEW_3D drawing, render sequentially, and remove only the temporary objects/scenes
after the frame is complete. The local generation cache uses `scene.session_uid`;
a new object transform alone did not reliably refresh it.

This path completed 145 unique frames for the 18-second RÅSKOG reveal. It proves
a baked-frame workflow on this installation, not reliable direct keyframed movie
export or a requirement to duplicate meshes/restart workers. First verify visibly
different assembled, detail and exploded proofs, then a small consecutive batch.
Estimate cost from warm batch throughput and the number of unique frames, not
the cold first frame or total playback frame count. Preserve completed frames so
an interrupted batch can resume without re-rendering accepted results.
Tie resume records to the source/pose manifest and render settings, not only PNG
filenames, so changed inputs cannot silently reuse stale frames. Keep pose capture
and frame rendering independently resumable; a render retry should not rerun the
solver. A later 192-frame native-physics tail completed without render errors or
restarts using this serialized baked-frame path; direct live playback remains a
separate capability, not something that result proves.
Benchmark both dense assembled and separated phases: their render costs can
differ substantially. Give a conservative range instead of extrapolating only
the fastest pose, and agree on economical settings before the full batch.

Reuse identical static holds and exact reversed motion only when the intended
camera, geometry, lighting and simulation states also repeat. Maintain an explicit
playback-frame-to-rendered-frame map and make saved Blender playback agree with
the encoded sequence; retain the original sparse authored actions separately
when baking playback keys. Reversal is unsuitable for irreversible simulation
or time-dependent effects. Do not replace unique motion with repeated stills
merely to claim a completed animation. Encoding OVRTX PNGs does not change their
rendering engine.

Earlier attempts hit `CreateSimulation ALREADY_EXISTS` even after good isolated
proofs. Use the bounded [OVRTX batch recovery](ovrtx-batch.md) only on failure;
do not reload between healthy frames. If normal recovery fails, preserve the
editable animation and completed outputs, report the blocker, and do not retry
unchanged or substitute another renderer. Never present an old product image as
a successful render of the changed scene.

Save the animated `.blend`, rendered preview video, and final product still. Verify
renderer, frame range, resolution, frame rate, final assembled pose, and nonempty
decodable output. Restore the intended hero or final frame in the saved scene.
Use the existing media-staging workflow and verify its returned integrity receipt.
