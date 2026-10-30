# Texture refinements that survive OVRTX

Project adapter note: paths and commands outside this skill directory describe
optional integration examples. They are not bundled dependencies. Locate a
maintained equivalent and verify its interface before execution; no historical
helper, local service or schema is assumed to be installed.

- Inspect the original image, graded file, live socket links and color spaces before
  compensating with exposure or stronger tint. A float-image save round-trip in this
  project brightened oak and halved contrast. Compare basic pixel statistics when
  diagnosing that symptom; do not assume every float-image save is faulty.
- Grade from the untouched source with an explicit color-space path. Color maps use
  sRGB; roughness/normal maps use Non-Color. Keep the grade absolute and reproducible,
  and prevent old appearance helpers from reapplying it. Existing implementation:
  blender/materials/prepare_natural_oak.py and natural_oak.py.
- Prefer the matching scanned roughness to unrelated noise: grain, pore relief and
  sheen should align. Remap to the intended finish range rather than blindly using
  raw wood roughness for clear-coated joinery. Preserve direct image inputs where
  the installed bridge supports them; shader-node availability in Blender alone
  does not establish export support.
- For variation without new images, change existing UV coordinates using stable
  independent hashes of part IDs, independent U/V offsets and restrained scale
  variation. Preserve intended grain direction and use the same UVs for color,
  roughness and normals. Avoid additive character-sum seeds: similarly named parts
  get correlated offsets. Compute absolute UVs so reruns do not accumulate drift.
- Reuse library.py::apply_metric_uv, explicitly set the active render UV layer, and
  isolate mesh data only where shared consumers need different mapping. No new
  image maps or material copies are necessary for UV-only variation.
- Live material/UV edits can remain stale in OVRTX despite successful captures.
  Compare visible grain placement against actual stored links/UVs before concluding
  a look adjustment failed. On confirmed mismatch, follow the existing bounded
  save/reopen recovery; do not routinely restart or stack appearance corrections.
- Review one close-up, freeze appearance, then capture the requested scope. For a
  small follow-up, representative room views can suffice; clearly record which
  full sheets remain from the earlier revision. Do not rebuild CAD for UV changes.

## Wood edges and bevels

Treat broad veneer faces, longitudinal edge banding/lipping and genuine solid-stock
crosscuts as separate surface regions. Real cabinet edging often uses matched
long-grain veneer tape or solid edging; a thin panel cap is not automatically end
grain. Preserve accepted broad-face charts and finish color when repairing edges.
Give narrow edges and generated bevel bands nonzero UV area, consistent physical
texel density and grain along their actual stock direction. A front-only planar
projection collapses perpendicular edge charts; do not stretch it around a corner.
Use cylindrical/path-aware charts for round or bent stock, with intentional seams.

Inspect evaluated output after Bevel/Solidify/Geometry Nodes, not just base Mesh UVs.
Check the active render UV exported as st as well as shader-named UVs; an existing
named reader does not establish native sampling. Keep color/roughness/normal phase
aligned. Use source surface/grain IDs when available. Scope collapsed-chart and
severe-anisotropy measurements to relevant visible joinery; floor undersides and
hidden drawer interiors are not a measured visible defect count.

For this remodel, `blender/tools/audit_oak_edges.py::audit(names)` diagnoses affected
oak consumers; `blender/materials/oak_edge_projection.py::apply(names)` adds the
reviewed UV-only edge overlay while retaining original Mesh/material/normal/face
UV data. Run explicitly under idle exclusive ownership, then `assert_current`.
Reapply after source/UV/material/placement changes; revision tags alone are not
cache identity. Do not blindly apply the planar repair to manufactured curved
hardware or linked product masters. Inspect one actual native edge close-up before
repeating the repair; save with the guarded Default helper after acceptance.

Evidence: real cabinet construction [edge treatments](https://www.woodmagazine.com/wood-supplies/lumber/hide-sheet-good-edges-like-a-pro),
Blender [UV methods](https://docs.blender.org/manual/en/5.0/modeling/meshes/editing/uv.html),
and `blender/docs/engineering-changes/prado-spill-artifact-and-oak-edges.md`.
