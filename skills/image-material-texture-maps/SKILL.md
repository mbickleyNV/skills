---
name: image-material-texture-maps
description: Analyze reference images and lobe studies to choose, prompt, generate, and inspect spatially coordinated material texture maps. Use when converting appearance hypotheses into explicit channel contracts for shader assembly.
---

# Image Material · 4 · Derive coordinated texture maps

Read the case analysis, lobe-study reviews, and [shared handoff](../image-material-analyze/references/handoff.md). Inspect the images. Preserve uncertainty when a generated study merely illustrates an assumption. A lit lobe image is not a texture property map; do not connect it directly to a shader socket.

For a prompts-only or planning request, work from the available reference and hypotheses even if no lobe studies exist. Produce provisional channel contracts and executable prompts; identify missing inputs and mark generation, numeric inspection, and alignment checks not run. Do not require upstream images that have not been requested or claim to inspect them.

For defining resolved texture, the [detail pilot](../image-material-detail-pilot/SKILL.md)
owns the early source/field/native acceptance decision. Generate only the fields
needed for that experiment before expanding the full set. Reuse its accepted
revisions and rerun affected checks after layout or numeric conversions change.

## Decide the channels before generating

Use the [architecture](../image-material-architecture/SKILL.md) input audit and representation plan. Every active spatial property must reach a channel contract or an explicit limitation; constants need a reason, not a placeholder map.

For each supported surface feature, ask: what physical property varies, on which layer, at what scale, with what evidence? Choose map, scalar, geometry, or unresolved. Explain why a map is needed. A light-colored scratch need not be higher, rougher, metallic, or a hole; determine these effects separately.

Define one channel contract per chosen property using [map contracts and prompt guidance](references/map-contracts.md). Specify meaning, intended range/units, polarity, layer, coordinate system, storage/encoding, processing, and uncertain values. Use plausible provisional ranges or parameter sweeps when the image cannot determine values. Preserve genuine variation while avoiding precision claims based on appearance alone. Trace each active mechanism to its spatial controls or justified constants, including distinct layers and material regions. Three generic base-color/roughness/normal maps are not a sufficient default for a layered material.

Use [multiscale map quality checks](references/map-quality.md) for high-fidelity work. Allocate texture resolution from the intended closeup, feature size and UV coverage. Separate geometry-scale relief from meso and micro detail before generating; a normal map cannot supply missing silhouettes, deep cavities or view-dependent parallax. Decide which detail belongs to which representation and frequency band.

When that fine structure is identity-defining or has failed in an earlier render, execute [detail reconstruction](references/detail-reconstruction.md), or plan it when the request is planning-only: actual pixel/physical-size checks, selected standalone patches, inspected scalar profiles, and an early native detail pilot. Approve the patch by preserved shape and rendered behavior, not by requested resolution or barely visible grayscale noise.

## Keep components editable and features consistent

Read the [layer architecture](../image-material-analyze/references/layer-architecture.md) for multi-component surfaces. Separate color sources, coverage and scales that require independent control; do not silently collapse the planned stack into one beauty-derived base-color texture. Record component-to-mask relationships and the intended combination operations. A clearcoat plus one composite color map does not constitute independently layered color.

Apply [prompt continuity](../image-material-lobe-prompts/references/prompt-continuity.md) to map generation. Carry source morphology and accepted coordinates separately. Check contours, edge profiles, populations and intentional pigment-versus-relief differences; small centroid errors alone do not establish correct registration. A sharpening revision that changes rounded marks into angular islands fails preservation even if it looks more detailed.

For multiple relief fields or a layer boundary that should have depth, use [relief composition](references/relief-composition.md). Distinguish optical coverage from physical height, preserve the height datum, and compose the affected interface before deriving its final normal.

## Establish one spatial authority

Choose a rectified source patch, user UV atlas, or explicit layout guide as the common coordinate authority. Record the crop/warp, aspect, orientation, coverage, physical scale, tileability, and layout revision. A curved object's photograph is not automatically a flat texture; mark synthesized or unwrapped coverage.

Preserve anchors and semantic masks across all channels. Request controlled edits/derivations from that common guide rather than independent reinterpretations. Shared text or a nominal seed does not prove pixel alignment. Generate channels separately if that avoids contact-sheet labels, borders, or cropping drift.

If alignment fails, re-register or regenerate the affected map using the actual guide. Preserve the transform and recheck every affected feature; do not quietly warp one channel and call it aligned. Request periodic boundaries only when the output should tile; do not invent repetition for a unique decoration.

## Prompt, generate, and inspect

Write a detailed, property-specific prompt using the reference, selected studies, layout authority, and channel contract. Describe what dark/light or RGB values mean, where features occur, which correlations are justified, and which lighting cues must be removed. Use the host image-generation workflow for image generation/editing. Preserve original outputs.

Inspect each map for identity drift, baked shadows/reflections, unwanted relief, clipped or implausible values, labels, borders, seams, and lost fine structure. Then compare maps using overlays or matched crops at multiple feature anchors and scales. Matching dimensions and large seams do not prove aligned grain. Correlation is semantic: color and roughness may differ while boundaries still align. Inspect the intended material closeup, not only a reduced thumbnail.

Generator output is an appearance candidate with unverified numeric calibration. Use supported deterministic tools to inspect encodings and perform documented range conversion, extraction, or physically defined derivations. Do not pretend that requesting 16-bit output produced it or that exporting 8-bit data as 16-bit restored precision. Follow the host image-editing policy; if a needed conversion is unavailable or restricted, report that limitation rather than silently altering pixels.

Prefer deriving a normal map from accepted height with a declared physical scale when the relief hypothesis supports it. If generating a normal directly, verify vector interpretation, handedness, orientation, and feature correspondence; never accept purple coloring alone as correctness. Do not infer height from color luminance without evidence. Avoid counting the same relief twice through displacement and normals.


For varied finish or overly uniform reflection, use [spatial finish fields](references/finish-fields.md). Generate and inspect independent roughness and reflection-strength/coverage fields when supported, rather than deriving all finish from height. Record the final graph ranges, uniform-region intent, layer ownership and the matched native influence checks required before acceptance.

## Handoff

Provide original and processed maps, their contracts, common layout revision, exact prompts and parent images, feature-alignment findings, and remaining uncertainties. Mark maps usable, provisional, or rejected. Route changed physical interpretations back to [analysis](../image-material-analyze/SKILL.md), unresolved appearance questions to [lobe studies](../image-material-lobe-prompts/SKILL.md), and usable map contracts to [assembly](../image-material-assemble/SKILL.md).

When correct detail lands in the wrong regions, or several feature scales share one overloaded mask, use [spatial design](../image-material-spatial-design/SKILL.md). Verify actual output size, bit depth, channel equality and background pedestal before extraction. State the selected scalar channel explicitly when an RGB image is used as data; inspect it before range conversion. Requested resolution and grayscale wording are not encoding guarantees.

For hierarchical strand detail, carry the separate bundle/fiber/aggregate records from [textile construction](../image-material-architecture/references/textile-construction.md) into map prompts. A physically tiny fiber mask cannot stand in for resolved yarn depth or loop packing. Preserve intrinsic data semantics even when lit appearance studies contain richer shading.
