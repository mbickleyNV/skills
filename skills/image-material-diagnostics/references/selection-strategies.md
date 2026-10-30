# Select a discriminating diagnostic set

These are conditional routes, not required passes for every material. Select rows
from visible uncertainty and shader construction; omit irrelevant paths with a
reason. Use exact renderer semantics rather than transferring another DCC's AOV names.

| Consequential question | Useful transport observations | Control or fixture that makes them meaningful |
| --- | --- | --- |
| Roughness versus relief versus reflected amount | Direct reflection, individual light contributions, indirect reflection separately | Lock the other fields and light shape; flatten one field at a time; inspect highlight width, displacement and integrated response without automatic normalization |
| Coat versus base interface | Same direct/light-selected reflection before and after coat or coat-normal change | Preserve substrate, compare beauty too; layer removal changes energy reaching the base |
| Fiber sheen versus body tint or normal noise | Direct/indirect diffuse and reflective families, grazing/front lighting and controlled turn | Fuzz weight/color/roughness and tangent controls; classify their observed event bins instead of guessing a fuzz token |
| Yarn depth versus painted/bumped textile | Source-scale neutral relief, body and reflective selections under changed direction | Check actual occlusion, silhouette and parallax on a labeled detail proxy; a surface pass cannot prove missing geometric effects |
| Glass roughness versus lensing or scattering | Rough/delta R/T, background-through-transmission, selected later-event paths and volume where emitted | Known thickness, structured background, interface-normal/roughness controls, clear/absorbing and scatter-disabled pairs |
| Warm thin edges versus polish | Reflective and transmission/diffuse-transmission families, renderer-verified subsurface behavior | Fixed pigment and roughness with thickness/backlight and subsurface controls; empty volume alone does not rule out SSS |
| Flakes, film or crossing directions | Light-selected reflection at multiple angles and delivery-size closeups | Fixed exposure; normal/tangent/population/film interventions; retain quiet regions and distribution as well as visible glints |
| Emission or projected caustics | Camera-visible emission; labeled receiver and selected later transport through target | Known emitter or refractor positive control; receiver-first caustics are not a specimen transmission-first output |

Direct/indirect separates path length classes; it does not identify shader layers.
Depth means scattering-event count, not shell count or physical thickness. A
named-light selection and a direct-light selection overlap unless explicitly
partitioned. A surface normal output can establish orientation but not the radiance
consequence; record whether it shows geometric or perturbed shading normals.

For fine populations, choose a final-size view and a resolved diagnostic crop.
More samples cannot recover missing yarn topology. A high-sample raw control can
reject denoising as the principal cause; then return to morphology, scale or
representation rather than repeatedly raising sample count.

Contact sheets should answer a question. A useful finish sheet might compare
direct key reflection, indirect reflection and the matched direct response with
roughness flattened. A useful textile sheet might compare two light directions
with fuzz enabled/disabled, alongside a neutral detail crop. Describe the retained
paths in every prompt; do not request vague grayscale “roughness lobes.”
