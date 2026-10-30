# Compose relief on the intended interface

Read when several generated/procedural fields describe one physical surface, or
coverage boundaries should create measurable relief. Keep the accepted source
morphology and map contracts authoritative; this branch supplies coherent normal
response, not invented damage or extra layers.

## Decide whether the mask changes height

Give each mask a meaning before using it in geometry: pigment partition, optical
coverage, particle population, or a finite height/thickness transition. Pigment or
optical coverage alone does not imply a step. A blend of scattering populations is
not automatically a blend of heights. Route that ambiguity to architecture.

For a real height contribution, state its reference plane, sign, amplitude, edge
profile, coordinate domain and affected interface. For a coverage mask m and height
h above that plane, the chosen construction H = m h has the derivative

`gradient(H) = m gradient(h) + h gradient(m)`.

This follows from the product rule. Multiplying only the already-derived slopes
by m omits the boundary term. A constant positive h can therefore produce a flat
interior and a sloped transition even though gradient(h) is zero. Conversely,
adding an arbitrary offset to h before masking changes the implied edge step;
height zero is a physical reference in this construction, not cosmetic contrast.
Do not add a step where the source supports only a color/roughness boundary.

An ideal hard mask has a discontinuity, not a finite bump slope. Choose a justified
finite edge width or supported geometric boundary and sample it adequately. An
imagegen antialiasing ramp is not a recovered physical bevel. Inspect the scalar
profile and the resulting slope; clamping an extreme normal is not evidence that
the intended edge is represented.

## Compose compatible fields before perturbing the interface

Keep height amplitudes and derivatives in a shared physical metric. Texture-axis
slopes must account for the physical distance along each axis and the actual
mapping transform. Refer to [coordinate transfer](../../image-material-spatial-design/references/coordinate-transfer.md)
for projection, basis and handedness; a rotation or nonuniform scale changes the
meaning of the derivatives.

For contributions representing the same height surface, combine accepted heights
then derive its slope, or combine compatible surface gradients relative to the
same reference surface/frame through a supported implementation. Form that
interface's shading normal once. Do not add encoded RGB normals, normalize each
contribution as though it were a new base surface, or apply the same height band
again as bump after it already moved the geometry. Independent particle normals
or multiple scattering populations need their declared representation, not forced
conversion into a continuous height field.

Keep the substrate and outer interface distinct. A conformal layer may inherit
relief; a filling/smoothing layer needs its own height hypothesis and residual
detail. Shared coverage does not require identical normals. Preserve the selected
normal-only or geometry-based representation: deriving height for normals does
not authorize displacement or changes to the user's benchmark.

## Use a small control before the full layered graph

If masked relief is consequential or suspect, test a constant-height patch with a
finite coverage ramp at known scale. Check that the interior remains flat and the
boundary has the predicted sign/width. Add one directional height variation only
when needed to test both terms. Inspect the actual numeric profile and native
neutral-color/reflection response with pigment disabled; reuse existing evidence
when sufficient. These are synthetic controls, not source-detail recovery.

Use [the detail pilot](../../image-material-detail-pilot/SKILL.md) for the source,
field and native acceptance decision. Preserve per-interface ownership and the
operations tested. Return missing or wrongly shaped fields to generation; route
wrong slopes/basis to conversion or assembly. A convincing edge highlight alone
cannot prove either correct geometry or source fidelity.

Public technical background: [Mikkelsen, Surface Gradient-Based Bump Mapping Framework](https://jcgt.org/published/0009/03/04/).
The product-rule example above is a mathematical construction; it does not imply
that an installed MaterialX node automatically implements this entire workflow.
