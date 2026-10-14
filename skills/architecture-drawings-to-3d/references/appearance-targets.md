# Part identity through image studies and Blender

Use this when room review will lead to targeted material/image changes. A mesh
inventory is not yet a reviewed feature catalog. One architectural feature may
comprise several meshes, and one mesh may need several independently finishable
surfaces. Preserve stable IDs and authored groups; do not rely on display names,
triangle indices, preview colors or fresh visual recognition as identity.

During room review, show numbered callouts plus an isolated/highlighted selection
for each user-facing feature. Link the feature to source evidence, semantic role,
member part IDs, controlling dimensions, material/finish slots and review status.
Keep recognition, placement and finish approval separate. A generic “countertop”
can be ambiguous between a wall run, island and vanity; resolve room and feature
scope before editing. Exclude sink bowls, fixtures and backsplash unless included
in the selected feature. Preserve retired IDs with replacement links after splits.

Keep appearance variants outside geometric build inputs. Store proposed and
approved finish intent separately from preview tint and from renderer-specific
shader settings. An example finish request is not an instruction to apply it.
Link per-room appearance records from a small index; load only the chosen target.

## Assembly and child review

Author a nested feature hierarchy in the room XML, then compile the mesh lookup,
labels and selection lists from it. A vanity can contain countertop, sink, faucet
and drawers; a countertop feature may own several mesh segments. Each exported
part has one leaf owner; parent selections are unions of descendant leaves.
Keep stable IDs separate from short review numbers and palette colors. Check
coverage and duplicate ownership against the actual export before publishing masks.

Treat legacy mesh names as identifiers, not proof of function. A generic cabinet
builder may name a hinged upper front “drawer”; label its semantic role from the
source swing marks and keep the existing ID. Mark unresolved panels and placeholder
fixtures explicitly rather than silently assigning a function.

For primary-part review, isolate existing exported members by hierarchy and render
them directly. Do not reconstruct the assemblies or rerun source interpretation.
Use a small assembly legend for a room overview and expose children in focused
views or selection controls. A complete hierarchy does not make hidden surfaces
visible: retain separate assembly views for concealed or occluded components.

## View packets and image editing

Save a reproducible camera/projection, model revision/digest, image size, crop,
visibility/cutaway state and units with each base view. Generate a beauty/neutral
view and visible-surface selection mask from the same scene and camera. Use an
object-ID or material/region pass with depth/occlusion, not a bounding rectangle or
target-only silhouette through foreground objects. A finish spanning several
meshes gets the union of those visible masks. Derived masks are view-specific,
not universal persistent part identity; invalidate them when geometry, camera,
resolution, cropping or visibility changes.

Reuse one depth-tested ID pass to derive leaf masks and parent unions; do not
render every binary mask separately. Cache by mesh content, hierarchy, camera,
visibility, dimensions and renderer implementation, and regenerate missing outputs.
Any software fallback must resolve nearest surfaces, with explicit coplanar
priorities if needed; do not carry room-specific numeric IDs into a shared renderer.

Submit the base image, selected region and scoped finish request to an editor
with the control it actually supports. A highlighted reference is guidance, not
a hard editing mask. Some image tools do not expose masking controls. Do not
promise pixel-perfect preservation from prompt-only editing. Inspect changes to
layout, boundaries and unrelated objects before accepting a variant. Reflections
and shadows can legitimately change outside the direct target mask; distinguish
appearance effects from unintended geometry changes.

Save variants with target IDs, source view/mask references, prompt, requested
finish, output path and approval state. Generated images are appearance references;
keep accepted CAD dimensions and topology authoritative unless the user approves
a geometric change. A generated image is not a calibrated material/lighting model.

## Blender handoff

Import the named CAD geometry and preserve each stable part ID as metadata. Carry
feature memberships, finish slots and cameras into Blender. Refine materials,
lighting and any approved detail there using selected images as references rather
than reconstructing already-known geometry from those images. Blender's object/
material Cryptomatte passes are one option for visible-region selection masks.
Use the Blender workflow skill when implementing that scene work.

## Reference styling during design iteration

Translate the reference into finish roles on existing features: wood species/tone
and grain direction, tile color/layout/scale and grout, counter aggregate, metal
finish, glass and lighting mood. Record scale as an estimate unless supplied;
a photograph does not establish an exact tile size or product. Keep the material
palette separate from where each material is assigned so one shared material can
be reused and edited across several named parts.

A vessel basin, wall-mounted tap, enlarged mirror or expanded tile coverage may
change geometry or fixture placement. Distinguish those proposals from material
changes to the current basin, tap and authored tile region. Do not import the
reference room's layout implicitly. A hypothetical “what would you do” calls for
a scoped mapping/proposal; it is not automatically an instruction to restyle.

For dimension-sensitive reviews, style the existing Blender scene and retain the
approved camera. Compare low-cost proofs under the same lighting/exposure before
changing lighting as a separate decision. Record the geometry revision, palette
variant, camera and visibility with the saved scene. A cabinet-width correction
in an image is not complete merely because it was logged: identify whether the
CAD correction is proposed, applied, or only depicted in an appearance study.
Reconcile accepted geometric corrections upstream before treating the next render
as a dimensional review. Reuse unchanged room inputs and view packets.

For native Blender mesh replacement and material preservation, read
`blender-product-assembly/references/iterative-cad.md` through that skill's root.
