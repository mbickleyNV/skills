---
name: blender-mcp-workflow
description: Perform Blender scene edits, imports, rendering, animation and media delivery through the host Blender MCP. Use for Blender work; exporter/runtime optimization uses blender-scene-updates.
---

# Blender MCP workflow

Use the existing `blender-gym` MCP and `execute_blender_code` for Blender Python.
One owner controls live Blender. Keep safe mode and existing MCP configuration;
do not start a second daemon. Shell Blender work is limited to an explicitly
requested implemented headless workflow; read
[runtime routes](references/runtime-session.md) for that exception or an actual
connection failure. Preserve unpublished authoring during recovery.

## Work from current state

Follow the project canonical scene, backend, helpers and save/publish contract.
Use the requested engine; OVRTX requests use `OVRTX_EXAMPLE` and the installed
backend. Reuse accepted names and saved geometry. Inspect only relevant objects;
no whole-scene inventory or historical proof replay for an ordinary capture.
Use [scoped inspector](references/scene-inspection.md) and `scripts/inspect_scene.py`
for repeated object/material/bounds queries instead of rebuilding ad hoc code.

Create a task-owned scene for a new product while preserving existing work. Do
not use `read_factory_settings` as cleanup: it can unload the renderer. Safe-mode
rejections do not justify probing forbidden APIs. Batch authoring changes before
one dependency-graph evaluation and renderer refresh. For repeated imports, use
compact stable-ID mesh payloads/digests and preserve existing Object identity.
After opening a scene, inspect it in a subsequent call after context restoration.

For generated geometry/modifiers, read
[evaluated verification](references/evaluated-scene-verification.md). Check the
changed owner and evaluated result, not the whole house. For CAD/finish work,
read [fast iteration](references/fast-iteration.md). For slow exporter/stage updates,
use `blender-scene-updates`; performance auditing is not a routine render step.

## Capture and deliver

Use project capture helpers and persisted native tickets/receipts when present.
Set frame before matching camera, evaluate once, then capture. New composition
needs one cheap preview before final quality; approved existing cameras do not.
Observe completion outside Blender while native preparation owns the controller.
A lost reply is a receipt-recovery problem, not a reason to rerender or restart.
Native image completion and sequence retirement are distinct boundaries.

Inspect the affected image and verify current receipt identity/settings/file.
Do not duplicate receipt checks with a full save/reopen audit. Save durable
changes only when authorized by the project/user. Follow canonical room output
paths; otherwise use the Blender output root. Keep intermediates/proofs in the
project scratch area, replacing current deliverables rather than creating histories.

For Blender 5.1 video use `scene.render.image_settings.media_type = 'VIDEO'` and
`scene.render.ffmpeg`; MP4/MOV/WebM/MKV are supported delivery containers.
For Hermes delivery call `stage_blender_media` with the exact existing media path.
Require matching `sha256`/`sandbox_sha256`, then emit its returned MEDIA value once.
An error is failed delivery. Follow native app artifact display when available.
Do not rerender solely to stage or recover an existing image/video.
