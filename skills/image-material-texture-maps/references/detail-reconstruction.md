# Recover fine detail before assembling the whole material

Use this procedure when small structures define the source's identity or a valid material still looks generic. Select the most consequential unresolved feature families; do not run it ceremonially for every channel. A detailed prompt, a large file, and a connected normal input are not evidence that the detail survived.

## Establish a detail target with observable shape

Choose source crops that show a typical feature, a larger or rarer instance, and adjacent quiet surface. Keep the uncropped context. Inspect at native source resolution; enlargement helps inspection but supplies no new evidence. Separate material structure from photographic noise, compression, blur and sharpened halos. Unresolved source texture remains uncertain, not permission to invent crisp pores.

For each selected family, record in `detail_targets`:

`feature ID | source crop | width/profile and size spread | density/clustering/quiet space | scale basis | property or competing causes | intended hero and closeup visibility | acceptance observation`

Use relative dimensions when absolute size is unknown; label any physical scale assumption. Distinguish the smallest silhouette chip, the typical inclusion, and aggregate grain. Describe the interior and edge of a feature, not only its center or class. A flat white island loses distinctions between a diffuse inclusion, a raised flake, a soft-edged density change and an open pit.

Do not infer low roughness from a bright boundary. Competing causes can include surface reflection, exposed pigment, changed surface orientation, thin-edge internal transport and photographic halos. Carry the unresolved alternatives into a causal test before generating an edge-gloss or edge-color mask. Warm scattering edges are not a universal interpretation either.

## Calculate whether the detail can exist in the output

For a uniform rectangular patch, estimate `feature_texels = actual_image_width * feature_width / patch_width`. Include the occupied UV span for an atlas and check both axes and the relevant region of a curved mesh. Use actual returned dimensions, not the requested dimensions. Record the calculation and assumptions in `sampling_checks`.

For example, a 0.15 mm feature in a 1,254-pixel image covering 100 mm spans about 1.9 texels. Its profile cannot be inspected reliably there. A newly generated 20 mm patch at the same resolution gives about 9.4 texels across it. This is a sampling example, not a universal feature size or acceptance threshold. Detailed contours generally need several samples across their profile; verify sufficiency on the actual feature.

Estimate projected render pixels separately. A feature can be resolved in a texture but subpixel in the hero view. Test it in a closer diagnostic view; at hero distance it may contribute aggregate roughness or color variance rather than visible dots. Do not enlarge or deepen it merely to force visibility. Upscaling a sparse map cannot recover the missing profile.

If resolution is insufficient, generate a smaller physical patch, a higher-resolution selected output, or additional unique atlas/UDIM regions if supported. A new detail patch must preserve physical population density; repeating the original coarse map more often also changes feature sizes, counts and spacing. Separate global gradients and unique landmarks from repeated detail so this correction does not move them. Use repeating patches only for genuinely repeatable structure; localized wear and designed motifs need region-specific coordinates. Inspect seams and repetition after integration.

## Explore morphology separately from optical appearance

Use contact sheets to compare consequential alternatives in profile, size distribution or clustering at the same scale. Keep the material identity, ordinary feature population and quiet regions fixed when testing another variable. A tiny sheet cell can select a direction but cannot certify microstructure. Generate the selected patch as a standalone image at the resolution needed above.

Carry the actual source crop for morphology and the accepted patch for coordinates. A smaller patch is a new spatial authority, not a zoomed claim of exact recovery. Generate related masks and properties from that same authority; preserve per-feature boundaries only where the physics calls for them. A text-only scalar prompt may help eliminate baked lighting, but recheck it against source morphology: cleaner data semantics alone do not make a random dot field faithful.

Describe field structure directly when the generator produces embossed-looking grayscale: which values represent land, feature centers and transitions; which profiles are allowed; which edge pairs or halos would falsify the interpretation. Inspect numerical cross-sections and representative contours before acceptance. Preserve meaningful within-feature variation and partial coverage where evidenced. Do not flatten every inclusion into one class color or distribute identical bumps over the entire surface.

Separate data encoding contrast from physical effect strength. A shallow relief can use a well-resolved numeric range and a small physical amplitude in the shader. Asking for an almost invisible grayscale field can waste precision and erase morphology. Choose encoding ranges from inspected outputs and bit depth, then document the conversion to height or roughness. Wider numeric contrast is not permission to exaggerate physical depth. Do not recover height from shaded appearance by renaming it a data map.

## Make one detail pilot in the native renderer

Before propagating a newly selected feature field across a complex material, test it on a suitable small patch or proxy region. Keep the user's primary shader ball and rig unchanged; add a separately labeled closeup/raking-light diagnostic where needed. Share real feature scale and mapping with the intended material.

Select controls for the disputed cause. Useful examples are neutral-color constant-roughness relief, color-only with flat normals, and the selected field enabled versus disabled. For thin-edge warmth, vary internal transport or thickness while surface finish stays fixed, then vary roughness independently. Some feature families need more than one control; many need only the relevant pair.

Inspect the actual source crop, generated field/profile, and native closeup together. Check both the diagnostic and intended hero view. A larger normal strength is not the first remedy for missing detail: inspect actual resolution, UV density/aspect, profile conversion, amplitude units, tangent basis, representation and filtering first. A silhouette chip or depth-dependent occlusion requires supported geometry/displacement; a normal-only approximation must be labeled.

Use matching sample counts and display settings for quantitative comparisons. If noise obscures the effect, repeat a baseline or increase useful sampling before interpreting the difference. A denoised versus sufficiently sampled raw crop can reveal erased detail or noise mistaken for grain. Do not count noisy side-face speckle as working relief. Qualitative controls with unequal samples remain useful but cannot establish a precise effect magnitude by mean absolute difference alone.

Record `detail_pilots` as `feature | accepted source/field revisions | mapping/scale | changed and fixed variables | native crops/passes | observed shape and visibility | pass/fail/uncertain | earliest loss | next action`. Propagate a passed pilot, or a clearly declared approximation accepted within the requested scope, into the full material. Keep unresolved defining detail visible in the quality decision.

## Diagnose the earliest loss

| Last place the feature was intact | Next action |
| --- | --- |
| Source only | Improve the crop/prompt, patch coverage or generator strategy; more shader nodes cannot restore absent morphology |
| Generated field, lost after extraction/remap | Inspect thresholds, soft edges, feature interior and numeric profiles; preserve the original before revising the conversion |
| Converted map, distorted on proxy | Check UV aspect/density, seam continuity, orientation, geometric sampling and real size |
| Diagnostic render, lost in beauty | Inspect masking, layer attenuation, illumination, display compression, filtering and denoising; do not invent extra grain |
| Closeup only | Determine whether hero-scale aggregation is correct; do not demand subpixel features appear as enlarged marks |

Preserve quiet land, feature populations and previous optical/color findings through each revision. Continue targeted corrections when the defining detail fails and a useful test remains. More generated sheets, more active lobes or a technically valid graph do not compensate for a failed detail target.

## Check filtering of directional detail

When reducing flake or fiber scale makes the surface smooth, inspect texture filtering and projected pixels before increasing normal strength. Averaging opposed normals can remove directional variance without adding the equivalent roughness. Compare adjacent scale brackets under the same light and render resolution; keep a resolved closeup as a separate diagnostic. Record any loss of far-field glitter or anisotropy statistics that the chosen representation cannot retain. A large source texture alone does not establish final-screen detail.
