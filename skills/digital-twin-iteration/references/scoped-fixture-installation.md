# Install an accepted fixture layout without replaying the house

Use for a reviewed multi-room fixture placement that also changes apertures or
other host geometry. Keep the accepted source-local positions/counts; installation
does not restart layout optimization. Session authorization carries forward.

## Identify the real source delta

Resolve each fixture's mounting datum, linked product master and every affected
host layer. A shaped ceiling can have continuous backing above it: cut both, and
probe the actual exported geometry for body clearance and surrounding stock.
Preserve existing non-target lights and reconcile retired IDs explicitly.

Choose source parts, not whole rooms, as the import scope. A house-wide placement
can require only a few ceiling Mesh changes. Use the guarded named-part preparer;
do not start with `prepare-ovrtx-source.py` merely because several rooms are involved.
Its full path also authors other producer families. If a target actually changes
a tile host, include that dependency using its supported producer-owned path.
An unrelated legacy-tile refusal means fix routing; it does not authorize bypassing
admission or rebuilding the tile family.

## Prepare the complete batch before touching controls

Use `blender/tools/prepare_scoped_installation.py` with a
`scoped-cad-installation/1` manifest containing explicit room/part selections.
Optional `material_keys` maps the exact selected CAD IDs to known fallback keys;
existing valid artist bindings still win. Supply explicit fallback intent for
unsupported semantic classes such as photo-derived cove plaster. Check the actual
saved room collection instead of guessing its label. Material readiness includes
fallback resolution, not just the presence of an artist Material.

The tool prepares independent room scripts and content-addressed, namespace-qualified
OBJ files under project scratch with unrelated synchronization disabled. Every
selection must match; a partially valid selection must fail. A new revision must
not overwrite a packet that another step has already prepared. Inspect `prepared.json`
for exact owners, collection, source hashes and script hashes. No live mutation is
authorized by a prepared packet alone.

At the idle/exclusive Blender boundary, run
`scoped_installation_preflight.validate_prepared(path)` read-only. It verifies
packet/OBJ hashes, target collections, local CAD owners, supported modifiers and
artist binding or explicit material intent. For Prado adoption,
`adopt_prado_layout.begin(prepared=path)` runs this check before detaching controls.
Preflight the linked master and all non-geometry dependencies needed by the specific
fixture family as well. This generic check does not resolve every material key or
prove native renderer readiness.

Apply scoped geometry, reconcile linked fixtures, then restore/control-wire the
accepted assignments. Retain the first transaction snapshot across retries; a
second snapshot of already-detached controls loses original intent. If a later
phase fails, restore the owned wiring using that snapshot before handing off;
keep completed scoped geometry and explicit failure evidence. Do not replay a
successful geometry phase merely because reporting failed.

## Identity, optics and result handling

Use canonical source IDs and actual native collection membership. Query local
scene objects for room owners. Linked master IDs can share names across libraries;
use `override_library.reference` or name-plus-library identity. A bare datablock
name or guessed `ASSEMBLY` label is not an identity proof. Preserve product Mesh
and material definitions across overrides; local placement/tilt/light-control IDs
are legitimate instance state.

Keep optical concepts separate: nominal beam/FWHM, renderer support cone, intensity
falloff and direct IES transport. Prado's existing nominal40° fit uses80.5° support
with a soft falloff. Checking support angle against nominal angle is wrong; compare
the installed properties with the product's saved fit contract. State what the
renderer actually consumes.

The existing MCP wrapper can report execution errors as ordinary text while
`isError` remains false. Treat `Error executing code:` as failure and retain the
phase/result. Record where mutation stopped. Separate application, native capture,
collection, guarded save and reporting. Check an existing successful save/readback
before retrying a failed reporting step.

## Validate and finish proportionally

Check all source openings, linked references/shared meshes, positions, explicit
retirements and user control values. Inspect one representative native render using
saved cameras, collecting its receipt once. A cold reopened scene needs population;
keep the active native session for the final capture. Compare performance only at
matching settings and include warm edit, reversal and unchanged phases when changing
exporter/runtime behavior. Session reuse alone does not prove sparse updates.

Save through the guarded project helper when the user authorized authoring. Preserve
unpublished state. No blanket house re-render, product turntable, tile reauthoring,
backend restart or publication follows implicitly from fixture installation.
