# Mechanism coverage and fidelity planning

Inventory the whole surface before spending the generation budget. This is a checklist of questions, not an instruction to enable every effect. Several mechanisms can share a renderer event class; one physical layer can affect several classes.

| Candidate mechanism or structure | Evidence to inspect; useful discrimination |
| --- | --- |
| Body color and diffuse response | Pigment boundaries versus illumination; diffuse shading versus unlit albedo; subsurface alternatives |
| Dielectric or conductor reflection | Neutral/tinted reflections, angle response, exposed regions; distinct base materials rather than an averaged metallic slider |
| Clear or tinted coats, polish, layered films | Highlight families, coverage edges, substrate attenuation, distinct coat/base roughness and normals; layer-on/off comparisons |
| Transmission, refraction, absorption | Background distortion, thickness-dependent color, internal boundaries; assumed thickness and controlled background |
| Subsurface scattering | Soft transport near edges and illuminated thin regions; thickness and backlighting versus surface-only reflection |
| Fuzz, sheen, fibers | Grazing brightening, directional fibers, edge silhouette; grazing views and geometry versus a shader approximation |
| Anisotropy and oriented structure | Directional highlight stretching and local orientation changes; rotate light/view independently of grain |
| Thin-film or other angle-dependent color | Hue changes with view, layer boundaries; compare ordinary pigment and colored-light alternatives; verify renderer support |
| Emission | Persistent brightness and possible light contribution; distinguish reflection, clipping, and fluorescence assumptions |
| Opacity, perforation, mixture coverage | Actual holes versus translucency or dark pigment; spatially distinct material regions and edge filtering |
| Macro/meso/micro relief | Silhouette, parallax, self-shadow, bevels, pits, pores and scratches; distinguish geometry, displacement, bump and normal detail |
| Wear, contamination, inclusions and interfaces | Which properties change together, which stay independent, and how one layer exposes or occludes another |

For each row record an ID, relevant regions/layer, active/uncertain/unsupported status, evidence and counterevidence, expected appearance, planned generated study, and native test. An unsupported row needs a reason; an uncertain row affecting a defining feature needs a discriminating experiment. For active mechanisms, link generated study coverage to native validation. Do not dismiss an ambiguous coat or grazing fiber response simply because it is not captured by a diffuse/glossy pair.

Separately list material regions and layer order, with spatial support and interface behavior. Ask whether a continuous coat smooths substrate relief, whether wear removes it, whether cracks reveal another material, and whether a boundary requires actual depth. Reject invented detail even when attractive.

Define the fidelity target with observable criteria: joint width and depth, grain frequency, reflection width/contrast, color family, translucency at a known thickness, or spatial variation across a coating. Use reference crops and declared scale assumptions. Avoid unsupported numerical quality scores or equating a resolution label with quality. A surface can have only two active optical event classes and still require extensive relief, roughness, coverage, and lighting studies.
