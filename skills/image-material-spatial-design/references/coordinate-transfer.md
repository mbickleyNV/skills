# Transfer fields without changing their meaning

Read when moving a material from a flat/generated patch to a curved specimen, replacing a projection, rotating an object, or delivering a reusable material. Keep the established benchmark mesh and original UVs immutable; put additional coordinate attributes or diagnostic fixtures in explicitly identified overlays.

## Give each field the right frame

Separate repeatable local structure from product placement. A global pigment grade, wear boundary or density gradient needs its own coordinate/control when it must stay in place while grain scale changes. Do not bake that grade into every repeated local texture. Retain the local pigment residual and global grade as editable components where the evidence supports that separation. If decomposition is uncertain, label the approximation instead of treating the recovered components as measured.

Record for each field: coordinate frame and axes; patch dimensions in scene units; wrapping; region/height controls; expected object-motion behavior; and required attributes with defaults on a new mesh. Object-space, world-space and UV mapping have different movement semantics. Test the intended one. An existing atlas can be nondegenerate yet distort size and orientation severely.

Choose mapping from the feature's invariants, not from a preferred algorithm:

| Mapping | Useful when | Inspect before acceptance |
| --- | --- | --- |
| Existing UVs | Exact layout and supplied atlas must remain authoritative | Metric distortion, chart boundaries, mirrored basis, poles/caps |
| Planar/cylindrical or hard box projection | Surface shape supports a simple region mapping | Foreshortening and abrupt axis changes, especially on rear/cut faces |
| Blended projections | Local stochastic structure can tolerate overlap | Doubled/softened motifs, distorted contours, weight transition bands |
| Authored surface coordinates or separate assignments | Organized motifs or directional structure need continuity | Required attributes, boundary treatment, transfer to another mesh |

Blended projections are a tradeoff, not a universal seam cure. They can turn one round feature into overlapping shapes. If an organized motif cannot tolerate that, route back to representation rather than hiding the defect in roughness. Review contours, density and orientation near projection boundaries, not only the absence of a hard color seam.

Check the composed primvar, interpolation, index array and flattened element count before declaring existing UVs usable. An authored empty index array can invalidate lookup despite a populated face-varying value array. If the value count matches face vertices and the indices are erroneously empty, a task overlay may block the empty indices while preserving original values and geometry; record the repair and verify actual sampling. Hash equality alone does not prove a valid UV lookup.

## Transfer normals with their coordinate basis

A tangent normal belongs to the frame in which it was authored. Sampling its RGB through a different projection does not transfer that frame. Record axis signs, handedness and the transformation into the frame expected by the renderer. For multiple projections, reorient each normal or height gradient into a shared frame before a supported combination and normalization; do not blend unrelated tangent RGB values as colors. Check the installed normal/vector transform semantics rather than assuming a node name proves the correct operation.

For height-derived slopes, carry physical height amplitude and surface distance in both texture axes. Recheck amplitude, basis and filtering when patch scale, UV transforms, projection, object scale or height remap changes. Distinguish an explicit scalar-gradient construction from a derivative-based bump node: they can have different native support. A useful purple diagnostic preview need not be the texture actually consumed by the live graph; label preview versus live source and trace the latter.

Base and coat may share coordinate authority while using different slope response. Preserve each layer's declared conformity, smoothing and independent residual detail. Changing coordinates must not silently apply substrate relief twice or erase the outer interface's intended behavior.

## Qualify a changed normal path with simple probes

Before judging a complex normal texture through a new or modified projection,
compare a neutral tangent normal with the unperturbed shading baseline. It should
add no tilt on the tested faces, including negative-facing projection axes and
transition regions. Preserve geometry and the original shading normals; the
expected baseline is not a single world-space direction.

Then use a known asymmetric directional slope or ridge to distinguish U from V,
rotation, mirroring and sign. A flat-only test can pass while directional detail
is reversed. Use the expected transformed normal or fixed-light reflection response,
not color-texture alignment alone. Repeat only for changed coordinate/interface
paths and reuse still-valid probes.

Track image-row origin, UV lookup transformations and tangent-basis handedness
separately. One deliberate V reflection can require a basis adjustment, but it
does not justify independently flipping both the lookup and normal channel by
habit. Verify the actual combined transformation; qualify native node behavior
rather than assuming a purple map or node name establishes it.

Public example: NVIDIA's [triplanar normal-map interface](https://docs.omniverse.nvidia.com/extensions/latest/ext_material/ext_material-graph/nodes/Texturing_High_Level/triplannar_normalmap_texture.html)
exposes projection-specific handedness. This illustrates the contract to inspect,
not guaranteed availability or equivalent semantics in a MaterialX renderer.

## Make the angular transfer test early

Before a costly sequence or acceptance of a new mapping, inspect a few revealing orientations under the fixed benchmark rig: front, side, back and a cap/cut surface when present. Add views around known chart or projection transitions; a small fixed angle list can miss them. Use the final material plus a neutral-color normal diagnostic if pigment hides errors. Freeze lighting/camera/exposure while rotating only the intended specimen.

Check local feature scale/aspect, contour/rim profile, global grade placement, color/normal registration, blend-band populations and whether the pattern moves with its intended frame. Compare at delivery resolution and a matched closeup. Record the graph/maps/coordinate artifact hashes and inspected angles. A good front still does not validate a turntable.

Keep a compact `coordinate_transfer` record in the case when this branch applies: field ownership and frames, required attributes/defaults, mapping choice and tradeoffs, tested views/controls, observed failures, accepted artifact IDs and invalidated checks. A coordinate edit invalidates prior relief and finish evidence where it changes scale, basis, placement or correlations; rerun those affected checks, not every unrelated experiment.

## Qualify synthesis separately

For hex/stochastic tiling or softened/doubled projection detail, use [mapping-blend diagnostics](mapping-blends.md). Preserve continuous motifs and broad deformation in separate fields. Test actual native execution through [assembly](../../image-material-assemble/references/assembly.md#verify-translated-texture-paths) before interpreting a finite render as sampled detail.
