# Drawing overlay for product reconstruction

Use this for every product reconstruction with a usable manufacturer dimensioned
orthographic view, especially when visible edge treatments matter. Do it after the first source export and before adding
small hardware, materials, or render polish. This caught a 14 mm missing rear
glass section and an incorrect groove pitch in the RBW fixtures.

1. Inspect the actual drawing pixels. Identify the finished side/end/front view,
   printed dimensions, the mounting datum, and whether an inner line is a real
   part edge, a thickness edge, a leader, or a hidden detail. Record which dimensions
   are specified and which shapes must be estimated.
2. Derive pixels per millimetre from a printed dimension in the same view. Check
   another dimension when present; a perspective image or nonuniformly stretched
   scan is unsuitable for a strict orthographic overlay.
3. Export named 3MF meshes. Run `scripts/overlay_drawing.py` from this skill with
   the two projected mesh axes, their signed directions, the common mesh/drawing
   datum, and the measured pixel scales. The result contains a plain side CAD
   projection and a drawing overlay. Red marks CAD edges, blue fills its silhouette,
   and the manufacturer's strokes remain black.
4. Compare the exposed outer profile first: overall envelope, mounting face,
   depth split, bevel/round transitions, repeated-groove count/pitch/depth, and
   attachment tabs. Then compare internal seams only where the drawing actually
   defines them. Fix source geometry and regenerate the overlay; do not solve a
   shape mismatch with smoothing or color.
   For nested translucent or perforated parts, also render **separate named-part
   outlines** over the same registration; a union silhouette can hide an incorrect
   inner taper or top datum. Check each part's top and bottom Z, half-width at
   several heights, and whether the line is a near/far edge, interior seam, or
   hidden continuation. Keep exact callout dimensions separate from silhouette
   estimates: one maximum diameter does not prove a constant diameter. Treat
   user traces as evidence about the indicated edge, and recheck other exposed
   parts after changing a profile. Do not infer a component's top from the
   assembly's top or from another component's horizontal line.
5. Inspect exposed edge treatments in both the elevation and product imagery:
   glass rim returns, rounded shoulders, bevels, flute ends, fin tips, and finish
   seams. Magnify each visible curve join: matching endpoints and overall bounds
   can still conceal an abrupt change of tangent or an undersized radius. Compare
   the tangent on both sides of the join and the spread of curvature through the
   transition. Model sampled arcs or blends with continuous tangents where the
   reference is soft, while preserving the dimensioned datums and wall thickness.
   Check the exported mesh in an enlarged overlay and a close CAD view; raster
   aliasing and smooth shading can each disguise the actual source radius. Record
   which radii remain inferred rather than treating a visual fit as a tolerance.
6. Keep registration error and inferred manufacturing detail separate. Report
   meaningful remaining differences, not a blanket claim of exact fit. Pixel-edge
   statistics can help on a clean segment, but line thickness, scale rounding,
   anti-aliasing, and dimension leaders limit their accuracy.

Example for a side view with mesh Z to the right, negative Y downward, and a
380 mm printed length spanning 1496 pixels. These values illustrate the CLI;
read every datum from the next product's own drawing:

```bash
python3 scripts/overlay_drawing.py product.3mf drawing.png scratch/side \
  --u-axis z --v-axis=-y --u-zero -190 --v-zero 0 \
  --pixel-x 213 --pixel-y 273 \
  --px-per-mm-u 3.93684 --px-per-mm-v 3.92857 \
  --crop 170 245 1750 520
```

Keep original manufacturer images as reference evidence. Put comparison PNGs in
the project's scratch or diagnostic area. The overlay is a geometry review aid,
not a replacement for a product photo or a certified tolerance drawing.
