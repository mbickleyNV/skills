# Fast CAD and finish iteration

Classify the delta before rebuilding. Material-only changes need no CAD export;
camera-only changes need neither CAD nor node reconstruction. A source-boundary
change needs only affected named meshes plus their procedural consumers. Reuse
the saved scene, environment and named camera. Cache geometry by source digest
and placement, but still reconcile canonical materials after a cache hit.

Keep a project entrypoint that orders node installation, versioned upgrades,
source-marker sync and material preparation. A feature available only through a
one-off patch will disappear on a fresh build. Guard upgrades by interface/version,
not a similar node label in an archived group. Inspect current socket names and
enabled inputs once when a node API differs; don't guess successive APIs.

For a new camera, first render a small low-sample composition check, then the
requested quality once. For a contact sheet, hold camera/light/exposure fixed and
change only supported controls; compose the actual renders. Keep manufacturer
inspiration distinct from measured glaze colors. A user's “show me” variant is
normally a separate saved copy, not a replacement for their base design. Restore
mutable scene/material controls even on failure. Set the timeline frame before
the camera; a marker may otherwise override it at render evaluation.

Procedural finish markers are coverage authority, not renderable backing panels.
Bounds suffice only for a true rectangle. Preserve apertures and recess mouths
with actual source-shaped clipping; clipping the whole realized finish once is
preferable to per-tile Boolean objects. Keep markers dependency-evaluable while
excluding them from the render. Tile back/returns and wall finish around a recess
are distinct planes; exposed substrate flanges must not become accidental trim.

When the target OpenPBR translator does not support a procedural shader network,
small geometry-backed face crown or per-tile depth shear can vary highlights
without losing the exact in-plane cuts. Expose bounded amplitude and a stable
seed, with zero disabling the effect. Document this as appearance geometry, not
installation tolerances or a simulated laying process. Avoid coupling tilt to
the color palette or adding expensive topology for invisible detail.

Reconcile materials for every finish consumer, not only the first object. Shared
node groups with embedded palette materials share those materials too; independent
palettes need independent groups/materials. Use canonical original material IDs,
not evaluated wrappers, and mirror evaluated slots when the exporter requires it.

A repeated renderer session-identity failure is not a material/geometry failure.
After one supported bounded recovery fails, record the blocker; do not retry
resets or switch engines silently. An authorized fallback gets its own exposure
and clear engine label. Do not assume exposure transfers between renderers.

At pause, preserve source, reusable scripts, latest accepted outputs, external
textures/HDRs and named camera settings. Archive scoped diagnostics recoverably;
don't purge global orphan data or a shared renderer output root. Leave one short
project handoff with main versus variant scene paths and remaining limitations.
