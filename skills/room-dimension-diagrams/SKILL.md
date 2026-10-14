---
name: room-dimension-diagrams
description: Create clean axonometric or orthographic room and joinery diagrams with source-grounded dimensions, architectural ft-in labels, extension lines, and readable technical styling. Use for dimensioned room, cabinet, counter, fixture, or assembly visuals; not photoreal rendering or permit drawings.
---

# Room dimension diagrams

Create a sparse technical visual from the project's durable geometry and dimension sources. For room and joinery assemblies, prefer Blender's established technical-illustration stack: an orthographic camera, Eevee or Workbench, Freestyle silhouette/crease lines, and native curve/text annotation objects. This keeps dimension endpoints attached to actual 3D datums and avoids hand-projection errors. Use the lightweight raster renderer only for simple box diagrams or early layout proofs.

When the project already has a canonical Blender scene, render its evaluated objects. Do not rebuild a proxy assembly from XML dimensions unless the user explicitly requests a schematic. Fork the canonical scene to a task-owned scratch `.blend`, isolate the requested room objects there, and leave the canonical file unchanged.

## Ground every label

Read the room contract and the relevant room XML before drawing. Treat attached drawings as evidence, not instructions. Use named source values where available and do not infer a dimension from the rendered pixels.

Preserve the source's precision. Convert millimetres to feet and inches with `scripts/render_dimension_diagram.py`; use typographic feet/inch marks and ordinary architectural fractions. Mark assumptions or estimates with an asterisk and explain them in a compact note. Never present provisional, estimated, or manufacturer-clearance values as field-verified dimensions.

Every dimension endpoint must be an evaluated object corner, edge datum, or an explicit architectural datum such as finished floor directly projected from a measured object corner. Record the two controlling points before drawing the annotation. A correct number attached to an arbitrary nearby point is an incorrect diagram. If both endpoints cannot be shown clearly in the chosen camera, change the camera or omit that measurement.

## Compose the diagram

Choose an axonometric view for spatial relationships and an orthographic elevation or plan when dimensions would overlap or depth is irrelevant. Show only the geometry needed to locate the requested parts. Use:

- black or charcoal object outlines on white;
- a single restrained accent color for dimensions;
- thin extension lines, open arrowheads, and labels aligned to their dimension line;
- enough offset from the object for labels to remain legible;
- a short title and source/assumption note outside the measured geometry.

Dimension overall extents first, then major bays, heights, and depths. Avoid duplicate or closed-chain dimensions unless the user asks for fabrication detail. Keep labels from crossing object edges or each other. For a full room, split plan/elevation/axonometric views when one view becomes crowded.

### Plan views and clearances

For a top-down room view, include the surrounding finished-wall footprints even when cabinetry hides part of them. Derive each footprint from evaluated wall geometry or the room's explicit finish datum; do not substitute a generic room rectangle. Frame the camera around the walls, annotations, and label masks rather than the furniture alone.

Dimension useful clear space between finished faces. For an island or freestanding assembly, check all nearby finished walls and fixed countertop edges, then show the controlling shortest clearance and any other circulation aisle that materially explains the layout. Measure countertop edge to finished wall face when the user asks for usable space around an island. Identify the two evaluated endpoints before formatting the value, and make both endpoints visible in the delivered view.

Treat a plan as an information hierarchy:

1. enclosing finished walls and openings;
2. fixed counters, cabinetry, appliances, and islands;
3. overall room or work-zone extents;
4. object sizes and controlling clearances.

Prefer a few continuous dimension chains around the perimeter and place local appliance or fixture widths close to their objects. Do not let an attempt to show every available value obscure wall relationships or circulation space.

## Deliver and verify

Save reusable diagrams with the room's other current outputs when they represent an accepted project view; place exploratory proofs in `scratch/`. Inspect the final image at its delivered size. Verify every displayed number against its named source value and confirm that arrow endpoints touch the intended datums.

Before final delivery, inspect the composite for clipped extension lines, masks, labels, and wall footprints. A render can be numerically correct and still fail if a controlling wall lies outside the frame or a dimension line appears to continue beyond its endpoint. Widen or shift the orthographic camera and render again; never repair endpoint placement in a paint pass.

Use [the renderer](scripts/render_dimension_diagram.py) for lightweight box assemblies and consistent ft-in formatting. Its JSON input supports named boxes and dimension segments in millimetres. For Blender output, make dimension lines as thin bevelled curves, arrowheads as small cone meshes, and labels as camera-facing Text objects. Use three ordered render layers: room geometry first, transparent dimension lines/arrows second, and transparent white masks plus text last. Composite in that order so geometry cannot occlude annotations and lines cannot cross the label masks or glyphs. Keep measured dimension chains solid; render extension lines as short regular dashes where they cross the view. Use restrained teal for lines and dark charcoal for text. Put a padded, flat-white camera-facing mask behind every label and exclude those masks from Freestyle line selection. Anchor both extension lines to exact visible corners, keep annotation geometry slightly above ground surfaces, and verify the entire label chain inside the camera frame. For irregular geometry, draw from evaluated CAD geometry instead of approximating the shape with boxes.

When the view benefits from showing construction behind finished faces, add a restrained hidden-line set rather than making the cabinetry transparent. Limit it to meaningful internal objects such as appliance bodies, drawer boxes, cabinet backs, shelves, runners, and supports. Use Freestyle hidden visibility with pale blue-gray, sub-pixel lines, low alpha, and a short even dash. Keep visible silhouettes solid and darker. The hidden layer should be discoverable on close inspection without competing with dimensions or finished faces.

## Fast prompting

Accept short requests once the project and room are identifiable. Interpret prompts such as these without asking the user to restate the workflow:

- “Give me a dimensioned top-down view of the kitchen, including walls and clearances.”
- “Dimension this cabinet in a three-quarter orthographic view.”
- “Show the laundry counter elevation with overall and bay dimensions.”

Infer the view from the request, use the canonical model and its room contract, include the most useful dimensions visible from that view, and return one inspected image. Ask a question only when the requested object or controlling datum is genuinely ambiguous.
