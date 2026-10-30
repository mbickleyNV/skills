# Controlled contact-sheet exploration

Use contact sheets to obtain several informative swings per generation. Choose panel count by the discrimination needed. For complex transmission/reflection, begin with full-resolution contributions or a matched two-panel study grounded in actual path behavior; use 2×3/3×3 exploration only when each cell remains legible. Split unrelated questions across sheets. More cells do not compensate for tiny unreadable detail.

## Design the experiment before prompting

Create a cell manifest: stable cell ID and row/column; hypothesis/mechanism IDs; changed variable; locked variables; predicted visual distinction; reference crop; acceptance question. Store it outside the pixels. Ask for fixed cell order and no text over the surface; add external captions with supported tools if needed. Verify actual panel order and content after generation instead of trusting labels.

Useful sheet types, selected by the evidence:

- **Interpretations:** rows are competing physical models, columns a shared beauty plus diagnostic responses. For example, surface reflection over pigment versus a continuous coat over rough substrate. A whole-model comparison intentionally changes several coupled properties; document this separately from single-variable tests.
- **Mechanism coverage:** path-selected body/reflection/transmission studies, or separately identified layer/fiber controls, on the same declared specimen. Give each radiance cell a [transport contract](transport-semantics.md). Put absorption in matched clear/absorbing controls; never imply that all cells are additive components. Do not invent unsupported mechanisms to fill a grid.
- **Response brackets:** columns vary one uncertain property such as roughness, anisotropy, coating coverage or relief amplitude; rows hold a controlled light/view condition. Use low/middle/high qualitative behavior, with provisional numerical brackets only when useful. Generator labels are not measured shader values.
- **Scale and interfaces:** matched closeups of grain, pores, scratches, layer edges, grooves and wear. Distinguish changed feature frequency from changed depth. Test the interaction of macro geometry with fine normals. Where morphology is uncertain, bracket contour/profile or population while holding depth, pigment and lighting fixed; do not change all of them in a single cell.

Choose enough sheets to cover active mechanisms and unresolved defining features. For high-fidelity work, expect broad exploration followed by focused refinement and inspection; do not use one sheet as an automatic completion quota. Reuse accepted cells as references to keep later rounds coherent. A sheet that ignores its controls is a failed experiment, not six successful studies.

## Prompt a complete sheet

Combine the [prompt specification](prompt-spec.md) with explicit cell instructions. State:

1. The role of each attachment: source identity, spatial authority, evaluation specimen, previous candidate, or lighting reference.
2. A common specimen with fixed geometry/thickness, camera, feature coordinates, grain scale, light shapes/positions, environment, background and display/exposure intent. Keep a user-locked benchmark unchanged across trials. A separate diagnostic rig can expose a particular behavior; label its intervention and do not substitute it for the benchmark.
3. The grid and cell order. Describe each cell's output type, physical hypothesis, selected and excluded paths with retained later interactions (or ablation intervention), and exactly what varies. Preserve everything else.
4. Expected regional behavior: highlight shape, attenuation, layer continuity, coverage boundaries, shadow/parallax cues, and angular response. Explain the uncertain alternative rather than just naming a material class.
5. What to exclude: new motifs, changed geometry, painted highlights, text on surfaces, unrelated camera changes and arbitrary exposure normalization.
6. The comparison question and required inspection scale.

The generator may fail to honor these controls. Record deviations; “same lighting” in a prompt is intent, not proof. Do not calculate physical or pixel deltas from uncalibrated generated cells.

## Review and take the next swing

Inspect all cells individually and against the source. Record whether each is recognizable, internally plausible, distinct in the intended way, and usable for its question. Select by evidence, not by which looks most dramatic. Record acceptance by purpose: a cell may inform roughness while failing shape preservation, and therefore cannot supply downstream layout. Refine contradictions through targeted edits or a better-controlled sheet. If source color is muted but a generated reflection is spectacularly glossy, do not tune the real material to the hallucinated gloss.

Regenerate selected studies individually at adequate resolution with their identity/layout references attached. Contact-sheet cells are exploration assets; do not enlarge tiny cells into final textures. Reinspect the enlarged result for changed interpretation. Map prompts may use a contact sheet to explore candidate property structure, but production maps must have clean boundaries and a shared spatial authority, with no labels, gutters, or unexplained cell crops.

## When generated isolation keeps failing

After a meaningful targeted retry still copies beauty shading, pigment or background into an incompatible isolate, preserve the failed cells and state the specific semantic defect. Keep the useful morphology or angular hypothesis separate from the rejected path claim. Route the disputed mechanism to a native ablation or verified path selection. Do not keep altering the physical shader to match an invalid imagegen isolate, and do not silently omit the failed study from the coverage ledger.
