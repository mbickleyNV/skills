# Mapping and surface-detail recipes

Use standard Texture Coordinate, Separate/Combine XYZ, Math, Vector Math,
Image Texture, Color Ramp, Bump, Normal Map and group nodes where supported.
Discover operation support in the installed converter; a Blender node's presence
does not establish add-on support. Name physical controls and retain stable IDs.

## Metric coordinates and triplanar mapping

Choose one coordinate authority for the finish. Object-space positions should
have a declared origin and physical scale; use a shared reference object when
multiple pieces need continuity. World-space projection can swim on moving
objects. Generated coordinates are normalized to bounds, so equal texture Scale
values do not establish equal feature sizes across differently sized objects.
For a static normalized study, compensate by known bounds or label the scale
as specimen-relative. Preserve UVs for directional, authored or slab textures.

For explicit triplanar sampling, define position p in metres and normal n in the
same frame. Under nonuniform transforms use the inverse-transpose for normals;
assemble tangent-map normals in the source corner frame, then transform once.
Sample yz, zx and xy at their declared physical texture extent.
Weights are abs(n_i)^k / max(sum(abs(n)^k), epsilon). Sign-aware projection frames
prevent mirrored direction fields. Blend scalar/color results using these weights;
expose projection sharpness separately from texture scale. Image Texture BOX
with blend is a compact Blender-native option when the converter admits it, but
its blend control is not numerically interchangeable with this exponent formula.

Triplanar sampling addresses UV chart seams; it does not suppress source-image
repetition. Use it for stationary trowel/stone/pore fields and shape transitions.
Do not project tangent-space normal RGB independently on three axes and average
the colors: decode each normal or surface gradient in its projection frame,
rotate into a common frame, combine and normalize. Prefer a scalar height field
plus a qualified derivative route if the normal-transform path is unavailable.

## Three-sample hex stochastic synthesis

Hex tiling here means stochastic texture synthesis over a triangular lattice;
it does not create a physical hexagonal tile floor. Preserve architectural tile
geometry, grout and dimensions independently.

For a 2D coordinate u in metres, choose a physical cell length and origin. Define
dimensionless v=(u-origin)/cell_length, or use a declared inverse-length matrix
for cell aspect/direction. Then form triangular-lattice coordinates
q=(v.x-v.y/sqrt(3), 2*v.y/sqrt(3)). Let i=floor(q), f=fract(q).
If f.x+f.y<=1, vertices are i, i+(1,0), i+(0,1), with weights
1-f.x-f.y, f.x, f.y. Otherwise vertices are i+(1,1), i+(1,0), i+(0,1), with
weights f.x+f.y-1, 1-f.y, 1-f.x. Guard weight domains, sharpen with an exposed
exponent, and renormalize by max(sum, epsilon).

Hash each integer vertex to a reproducible offset (and only justified rotation).
Sample the same source texture three times with those transforms and blend the
results. Three nearest lattice vertices matter: an ordinary Voronoi Color field,
one repeating image or a hex-shaped mask alone is not this synthesis method.
Share vertex identities, transforms and weights across correlated color,
roughness, height and coverage. Match filtering and transform gradients/tangents
when rotating samples. Keep hash/trigonometric cross-renderer differences visible;
do not promise pixel-identical locations from an unverified hash implementation.

Blending loses contrast and can duplicate coherent motifs. Sharpening weights
reduces overlap while concentrating boundary changes; it is not histogram
preservation. Record any variance/histogram correction and avoid clipping height
or roughness. Inspect actual field statistics and a representative curved region.
Use coherent base shape with stochastic local residuals for plaster or textile,
rather than averaging entire trowel strokes, folds or weave crossings.

For hex plus triplanar, explicitly synthesize each projected plane, then blend
the results in the shared frame. This can require nine texture evaluations per
channel; derivatives and extra normal/coat branches can multiply graph cost.
A cheaper useful alternative is independent hex-UV microdetail plus triplanar
coarse variation, if their coordinate and property ownership is intentional.
Measure preparation and native costs when they become relevant; do not equate
small file size or fast authoring with inexpensive rendering.

## Relief, flakes and independent interfaces

Compose compatible scalar heights in physical units before Bump where their
surface ownership is shared. Avoid adding encoded tangent-normal RGB. Use a
qualified common-frame normal/gradient composition for independent normal maps.
Subdivision and geometry are required for silhouette or contact-scale relief;
a shader normal changes response without changing the boundary.

For flakes keep population/coverage, local orientation, conductor color and
reflection width distinct. Population density is not the same as reducing every
flake's strength. Keep the outer coating normal separate from the flake normal.
If RTPT loses oriented glints, preserve the editable original and either label
the flatter RTPT approximation or use a validated representation for the intended
view; a roughness-only substitute does not preserve resolved glint morphology.

Sources: [Practical Real-Time Hex-Tiling](https://jcgt.org/published/0011/03/05/),
[reference implementation](https://github.com/mmikk/hextile-demo),
[surface-gradient framework](https://jcgt.org/published/0009/03/04/).
These explain algorithms; no third-party implementation is bundled here.
