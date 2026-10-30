---
name: image-material-spatial-design
description: Separate feature morphology, regional distribution, and property ownership when an image-derived material needs multiple scales, organized motifs, wear fields, or independently controlled surface populations. Use between material architecture and texture generation, or when correct detail appears in the wrong places.
---

# Image Material · Spatial design

Read the case's source anchors and [architecture](../image-material-architecture/SKILL.md). This branch designs fields and their relationships; [texture maps](../image-material-texture-maps/SKILL.md) owns generation, encoding and map inspection. Use this branch for meaningful spatial complexity, not for a uniform material with no evidenced variation. Planning-only requests stop at contracts.

## Separate the three jobs

For each feature family record:

- **Morphology:** contour, internal profile, edge character, aspect ratio and feature-size distribution. A rounded pit, torn flake and fuzzy yarn must not converge to the same thresholded noise.
- **Distribution:** density, clustering, orientation, hierarchy, quiet land and source regions. Define whether the field is stationary, an organized motif, or varies with product region. Correct local shapes distributed uniformly can still miss the source.
- **Property ownership:** which component's color, coverage, roughness, normal, tangent, scattering or thickness it changes, and which it leaves alone. A colored island is not automatically a bump or a separate physical coating.

Keep separate fine, intermediate and coarse families when their profiles or responses differ. Passing a microdetail pilot does not establish the presence of larger flakes, cut marks or motif boundaries in the hero view. Specify independent controls for consequential families without creating arbitrary frequency bands.

Before accepting a population, compare a few identity-bearing descriptors with
the source: connected versus isolated features, length/width and size spread,
orientation spread, occupancy/clustering and quiet space. Use actual crop evidence
or clearly labeled visual ranges; do not invent measured densities from an unknown
physical scale. Exact source placement may be unavailable while these descriptors
still discriminate faithful structure from generic noise. Send the selected
construction to the [detail pilot](../image-material-detail-pilot/SKILL.md).

## Define coordinates and composition

Choose the intrinsic coordinate field and physical scale for each family. Describe how product-specific region controls modulate it. A painted region weight, vertex attribute or procedural field may encode source-led placement; document its coordinate convention, default on other geometry, and whether it represents coverage or feature density. Scaling partial coverage weakens every feature; it does not reduce their population. If the observation is fewer features, vary placement or selection instead.

Use one accepted authority for shared boundaries. Derive consequential correlated channels from that field or inspect their registration. Preserve separately justified structures such as buried grains beneath a smoother coat. Keep base and coat normals separate where the outer interface smooths underlying structure.

Write the combination operation and its meaning. For fractional coverages of the same finish, a declared union such as `1-(1-a)*(1-b)` can prevent values exceeding one; it assumes a particular overlap model, not arbitrary physical layering. For mutually exclusive regions use a partition with a defined remainder. For vertical layers use the selected shader's supported physical composition. Scalar mixing of parameters is an approximation to mixing distinct materials; name where it loses behavior.

Do not derive relief from color brightness merely to add complexity. If only color/coverage morphology is acceptable, use it there and keep relief unresolved or independently constructed. Tangent direction and layer-normal differences need their own native tests.

## Preserve scale through revisions

An imagegen request to halve feature size is not proof that it happened. Inspect actual pixels, contour/profile and population before accepting. Changing UV scale changes both apparent size and density and can introduce repetition; record and review all three. Preserve partial interiors when removing a background pedestal, and route numerical conversions to [map contracts](../image-material-texture-maps/references/map-contracts.md).

## Hand off and test

Write `spatial_plan`: family IDs, source anchors, coordinate/scale, regional controls/defaults, property ownership, combination operations, uncertain correlations and acceptance views. Trace each to map contracts and graph controls. Inspect a source/field/native detail chain and the overall distribution on the product proxy. Use the unchanged standard benchmark for response; its atlas is not automatically a metric or continuous layout.

Route lost local shape to [texture maps](../image-material-texture-maps/SKILL.md), wrong regional placement here, missing geometry or unsupported composition to [architecture](../image-material-architecture/SKILL.md), and optical uncertainty to [calibration](../image-material-calibrate/SKILL.md). Record limitations rather than claiming a portable intrinsic material when its appearance depends on unshipped object attributes.

For organized microstructure, use [structured scattering](../image-material-architecture/references/structured-scattering.md): retain resolved yarn/flake structure between motif scale and subpixel statistics, and specify direction fields independently of anisotropy magnitude.

## Transfer to the specimen

When fields move from a patch to curved geometry, a mapping changes, or the result must turn, use [coordinate transfer](references/coordinate-transfer.md). Separate global placement from local detail, transfer normals in the correct basis, and inspect projection transitions under rotation before a full sequence. Preserve the benchmark's original mesh/UVs; additional material coordinates do not establish unchanged appearance.

For repeated structure or mapping blur, use [mapping blends](references/mapping-blends.md) to separate coordinate seams, stochastic synthesis and filtering. For folds or drape that become narrow branching ridges, use [coherent deformation](references/coherent-deformation.md) before optical tuning; keep continuous shape separate from local stochastic texture.
