# Blender-owned articulated furniture

Project adapter note: paths and commands outside this skill directory describe
optional integration examples. They are not bundled dependencies. Locate a
maintained equivalent and verify its interface before execution; no historical
helper, local service or schema is assumed to be installed.

## Ownership

Manual → named CAD geometry + Articraft recipe → Blender authoring → add-on
USD compilation → installed add-on runtime backend → OVPhysX simulation and OVRTX rendering.

Resolve the backend from the current project handoff and installed add-on.
Projects using public SDK/OVStream must keep that route; historical SIL smoke
evidence below is not a dependency, installer or recovery recipe.

Articraft bootstraps and validates the mechanism. After import, the saved
`.blend` owns geometry, body membership, joint definitions, materials, and
simulation inputs. JSON and USD exports are derived snapshots, not competing
authorities. Run subsequent Articraft checks against a snapshot of current
Blender state. Reimport must preserve local edits or explicitly replace selected
content, never silently reset the scene from the original recipe.

## Native properties plus extension metadata

Map native Blender transforms, materials, body properties, and constraints when
their semantics match. Store missing concepts in persistent add-on property
groups with ordinary panels: articulation roots, joint-local frames, specialized
drives, friction, solver options, and simulation policy as needed.

Define one owner per concept. If mass is native, custom metadata must not carry
another independently editable mass. Convert units and joint axes explicitly;
matching labels between Blender and PhysX do not prove matching semantics.
Native constraints may describe the mechanism without enabling Blender's own
solver: when OVPhysX owns simulation, do not run a competing Blender rigid-body
simulation on the same bodies.

Store stable IDs and persistent endpoint references rather than relying on
display names or runtime session IDs. Preserve these through save/reopen;
duplication needs new identities and correctly remapped references. A body root
can carry a set of detailed child meshes without merging those meshes.

## Add-on and bridge responsibilities

The add-on reads evaluated Blender geometry and authored mechanism properties,
validates them, and compiles a normalized snapshot into USD/PhysX schemas. Export
must work from a reopened `.blend` without needing the original Articraft recipe.

The bridge transports supported scene edits and simulation controls. Extend its
capabilities where the required data/control is missing; do not add a new
protocol for attributes its existing stage-update path already carries. A
successful write acknowledgment is not proof that a solver applied the change.

Classify edits simply: transform/material changes can use the existing live
update path; changes to joint topology, body membership, or unsupported live
physics properties can rebuild/reset the simulation. Not every edit must be
hot-swappable to make Blender the source of truth. Show unsupported properties
as unsupported rather than silently dropping them.

Keep authored/rest state separate from simulated state. Solver poses drive the
preview, or are explicitly baked into an animation action/cache; they must not
silently overwrite rest transforms, joint frames, or authored limits. Reset
returns to authored state. Live simulation and baked playback are distinct modes.

## Small integration proof

For new integration code, start with one drawer and one hinged door. Import their recipe, save and reopen
the `.blend`, edit a slide limit and a hinge property in Blender, then export
through the installed add-on and run OVPhysX. Verify the actual motion reflects
the edits and display it through the Blender/OVRTX path. Check reset preserves
authoring state. Then repeat with the full cabinet.

The maintained local evidence is
`/absolute/product-pipeline/spikes/blender-articulation-handoff/ENGINEERING-HANDOFF.md`.
It supersedes older standalone/core-only tests: actual gRPC live tilt/render and
native Blender Play/pause/Reset have been validated with source add-on changes.
Installed add-on deployment is a separate gate. Use OVRTX when requested; do not
substitute baked motion when the user requires a live solver.

For reuse, see the local handoff's `bridge/KITCHENETTE-VALIDATION.md`. Preserve
named detailed meshes beneath rigid-body roots. Empty roots need explicit COM
and inertia: visual meshes without colliders do not supply mass distribution.
That historical test verified every source part's body ownership and unanimated
authoring state after reopening. Native live Play/pause/Reset were subsequently
validated; reuse the current owner instead of repeating that integration spike
for every new product. For an asset-only task, test the requested target mechanism.

Inspect implementation as well as docs; some upstream skills describe obsolete
tensor-only paths. Current source has generic ovstage scalar updates, a native
client scalar helper and mixed rigid-body/articulation-link reads. Keep those
changes in the engineering handoff, not a new transport abstraction per asset.

## SimReady and robot asset delivery

Use `/absolute/product-pipeline/spikes/simready-kitchenette/README.md` and its
small scripts. The recipe-book `contact_recipe.py` implements per-panel boxes,
source-declared box through-openings, and spherical knob contacts. The importer
stores proxies/materials/grasp curves in `.blend`; `export_blend.py` subsequently
reads only saved Blender authoring, not CAD or bootstrap JSON. The add-on's role
packager consumes its existing compiler output; it is not another geometry exporter.

Propagate common failures into the generator/compiler once: explicit polygon
`subdivisionScheme=none` after tessellation, default-prim preservation through
layer composition, unit/body-frame conversion, and relative asset paths.
Float32 boundary roundoff must not leave a microscopic collider lid across a
source-declared through-opening. Test the opening geometrically, not only schemas.
Grasp-reference curves must use guide purpose and explicit stage-unit widths.
Default Blender point radii once exported as two-metre tubes that passed the
static profile but obscured Isaac rendering; product04 fixes this upstream.

Separate the product from its test fixture. Export current rest state, no tilt
stand/action, with an intentional fixed/free root policy. Do not drop joints or
run the older uni-body-only SimReady converter on articulated furniture.

Run the official pinned profile validator out of process in a compatible USD
environment; Blender's AutoChecker is a different gate. Respect the profile's
versioned executable requirements, and distinguish them from Isaac loader
requirements. Missing defaultPrim can make downstream checkers early-return and
produce misleading feature pass flags: repair root first, then rerun the full
profile. Keep unsupported/schema/runtime checks explicit, not automatically passed.

A SimReady static pass does not prove contacts or policy success. The kitchenette
historical contact smoke dropped a small sphere inside a real drawer through
SIL/OVPhysX;
it checks floor contact and anchoring, not a robot grasp. Retain separate Isaac
import, robot-handle contact and learned-policy acceptance. Record approximated
mass/friction and excluded hardware contact surfaces without claiming factory fidelity.
