# Preserve coherent deformation and local texture

Read when folds, creases, drape, pressing or broad undulation define a surface,
especially when a reconstruction becomes veiny, crumpled or uniformly noisy.
This is a morphology and representation branch, not a fabric recipe. Use only
features supported by the source or an explicit user-selected target.

## Describe shapes before calling them wrinkles

Separate broad deformation, intermediate construction and fine surface residual.
For a visible fold record its shoulder width and curvature, trough width/depth,
length, direction, continuity, endpoints, convergence and adjacent quiet land.
State whether it is a broad rounded sheet bend, sharp crease, packed pleat or a
small surface ridge. Thin branching ridges with repeated junctions can read as
veins even when their frequency resembles cloth. Sparse broad folds separated by
quiet areas are not equivalent to a dense network of narrow noisy ridges.

Anchor a few diagnostic source crops and relative feature widths. When scale is
unknown use observed ratios and uncertainty; do not invent measured fold dimensions.
Keep unsupported hidden folds explicitly synthesized. A reflective highlight can
suggest curvature without supplying a trustworthy height profile by itself.

## Assign scales to representations

| Feature family | Representation question |
| --- | --- |
| Broad coherent bends | Does normal-only shading suffice, or are silhouette, parallax and self-occlusion needed? Use supported displacement or separately labeled geometry when these cues matter. |
| Yarn/bundle crossings or embossed construction | Preserve pitch, crossing order, alignment and local orientation; inspect at a matched source footprint. |
| Local grain, fibers or microtooth | Use a residual field with its own scale and bounded amplitude; stochastic synthesis may be appropriate. |
| Outer film/coating | Decide whether it conforms to broad folds, smooths fine substrate relief, or adds independent detail. A smooth film need not erase all larger-scale bending. |

A standard shaderball can test local response but cannot prove reconstruction of
product drape or fold silhouettes. Keep that benchmark unchanged; use an identified
source-like proxy for geometric questions. Do not solve missing fold volume with
one high-amplitude noise normal. Keep global deformation and local residual controls
separate so mapping the latter does not duplicate, randomize or narrow the former.
A continuous tangent/orientation field should follow the construction where visible;
anisotropy magnitude alone supplies no direction.

## Carry the morphology into generation and native review

Write concrete positive constraints: broad soft shoulders, long continuous troughs,
observed fold spacing/endpoints and quiet panels, plus the appropriate smaller
construction. State exclusions tied to actual drift: branching cords, reptile-like
veins, invented sharp crinkles or exaggerated embossing. Do not request all of these
traits for every source. Save which channel owns each family and what must remain
unchanged. Imagegen appearance studies illustrate shape; numeric height/normal maps
need separate data contracts and profile review, not grayscale lit folds.

Compare source, chosen appearance study, structural field and native crop at similar
feature footprints through [the detail pilot](../../image-material-detail-pilot/SKILL.md).
If a field is already veiny, return to morphology rather than optical fitting. If
only the final render becomes veiny, inspect field composition, masking derivatives,
mapping overlaps, scale and normal amplitude. Use broad-deformation-only,
local-residual-only and combined controls where their interaction is disputed.
Then inspect the full rotating ball for consistency and the proxy for coherent
deformation. More gloss or fuzz cannot repair an incorrect fold network.
