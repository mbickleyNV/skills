# Texture refinements that survive OVRTX

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
