# Frozen product packet v1

Project adapter note: paths and commands outside this skill directory describe
optional integration examples. They are not bundled dependencies. Locate a
maintained equivalent and verify its interface before execution; no historical
helper, local service or schema is assumed to be installed.

`prepare_product_asset.py --packet /absolute/packet.json --output
/absolute/project/products/<slug>/product.blend` is the host command. Existing
Blender: `/absolute/installed/blender`. Work requires user systemd resource
scopes and `/usr/bin/nice`. `--plan` prints the nonexecuting launch plan;
`--replace` permits a reviewed replacement, preserving prior asset in scratch.
Default timeout is 900 seconds. Interrupted/OOM/failed validation leaves the
accepted asset intact. No live Blender lock is acquired or released.

Packet is declarative JSON, never a task Python script:

```json
{
  "schema": 1,
  "product": "product-slug",
  "collection": "ASSET | product-slug",
  "mesh": {"path": "/absolute/mesh.json", "sha256": "actual source SHA256"},
  "expected_dimensions_m": [1.8, 0.95, 0.75],
  "materials": [{
    "id": "oak",
    "base_color": [0.45, 0.3, 0.1, 1],
    "roughness": 0.39,
    "ior": 1.5,
    "shader_inputs": {"Coat Weight": 0.0},
    "maps": {"basecolor": {"path": "/absolute/color.png", "sha256": "actual image SHA256"}}
  }],
  "surfaces": {
    "top.longgrain": {"material": "oak", "uv": {
      "mode": "planar", "u_axis": "X", "v_axis": "Y",
      "extent_m": [2.4, 1.2], "offset": [0.5, 0.5]
    }}
  }
}
```

Values above illustrate the schema; they are not a verified product recipe.
Optional `mount_empties` is a list of `{id,matrix_local_m,properties}` records.
Matrices use row-major column-vector convention, metre translations, and rigid
right-handed rotation. `properties.owner` resolves to a mesh `id` or its optional
`source_part`; pose, kind and source_id are retained as custom properties. These
produce actual geometry-free Empty objects in the saved library. Empty transforms,
metadata and geometry-free identity must persist through save/reopen.

Optional `pose_collections` is a list of `{name,part_ids,empty_ids}` records. Each
defines a child collection of the packet root; all objects must be assigned to at
least one child, and unchanged objects may belong to multiple children. Link one
pose child into the house, not the parent containing simultaneous endpoints.
The worker verifies exact memberships and shared actual Material identity after
save/reopen. Static endpoint collections do not establish a valid kinematic sweep.
Without these fields the original single-collection mesh packet behavior applies.
Optional `linked_hardware` records contain `library` and `receipt` frozen
`{path,sha256}` sources, accepted `collection`, and `instances` records
`{id,mount_empty}`. Each creates a unit-scale collection instance parented at an
existing attachment Empty, with no basis offset; pose memberships inherit the
attachment's memberships. The existing manufacturer blend, Meshes, material
graphs and texture packing stay immutable and library-linked. The worker validates
the library/receipt/source hashes, actual linked collection, attachment parenting
and unit basis through save/reopen. Receipt bounds separately describe the linked
hardware; the main dimensions remain those of the source furniture meshes.
Absolute library paths intentionally survive private staging and promotion.
This is a declared external project dependency, not a self-contained copied mesh;
a later relative-path conversion must be guarded, saved/reopened and re-receipted.
Optional `mode: "linked_mesh_objects"` creates local Mesh Objects that directly
share the immutable linked manufacturer's Mesh and Material data, instead of
the default `collection_instances`. This mode currently requires exactly one
Mesh Object in the source collection. It retains the source object's rigid
unit basis and collection offset at each attachment; no Mesh copying, geometry
realization, normal repair or material replacement occurs. Staged and canonical
readback compare exact source geometry, corner normals, UVs and material binding
fingerprints and require actual shared linked Mesh identity across placements.
This permits consumer paths that do not expose nested collection instances;
native appearance still needs coordinator validation.
Optional `asset_metadata` is a JSON object of declarative product identity and
mounting information. The worker serializes it as sorted JSON in the owning
collection's `product_asset_metadata` custom property, checks exact persistence
before and after reopening, and includes it in the accepted receipt. Non-object
metadata and nonfinite JSON numbers fail. This adds no executable behavior or
automatic placement. Hardware uses `cabinet-hardware-asset/1`; see
`products/cabinet-hardware/README.md` for its mounting datum and catalogue rules.
Optional `dimension_tolerance_m` defaults .001. Every material/surface used by
source faces must resolve. Material IDs are unique. Supported maps: basecolor,
roughness, normal; image hashes mandatory, images packed. Color is sRGB, other
maps Non-Color. Extra Principled inputs are explicit `shader_inputs`, with
socket validation; unknown material fields/channels fail. Unsupported advanced
OpenPBR graphs require an explicit adapter extension, never silent simplification.
Native translator support remains a downstream review gate.

Mesh JSON is `{"parts": [...]}`. Each part has unique `id`, `vertices_mm`,
`faces` (vertex-index lists), `face_smooth` (one boolean per face) and
`face_surfaces` (one semantic ID per face). Source/world coordinates are converted
from millimeters to Blender meters without placement changes. Optional
`corner_normals` are unit vectors in face/loop order; optional `sharp_edges` are
vertex-index pairs. Optional `uv_coords` are per-loop pairs and take precedence
over recipe UVs. Without them, every semantic surface requires a recipe.
Optional `source_part` preserves the stable CAD identity when static pose Object
IDs differ; `product_source_part` stores that source identity, while
`product_endpoint_object_id` retains the unique exported Object ID.

Cylindrical UV recipe: `mode:cylindrical`, `axis:X|Y|Z`, `center_m:[x,y,z]`,
`radius_m`, `extent_m:[circumference-patch-length,axial-patch-length]`, optional
`seam_radians`/`offset`. Local polygon seam unwrapping keeps side triangles
continuous. Complex transitions, varying-radius forms or special grain paths
need explicit UVs; a cylinder recipe is not a universal wood unwrap.

Progress/logs/staged asset remain in `scratch/product-assets/<slug>/<output-key>/`.
The accepted output has a sibling `<stem>.asset-ready.json` storing stage,
collection, bounds, sources, asset digest, normal/UV validation and worker identity.
An asset/input mismatch invalidates reuse. Coordinator checkpoints reference this
receipt and product-specific uncertainties. Native captures stay separate.

Image-generated materials declare `provenance: "image-generated"` and require
`scale_receipt`: `patch_extent_m`, `confidence: "measured"|"inferred"`,
`reference_evidence`, `generated_review_evidence`, and `features` containing
`axis`, `target_size_m`, `observed_fraction`, `relative_tolerance`.
For example extent [0.3,0.3], axis 0, target .003, fraction .01, tolerance .2
represents a reviewed 3 mm feature with 20% allowed discrepancy. This is an example,
not oak evidence. Each affected surface declares `grain_direction` and its UV
extent matches the patch. Aligned maps share ProductUV. Explicit per-loop UVs with
scale receipts require a per-surface `uv_validation` object with schema
`metric-uv-triangles/1`. It compares every source polygon boundary edge and fan
area with explicit UV coordinates multiplied by the declared physical patch
extent. Optional `max_relative_edge_error` defaults .15 and cannot exceed .15;
`min_area_ratio` defaults .8 and cannot be lower; `max_area_ratio` defaults1.25
and cannot be higher. A missing adapter, collapsed chart or excessive distortion
fails. Receipts record checked face counts and observed limits per part/surface.
This establishes bounded metric density, not seamless phase continuity, exact
wood anatomy or measured photographic calibration. The accepted receipt retains
material scale evidence; legacy materials without it stay uncalibrated.
