# Retained-image iteration

For grade, grain, vignette or bloom changes, first check whether the accepted native
HDR/source frame and supported compositor evaluation path still exist. Recompose
that frame when they do; record source identity, settings and output. Missing source
or unsupported graph is a reason to capture, not permission to invent an API.

Geometry, lights, camera pose, focus and physical aperture require a new native
image. Lens distortion may be compositor-only, but gallery semantic labels need
the same spatial warp with nearest-neighbor resampling. Reuse the established
gallery helper; see `blender/docs/engineering-changes/house-gallery-compositing.md`.

Keep camera, exposure and source identity stable during comparisons. One affected
frame is enough for a bloom adjustment; movement uses first/middle/last review
before a full movie. Inspect pixels and confirm the intended improvement before
launching long captures. Observe native completion offline and recover the existing
receipt after a lost reply. Re-encoding or delivery failure does not justify rendering
again. Task-specific graph experiments remain in scratch until made reusable.
