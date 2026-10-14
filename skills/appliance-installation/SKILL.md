---
name: appliance-installation
description: Model or replace built-in appliances in CAD and Blender using manufacturer installation manuals, coordinated cabinet openings, ventilation and service clearances. Use for installed appliance fit, not standalone product visualization or installation certification.
---

# Appliance installation and replacement

Use this skill for the installed relationship between appliance, cabinetry and
neighboring equipment. Route source modeling to `luacad-product-reconstruction`,
Blender edits to `blender-mcp-workflow`, and requested OVRTX room proof to
`ovrtx-room-rendering`. Follow the project's canonical scene and source contracts.
Do not turn a visual replacement into permission to redesign adjacent cabinetry.

## Establish the installation envelope

Identify the exact model, market and installation option. Obtain official product
data, installation instructions and, when applicable, separate furniture-panel
fitting instructions. Inspect relevant dimension drawings and their notes visually;
text extraction alone can lose projection arrows and support datums.

Record sources and page numbers alongside the dimensions. Distinguish:

- Finished front envelope, chassis envelope, and minimum clear niche.
- Flush versus proud mounting, front projection and handle projection.
- Support elevation versus visible front bottom; they need not coincide.
- Above-counter height versus below-counter depth and cutout geometry.
- Furniture-panel thickness, reveals, hinge clearance and permissible leveling.
- Ventilation openings, wall setbacks, service space and removal access.

Keep published values separate from photograph-derived radii, trim, glyphs and
hidden-detail estimates. Resolve conflicting metric/inch or web/manual dimensions
using the applicable installation drawing; record discrepancies and don't average
them. An unresolved conflict affecting fit is a reason to pause that decision.

## Coordinate the installed assembly

Share units, axes and wall, floor, cabinet-front and countertop datums before
independent modeling. If delegation was requested, assign separate appliance
modules; one integrator owns shared cabinetry and one operator owns live Blender.

Check appliances together, not only against their individual niches. Measure the
actual overlapping geometry: a cooktop's underside, an oven's upper chassis/front,
and any intervening filler or rail. Check cutout lands and corner radii, support
height and rear ventilation, plus accessible services. Tiny support shoulders can
still violate a no-wall-contact instruction despite a large central vent notch.
Report the controlling gap and required minimum, rather than saying only “fits.”

Preserve the approved cabinet chain and countertop exterior. Subtract the real
cutout and model required supports/vents in the source; don't conceal collisions
with Blender patches. If flush installation exceeds available depth, use a
manufacturer-supported proud option only when consistent with user intent, and
disclose its projection. Otherwise ask before changing the installation or cabinetry.
Align requested visual datums only within the appliance's documented adjustment
range; a raised model is not proof of an approved support or leveling solution.

Separate geometric fit from construction approval. Flag unresolved structural
supports, electrical routing, ventilation provisions or model-specific hood
requirements without inventing a certification or broadening the task into design
of those systems.

## Preserve editable geometry and finishes

Keep stable part IDs when replacing schematic appliances. Separate real material
boundaries: stainless trim, opaque ceramic glass, smoked viewing panes, frit,
rubber seals, chrome and printed markings. “Glass” does not imply transparency;
an induction surface should not inherit a window-glass shader. Keep tiny printed
glyphs grouped without requiring them to be one connected manufactured solid.

Use scoped live updates with the correct room placement. Preserve Blender Objects,
replace mesh data, and reconcile genuinely retired IDs. Put named finish bindings
in the reusable import/material workflow, not only a one-off console correction.
Include dependent countertop/support geometry in the update. If the live watcher
and final preparer both write meshes, stop the watcher before final UV/normal work.

## Validate and hand off

Check changed source bounds, closedness and intended component structure once;
compare unaffected envelopes when adjacent dimensions must stay fixed. Verify
evaluated material assignments as well as authored slots. Blender evaluated
datablocks may be copies: compare their original identities and face material
indices, not raw evaluated-versus-authored pointer equality.

Send an early native CAD preview when useful, then inspect a cheap in-room Blender
preview before final captures. A successful live-update receipt does not establish
correct pixels. Reuse the open render session for accepted views; don't require a
whole-house audit or reopen cycle for an ordinary replacement. Save the canonical
scene with durable settings and report inferred details and unresolved fit items.
Publishing the scene is a separate user-authorized action.
