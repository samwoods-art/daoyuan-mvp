#!/usr/bin/env python3
"""Generate 道缘 app icons: a gold taiji (太极) on a deep crimson field with a gold ring.
Drawn at high supersample then downscaled for smooth curves."""
from PIL import Image, ImageDraw
import math

GOLD = (201, 168, 76)
GOLD_LIGHT = (232, 212, 139)
CREAM = (245, 236, 215)
CRIMSON = (139, 26, 26)
CRIMSON_DK = (74, 12, 12)
INK = (28, 20, 16)


def radial_bg(size, inner, outer):
    """Vertical-ish radial gradient background."""
    img = Image.new("RGB", (size, size), outer)
    px = img.load()
    cx = cy = size / 2
    maxd = math.hypot(cx, cy)
    for y in range(size):
        for x in range(size):
            d = math.hypot(x - cx, y - cy) / maxd
            d = min(1.0, d)
            r = int(inner[0] + (outer[0] - inner[0]) * d)
            g = int(inner[1] + (outer[1] - inner[1]) * d)
            b = int(inner[2] + (outer[2] - inner[2]) * d)
            px[x, y] = (r, g, b)
    return img


def draw_taiji(draw, cx, cy, R, light, dark):
    """Classic yin-yang. Light (yang) and dark (yin)."""
    # full circle = light
    draw.ellipse([cx - R, cy - R, cx + R, cy + R], fill=light)
    # right half dark
    draw.pieslice([cx - R, cy - R, cx + R, cy + R], -90, 90, fill=dark)
    # small circles
    r2 = R / 2
    # top small circle: dark (sits in light region)
    draw.ellipse([cx - r2, cy - R, cx + r2, cy], fill=dark)
    # bottom small circle: light (sits in dark region)
    draw.ellipse([cx - r2, cy, cx + r2, cy + R], fill=light)
    # dots
    r3 = R / 7
    draw.ellipse([cx - r3, cy - r2 - r3, cx + r3, cy - r2 + r3], fill=light)
    draw.ellipse([cx - r3, cy + r2 - r3, cx + r3, cy + r2 + r3], fill=dark)


def make(size, maskable=False):
    SS = 4
    S = size * SS
    img = radial_bg(S, CRIMSON, CRIMSON_DK)
    d = ImageDraw.Draw(img)
    cx = cy = S / 2

    # Safe zone: maskable icons need symbol within center ~80%
    ring_outer = S * (0.40 if maskable else 0.46)
    ring_inner = S * (0.355 if maskable else 0.41)
    # Outer decorative gold ring
    d.ellipse([cx - ring_outer, cy - ring_outer, cx + ring_outer, cy + ring_outer], fill=GOLD)
    d.ellipse([cx - ring_inner, cy - ring_inner, cx + ring_inner, cy + ring_inner], fill=INK)

    # Taiji in the middle
    R = ring_inner * 0.80
    draw_taiji(d, cx, cy, R, CREAM, GOLD)

    img = img.resize((size, size), Image.LANCZOS)
    return img


for sz, name, mask in [
    (512, "icon-512.png", False),
    (512, "icon-512-maskable.png", True),
    (192, "icon-192.png", False),
    (192, "icon-192-maskable.png", True),
    (180, "apple-touch-icon.png", False),
    (32, "favicon-32.png", False),
]:
    make(sz, mask).save(f"icons/{name}")
    print("wrote", name)
print("done")
