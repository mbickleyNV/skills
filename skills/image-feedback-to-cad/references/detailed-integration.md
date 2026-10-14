# Detailed integration

Read for mating details, delegated integration, new emitters or explicit continuity audits.

## Lessons from detailed room iteration

- Resolve image proportions against the plan before splitting joinery: keep the
  printed outer width and fixture center, then derive residual shelf bays and
  usable depth after stock thickness. Do not scale the room to match generated pixels.
- Size angled louvers from their projected blade thickness/height, not nominal
  pitch alone. Check that the intended gaps read in one head-on preview; keep
  blade dimensions and angle in room source, not skill defaults.
- A flush surround follows the finished cabinet-front datum, not appliance door
  or handle projection. Keep appliance service clearances independent.
- Mount hardware from the finished mating surface, including backsplash/tile
  thickness. Share that datum between the fitting, escutcheon, seal and finish;
  a wall-coordinate mount can bury hardware behind a newly added finish.
- If a fitting is absent from the representative preview, compare its live bounds with source and
  mating surface. Agreement plus an old silhouette is evidence of stale export,
  even when the render call succeeded; use documented save/reopen recovery.
- Keep each saved camera's aspect ratio as well as pose/lens. New close-ups
  should be framed past intervening glass or handles when those hide the detail.
- Finish and freeze a delegated source export before staging it. A late added
  part needs its own explicit delta, not an assumed inclusion in an in-flight import.
- Lighting helpers must take each fixture's actual world-space emission direction.
  Scope emission materials and daylight-fill assumptions to the edited room,
  then let native exposure meter the result. Shared material names are not
  permission to alter another room's appearance.

### Verify new accent lights
For a newly installed fixture, compare light-on and light-off images. Unchanged native auto-exposure settings do not lock exposure: use a genuinely fixed exposure for quantitative comparisons, otherwise report only the visible difference. A clear center ray and populated light properties do not establish visible contribution. Separate manufacturer photometry/design intent from renderer-calibrated energy; label an empirical brightness override honestly when the backend radiometry has not been independently validated. Keep the emitter at its physical optic when the comparison confirms it works there.

## Faster scoped integration

- The guarded preparer batches selected OBJ parts into one import operation; use it instead of one operator per part. Preserve `part-namespace` and merge object metadata with part semantics. Render meshes receive stable `CAD RENDER | <part-id>` names, not temporary batch names. Keep tool responses to counts, errors, changed IDs and actual captures; do not echo mesh payloads or duplicate structured/text results.
- Before diagnosing stale rendering, identify the visible source component and its evaluated material. A wood refrigerator door does not cover an exposed white appliance side; a toe board behind full-height end panels does not create a continuous toe recess. Check the mating geometry, not just the intended part's material. Hidden obsolete standalone inserts can be unlinked from the active scene while retaining their datablock identities; do not apply this to live procedural dependencies.
- For authorized parallel work in a folder without Git, create one temporary source-only Git snapshot under scratch and worktrees from it. Give agents nonoverlapping modules or explicit source sections. Merge shared XML by named elements, freeze exports, then run one geometry-only build. Avoid copying the canonical blend and large finish assets into every worktree.
- For neighboring delegated geometry/finish work, share a compact interface handoff: controlling XML parameter names, finished mating planes, stable part IDs and placement. Return an exact changed-file list plus merge snippets for shared XML; one owner applies those snippets. This avoids rediscovering dimensions or overwriting another agent’s source with a whole-file copy.
- Freeze geometry, materials and lighting before the final camera batch. Inspect one representative affected preview; add a close-up only if the detail cannot be judged there. Reuse unchanged camera framing and capture each requested final view once. During accumulation, document or prepare the sheet; do not poll every second or reread unchanged source.

## Continuous-geometry sweep

- Audit source exports before Blender objects. Flag single semantic parts with
  multiple connected components, face-touching or near-coincident same-material
  neighbors, repeated primitive suffixes, and visible seams across an intended
  continuous finish. High object count alone is not a defect.
- Classify every candidate as one physical solid, intentional construction joint,
  separate material, operable body, removable hardware, glazing, or annotation.
  Leave the latter categories separate and preserve their stable identities.
- Rank candidates by visible seam/shading risk, source-topology failure, repeated
  Boolean/import cost and editing burden. Start with one representative junction;
  do not bulk-union the house from proximity alone.
- Repair the owning XML/LuaCAD source with an extruded profile, aperture subtraction,
  sweep/loft, or an in-stock Boolean union. When IDs consolidate, declare and retire
  superseded Blender objects explicitly; mesh replacement is not deletion.
- Validate changed solids for one connected component, closed edge incidence,
  positive volume, unchanged controlling bounds/openings and intended silhouette.
  Render a native LuaCAD proof first, then one scoped Blender view when shading or
  material continuity matters.

