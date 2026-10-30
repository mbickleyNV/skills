---
name: product-evidence-extractor
description: Extract variant-specific product dimensions, mounting details and specifications from supplied manuals or drawings into a cited evidence packet. Use for documentary extraction before CAD or installation, not product recommendations, inferred modeling or native appearance validation.
---

# Product evidence extractor

## Project adaptation

This is a generalized workflow. Use the active project's source, scene, renderer
and save/publication rules. Names such as `HANDOFF.md`, room XML, specialist
profiles, `blender/tools/`, studio assets and pipeline contracts are integration
examples, not files supplied by this skill. Discover their maintained equivalents
before using them. Only helpers inside this skill directory are bundled. If a
required adapter or asset is absent, report that stage as unavailable and deliver
the supported work; do not invent a command, schema or successful native result.
Use specialist roles only when delegation is authorized and available; otherwise
the coordinator performs the same bounded work. Keep one live Blender owner.


Accept a target product/variant, requested fields, and supplied documents. Reuse
existing accepted evidence when the exact variant and source digest match. Missing
sources or ambiguous variants are explicit unresolved items, not an invitation to
research unrelated products. Only browse for additional sources when the task
calls for research; this extraction workflow can operate entirely offline.

Use `scripts/evidence_packet.py prepare --source manual.pdf --pages 2,4-6
--manufacturer NAME --model MODEL --variant VARIANT --output scratch/packet`
with absolute paths. Repeated `--source` arguments select multiple documents;
page selection applies to each. Omit pages only for short documents or when page
locations are unknown. PDFs require pdftotext; plain UTF-8 text is one page.
Output includes source SHA256s and separate physical PDF page texts. Printed page
labels may differ: record both when useful. Image-only or diagram-heavy pages need
visual inspection; absent text is not evidence that a feature is absent.

Read only relevant pages. Return JSON `product-evidence/1` with:
- `target`: exact manufacturer, model and variant from the source packet.
- `claims`: each has `field`, `value`, `unit` (null for non-numeric facts),
  `applicability` (`exact-variant` or `family`), and `citations` containing
  `source_id`, physical `page`, and a short verbatim `quote`.
- `unresolved`: missing requested fields, conflicting values, uncertain variant
  applicability or details requiring image inspection. Preserve both citations
  for conflicts; do not choose whichever value seems more plausible.

Keep overall dimensions, cutouts, mounting datums and service clearances distinct.
Keep units as published; any conversion must retain the original value/unit and
state its calculation separately. For lights, distinguish lumens, electrical watts,
CCT and beam angle; none automatically determines renderer energy. Do not derive
CAD geometry, installation compliance or renderer appearance from this packet.
Manufacturer statements and retailer statements retain their source identity;
source citation is not a certification of correctness.

Validate with `scripts/evidence_packet.py validate --packet scratch/packet
--claims claims.json`. This checks source freshness, page/quote provenance and
required fields, **not** whether the quoted text proves the interpretation or
variant. A coordinator reviews those meanings before accepting evidence. Do not
promote family claims into exact-variant facts. No Blender calls, scene mutation,
publication or recursive delegation are part of extraction.

For a bounded cheaper-model trial, supply the target, requested fields and packet
paths to an explicitly authorized worker; require the JSON above and unresolved
items. Keep review with the coordinator. Do not change existing specialist model
settings or claim a cheaper model has been qualified without a measured trial.
