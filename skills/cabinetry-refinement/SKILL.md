---
name: cabinetry-refinement
description: Refine existing dimensioned cabinetry from a render and accepted image-generated finish concept, coordinating product, LuaCAD, material and offline asset specialists while preserving source dimensions and scoped room integration.
---

# Existing cabinetry refinement

Use cabinetry_refiner as a source/appearance coordinator, not a second live Blender
owner. Read current HANDOFF, AGENTS, docs/specialists/CONTRACT.md and affected room
XML/house/ROOM-CONTRACT.md; LuaCAD integration also uses blender/PIPELINE-CONTRACT.md.
Use image-feedback-to-cad for scoped integration and room-variations for ownership
of supported appearance choices versus shared geometry/mounts. Do not overwrite
other committed looks to improve one finish. No automatic turntable or publication.

## Establish current scope and dimensional authority

Record the latest user-requested coverage and outcome in the checkpoint before each
handoff. A later whole-image/whole-room request supersedes an earlier pilot scope:
representative-bay validation is sequencing, not the final delivery boundary. Inventory
ALL visible requested assemblies against existing IDs (uppers, base fronts, fillers,
fridge surrounds, shelves/posts, island slats/end panels and their joints). Every item
has a source owner and implementation/review status; an overall improved concept is
not coverage proof. Pass this latest inventory to each specialist, not a stale pilot brief.

Read current source/export hashes, room transforms and active look. Divide constraints:
- Fixed: architecture, appliance dimensions/cavities, ventilation/service clearances,
  countertops/installation footprints, room anchors and explicit user locks.
- Construction refinements: panel decomposition, veneer/edging, exposed-edge easing,
  fitted seams, filler construction and shared-panel ownership, within fixed envelopes.
- User-authorized adjustable joinery: local filler/cabinet-front allocation and stock/
  reveal changes permitted by the latest instruction, bounded by adjacent fixed datums.

Source remains measurement authority. Do not interpret this as freezing every defective
internal detail. Record numeric baseline and permitted changes before modeling. For a
single shared panel replacing a double stack, evaluate actual opening/shelf/mount effects
and use explicit prior authorization when available. If a necessary dimensional decision
is still missing, present the smallest concrete numeric delta while continuing unaffected
work. Never widen a fridge/hood to improve a neighboring cabinet or silently move windows.
Preserve stable integration IDs; constituent panels/surfaces may be added under those IDs
with a documented mapping. Reconcile source versus COMPONENT/MOUNT/live placement without
assuming file recency. Use predeclared export precision tolerance, not arbitrary relaxation.

## Generate and interpret a finish concept

When authorized, use imagegen skill/tool to edit the supplied render into the desired
whole-scope cabinet-shop construction/detail study. Prompt preserves fixed camera, architecture and appliance envelopes and names every
assembly in the current scope. Show believable fabricated panels, edging, seated joints,
separate fillers, controlled reveals and grain/finish hierarchy. Apply authorized local
joinery changes only inside available spans. Do not reduce a construction request to
quieter grain or a matte recolor. Use real finish/craftsmanship references when available. Actual generation may drift: inspect and reject
unauthorized changes to fixed layout/dimensions, even if the image is attractive. Obtain user
acceptance of the concept before dependent CAD/material integration when the task
explicitly requests an accepted concept; preparation/evidence work can continue.
Generated imagery supplies appearance/detail intent, not dimensions or construction
proof. Keep concept imagery separate from production maps and do not map a lit room
image onto cabinet surfaces.

## Reuse the specialists

Delegate only scoped nonoverlapping outputs with shared dimension lock/surface IDs:
- product_detail: reference/accepted concept → existing-part feature/region ledger;
  distinguish new design intent from factory evidence and unresolved construction.
- luacad_modeler: reuse existing modules; real in-stock bevels and reference-specific
  edge/hardware details, preserving fixed envelopes/IDs and implementing permitted joinery deltas and broad planar normals.
  Use luacad-fidelity-modeling and all four linked LuaCAD methods. Return mismatched
  dimensions separately; do not silently resize, offset or renumber fronts.
- material_specialist: oak/finish evidence and image-generated OpenPBR workflow;
  physical-feature scale receipts, face/edge/endgrain construction and stable per-part
  crop/phase variation at one metric scale. Respect intentional veneer matching;
  randomization is not a substitute for board/veneer construction. Grain direction
  is a documented design choice, not universally vertical. All channels align.
- asset_preparer: isolated cabinet-bay preparation using current bounded worker;
  save/reopen normals/UV/semantic materials, consume scale receipts and report unsupported
  adapters. House import remains the root coordinator's job; standalone asset is a proof.

Pass saved project developer instructions verbatim if native profile loading is
unverified; report selection/fallback once. Inherit coordinator model. Source work
may proceed while rendering is busy. No delegated live Blender or renderer cancellation.

## Validate the bay before propagation

Compare affected source and exported dimensions/transforms with the frozen lock;
check dependent reveals, openings and mounting datums, not bounds alone. Report measured
before/after deltas with tolerance. Any unapproved dimensional mismatch blocks integration; approved construction deltas
are compared against their declared target rather than the obsolete baseline.
In-stock bevel geometry may change individual vertices but must preserve locked envelope
and stock thickness; missing extrema require an analytic datum check, not relaxed tolerance.

Inspect one representative bay in neutral and grazing detail views with fixed camera,
lighting and exposure; evaluate edge highlights, gaps/contact, grain scale/direction,
repeated motifs, seam flow, UV stretching and finish response against the accepted
reference. Orbit/beauty appearance alone doesn't close those items. Reuse existing
previews; native requests wait for sole-owner transfer. Geometry changes use the
geometry-only room build and guarded changed-part/dependency import; materials/UV-only
changes skip CAD rebuild. Preserve native Objects, materials, variation assignments
and unchanged geometry. Follow manual save and explicit publication rules.

Return dimension-lock comparison, affected IDs/hashes, feature/region acceptance,
inspected images, remaining estimates and coordinator-reviewed checkpoint. Propagate
only the accepted recipe within user-authorized scope. A bay may validate the recipe first, but continue through the full authorized coverage
inventory. Do not stop after a pilot when the latest request covers the whole room.

## Complete the in-place replacement

A remodel-and-replace request authorizes root-owned integration after concept acceptance
and relevant validation, within fixed constraints and latest scope. Root updates the
existing source/helper recipes and native Objects in place via scoped import; a separate
standalone product or optional pilot flag is a proof, not the finished room source.
Preserve identities, parents, mounts, linked dependencies and other-look ownership.
Use supported appearance variation draft/commit/save rules when applicable; update the
requested committed look only with its guarded revision and do not overwrite unrelated
looks. Verify save in the tracked local house copy under AGENTS manual save rules; never
publish without explicit instruction. If save/commit authority is genuinely missing,
finish reviewable integration and identify the specific remaining boundary.

Keep the accepted replacement as the delivered authoring state. Snapshot prior data for
rollback, but do not automatically restore old meshes/materials after successful review
unless the user requested a temporary study. Restore transient cameras/render settings
and release native ownership independently of keeping cabinet edits. If restoration is
required, synchronize/verify renderer state so the visible stage is not stale. Final
handoff distinguishes persistent source, applied scene, saved revision and publication,
with whole-scope before/after and generated-target versus modeled-detail evidence.


For shared image-to-construction delta ledgers, accepted-profile persistence and current-revision review, use skills/existing-asset-refinement/SKILL.md. Cabinetry constraints above remain the specialized extension. Stronger bevel never silently revokes accepted roundover or covered edging.

For rough cabinet blockouts, the fixed dimension contract is installation/fit authority,
not an automatic lock on door count, arbitrary gaps or proxy hardware. A cabinet-maker
concept may propose paired doors and coherent rails/stiles inside the fixed envelope;
carry accepted internal redesign through source IDs/retirements as described in
existing-asset-refinement. Explicit layout locks still apply. Do not reverse credible
construction proposals merely because they differ from an unapproved proxy.
