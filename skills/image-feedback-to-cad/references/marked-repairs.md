# Marked repair diagnosis

Use this for a localized defect identified in a rendered image. Keep the repair
scoped to the visible problem and its actual dependencies.

- When a native semantic capture exists, inspect the marked pixel's label to
  narrow the owning surface. A class label can cover several Objects: confirm
  the specific part using world bounds, source membership or a targeted ray.
  A protrusion beside tile may belong to a cross-room wall finish, not the tile.
- For a dark seam, compare the mating planes and source topology first. If the
  surfaces meet and are flat, inspect broad-face corner normals against geometric
  face normals. Missing flat-joinery treatment on a scribe can imitate a bowed
  panel or open gap. Correct that import policy, retaining smooth bevel bands;
  do not move geometry, change lighting or soften shading to hide a real gap.
- For a narrow wood filler, inspect the assigned oak material, active render UV
  layer, physical texture scale and grain direction before replacing textures.
  Reuse metric UV helpers. Preserve the accepted grain direction on later mesh
  replacements; a geometry cache hit still needs appearance validation.
- Repair protruding architectural stock in its owning XML/LuaCAD solid while
  retaining required backing. Update the dependent continuous finish. When
  scoping finish-mesh replacement, retain the complete active ownership set;
  removing unrelated groups from that set can hide their finishes or expose
  duplicate source members. Compare actual geometry when a shared digest changes
  for several otherwise unchanged finish groups.
- A moved cabinet boundary can leave a toe kick at its old start, and a recessed
  plinth can remain hidden behind an unrecessed appliance body. Check adjoining
  source envelopes and derive dependent ends from the same finished datum.
  Keep appliance ventilation separate from a neighboring marked trim panel.
- Retire a removed source part explicitly and keep its Blender Object hidden
  and recoverable under the project's identity-preservation contract. Verify
  retained geometry Objects' parents, collections and transforms. Check any
  intentionally repositioned dependent Lights against their new source datums,
  rather than asserting that every Object transform must remain unchanged.

If new notes arrive during a render, prepare independent source work while the
capture finishes; keep one live Blender owner. Apply the delta after confirming
the active execution has ended, inspect one representative proof, and refresh
the views that actually show the changed geometry or appearance. Do not present
earlier captures of affected views as the repaired revision.
