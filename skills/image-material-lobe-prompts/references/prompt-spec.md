# Detailed lobe-study prompt specification

Expand these fields into coherent instructions with actual image-specific content. Include details that constrain the output, not decorative adjectives. Save the final prompt verbatim.

## Prompt structure

**Deliverable and status.** Choose an output type using [transport semantics](transport-semantics.md). Request one approximate appearance study or controlled comparison. Name the physical question and specimen. Explicitly deny calibrated/additive-AOV status for generated radiance.

**Image roles.** Identify the source photograph, selected crop, layout guide, previous accepted output, or rejected output separately. Explain which supplies identity, which supplies coordinates, which fixes benchmark geometry/rig, and which supplies verified native path behavior only. Save the behavior example's source and actual semantics.

**Observed identity.** Describe the surface's distinctive shapes, boundaries, color families, directional patterns, feature frequency, wear distribution, and region relationships. Use normalized anchor positions or an attached guide when spatial fidelity matters. Separate observed features from inferred completion.

**Working physical hypothesis.** Describe the proposed order and behavior of the relevant layers, and what remains uncertain. Translate behavior into visible consequences: highlight continuity, sharpness variation, grazing response, color attenuation, or deformation by surface relief. Do not imply an inferred numerical parameter was measured.

**Controlled presentation.** Specify camera angle/projection, geometry, framing, light shapes/directions, environment, background, and consistent exposure. Prefer a simple diagnostic lighting arrangement when it makes the hypothesis easier to judge. For transmission specify the assumed object thickness and the background seen through it.

**Transport selection or intervention.** For radiance, state target object, first event (or other precise selection), allowed later interactions/endpoints, excluded paths, and expected visible scene structures. Distinguish black unselected output from a physically black/absent background. Never use an unqualified “suppress reflections” for transmission-first: later reflections and refracted light shapes can remain. For ablations, name the one intervention, matched control and causal prediction instead. Absorption is attenuation, not an additive image.

**Semantic falsifiers.** Give a positive and negative visual test tied to the declared scene. For example, a structured background must appear transformed through a transmission study; erasing all highlights is not a valid isolation test. State what a failed test invalidates before the next generation consumes it.

**Preservation constraints.** Compile the relevant [feature and layer constraints](prompt-continuity.md) into concrete language. Fix contour shape, edge/rim profile, population and spacing, pigment-versus-relief relationships, motif placement, scale, boundaries, and coverage relevant to the reference. Name permitted changes explicitly. No new ornament, material category substitution, labels, borders, or unrequested geometry.

**Output and review criterion.** Request the supported size/aspect and separate images when needed. Describe the specific visual question the output should answer. Record unsupported requirements outside the prompt instead of pretending they were satisfied.

## Reusable skeleton — replace all fields before submission

“Create a qualitative [output type] of [specimen]. Image A supplies [source identity]; image B supplies [accepted coordinates/benchmark]; image C supplies [documented path behavior only]. Preserve [concrete features]. The proposed construction is [interfaces/media/regions], with [uncertainty]. Keep [geometry, view, thickness, lights, environment, background, exposure]. Select complete paths whose [first event and target scope]; retain [later interactions, endpoints and resulting structures]; exclude [specific path classes]. [Scene elements] remain physically present even where output is black. Expect [regional behavior]. Change only [allowed interpretation]. Return [output]; this is not a calibrated/additive AOV. Accept only if [positive visual test]; reject if [specific semantic or morphology failure].”

For an ablation, replace the path-selection sentences with the changed parameter/layer, matched control and predicted causal difference. For intrinsic data, use the map skill's channel contract instead; do not request a lit appearance.

## Critique-to-edit pattern

Name the failed observation, explain its effect on the intended test, and ask for the smallest visual change: “The generated band stays painted into the surface instead of behaving like a reflection. Preserve the underlying motif and its coordinates. Remove the fixed pale pigment in that band; depict the band as the reflection of the specified strip light, distorted only by the existing relief.”

If the generator repeats the error, leave the hypothesis unresolved and move that discrimination to controlled rendering. Do not conceal a failed generation with a caption that calls it correct.

## Structured-response prompts

For fibers or flakes, carry the accepted intermediate morphology, projected feature size, orientation and layer ownership into every prompt. State whether an image depicts intrinsic fields, an event-class reflection, or a causal layer-off result. Request angular-response comparisons when fuzz or anisotropy is disputed: same geometry, lights, exposure and body pigment, one named change. A reflection panel must not retain an unchanged diffuse-painted body. A fuzz-off panel can alter both added scattering and substrate attenuation, so it is not an additive fuzz pass. Preserve source motif boundaries while generating structure separately; inspect for invented rope, embossed platelets or oversized glitter before wiring. Use [structured scattering](../../image-material-architecture/references/structured-scattering.md) for physical semantics.
