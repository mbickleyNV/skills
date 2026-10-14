---
name: articulated-furniture
description: Make CAD furniture articulate in Blender and live OVPhysX, export SimReady assets, and validate robot manipulation. Use for drawers, doors and furniture mechanisms, not Blender environment administration.
---

# Articulated furniture

LuaCAD emits named geometry and contact intent; Articraft bootstraps body
membership, joint frames, limits and mechanism checks. Import into Blender,
then let the saved `.blend` own geometry, physics and grasp metadata. Exports
are snapshots; never silently overwrite artist edits with the bootstrap recipe.

## Three useful gates

1. **Looks right:** compare the product view and relevant mechanism inset with
   the input. Resolve silhouette, placement and functional openings first.
2. **Moves right:** one short live test of each distinct mechanism with actual
   contact shapes, authored travel and passive behavior. Reuse repeated-part
   results; check changed/handed interfaces where they differ.
3. **Robot-ready:** robot-only contact can grasp and operate the intended part.
   Capture useful demonstrations during this same run. A learned-policy request
   additionally needs fresh closed-loop policy success; neither a SimReady pass
   nor a controller demonstration proves that.

Default to the user's first target drawer, not every possible mechanism or policy.
Test it inside the complete assembled furniture, with neighboring parts and
collision geometry present. One target does not mean an isolated drawer coupon.
Run one official profile check on the final export when SimReady is requested;
treat it as a deterministic packaging check, not another conversational approval.
Before robot launch, verify the final portable package's authored physics API
tokens, collision settings and body/joint inventory against the current saved
Blender export contract. `run_target.sh` performs this CPU gate before Kit starts;
missing/stale contracts require re-export, never expectations rebuilt from a
candidate USD. A static profile pass does not establish mechanism contacts. PhysX filters
adjacent parent/child links despite per-joint collision flags; check required
case/moving contact topology before Kit and retained runtime links after loading.
Expand testing for observed defects or explicit fidelity requirements, not by
repeating old environment, bridge or whole-suite qualification on every asset.
A small timestep comparison is useful for suspicious contact/limit behavior,
not a mandatory extra run for every cosmetic edit.

## Choose the relevant recipe

- For new PDF geometry, use `luacad-product-reconstruction`.
- For Blender integration/export, read [authoring contract](references/blender-authoring.md);
  actual Blender operations use `blender-mcp-workflow`.
- For Isaac manipulation or learned feedback, read [robot recipe](references/robot-drawers.md).
- For parallel product workers, share the [compact handoff](references/batch-handoff.md) first.
- Existing local code/evidence lives under
  `/home/mbickley/product-to-3d/spikes/`: `simready-kitchenette`,
  `isaac-kitchenette`, and `blender-articulation-handoff`.
  Read the relevant current entrypoint/report, not every historical spike log.
  Use `simready-kitchenette/examples/README.md` for the implemented CAD-intent
  adapter and `isaac-kitchenette/run_target.sh` for target-ID robot operation.
  PDF interpretation remains agent-assisted; respect the documented v1 limits.

## Mechanism invariants

- Preserve stable source IDs, installed transforms and explicit units. Group
  hardware by what it moves with: hinge cups follow doors, plates stay fixed.
- Derive contacts and openings from the same CAD parameters as visuals. Use
  separate panel proxies, never a convex hull that closes the whole cabinet or
  drawer. Grasp directions are candidates to test, not arbitrary universal rules.
- Native Blender properties own concepts where meanings match; persistent
  metadata supplies missing USD/PhysX concepts. Use the installed add-on's USD
  compiler and configured runtime backend. Follow the project's current handoff;
  historical SIL evidence does not authorize installing or restoring that backend.
- Keep rest state separate from live preview; Reset restores authored state.
  Export the product without test stands or drive curves unless requested.
- Articraft FK checks must reflect current Blender-exported frames/limits.
  Placeholder kinematics does not establish contact correctness.
- Only the intended input is driven: passive drawers/doors get no hidden motors,
  constraints or pose writes. Unlatched doors are not necessarily self-closing;
  springs, stops, mass and friction assumptions must be explicit.
- Live means fresh solver motion. Never present baked playback, reversed video
  or stitched resets as live proof. Use OVRTX for Blender rendering, never EEVEE.
  Isaac Sim RTX is a separate integration; label it accurately. Use the existing
  installed add-on's supported session-update adapter and verify a visibly moved
  body's pose agrees with the measured solver pose before recording. Derive
  validation scope from the loaded inventory and the checks actually executed.
- Judge the first rendered frame before a long capture. Fix guide visibility
  and width in authoring, not by hiding defects in the camera. Close recording
  before a separate reset check. Solver-clock video is not real-time throughput.

Deliver the asset, short live evidence and reusable entrypoint with an honest
controller-versus-learned result. Avoid expanding a scene task into infrastructure.
