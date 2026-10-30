# OVRTX light-path adapter

Use the [official LPE documentation](https://nvidia-omniverse.github.io/ovrtx/sensors/cameras/light_path_expressions.html)
and [runnable example](https://nvidia-omniverse.github.io/ovrtx/examples/python_lpes.html)
against the installed version. This reference supplies authoring recipes, not a
runtime implementation or universal native-support certification.

OVRTX documents PathTracing, at most nine LPE RenderVars per product, and raw
floating-point output. Author `sourceType=lpe`, the expression in `sourceName`,
and include the variable in `orderedVars`. Disable radiance caching for complete
path history. Overflow outputs can be ignored: batch the experiment and verify
every requested buffer actually returned. Keep a raw baseline in each batch.

Labels belong to geometry (`primvars:omni:label`, uniform token) or lights
(`omni:label`, uniform token). Verify labels at the actual contributing primitives.
`sample`, `key` and `receiver` below are labels you must author, not magic names.

`G` means rough/glossy; `S` means ideal delta, not every specular input. Volume
events are `VG`. Area `La` and environment `Le` endpoints are documented as
produced; `Lp`, `Lm`, `Lv` parse but are not currently produced. Recheck when the
runtime changes. OpenPBR coat/fuzz/subsurface socket names are not documented
scene-label selectors.

## Compose recipes from the question

These expressions follow the documented grammar. Native verification is
case/version-specific; retain a positive control for newly used families.

| Selection | Expression |
| --- | --- |
| Sample reflective family | `E<R[GS]'sample'>.*L` |
| Direct sample reflection | `E<R[GS]'sample'>L` |
| Sample reflection with later scattering | `E<R[GS]'sample'>.+L` |
| Direct / indirect diffuse reflection | `E<RD'sample'>L` / `E<RD'sample'>.+L` |
| Rough / delta reflection | `E<RG'sample'>.*L` / `E<RS'sample'>.*L` |
| Rough / delta transmission | `E<TG'sample'>.*L` / `E<TS'sample'>.*L` |
| Diffuse transmission | `E<TD'sample'>.*L` |
| Reflection ending at named key | `E<R[GS]'sample'>.*<L'key'>` |
| Reflection ending at environment / area sources | `E<R[GS]'sample'>.*Le` / `E<R[GS]'sample'>.*La` |
| Exactly one later event after reflection | `E<R[GS]'sample'>.L` |
| Two or more later events after reflection | `E<R[GS]'sample'>.{2,}L` |
| Whole-scene directly visible emission | `EL` |
| Whole-scene paths containing volume scattering | `E.*<VG>.*L` |

The last volume expression is not a sample-specific subsurface isolate. Likewise,
direct reflection contains every contributing interface assigned that event bin.
Keep optical-component classification provisional until controlled fixtures test it.

## Conditional path-topology probes

- `E<T[GS]'sample'><T[GS]'sample'>L`: two sample transmission events
  ending at a light. Excludes a lit diffuse background; not the complete glass image.
- `E<T[GS]'sample'><R[GS]'sample'><T[GS]'sample'>.*L`: selected
  T–R–T family. Call it internal reflection only after checking closed geometry
  and which surfaces carry the label.
- `E<RD'receiver'><T[GS]'sample'>+L`: a narrow transmitted-caustic
  family. Requires a labeled receiver and positive-control illumination; excludes
  other caustic families and is not an exhaustive caustics pass.

Test new topology recipes on a known contributor before using a black output as
evidence about the target. Preserve ray-depth, integrator and sampling settings.
The official example's broad caustic shortcut does not replace a scene-specific
path contract. Never infer zero absorption or no subsurface transport from one
empty event bin.

## Built-in AOVs complement LPE selection

Consult the [output inventory](https://nvidia-omniverse.github.io/ovrtx/sensors/cameras/outputs.html)
and [decoding rules](https://nvidia-omniverse.github.io/ovrtx/sensors/cameras/decoding_outputs.html).
Author these as raw outputs, not LPE expressions. A built-in direct-illumination
name is not a guarantee of equivalence to an explicit one-scatter reflective LPE;
compare against that path selection before substituting it. Relevant documented names include
`PtSubsurfaceScattering`, `PtDirectIllumation` (exact spelling),
`PtGlobalIllumination`, `PtReflections`, `PtRefractions`, `PtSelfIllumination`,
`PtPreDenoisedResult`, `PtDiffuseFilter`, `PtReflectionFilter`, `PtRefractionFilter`
and `PtIlluminance`. Choose them for a specific question, not as a blanket export.

Compare `PtWorldNormal` and `BumpNormal` when normal execution is disputed.
The documentation calls the former geometric and the latter shading with bump;
qualify that interpretation on the installed material path before using either as
proof of an executed normal input. With distinct base/coat normals, test flat,
base-normal-only and coat-normal-only controls. Unexpected smoothness or relief
in a buffer is a semantic uncertainty, not permission to swap labels or declare
the material broken. `Roughness` stores its scalar in blue, not luminance;
`DiffuseAlbedo` and `SpecularAlbedo` can assist input diagnosis. Respect actual
buffer types, channel packing and semantic space; normalize UNORM bytes as data
and convert half floats for arithmetic. Do not apply a color transform to normals
or roughness. A single roughness output is not proof of every layered roughness
input; use controlled base/coat fixtures to learn what it represents.

Built-in outputs need the same validation states as LPEs: documented → returned →
positive contribution → controlled semantic behavior. For radiance nonzero tests,
inspect RGB without alpha/coverage. A black SSS output on metal proves neither
lack of support nor correct SSS isolation. Require a positive SSS fixture and
matched subsurface-off control for that claim. These outputs can have different
scope and conventions from a labeled LPE; verify before comparing or combining.
