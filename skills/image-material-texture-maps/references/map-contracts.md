# Channel decisions and prompt construction

## Questions per channel

- What physical quantity or coverage does this represent? Which layer owns it?
- What observation supports spatial variation? What should remain constant?
- Which feature IDs affect it, and which do not? Is its mask shared or distinct? What contour/profile must survive, and what intentional offsets are permitted?
- Which independent controls and combination operation in the layer plan will consume this map? Would a composite prevent meaningful editing?
- What do minimum, maximum, and neutral values mean? What are the units and plausible range?
- Is it color, scalar data, vector data, or categorical coverage? What is the actual file encoding and downstream interpretation?
- Does it need precision the generator cannot deliver? Can a smooth scalar field be derived from a mask instead?
- What source coordinates, UV set, UDIM tile, physical scale, and border behavior apply?
- What observation or render will detect a polarity, orientation, or semantic mistake?

## Distinctions that change the map

**Color:** reconstruct intrinsic color as plausibly as evidence allows; remove cast shadows, specular highlights, and camera gradients without erasing real staining. Do not automatically darken cavities in base color. Record the image's encoding rather than assuming every color file is sRGB.

**Roughness:** describe reflection sharpness variation, not brightness. A bright area in the photo may be smooth and reflective. Define white/black convention and later numeric remap. Base and coat may require different roughness fields.

**Height:** specify positive and negative relief, neutral plane, patch size, and amplitude in physical units. A grayscale image alone does not establish height. Cracks may be pigment-only, shallow grooves, or real breaks; preserve that distinction.

**Normals:** declare tangent/object space, axis conventions, flat normal, strength, and relation to accepted relief. Separate normal detail from displacement frequency when both are used. Renormalization cannot repair wrongly oriented features or an incorrect tangent basis.

**Coverage:** identify what is present where. Distinguish layer coverage, material mixture, metalness, transmission, and cutout opacity; one generic “mask” is not interchangeable among them. Edge softness must reflect scale/coverage, not blur used to hide misalignment.

**Direction and volume:** anisotropy direction is not a generic colored pattern. Transmission/absorption depends on geometry and thickness; painted darkening is not evidence of a thickness field. Prefer constants and explicit geometry assumptions until spatial evidence justifies more maps. A transmission-first image contains refracted scenery, later reflection and illumination; none is an intrinsic transmission texture. For bulk color, specify absorption/transmittance at a verified reference distance and test known thicknesses. Do not bake apparent dark bases or bright rims into color/roughness merely because they occur in a generated contribution.

## Map prompt skeleton — instantiate for each chosen channel

“Generate only the [property/layer] map in the exact coordinates of layout image A. Use image B for [surface identity], and study C only for [behavior hypothesis], not its baked lighting. Preserve [anchor features, region boundaries, aspect, scale, orientation]. This map represents [physical meaning]. Encode [polarity/channel convention], with [region-specific relative values and justified variation]. Keep [features] independent of this property because [evidence]. Depict [microstructure distribution] at [relative frequency]. Remove [specific shadows, highlights, perspective cues] while retaining [intrinsic features]. No labels, borders, decorative lighting, or invented motifs. Use [unique/periodic/UV-atlas] coverage and [boundary requirements]. Return [supported output format/size].”

Numeric ranges in the prompt are intent, not proof. Record the actual observed channel statistics and any subsequent remap, for example normalized candidate values mapped to a provisional roughness interval. Keep endpoints tunable in the graph when useful.

## Review output

For each map, save a brief verdict: feature correspondence, physical meaning, encoding/precision, seams, numeric range, and readiness. For the set, name at least one checked shared feature and one intentional independence, when present. Preserve evidence of rejected alignment or semantics so later stages cannot reuse a stale file by accident.
