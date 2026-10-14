# Runtime session and implemented headless routes

Read the relevant section only for an actual connection failure or an explicitly requested implemented headless workflow.

## Implemented headless route

When the user explicitly requests an implemented headless pipeline, use its
documented task-owned launcher and existing environment. For PDF articulation,
start with `product-to-3d/spikes/blender-articulation-handoff/PIPELINE-FAST-PATH.md`.
Preserve saved Blender authoring as the downstream source and use the requested
renderer. This exception does not authorize changes to shared services or
infrastructure, or bypass MCP safe mode inside an interactive session.


## Connection recovery

Separate renderer registration, MCP transport, stale scene translation and actual
render failures. A live process does not prove the renderer is registered. On
`Transport closed`, read the current handoff and inspect the managed MCP service
before retrying a tool call. If that service was intentionally stopped and the
current user has authorized Blender work or restoration, start that existing
managed service; do not launch a second MCP daemon. Confirm it is active. A tool
proxy from before the stop may remain stale even after the service starts. In
that case initialize a fresh session through the project's existing authenticated,
TLS-verified MCP client and call the same safe-mode tools. Never print tokens,
weaken TLS, or change MCP configuration to reconnect. Verify the live scene with
a read-only call before opening or replaying work, and check that no previous
render or script remains active. Preserve unsaved authoring. Treat service state,
client transport and renderer state as separate failure layers.

