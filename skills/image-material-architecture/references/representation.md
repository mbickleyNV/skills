# Representation, layout and scale

## Choose by the visible consequence

| Defining consequence | Candidate representation and test |
| --- | --- |
| Silhouette, open cavity, self-occlusion, wall thickness or refractive path change | Mesh or supported true displacement; verify cross-section, orientation and oblique/backlit response |
| Resolved shallow relief without consequential parallax | Height-derived bump/normal, tested in reflection; retain depth as a hypothesis |
| Unresolved fine surface slopes | Roughness or supported multiscale normal filtering; inspect at hero distance and closeup |
| Intrinsic pigment or staining | Color components and masks; prove that color edits do not deform relief |
| Separate material/volume interface | Supported physical composition or separate surfaces; verify bindings and medium boundaries |

A shallow mark on transparent material can change light paths enough to require real relief even if its silhouette is invisible. Conversely, roughness should not erase designed indentations whose contours are resolved. Choose representation per feature band. Split displacement and residual normals to avoid applying the same height twice. Escalate to geometry when a defining failure is caused by missing depth; if unavailable, mark it as a quality limitation.

For hollow or nested objects record inner/outer surfaces, lip/base cross-sections, scale, normals, overlap, nonmanifold defects, and medium entry/exit assumptions. Multiple material assignments on one closed medium need compatible volume parameters and a verified renderer interpretation. A watertight mesh alone does not verify absorption distances or nested-medium behavior.

## Preserve design grammar

Use source anchors and patches to describe feature families, size ratios, density gradients, orientation, spacing, repeat rhythm and transitions. Distinguish smooth lands, decorated regions, rim margins and base bands. On transparent objects distinguish front-surface marks from back-wall images before counting density or inferring overlap. Treat occluded coverage as synthesized.

Require prompt/map/native comparisons of a typical feature, a distinctive exception and the population as a whole. Whole-object resemblance can conceal missing symbol families or wrong spacing. Generated candidates that replace designed motifs with uniform noise fail identity even when they look convincingly textured.

## Carry scale through the graph

Record physical patch size, UV transforms, aspect, repeat, feature dimensions and projected pixel size at the intended camera. Test both UV axes with an appropriate checker and inspect seams, caps and poles. Square texture pixels do not guarantee equal physical texel dimensions.

For height-derived normals, carry height units and surface distance per UV axis into slope conversion. A finite-difference gradient in texture coordinates must account for UV tiling and the surface metric/tangent basis; an arbitrary constant is an artistic amplitude, not calibrated depth. Recheck when repeat, geometry scale or UVs change. Remapping height through a curve changes slopes and profiles, so it invalidates prior relief checks even when feature centers stay fixed.

Allocate enough independent samples across defining features; judge actual generated resolution, mip/filter behavior, tessellation and denoising at delivery scale. Increasing file dimensions or render samples cannot recover a missing motif. Reference: [texture sampling and surface derivatives](https://www.pbr-book.org/4ed/Textures_and_Materials/Texture_Sampling_and_Antialiasing).
