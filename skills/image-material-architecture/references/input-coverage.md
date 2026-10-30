# Cover the installed material interface

Record the MaterialX package version, node definition name/version and library provenance separately from the renderer version. Label the inventory as a candidate interface or the actual selected target. An installed interface from another case does not establish this case's renderer or shader version. Read the input descriptions as well as formal unit attributes: units and special zero-value modes may appear only in prose. Missing unit metadata does not imply unitless. Record unresolved semantics before numeric fitting. Declared, connected, rendered influence and visually accepted are different states. Recheck capabilities when the backend, definition or translation path changes.

Use these families to ask questions, then resolve their actual installed input names. The table is a reasoning guide, not a fixed socket schema.

| Family | Questions that change construction |
| --- | --- |
| Base | Which body colors, diffuse response and conductor/dielectric regions are evidenced? Are diffuse roughness and specular roughness being confused? |
| Specular interface | Which IOR, roughness, anisotropy and tangent orientation explain angular behavior? Is colored reflection physical conductor behavior or an artistic tint? |
| Transmission/volume | Is color from bulk absorption, scattering, or the background? Which depth, phase direction and dispersion controls matter? Is the object solid, hollow or thin-walled? |
| Subsurface | Does internal transport explain edge softness better than surface blur? Which color, distance, channel-dependent scale and directional controls are justified? |
| Coat | Is a separate interface supported? How do coverage, color, IOR, roughness, anisotropy, substrate darkening and separate normal/tangent affect it? |
| Fuzz | Are fine fibers or grazing microstructure visible? Which coverage, color and roughness controls help, and which fibers need geometry? |
| Thin film | Is angle-dependent hue evidenced? Check thickness, IOR, weight and the interface receiving the film; distinguish colored lights or ordinary pigment. |
| Emission | Is self-emission supported? Separate luminance from color and scene exposure. |
| Geometry | What do opacity, thin-walled mode, base/coat normals and tangents mean here? Opacity is not glass transmission; a normal input does not supply actual thickness. |

Per-input record:

`definition/input/type/default | component/feature | disposition | value/map/geometry contract | evidence or inactive rationale | capability status | influence-test ID/result`

Dispositions may be constant, mapped, geometry-controlled, intentionally inactive, uncertain or unavailable. The helper starts everything unassessed. A default value is not a considered decision. Inactive child controls can reference their parent's rationale, but must remain visible in the inventory. Record additional nodes, spatially varying material assignments, volume/geometry controls and renderer limitations outside the surface input list too.

Use focused tests: alter one disputed control under a revealing view/light, inspect its expected response and unintended changes, then restore the candidate. If declared support produces no observable influence, first check binding, scale, branch activation and sampling. Keep an unresolved capability unresolved; do not silently replace a required effect with color paint.

Primary references: [OpenPBR specification](https://academysoftwarefoundation.github.io/OpenPBR/) for the model's structure and [MaterialX OpenPBR definition](https://github.com/AcademySoftwareFoundation/MaterialX/blob/v1.39.5/libraries/bxdf/open_pbr_surface.mtlx) for one versioned interface. Installed definitions remain authoritative for available names; renderer behavior needs its own evidence.
