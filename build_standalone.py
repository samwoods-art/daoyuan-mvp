#!/usr/bin/env python3
"""Build a fully self-contained single-file HTML for sharing via Telegram.
Inlines talisman photos + app icons as base64 data URIs and embeds the manifest,
so it works when Eva opens it on her phone (no external asset files needed)."""
import base64, json, re, pathlib

root = pathlib.Path(__file__).parent
html = (root / "index.html").read_text(encoding="utf-8")


def data_uri(path, mime):
    b = (root / path).read_bytes()
    return f"data:{mime};base64," + base64.b64encode(b).decode()


# 1) Inline talisman photos
for i in range(1, 7):
    src = f"assets/master/web/fu_{i}.jpg"
    html = html.replace(src, data_uri(src, "image/jpeg"))

# 2) Inline icons (apple-touch-icon, favicons)
icon_map = {
    "icons/apple-touch-icon.png": "image/png",
    "icons/favicon-32.png": "image/png",
    "icons/icon-192.png": "image/png",
}
for src, mime in icon_map.items():
    html = html.replace(src, data_uri(src, mime))

# 3) Embed manifest with inlined icons as a data: URI so install metadata travels with the file
manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
for ic in manifest["icons"]:
    p = ic["src"]
    mime = "image/png"
    ic["src"] = data_uri(p, mime)
manifest["start_url"] = "."
manifest["scope"] = "."
man_uri = "data:application/manifest+json;base64," + base64.b64encode(
    json.dumps(manifest, ensure_ascii=False).encode("utf-8")
).decode()
html = html.replace('<link rel="manifest" href="manifest.json">',
                    f'<link rel="manifest" href="{man_uri}">')

out = root / "道缘_DaoYuan.html"
out.write_text(html, encoding="utf-8")
print("wrote", out.name, f"{out.stat().st_size//1024} KB")
# sanity: ensure no leftover external asset refs
leftovers = re.findall(r'(assets/master/web/fu_\d|icons/(?:apple-touch|favicon|icon-192))', html)
print("leftover external refs:", len(leftovers))
