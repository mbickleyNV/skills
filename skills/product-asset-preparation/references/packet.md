# Frozen product packet v1

`prepare_product_asset.py --packet /absolute/packet.json --output
/absolute/project/products/<slug>/product.blend` is the host command. Existing
Blender: `/home/mbickley/blender/bin/blender`. Work requires user systemd resource
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
