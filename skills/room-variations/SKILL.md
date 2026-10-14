---
name: room-variations
description: Create, revise, recall and render committed room variations in this remodel's house.blend, including shared hardware placement and linked fixture choices. Use for inspiration-to-variation work or editing a base component shared by looks.
---

# Room variations

Read the current top section of `HANDOFF.md`, then `blender/LOOKS.md` for runtime
APIs and supported choices. The working implementation is a kitchen pilot;
other rooms need explicit ownership/target support, not just another room name.
Use the existing live Blender MCP session with one owner. Follow `AGENTS.md`
for canonical saves and publication; preserve local unpublished work.

## Choose what owns the edit

| Request | Owner and operation |
| --- | --- |
| Paint, tile parameters, alternate finish or hardware style | Live variation draft, then explicit commit and guarded save |
| Move a handle for every look | Shared `MOUNT` Empty; no style recommit |
| Move a whole cabinet/door component | Shared `COMPONENT` Empty, carrying front and mount |
| Select a catalogued faucet | Existing linked collection choice at its local fixture placement |
| Edit an unsupported room, parameter or product family | Extend the ownership descriptor/runtime first; validate one representative round trip |

Hardware hierarchy is `COMPONENT → (front mesh, MOUNT → style objects)`.
Keep component/mount parents semantically unlabeled; geometry leaves carry
surface labels. Edit the mount for shared placement, not each style child.
Native parenting supplies inheritance. Linked fixture collections, mesh reuse,
Geometry Nodes and the durable authoring view layer each have distinct jobs; this
is not a universal library-override system. Use an actual library override only when
editable linked product internals require one.

## Operate a variation

1. Read the inspiration and user exclusions; identify supported switches and
   the smallest affected geometry. References supply design intent, not dimensions.
   Use `skills/image-feedback-to-cad/SKILL.md` for new CAD/finish work.
2. Load `blender/tools/room_looks.py` in an isolated namespace. Inspect `status()`
   and committed choices. Recalling a named study uses `apply_look`; writing the
   controller's string properties does not apply a look.
3. Assemble related edits into one `apply_choices('kitchen', choices, notify=False)`
   draft when practical. Each separate switch call reevaluates the room; avoid
   repeated expensive transactions for one intended edit. Use `refresh_renderer()`
   once when an OVRTX preview is needed. `notify=False` still evaluates Blender.
4. Inspect one useful affected preview. Correct the draft before committing.
5. `commit_variant('kitchen', name)` records a new study in the scene. Replacing
   an existing name requires its expected `replace_revision`; never rewrite a
   committed definition or index by hand. For a placement-only edit, skip commit.
6. Restore `apply_look('kitchen', 'default', notify=False)`, then
   `save_default_scene()`. Commit alone is not an on-disk save. The guarded save
   verifies Default, saves the scene, exports shared placement source, and writes
   the batch index. Do not manually save an active draft/variation as canonical.
7. Render the requested scope; visually inspect the changed look and a relevant
   Default comparison when validating a new switch or inheritance behavior.
   Check actual geometry/materials and saved status before claiming completion.

Scene `room_looks_registry` is authoritative; `blender/looks/committed.json` is its
saved index. Shared placement has a separate revision from committed style.
The API, sidebar addon and render batch operate the same choices. Blender's
Room Looks panel offers recall/commit/discard/save/refresh; Image Studio dropdowns
select verified rendered images and do not themselves author the Blender scene.

## Render only the needed scope

Use the managed Blender-Gym Python environment for the authenticated batch.
Reuse its existing connection configuration without exposing credentials.

```sh
# One matching Default + committed-look comparison, morning only:
python3 blender/tools/render_timeline_batch.py --room kitchen --shot fridge --presets morning --variant olive_wainscot
# Full room: Default at all requested times, committed studies morning only:
python3 blender/tools/render_timeline_batch.py --room kitchen --committed-variants
```

Use `--variants-only` to omit Default. Do not force fresh successful captures
without a reason. Shared placement changes invalidate render freshness without
changing style revisions. The batch detects stale images; Image Studio labels
old Default and variation images as needing a refresh while keeping them available for comparison. Report the views
actually refreshed; two comparison renders do not refresh the entire room.
See `skills/ovrtx-room-rendering/SKILL.md` for capture and bounded recovery.

## Preserve inheritance and replay

- Keep style fingerprints local to their mounting slot. Freezing evaluated world
  transforms would turn a shared placement edit into a style revision conflict.
- Preserve the original CAD coordinate frame during scoped mesh replacement.
  The guarded importers use `hardware_cad_world`; inverse current moved-world
  transforms would cancel the authored placement. For changes to mount/import
  logic, verify a real affected-part reimport, not only a visibility toggle.
- `hide_set` belongs to a view layer. Recall retains the durable `ViewLayer` and
  reapplies native visibility there. The general add-on owns accepted-generation
  snapshots, dirty admission, scoped population updates and conservative fallback;
  the room helper only recalls Blender settings. Deferred draft refresh compares
  current RNA with the accepted source, including mounts and component owners.
- On an unknown semantic class containing comma-joined labels, inspect ancestry
  and the captured ID map. Parenting differently labeled geometry under geometry
  can union surface labels; repair the hierarchy before retrying the render.
- A one-stop lower linear material color is half its value; it does not guarantee
  half the rendered pixel brightness across different light, gloss or exposure.
  Document material values separately from any visually calibrated adjustment.

Keep current state/revisions and unresolved work in `HANDOFF.md`; keep reusable
operating details in this skill and `blender/LOOKS.md`, not only session history.
