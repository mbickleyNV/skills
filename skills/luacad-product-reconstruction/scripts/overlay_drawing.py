#!/usr/bin/env python3
"""Overlay an orthographic projection of named 3MF meshes on a drawing view.

Requires Pillow. Coordinates and registration are supplied by the caller from
dimension lines and a common physical datum; this never guesses image scale.
"""
import argparse
from pathlib import Path
from xml.etree import ElementTree as ET
from zipfile import ZipFile

from PIL import Image, ImageChops, ImageDraw, ImageFilter

NS = {"m": "http://schemas.microsoft.com/3dmanufacturing/core/2015/02"}
AXES = {"x": (0, 1), "-x": (0, -1), "y": (1, 1), "-y": (1, -1),
        "z": (2, 1), "-z": (2, -1)}


def parse_args():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("mesh", type=Path, help="named 3MF export")
    p.add_argument("drawing", type=Path, help="manufacturer drawing image")
    p.add_argument("output_prefix", type=Path, help="writes PREFIX-overlay.png and PREFIX-cad.png")
    p.add_argument("--u-axis", choices=AXES, required=True, help="mesh axis toward drawing right")
    p.add_argument("--v-axis", choices=AXES, required=True, help="mesh axis toward drawing down")
    p.add_argument("--u-zero", type=float, required=True, help="mesh U value at drawing pixel-x")
    p.add_argument("--v-zero", type=float, required=True, help="mesh V value at drawing pixel-y")
    p.add_argument("--pixel-x", type=float, required=True)
    p.add_argument("--pixel-y", type=float, required=True)
    p.add_argument("--px-per-mm-u", type=float, required=True)
    p.add_argument("--px-per-mm-v", type=float, required=True)
    p.add_argument("--crop", type=int, nargs=4, metavar=("L", "T", "R", "B"))
    p.add_argument("--object", action="append", dest="objects", help="include only these named objects")
    return p.parse_args()


def main():
    a = parse_args()
    ui, us = AXES[a.u_axis]
    vi, vs = AXES[a.v_axis]
    if ui == vi:
        raise SystemExit("U and V must use different mesh axes")
    if a.px_per_mm_u <= 0 or a.px_per_mm_v <= 0:
        raise SystemExit("pixel scales must be positive")
    drawing = Image.open(a.drawing).convert("RGBA")
    mask = Image.new("L", drawing.size, 0)
    draw = ImageDraw.Draw(mask)
    selected = set(a.objects or [])
    found = set()
    with ZipFile(a.mesh) as archive:
        model_name = next(n for n in archive.namelist() if n.endswith(".model"))
        root = ET.fromstring(archive.read(model_name))
    unit = root.get("unit", "millimeter")
    if unit != "millimeter":
        raise SystemExit(f"3MF unit is {unit!r}; convert dimensions to millimetres first")
    build = root.find("m:build", NS)
    if build is None:
        raise SystemExit("3MF build items are missing")
    items = build.findall("m:item", NS)
    built_ids = set()
    for item in items:
        transform = item.get("transform")
        if transform and [float(x) for x in transform.split()] != [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]:
            raise SystemExit("nonidentity 3MF build transform; bake or apply it before overlay")
        built_ids.add(item.get("objectid"))
    for obj in root.findall(".//m:object", NS):
        if obj.get("id") not in built_ids:
            continue
        if obj.find("m:components", NS) is not None:
            raise SystemExit("component assembly found; flatten it before overlay")
        name = obj.get("name")
        if selected and name not in selected:
            continue
        verts = [tuple(float(v.get(k)) for k in ("x", "y", "z"))
                 for v in obj.findall(".//m:vertex", NS)]
        if not verts:
            continue
        found.add(name)
        points = [(a.pixel_x + (v[ui] * us - a.u_zero) * a.px_per_mm_u,
                   a.pixel_y + (v[vi] * vs - a.v_zero) * a.px_per_mm_v)
                  for v in verts]
        for tri in obj.findall(".//m:triangle", NS):
            draw.polygon([points[int(tri.get(k))] for k in ("v1", "v2", "v3")], fill=255)
    if not found or selected - found:
        raise SystemExit(f"no matching 3MF meshes; found {sorted(found)}, missing {sorted(selected - found)}")
    if mask.getbbox() is None:
        raise SystemExit("projected mesh misses the drawing; check axis signs and datum")
    if a.crop and mask.crop(tuple(a.crop)).getbbox() is None:
        raise SystemExit("projected mesh misses the crop; check pixel registration")
    cad = Image.new("RGBA", drawing.size, "white")
    cad.paste((70, 172, 218, 255), mask=mask)
    inner = mask.filter(ImageFilter.MinFilter(5))
    edge = ImageChops.subtract(mask, inner)
    red = Image.new("RGBA", drawing.size, (224, 48, 28, 0))
    red.putalpha(edge)
    cad = Image.alpha_composite(cad, red)
    tint = Image.new("RGBA", drawing.size, (0, 150, 208, 0))
    tint.putalpha(mask.point(lambda value: int(value * 0.28)))
    overlay = Image.alpha_composite(drawing, tint)
    overlay = Image.alpha_composite(overlay, red)
    if a.crop:
        cad = cad.crop(tuple(a.crop))
        overlay = overlay.crop(tuple(a.crop))
    a.output_prefix.parent.mkdir(parents=True, exist_ok=True)
    cad.convert("RGB").save(str(a.output_prefix) + "-cad.png")
    overlay.convert("RGB").save(str(a.output_prefix) + "-overlay.png")
    print(f"Projected {len(found)} named object(s); overlay: {a.output_prefix}-overlay.png")


if __name__ == "__main__":
    main()
