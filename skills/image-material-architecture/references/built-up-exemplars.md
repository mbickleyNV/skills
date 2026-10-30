# Learn built-up response from complete editable graphs

Use alongside [exemplar research](exemplar-research.md) when a generated appearance
has stronger surface construction than its reconstruction. The following are
inspection findings, not universal settings or promises of renderer equivalence.
Sources are linked; third-party materials and textures are not bundled.

[NVIDIA SimReady materials v0.2.0](https://github.com/NVIDIA-Omniverse/PhysicalAI-SimReady-Materials/releases/tag/v0.2.0)
provides category archives with USD materials inheriting a shared OpenPBR graph.
Compose the inheritance and trace the connected surface inputs. The inspected
shared graph has 36 shaders, but that count includes optional/default paths and
does not mean 36 active material layers. Tiled texture nodes use the corresponding
scalar/color value as a fallback; do not multiply the two unless the graph does.

| Example | Actual construction to inspect | Transferable lesson |
| --- | --- | --- |
| Woven_Metal_03_Steel_Glossy | Metalness 1, coat 0; independent sRGB conductor color, raw roughness and raw tangent normal textures | Reflective weave can use independent correlated fields without a coat; metadata says clearcoat but live weight is zero |
| Iron_Brushed_Very_Strong_Brushing | Metalness 1, anisotropy 0.65, coat 0; independent color/roughness/normal textures | Anisotropy establishes angular spread; resolved grooves still need a suitable normal population and sampling |
| Iron_Scratched_Dirty_Rough | Separate color, roughness, normal, metalness and specular-weight textures | Material replacement/coverage and reflection amount are independent questions; roughness alone cannot represent all finish changes |
| Brass_Foil_Yellow_Slightly_Wrinkled | Metallic base, coat about 0.235, specular weight about 0.94, inherited coat roughness 0 | A sharper secondary interface is an explicit hypothesis; inspect the effective coat normal/default instead of copying a foil label |
| Hammer_Paint_Aluminum | Coat 1, separate base/coat normal maps and coat roughness map; base specular weight 0, IOR 1, roughness 0.48 | Visible reflection can primarily belong to the outer interface; adding another strong base highlight would change the construction |

[ASWF MaterialX Teapot/Lion](https://dpel.aswf.io/materialx-teapot-lion/)
includes a metal teapot network with base conductor, rough diffuse dirt mixed by a
mask, and a second conductor response named grease selected by another mask. Its
base normals mix a painted normal field with a separately tiled fine normal at
scale 0.3, then normalize. Roughness maps pass through power 1.5 and the base is
mixed 70% toward a 0.01 vector. Read those transforms before comparing source maps
with reflections. The named grease branch is a conductor mixture, not an explicit
transparent oil slab. Learn separable spatial populations and fine/coarse ownership;
do not copy its labels as physical facts or its roughness remap into OpenPBR by rote.

When adapting an example, retain a translation ledger: original nodes and values,
new representation, preserved responses, approximations, capability tests and source
license. Render the translated control before using it as optical evidence. Distinct
base/coat normals or multiple closures are useful only if their predicted native
response survives. Keep graph-observed, native-tested and image-hypothesized claims
separate. Use [detail retention](../../image-material-detail-pilot/references/detail-retention.md)
to locate where an accepted hypothesis lost its defining features.
