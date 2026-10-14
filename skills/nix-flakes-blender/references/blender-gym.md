# Blender Gym: Nix integration notes

Repository: `/home/mbickley/spark-stack/blender-gym`.

## Current design

- Python package: Python 3.12 or newer; Hatchling build backend; runtime
  dependencies are FastAPI, MCP, Pydantic, and Uvicorn.
- The project runs a host-owned supervisor and MCP server, with state below
  `BLENDER_GYM_ROOT`.
- The renderer is a separate Docker image built from
  `docker/Dockerfile.blender-arm64`. The build script rejects non-aarch64 hosts,
  and runtime commands use Docker GPU support.
- The Dockerfile builds Blender 5.2.1 from source on ARM64 and deliberately makes
  a minimal runtime image. It is not merely a Python development container.
- Systemd services read `config/blender-gym.env`; do not put its values or tokens
  in a flake or lock file.

## Sensible first flake scope

Supply a developer shell only. It should contain a compatible Python interpreter
and the project’s everyday command-line tools. Add Docker CLI and Git LFS only
when the host workflow needs them and those package attributes exist in the
pinned nixpkgs. Do not add `blender` simply because this is a Blender project:
the tested renderer is the ARM64 Docker image.

Suggested verification after adding a dev shell:

```bash
nix flake check
nix develop -c python --version
nix develop -c python -m pytest
```

Run the Docker smoke test only when Docker, the locally built image, the target
architecture, and GPU access are already available. It is a runtime validation,
not a flake evaluation check.
