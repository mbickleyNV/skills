---
name: product-asset-preparation
description: Prepare and validate a standalone product blend from frozen CAD meshes and material recipes in an isolated CPU-only Blender process, while live OVRTX work continues independently.
---

# Offline product asset preparation

For shared material masters, freeze the recipe helper revision as well as maps
and packets before bulk preparation. Verify recipe equivalence from actual
graphs, content hashes and physical mapping, not names. Preserve per-part grain
mapping and portable packed delivery. A representative save/reopen check should
establish actual shared Material identity and unchanged source geometry/normals;
reuse that result while the path remains unchanged. The current hardware example
is recorded in `docs/specialists/knowledge/asset_preparer.md`.

For authorized standalone product delivery, route the CAD/material → saved blend
stage to `asset_preparer`. Use `docs/specialists/CONTRACT.md` for delegation or
its saved-instruction fallback. This role owns assigned product outputs and a
separate offline process; it never owns the managed Blender/MCP/OVRTX session.
It may work while that session renders. Live integration and native image review
remain coordinator/turntable work after exclusive live ownership transfers.

Read [the packet and execution contract](references/packet.md). Freeze source
mesh and material hashes, stable part/surface IDs, metric bounds, per-face
flat/smooth intent, sharp edges, authored normals when supplied and metric UV
intent. Prefer explicit per-corner UVs for complicated crown/endgrain/seam paths.
Use planar/cylindrical recipes only for surfaces they represent faithfully.
Label inferred material and UV decisions; missing evidence is not measured data.

Run `blender/tools/prepare_product_asset.py` with an assigned packet/output. It
starts the existing Blender binary with factory defaults, auto-execution disabled,
empty private preferences/extensions, two CPU-core quota, 8 GiB memory ceiling
and reduced priority. No rendering, network, MCP, renderer add-on or house file.
Per-output locks and two offline slots prevent overlapping writes/excess concurrency.
If required resource controls are unavailable, fail rather than run unbounded.

Preserve shading intent during import. No blanket angle smoothing, automatic
custom-normal freeze or repeated normal repair. Flat polygons retain face normals;
curved regions retain declared smooth shading and sharp boundaries. Explicit
corner normals are preserved and checked, not regenerated arbitrarily. Geometric
normal changes are separate from a material's tangent-space normal map. Never
use either to conceal missing shape or gaps. If supplied normals violate a declared
flat region, return the measured mismatch to the source owner for a scoped fix.

Read progress receipts instead of blocking a live control socket or repeating a
build. UVs use bulk writes; normal/face snapshots are read after writes settle.
The isolated worker saves and reopens its own staged file to verify flags, UVs,
normals, shader inputs, packed textures, material regions and dimensions. It then
exits. The host promotes only matching source/asset hashes and an accepted receipt.
An existing unchanged accepted asset is reused; changed output needs reviewed
`--replace`. A failed stage never replaces the accepted asset.

Return the blend path, named collection, exact asset/input hashes, receipt,
dimensions, preserved normal/UV results and unsupported features. This is
`asset-ready-offline`, not native appearance acceptance. Update checkpoint and
candidate knowledge through coordinator review. Never cancel a live renderer,
open another product's fixture as a starting template, install in the house, or
publish. The turntable specialist consumes the accepted saved asset only when
explicitly requested and the managed session is free.

Adrian pilot lessons: compact unused per-part material slots while preserving each
face's semantic material ID; inspect actual native bindings before accepting mixed
finishes. Keep welded source topology separate from scoped render index splits used
to preserve supplied corner normals. If normals fail, localize part/loop/region and
report source-versus-encoded vectors; preserve the gate and avoid repeated global
repair. Reuse the worker's current verified implementation rather than task copies.

Origin-centered offline acceptance does not prove room-transformed float geometry. For
placement-sensitive narrow parts, return actual coordinate/transform assumptions and
request scoped consumer precision validation before integration. Reuse current source-
datum diagnostics; do not relax normal or collapsed-triangle gates. Saved-file persistence
verification remains a distinct root-owned acceptance stage.
