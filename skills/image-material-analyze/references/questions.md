# Evidence questions

Use only questions that can affect the reconstruction. Each answer should name its evidence, uncertainty, and practical consequence. Treat the following as prompts for examination, not a user questionnaire.

## Observation and confounders

- What surface is being reconstructed, and how much is actually visible? Are reflections showing another object or environment?
- Is the reference a photograph, render, scan, illustration, or unknown? Could processing or artistic stylization explain a cue?
- Which colors persist outside highlights and shadows? Which regions are clipped or too dark to infer color?
- Does perspective permit a planar rectification? If not, what is the proposed UV layout and where will new coverage be invented?
- What real dimension anchors texture frequency? If none is known, what provisional patch size makes the result testable?

## Structure and optical interpretation

- Do boundaries describe pigment, material coverage, wear, cracks, cavities, or geometry intersections? Which features should coincide across maps, and which should be independent?
- Does a mark move with illumination, follow object curvature, interrupt a highlight, or persist in diffuse regions? When only one view exists, which answers remain unknowable?
- Are broad and narrow highlights evidence of two layers, two lights, changing roughness, or curved geometry? What minimal lighting/parameter change distinguishes these?
- Is a bright edge consistent with ordinary Fresnel reflection before adding fuzz? Could apparent translucency be reflected environment light?
- Does a dark region require absorption, pigment, depth, shadow, or a combination? What evidence supports each?
- Is metallic behavior supported by the reflection's color and diffuse response, or only by brightness? Is apparent emission distinguishable from clipping?
- Which structure is above which? Does the top layer bridge a groove or follow it? Should base and coat share normals, have different detail, or remain uncertain?
- What would materially change the answer: a second angle, grazing light, backlighting, a size measurement, or a close crop?

## Representation and test design

- What changes the silhouette or creates parallax and needs geometry/displacement? What can be represented with bump/normal? Are thin-walled and solid-volume models both plausible?
- Which regions vary in a property, and why? Does the evidence justify a map instead of a constant?
- Which features have been invented by the model? Are they acceptable completion of hidden coverage or an unwanted change to observed identity?
- What is the cheapest render that distinguishes the two strongest explanations?
- What visual discrepancy would cause a change in topology, a map revision, a parameter adjustment, or a lighting correction?

## Example of an evidence-linked decision

Observation E1: a pale band crosses a darker region but the image clips its center.
Hypotheses H1/H2: reflection versus pale pigment; confidence unresolved.
Decision: do not bake the clipped band into base color yet. Preserve the underlying region layout and generate competing studies if this feature controls the appearance.
Test T1: vary the light direction in the reconstruction; compare whether the observed kind of band can arise while the color map remains fixed.
Limit: this experiment demonstrates plausibility, not the original object's true composition.
