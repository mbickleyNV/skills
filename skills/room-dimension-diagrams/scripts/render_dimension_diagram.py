#!/usr/bin/env python3
"""Render a sparse axonometric dimension diagram from a small JSON description."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def ft_in(mm: float) -> str:
    eighths = round(mm / 25.4 * 8)
    feet, rem = divmod(eighths, 96)
    inches, frac = divmod(rem, 8)
    fractions = {0: "", 1: "⅛", 2: "¼", 3: "⅜", 4: "½", 5: "⅝", 6: "¾", 7: "⅞"}
    inch_text = f"{inches}{fractions[frac]}″" if inches or frac or not feet else "0″"
    return f"{feet}′-{inch_text}" if feet else inch_text


def font(size: int, bold: bool = False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


class Diagram:
    def __init__(self, cfg):
        self.cfg = cfg
        self.w, self.h = cfg.get("size", [1800, 1300])
        self.im = Image.new("RGB", (self.w, self.h), "white")
        self.d = ImageDraw.Draw(self.im)
        self.origin = tuple(cfg.get("origin", [320, 1040]))
        self.scale = cfg.get("scale", 0.285)
        self.accent = cfg.get("accent", "#087f86")
        self.edge = "#252525"

    def p(self, xyz):
        x, y, z = xyz
        ox, oy = self.origin
        if self.cfg.get("projection") == "ortho_3q":
            # True parallel three-quarter projection: equal X/Y foreshortening,
            # verticals remain vertical, and no perspective convergence is added.
            az = math.radians(self.cfg.get("azimuth_degrees", 30))
            elev = math.radians(self.cfg.get("elevation_degrees", 28))
            u = math.cos(az) * x - math.sin(az) * y
            v = math.sin(elev) * (math.sin(az) * x + math.cos(az) * y) - math.cos(elev) * z
            return (ox + self.scale * u, oy + self.scale * v)
        # Cabinet-friendly oblique projection retained for existing inputs.
        return (ox + self.scale * (x + 0.48 * y), oy - self.scale * (z + 0.28 * y))

    def poly(self, pts, fill, width=3):
        q = [self.p(p) for p in pts]
        self.d.polygon(q, fill=fill)
        self.d.line(q + [q[0]], fill=self.edge, width=width, joint="curve")

    def box(self, b):
        x, y, z = b["at"]
        w, dep, h = b["size"]
        front = [(x, y, z), (x+w, y, z), (x+w, y, z+h), (x, y, z+h)]
        top = [(x, y, z+h), (x+w, y, z+h), (x+w, y+dep, z+h), (x, y+dep, z+h)]
        side = [(x+w, y, z), (x+w, y+dep, z), (x+w, y+dep, z+h), (x+w, y, z+h)]
        self.poly(side, b.get("side", "#d9d5cb"))
        self.poly(top, b.get("top", "#f1eee7"))
        self.poly(front, b.get("front", "#e7e2d8"))
        for seam in b.get("vertical_seams", []):
            a = self.p((x + seam, y-0.5, z)); c = self.p((x + seam, y-0.5, z+h))
            self.d.line([a, c], fill=self.edge, width=2)
        for seam in b.get("horizontal_seams", []):
            a = self.p((x, y-0.5, z+seam)); c = self.p((x+w, y-0.5, z+seam))
            self.d.line([a, c], fill=self.edge, width=2)

    def arrow(self, a, b, size=13):
        self.d.line([a, b], fill=self.accent, width=3)
        ang = math.atan2(b[1]-a[1], b[0]-a[0])
        for p, direction in ((a, ang), (b, ang+math.pi)):
            for delta in (-0.55, 0.55):
                q = (p[0] + size*math.cos(direction+delta), p[1] + size*math.sin(direction+delta))
                self.d.line([p, q], fill=self.accent, width=3)

    def dimension(self, spec):
        a = self.p(spec["a"]); b = self.p(spec["b"])
        dx, dy = spec.get("offset", [0, 0]); aa = (a[0]+dx, a[1]+dy); bb = (b[0]+dx, b[1]+dy)
        self.d.line([a, aa], fill=self.accent, width=2)
        self.d.line([b, bb], fill=self.accent, width=2)
        self.arrow(aa, bb)
        value = spec.get("value_mm")
        label = spec.get("label") or ft_in(value)
        if spec.get("assumption"):
            label += "*"
        angle = math.degrees(math.atan2(bb[1]-aa[1], bb[0]-aa[0]))
        if angle > 90 or angle < -90:
            angle += 180
        f = font(spec.get("font_size", 30), True)
        box = f.getbbox(label); pad = 8
        tile = Image.new("RGBA", (box[2]-box[0]+2*pad, box[3]-box[1]+2*pad), (255,255,255,235))
        td = ImageDraw.Draw(tile); td.text((pad-box[0], pad-box[1]), label, font=f, fill=self.accent)
        tile = tile.rotate(-angle, expand=True, resample=Image.Resampling.BICUBIC)
        mx, my = (aa[0]+bb[0])/2, (aa[1]+bb[1])/2
        self.im.paste(tile, (round(mx-tile.width/2), round(my-tile.height/2)), tile)

    def render(self, out):
        self.d.text((80, 60), self.cfg.get("title", "Dimension diagram"), font=font(44, True), fill=self.edge)
        self.d.text((82, 116), self.cfg.get("subtitle", ""), font=font(24), fill="#666666")
        for b in sorted(self.cfg["boxes"], key=lambda x: x.get("order", 0)):
            self.box(b)
        for dim in self.cfg["dimensions"]:
            self.dimension(dim)
        notes = self.cfg.get("notes", [])
        y = self.h - 56 - 30*len(notes)
        for note in notes:
            self.d.text((80, y), note, font=font(20), fill="#555555")
            y += 30
        self.im.save(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", type=Path)
    ap.add_argument("output", type=Path)
    args = ap.parse_args()
    cfg = json.loads(args.input.read_text())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    Diagram(cfg).render(args.output)


if __name__ == "__main__":
    main()
