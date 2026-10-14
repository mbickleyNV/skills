---
name: tile-finish-lookdev
description: Refine or diagnose this remodel's procedural ceramic tile geometry, UVs, PBR materials, grout, and close-up renders. Use for tile appearance or mottling; not for structural wall redesign.
---

# Tile finish look development

Keep the room's dimensioned finish envelope in LuaCAD and the individual tile layout in Blender Geometry Nodes. Read `HANDOFF.md`, `AGENTS.md`, and `blender/tile-layout/README.md` before editing; follow the active local-save and manual-publish instructions. Work on the affected host and its dependencies, with one owner of live Blender.

## Diagnose the visible surface first

From the marked image, identify the actual frontmost object and its evaluated material at that camera ray. Distinguish the structural wall, non-rendered source marker, generated tile face, grout, glass, and Boolean cap. Confirm the intended surface plane and outward face normal in room coordinates. A source marker that touches a structural wall can create depth fighting once textured tiles are added; a source-material face count of zero alone does not prove the competing wall is hidden. Check for coplanar or nearly coplanar layers before changing color, roughness, or lighting.

For mottling, use a small differential review on one affected host: inspect its evaluated bounds, outward normals, material slots and UV layer; then temporarily isolate the suspected geometry or material channel and make one low-cost proof. Compare with an unaffected host in the same view. If the renderer shows old geometry or texture placement despite correct evaluated data, use the project's bounded saved-scene reopen path. Do not stack appearance changes on an unverified stale render. Query expensive evaluated meshes one host at a time; a whole-room per-loop audit can stall the Blender connection.

For white tiles, pale grout, or a broken threshold, count evaluated faces by material, face normal, and position. Check that every face's material index resolves to a populated evaluated slot; a connected `Set Material` node alone does not establish coverage. Trace the affected geometry through Boolean clipping and each `Join Geometry` multi-input socket: adding a new link does not remove the old stream, and coincident tile streams can hide grout or make an edge appear cut. A source cap or selector face can also survive clipping above the intended grout. Repair the owning node path, then check the pan top and boundary again on the evaluated mesh.

For reference provenance and cross-material comparisons, use
`skills/material-reference-lookdev/SKILL.md` only when those questions arise;
this skill retains the ceramic/GN-specific diagnosis.

## Author believable tile surfaces

- Keep physical tile size and grout width in the Geometry Nodes layout. Give tile faces tile-local UVs **before** instancing; carry stable per-instance UV offsets through realization and clipping. Confirm the evaluated render UV layer contains nonzero, varied coordinates on tile faces. Compare the active render UV layer on a flawed host with a clean host: legacy CAD `MetricUV` can remain active even when the material names `TileUV`, and an exporter may sample the wrong layer. Remove legacy UVs only from generated-tile source markers, then verify the evaluated mesh has `TileUV` active. Use the same UVs for albedo, roughness, normal and height.
- Set texture frequency in physical units. For example, a 512 px map covering a 2-inch face represents about 0.1 mm per texel; a 2×8 tile needs roughly four repeats along its long dimension for isotropic grain. View the contact sheet at native resolution, then check both a close-up and a room view because subpixel grain can disappear in one and alias in the other.
- Let fired color vary per tile within the reference's hue family. Make color changes visible at room scale without creating a checkerboard. Keep within-tile albedo variation finer and weaker than tile-to-tile variation. Keep normal and height amplitudes restrained; some exporters may not honor a shader strength input exactly, so reduce the map's encoded slope when needed.
- For a supplied product swatch, sample tile interiors away from grout, glare, and shadows. Compare the swatch with albedo map values and a rendered proof separately; room lighting and the scene white point can shift the render substantially. Set the requested white point before a final albedo pass, and keep the wall, pan, and floor shape variants on the intended shared material and UV path.
- Use direct image-to-Principled links when the installed OVRTX translator needs them. Bake shade-specific albedo maps when a shader mix does not export reliably. Check image color spaces: sRGB for albedo, Non-Color for roughness, normal and height. A connected node graph is evidence of authoring, not proof of rendered appearance.
- Inspect the exported USD shader when a tile stays mottled after Blender-side material changes. In this project, `ShaderNodeBump` sent a grayscale height image to the exported `normal` input, producing dirty false-normal shading. Connect the tangent normal image through `ShaderNodeNormalMap` directly to Principled Normal; keep the height map as a reference channel until its export path is verified. Save locally and clean-reopen Blender before assessing a shader fix, because a live OVRTX preview may reuse an older USD material graph.
- Check the normal image's numeric channel range as well as its thumbnail. The USD export keeps tangent normal pixels but can drop Blender's Normal Map Strength input; encode the desired restrained slope in the map and use Strength 1.0 in Blender for matching previews. Inspect USD `normal` for the tangent texture with 2× scale and −1 bias, `roughness` for the grayscale map, and `clearcoat` for the coat map. Compare macro renders under the same light; a correct connection does not guarantee visible variation if a map is nearly uniform or its details are below a screen pixel.
- Give each color block its own physical grout material when the exporter does not preserve a shader mask. Preserve clean tile edges, plausible recessed joints and the intended gloss or matte response. Source marker geometry should determine coverage without appearing in the rendered result.

## Review and handoff

Use one representative low-resolution room proof for seams and color balance, and a tight tile close-up for grain. Inspect the actual images before claiming a fix. Keep diagnostic renders and full-resolution PBR contact sheets in the project's diagnostic or scratch paths. Save local Blender iterations as authorized by the user; publish to OVStorage only on an explicit user command. Record the observed cause and the specific source change in `HANDOFF.md` so the next iteration does not repeat the diagnosis.
