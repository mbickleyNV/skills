#!/usr/bin/env python3
"""Inventory installed MaterialX inputs; never implies renderer capability."""
import argparse
import json
from pathlib import Path


def inventory(mx, document, nodedef_name):
    definition = document.getNodeDef(nodedef_name)
    if definition is None:
        raise ValueError(f"Node definition not found: {nodedef_name}")
    inputs = []
    for port in definition.getActiveInputs():
        metadata = {key: port.getAttribute(key) for key in (
            "unit", "unittype", "uifolder", "uimin", "uimax", "defaultgeomprop"
        ) if port.hasAttribute(key)}
        inputs.append({
            "name": port.getName(), "type": port.getType(),
            "default": port.getValueString() if port.hasValueString() else None,
            "description": port.getAttribute("doc"),
            "semantic_review": "pending_including_units_in_description",
            "metadata": metadata, "disposition": "unassessed",
            "component_ids": [], "evidence_ids": [], "rationale": "",
            "capability_status": "definition_present_renderer_untested",
            "influence_test": None,
        })
    return {
        "schema": "image-material-input-inventory.v1",
        "materialx_version": mx.__version__,
        "nodedef": definition.getName(), "node": definition.getNodeString(),
        "definition_version": definition.getVersionString(),
        "definition_source": definition.getSourceUri(),
        "interface_role": "unassigned_candidate_or_target",
        "renderer_version": None, "inputs": inputs,
        "limits": [
            "Definition discovery only; no renderer or visual checks executed.",
            "Missing unit metadata does not imply unitless; review descriptions and renderer conventions.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--nodedef", default="ND_open_pbr_surface_surfaceshader")
    parser.add_argument("--library", type=Path, help="Read this definition document instead of installed defaults")
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    try:
        import MaterialX as mx
    except ImportError:
        parser.error("Run this helper in an environment with MaterialX installed.")
    document = mx.createDocument()
    if args.library:
        mx.readFromXmlFile(document, str(args.library))
    else:
        mx.loadLibraries(mx.getDefaultDataLibraryFolders(), mx.getDefaultDataSearchPath(), document)
    try:
        result = inventory(mx, document, args.nodedef)
    except ValueError as exc:
        parser.error(str(exc))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    # Refuse to overwrite a case inventory containing human/agent decisions.
    with args.output.open("x") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(f"Inventoried {len(result['inputs'])} inputs; renderer support remains untested.")


if __name__ == "__main__":
    main()
