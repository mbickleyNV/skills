---
name: nix-flakes-blender
description: Create, review, and maintain reproducible Nix flake development environments, especially for the local Blender Gym project. Use for flake.nix, flake.lock, dev shells, package pinning, and Nix-based Blender tooling; do not use for general Blender scene work.
---

# Nix Flakes Blender

Use a flake to make development tools reproducible, not to silently take ownership
of the machine. The intended default is a project-local `devShell` that pins tools
for a contributor; an OS configuration, Nix installation, Docker migration, or
service activation requires explicit user direction.

## Start from evidence

Before changing a project, inspect its existing `flake.nix`, `flake.lock`, README,
and build/test entrypoints. Check whether `nix` is installed and whether the host
is Linux/aarch64 when Blender GPU/container work is involved. Do not invent
package attribute names: query the pinned nixpkgs (`nix search` or `nix eval`) or
use the relevant package documentation.

Treat `flake.lock` as a committed compatibility record. Make source changes and
lock-file changes separately understandable. Use `nix flake lock --update-input
<name>` for a deliberate single-input refresh; do not casually run a wholesale
`nix flake update` while editing unrelated work.

## Project environment workflow

For a normal application repository, prefer these outputs:

- `devShells.<system>.default` for developer tools and a shell hook.
- `packages.<system>.default` only when the project itself has a meaningful,
  reproducible build artifact.
- `checks.<system>` for cheap project checks that can run without privileged
  services or GPUs.

Keep the system list explicit; avoid pretending an ARM-only Blender/GPU workflow
supports every platform. Use `nixpkgs.lib.genAttrs` only when the outputs genuinely
work across those systems. Pin `nixpkgs` through the lock file. Keep secrets out
of the flake and retain the existing environment-file mechanism.

Validate in increasing cost/risk order: `nix flake check`, then `nix develop -c`
with the project test or import command. Report evaluation, build, runtime, and
GPU/container failures as distinct layers. Ask before commands that install Nix,
change NixOS/Home Manager, modify Docker state, pull large images, or build Blender.

## Blender Gym constraints

Read [references/blender-gym.md](references/blender-gym.md) before changing the
Blender Gym flake or build workflow. Its native ARM64 Blender image remains the
runtime boundary. A flake should first supply developer tooling such as Python,
formatters, linters, Docker CLI, Git LFS, and optional Nix inspection tools;
it must not claim that it replaces the project’s Dockerfile unless the user asks
for that migration and the aarch64 GPU runtime is verified.

When asked to add a flake now, propose a minimal `nixpkgs`-pinned dev shell, then
write it only with authorization. Preserve existing scripts and invoke them via
`nix develop -c ./scripts/...` after the dev shell checks pass.

## Explain it plainly

Describe a flake as a small, version-pinned contract: `flake.nix` states the
inputs and outputs; `flake.lock` records exact dependency revisions; `nix develop`
enters the declared tool environment. Distinguish that from containers: Nix gives
developers repeatable tools; the Docker image is the current isolated Blender
runtime.
