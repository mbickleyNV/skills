# Structured scattering and detail survival

Use this branch when resolved fibers, flakes, grains, ordered grooves or pile define the material. Complexity comes from the right structures and their coupled responses, not the number of nonzero shader inputs.

## Learn from an actual exemplar

Inspect a relevant downloadable MaterialX/OpenPBR graph and its maps when field morphology and mapping checks leave an unresolved representation or renderer-behavior question. A generic-looking result alone is not a reason to expand into exemplar research. For review-only work, use available evidence and record any new exemplar study as a pending experiment. When research is in scope, inspect the graph and maps, not just a beauty thumbnail. Record the version, license, actual image dimensions/encoding, inherited defaults, connected inputs, UV transforms and shader model. Separate the identity photograph from technical exemplar research. Never call a reconstruction strictly image-only if source material maps or parameters were reused.

For execution requests, render the exemplar on the established benchmark using the installed official runtime; planning-only requests record this control as pending. Inspect diffuse and reflection event sets and at least one disputed mechanism intervention. Preserve original settings in one result; name adaptations separately. A marketing label does not prove that a lobe is active, that normal maps represent true pile, or that the renderer evaluated a connection. External graphs can also contain simplifications and baked lighting.

## Split body, organized structure and unresolved response

Record three conditional scales: the overall motif/coverage, resolved yarn/flake/loop morphology, and subpixel slope or fiber statistics. Do not skip the middle scale by combining a crisp color motif with generic fine noise. Record projected width at the delivery camera. A closeup alone cannot establish hero-view visibility.

For fibers, distinguish body pigment, surface reflection, fuzz particle color/density/angular response, and any transmission or subsurface component supported by the source. Fuzz color need not equal body color. For OpenPBR fuzz, low roughness is fiber-like and grazing; high roughness is more isotropic/dust-like. Do not apply the intuition for ordinary glossy roughness without checking the model. Test weight, color and angular width separately. A lighter fuzz color is a hypothesis to bracket, not a universal recipe.

For ordered yarns or grooves, anisotropy magnitude is not orientation. Record tangent basis, direction field, warp/weft alternation and where competing directions need separate components. A single UV tangent cannot reproduce two crossing populations. For pile, normal maps can produce surface shading but cannot supply visible loose fibers, self-shadowing or silhouette. Route those defining consequences to geometry/displacement on a separate detail proxy while retaining the unchanged benchmark.

For buried metallic flakes, separate platelet orientation/population from the outer coat normal and filtering. Smooth coat plus rough reflective substrate is not by itself a visible sparkle model. Ordinary normal-map mipmapping can average away orientation variance and erase glints. Test at delivery resolution with matched lights, samples and denoising. Where available, use a supported statistical/microflake model or variance-preserving representation. Preserving average normal variance or roughness does not guarantee discrete sparkle. Check that resolved glints survive increased sampling under fixed conditions rather than accepting Monte Carlo speckle; inspect plausible evolution under a small light/view change. Enlarging flakes until visible is an artistic approximation; reject it if source morphology becomes hammered or glittery.

## Test population structure before blaming the shader family

Use [population models](population-models.md) and the
[detail pilot](../../image-material-detail-pilot/SKILL.md) when texture already
looks granular, regular or smooth in a way the source does not. First compare
visible morphology, the numerical meaning of height and actual projection scale.
Do not diagnose an unavoidable normal-map or OpenPBR limitation from a candidate
whose generated field already lost the source structure. Escalate representation
only after that distinction is clear; extra fuzz cannot reconstruct missing yarns.

## Acceptance

Require source crop → field crop → native crop at matching apparent scale, plus a final-size view. Compare combined, structure-disabled and disputed-layer-disabled results under fixed conditions. A tiny delta can mean subpixel filtering, dark layer tint, broad illumination, low coverage or a missing connection; choose a revealing control before declaring the renderer broken. Do not equate an event-class LPE with a uniquely isolated fuzz, coat or metal layer. Record limits when the chosen representation cannot reproduce the source.

Primary references: [OpenPBR specification](https://academysoftwarefoundation.github.io/OpenPBR/), [OpenPBR fuzz angular behavior](https://help.autodesk.com/cloudhelp/ENU/AR-Core/files/ac-shading/ac-surface-shaders/ac-openpbr-surface/arnold_user_guide_ac_openpbr_fuzz_html.html), [NVIDIA downloadable MaterialX/OpenPBR exemplars](https://github.com/NVIDIA-Omniverse/PhysicalAI-SimReady-Materials).
