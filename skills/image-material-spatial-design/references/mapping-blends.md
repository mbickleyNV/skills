# Diagnose synthesis and projection blending

Read for hex/stochastic tiling, triplanar transfer, doubled detail or mapping blur.
Use [coordinate transfer](coordinate-transfer.md) for frames, normal-basis probes
and geometry preservation. UV seam removal and repetition suppression are separate
jobs: object/surface coordinates address chart boundaries; hex synthesis mixes
source locations to reduce repeated patches. Neither guarantees coherent motifs.

## Decide what may be synthesized

Classify each feature family before selecting mapping. Preserve coherent folds,
weave crossings, long brushing and authored motifs in their own continuous field.
A stochastic local residual may use hex offsets when its identity tolerates sample
mixing. Share tile identity, transforms and compatible weights across correlated
color, roughness, normal and coverage channels. Independent random seeds can make
one feature's color belong to another feature's relief. Avoid random rotations for
direction-bearing detail unless they match the observed orientation distribution;
transform normal gradients and tangent directions with any chosen rotation.

Do not hex-average a whole fold or weave map and then repair the resulting veins,
mottling or crossed grain by increasing normal strength. Route coherent shape to
[deformation morphology](coherent-deformation.md). For directional residuals,
elongated cells and restrained offsets are candidates, not guarantees of continuity.

## Discriminate overlap from optical blur

Use a structured diagnostic with distinct circles, arrows, labels and several
stripe widths at known texel periods. Put it beneath the same declared interface
and retain the original roughness, normals, coat, lighting, exposure and geometry.
Compare UV reference, projection-only, then projection plus stochastic synthesis.
The last two isolate the synthesis addition; UV versus object-space placement is
usually only a qualitative reference. Include a flat-substrate-normal control if
relief distorts the chart, and a coat-off control only if the coating remains a
live competing explanation. A chart is deliberately hostile to stochastic mixing;
it diagnoses duplication and transitions, not production-texture fidelity.

Inspect uncompressed same-scale crops, then the real stochastic texture. Doubled
contours surviving flat substrate normals implicate sampling/blending without
proving every cause of fine-frequency loss. Check minification, derivatives,
filtering, grazing footprint, display resizing and video compression separately.
Keep contour identity, local contrast and effective normal-slope distributions
visible through each stage; average image deltas can hide narrow failed regions.

## Tune the two blends separately

Expose and record projection-weight sharpness, hex-weight sharpness, cell scale
and aspect, random offsets/rotations, and any contrast treatment. Change one stage
at a time where practical. Sharper normalized weights narrow overlap but concentrate
changes into boundaries; exact equal-weight transitions still mix samples. Smaller
cells alter frequency and population as well as repetition. A scalar contrast gain
is not full histogram or variance preservation, and cannot reunify split motifs.

A prior directional-metal trial improved with hex exponent 7 to 24, projection
exponent 8 to 24, and a gain control from identity .5 to .75. These values describe
that implementation and case, not portable defaults. Read the actual weight and
gain equations before using any numeric preset. Test representative stochastic
fields and transition closeups at delivery resolution before selecting a candidate.
Preserve effective ranges and avoid gain-induced clipping or normal amplification.

[Practical Real-Time Hex-Tiling](https://jcgt.org/published/0011/03/05/paper-lowres.pdf)
and its [reference implementation](https://github.com/mmikk/hextile-demo) distinguish
weighted synthesis, sampling gradients and histogram-preserving variants. Adapt
only the needed mechanism; record implementation/version and license if copying code.
For normals, use transformed slopes/gradients in a common frame rather than blending
purple RGB, following [surface gradients](https://jcgt.org/published/0009/03/04/paper.pdf).

## Qualify numerical and temporal behavior

Inspect beauty and every returned relevant AOV/LPE for nonfinite values. A finite
beauty does not clear invalid reflection buffers. Check normalization denominators,
zero-length tangents, exponent-base domains, gain endpoints and identity branches.
An intervention that guards zero bases and bypasses identity gain fixed observed
nonfinite buffers in one implementation; it did not establish the precise derivative
or compiler cause. Qualify the guarded candidate instead of crediting rejected runs.

Check front/back/cap and known blend transitions, then a short continuous rotation
for pops, shimmer, crossed grain and sliding patterns before the final turntable.
Sharpened blends passing stills remain temporally provisional. Compare material
response and morphology separately from exact feature placement, which a changed
mapping need not preserve. Record accepted settings, equations, artifacts, tested
angles/motion and remaining blend defects in `coordinate_transfer`.
