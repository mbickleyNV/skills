# Durable room evidence

Reuse existing project XML instead of inventing a parallel authority. The supplied
helper supports the `remodel-inference` layout used by this workflow:

- `sheets/sheet`: stable ID, PDF page and printed label.
- `rooms/room`: ID, plan-page, location bbox and space-separated elevation IDs.
- `interior-elevations/elevation`: ID, evidence-region ID, room IDs, viewing direction.
- `components/component`: ID, room ID, evidence ID, nested dimensions.
- `evidence-regions/region`: ID, image path, page, bbox.
- Optional `elements/element`, `relationships/relation`, `corrections/correction`:
  room attribute permits inclusion in a room packet.

Run:

```
python3 scripts/room_packet.py /path/to/map.xml ROOM_ID \
  --region PLAN_REGION_ID --output /path/to/room-packet.xml
```

The helper selects room-linked elevations/components and their evidence, resolves
image paths relative to the map, includes matching sheet records and preserves
optional room-tagged corrections. Explicit `--region` adds a needed plan inset.
It does not guess a plan-region link from all crops on the same page: that would
reintroduce unrelated images. Missing references are reported. Namespace or schema
variants require a small explicit adapter, not silent field dropping.

For modeling, extend a room packet or keep a linked room-model XML with:

- source digest and crop bounds with coordinate units/origin;
- parameter value, unit, basis, confidence and evidence;
- dependent values expressed as `same-depth-as` or a formula;
- physical element roles, material intent and aperture/enclosure relationships;
- aliases → stable part IDs → controlling parameters/source crop;
- user corrections and unresolved interpretations;
- full-model geometry distinct from preview visibility.

The geometry generator consumes numeric XML values. Crops are visual evidence for
the agent, not input that the LuaCAD parser can interpret. Avoid duplicating numeric
authorities: designate one canonical unit and derive display conversions.

A local revision should require a compact packet, affected image(s), targeted source
edit and one rebuild. Keep raw text/coordinates archived outside routine context.
