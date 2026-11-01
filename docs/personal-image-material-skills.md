# Personal image-derived materials and product reconstruction

These personal experimental workflows are separate from the inherited verified
NVIDIA catalog. They carry no NVIDIA signature or certification. Documentation
uses this catalog's CC-BY-4.0 terms; bundled code uses Apache-2.0. Technical sources
are attributed where used; third-party product images, sample assets, renderer
code and generated case media are not distributed with these skills.

## Entry points

- **Complex Blender → OVRTX / RTPT materials:**
  [blender-ovrtx-materials](../skills/blender-ovrtx-materials/SKILL.md), including
  metric triplanar mapping, hex synthesis, flakes and independent coatings.
  Install this optional adapter beside the material bundle when using Blender.
  See [capabilities and publication evidence](engineering-changes/blender-ovrtx-materials.md).

- **Product image → CAD + materials + movie:**
  [product-image-to-turntable](../skills/product-image-to-turntable/SKILL.md), version 0.1.0.
- **Surface image → material:**
  [image-material-analyze](../skills/image-material-analyze/SKILL.md), bundle version 0.15.0.
- **Modeling only:** [LuaCAD fidelity modeling](../skills/luacad-fidelity-modeling/SKILL.md).
- **Existing accepted asset → movie:** [product-turntable](../skills/product-turntable/SKILL.md).

The [current LuaCAD/product set](personal-blender-luacad-skills.md) supplies 16
related workflows. The combined entry coordinates them without replacing their
source-geometry, normal/UV, saved-asset or native-render acceptance gates. A product
image can support a plausible dimensioned reconstruction; unknown dimensions and
hidden construction remain explicit editable assumptions, not measured facts.

## Portable material bundle

Move/install these ten directories together as siblings:

| Skill | Responsibility |
|---|---|
| [image-material-analyze](../skills/image-material-analyze/SKILL.md) | Source evidence, identity and rival optical hypotheses |
| [image-material-architecture](../skills/image-material-architecture/SKILL.md) | Layers, representation and consequential material inputs |
| [image-material-spatial-design](../skills/image-material-spatial-design/SKILL.md) | Layout, coordinate families, mapping and coherent deformation |
| [image-material-detail-pilot](../skills/image-material-detail-pilot/SKILL.md) | Early source-anchored morphology and detail acceptance |
| [image-material-diagnostics](../skills/image-material-diagnostics/SKILL.md) | Hypothesis-selected AOVs/LPEs and matched interventions |
| [image-material-lobe-prompts](../skills/image-material-lobe-prompts/SKILL.md) | Detailed generated appearance studies and contact-sheet critique |
| [image-material-texture-maps](../skills/image-material-texture-maps/SKILL.md) | Registered physical fields, detail and independent interface normals |
| [image-material-calibrate](../skills/image-material-calibrate/SKILL.md) | Units, color conventions, numeric meaning and causal controls |
| [image-material-assemble](../skills/image-material-assemble/SKILL.md) | Effective graphs, settings, bindings and demonstrated native influence |
| [image-material-review](../skills/image-material-review/SKILL.md) | Source/generated/native deltas and focused correction loops |

The material bundle has no mandatory LuaCAD dependency. To use the combined route,
install the combined entry, all ten material directories and the 16 product
skills side by side in your agent's skill root. Skill folders are instructions
and bundled helpers, not a LuaCAD/Blender/OVRTX/image-generation installer. Locate
the active project's maintained integrations; missing tooling is an explicit
stage limitation. Public example paths in the product set are not installed tools.

## Try the combined route

Attach a product image and ask:

> Use $product-image-to-turntable. Reconstruct this product as editable LuaCAD,
> create detailed physically plausible materials from this image, and render a
> balanced studio turntable. Preserve source details and label inferred dimensions.

A known dimension or optional drawing improves dimensional confidence. For a
single-image experiment, do not supply or silently gather additional product views.
Reuse the accepted standard UV shader ball for material controls; use the product
for silhouette, wall thickness and final appearance. Keep source fidelity separate
from successful native execution and movie delivery.

See [publication scope and checks](engineering-changes/image-material-product-workflow.md)
and the [source/derivative inventory](personal-image-material-sources.json). No new
product has been recreated or rendered merely by publishing these instructions.
