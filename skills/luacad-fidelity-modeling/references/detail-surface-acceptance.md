# Detail and surface acceptance

## Feature ledger

Use one record per meaningful reference feature, keyed to stable part or feature ID:
source image/page/crop, variant, specified or inferred dimensions, intended detail,
status (modeled / deliberate simplification / unresolved), changed source/export and
inspection evidence. Deliberate simplification needs user-authorized scope or an
explicit coordinator decision consistent with the requested fidelity; disclosure
alone cannot waive a required feature. A silhouette match is not completion of
nested internal parts.
Prioritize distinguishing features in the intended views; preserve finer source
geometry when a room view cannot show it. Do not make its disappearance at room
scale a reason to omit a required product detail.

Examples: faucet aerator recess and lever gap; lamp neck windows, shade wall/lip,
carrier heads and underside diffuser clips; perforated furniture strand/bond shape
and formed edge; trim section and actual joint. A sheet is not expanded lattice,
a solid cap is not an aperture, a rectangular bar is not a curved rod. Reference-
specific details take precedence over generic hardware or catalog assumptions.

For unresolved construction, investigate the affected inset or alternate view.
Reasonable inferred dimensions can support a visibly faithful candidate when labeled;
absence of factory tolerances does not require a featureless placeholder. Do not
invent threads or machining details hidden from all evidence and unrelated to use.
When a constructor fails, try a representation suited to that form (profile, offset,
sweep, skin, robust in-stock union or controlled polyhedron), validate one junction,
and record any remaining inability. Do not silently fill a cavity or remove a lip.

## Exported shape and tessellation

Choose sampling against curvature, feature size and intended close-view silhouette,
not a fixed triangle count. Compare curved silhouette/highlights at increased sampling
when faceting remains; stop when improvement is no longer visible at the intended
scale and the required profile survives. Keep thin gauges, reveal clearances and
normal-offset shells dimensionally correct. No global subdivision on planar stock.
Check winding, section frame/twist and loft vertex correspondence, especially mirrored
members and inward offsets. Keep genuine separate hardware/materials/motion bodies.

## Render normals handoff

Welded topology checks establish physical connectivity; render loop-normal splits
establish shading continuity. Do not merge those contracts. Describe each part's
planar, curved and intentional-crease regions. Broad flat faces keep constant normals;
modeled bevel bands and continuous spun/swept surfaces use smooth normals within the
proper regions. Keep crease/material/contact boundaries as appropriate to construction,
not merely by an arbitrary global smoothing angle. Blanket smoothing can create bowed
panels; blanket flat shading can facet curves. Weighting normals cannot repair missing
geometry or a defective profile. Verify imported/evaluated normals after export, not
only the CAD preview. Cache hits retain the same normal gates.

## UV and material-region handoff

Specify per part: material region/slots, UV mode (metric planar/cylindrical/path-aware
or bespoke unwrap), physical repeat extent, grain direction, expected seams and
channel phase. Existing world-metre planar mapping is suitable for planar panels;
it is not automatically suitable for a neck, curved faucet, torus or bent rod.
Preserve smooth pattern flow around the visible surface; place unavoidable seams away
from hero-facing regions. Avoid degenerate UV faces, conspicuous stretching, inconsistent
texel density and unintended mirrored grain. Retain one coordinate/phase across color,
roughness, normal and coat maps. In an offline export that lacks UVs, provide this
explicit recipe and leave UV delivery pending; never invent tested support.

For wood joinery, declare broad veneer, longitudinal lipping/edge banding and
solid-stock endgrain regions separately. Supply edge grain axes and seams along
with the face chart; a front projection must not collapse perpendicular caps.
Verify the evaluated bevel bands retain physical UV scale after modifiers. See
`../../image-feedback-to-cad/references/texture-workflow.md` for the bounded oak
edge repair and post-import source-witness check; preserve accepted face grain.

Coordinator can inspect a metric checker/directional stripe on affected imported
surfaces when needed, then actual material highlights. Confirm active render UV layer,
tangent convention, slots and native consumption. Material/normal checks remain
mandatory on scoped cache hits. Do not rerender the house for a single fixture.

## Acceptance stages

Source-complete: ledger addressed, named export validated, actual reference/mesh
images inspected, deliberate simplifications disclosed. Drawing overlay required
where available; no claim of factory section accuracy from estimated inner geometry.

Render-ready: guarded imported normals/UV/material checks and native close-view
inspection additionally passed. Coordinator owns that stage. Neither high part count,
watertightness, a success log nor a beautiful CAD color image establishes it alone.
A real native defect returns to the owning source or mapping policy; no coincident
patches, smoothing disguises or extra render samples to conceal a missing feature.

## Continuous bowl and curved-surface fidelity

For basins, cast shells and sanitaryware, sample the analytic/profile construction
in both perimeter and depth directions. A fixed eight samples between loft stations
is a draft choice, not an acceptance target. Interpolated stations must preserve
monotonic depth, positive wall thickness and intended tangent continuity; inspect
overshoot and correspondence around corners. More rings cannot fix a wrong profile.
Use curvature-adaptive sampling with a declared maximum chord deviation; 0.1–0.25 mm
is an inferred starting tolerance for close product review, tightened when image
scale or specular response reveals facets. Preserve flat rim planes and intentional
creases. Primitive fn settings do not refine custom sampled lofts. Preview --smooth
changes shading only. Compare one affected mesh at finer sampling, including section,
silhouette and grazing highlights; keep the finer source if the coarse result fails.

Reference-visible details remain open until a comparable crop is inspected: basin
wall/floor transitions, drain/overflow seats, edge rolls, hardware mounts, slat
profiles, capped feet and visible joint treatments. Labeling a radius inferred is
provenance, not permission to simplify its visible profile. Source completeness and
native appearance are separate gates; washed-out or distant views cannot establish
small-feature acceptance. Use a neutral/grazing diagnostic when the beauty lighting
hides a transition. Do not add concealed factory hardware without evidence.
