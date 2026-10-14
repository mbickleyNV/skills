# Execution contract

The coordinator verifies other chats have relinquished live Blender, then passes
`--blender-ownership-confirmed`. This flag records that check; it does not perform
it. The shared `scratch/lighting-presets/active-batch.lock`, active-service check
and live native checks independently prevent captures over occupied rendering.

The product file must be saved and frozen. Identify an explicit collection with
only product geometry and materials, without cameras/lights or outside parent,
constraint or animation dependencies. Units are interpreted as Blender meters;
confirm real-world bounds against the accepted product dimensions before final
capture. The studio is never opened over the house: its scene is appended and
product collection linked. Native timeline captures use one persistent session.
The scene uses the copied accepted compositor and packed LUT, without semantic
mask output. The sequence retains native receipts and images in scratch.

Use the managed Blender-Gym Python environment:

```sh
/home/mbickley/spark-stack/blender-gym/.venv/bin/python \
  blender/tools/render_product_turntable.py \
  --asset /absolute/product.blend --collection ProductCollection \
  --product product-slug --blender-ownership-confirmed \
  --ffmpeg /absolute/installed/ffmpeg
```

If the HTTP MCP control service is unavailable but the existing managed worker
has independently confirmed idle, the coordinator may explicitly select
`--control local-worker`. This uses its existing localhost:9876 endpoint with
the same ownership/lock/native gates; it never starts or restarts a service.
Never switch transport automatically after a lost mutating reply.

Defaults: 1920×1080, 50 frames at 24 FPS (about 2.08 seconds), 256 samples, 65 mm camera,
20-degree elevation and 18% framing padding. Honor explicit alternatives. Check
four angles with `--frames 4 --width 640 --height 360 --samples 16` and a distinct
preview slug. Inspect PNGs and link the evidence, then run the final product slug.
The runner writes `renders/<product-slug>/diagnostic/turntable.mp4`; preview
outputs remain diagnostic. No primary-view promotion is implied.

Durable product findings belong in `docs/specialists/checkpoints/<product>.md`
after coordinator review. The machine checkpoint lives in
`scratch/product-turntable/<product-slug>/checkpoint.json`; intermediates stay in
its `frames/` child. `scratch/product-turntable/ownership.json` prevents an
uncertain interrupted run from being replaced. `--resume` must match all inputs;
verify native receipts rather than launching another sequence. A missing prepare
reply or stopped native job needs explicit reconciliation; do not clear the
reservation simply because a process ended. A new source revision requires
archiving/reconciling the old scratch frames/checkpoint, never mixing revisions.

Template revisions are explicit maintenance tasks. The reproducible CPU-only
builder is `blender/tools/product_turntable_scene.py --build-template` through
the installed Blender binary. It refuses to overwrite the template. It reads the
accepted house compositor, writes only the studio dependency closure and never
renders, opens or saves the live house. Engineering notes record the source
house digest, studio digest, controls, packed assets and actual native validation.

Turntable movies use 50 frames by default. Retain the saved film/color stack, but set Grain Amount, Distortion and Dispersion to zero in the private studio copy. Four-angle previews remain separate. Do not alter an active capture to apply new defaults.

Runner preflights sibling .asset-ready.json (or --asset-receipt) before live access: accepted stage, current asset/source hashes and collection. Legacy assets require stage coordinator-reviewed-asset with explicit review_evidence; no silent bypass. Historical receipts with changed producer/input hashes require reconciliation, not blind recreation.
