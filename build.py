#!/usr/bin/env python3
"""
build.py — bundle the codelab into a single self-contained file.

Development uses index.html + the content/ folder (loaded at runtime via a local
server). For sharing or publishing as one file, run this: it inlines every step
from content/ straight into the page, so dist/index.html needs no server and no
network.

Usage:
    python3 build.py            # writes dist/index.html
"""

import json
import pathlib
import shutil

ROOT = pathlib.Path(__file__).parent
CONTENT = ROOT / "content"
ASSETS = ROOT / "assets"
OUT = ROOT / "dist"

def main() -> None:
    shell = (ROOT / "index.html").read_text(encoding="utf-8")
    manifest = json.loads((CONTENT / "manifest.json").read_text(encoding="utf-8"))

    sections = []
    for step in manifest:
        html = (CONTENT / step["file"]).read_text(encoding="utf-8").rstrip()
        title = step["title"].replace('"', "&quot;")
        sections.append(f'<section class="page" data-title="{title}">\n{html}\n</section>')
    inlined = "\n\n".join(sections)

    # Drop the pre-built sections into the empty #pages container. boot() sees
    # the .page elements already present and skips fetching content/.
    bundled = shell.replace('<div id="pages"></div>',
                            f'<div id="pages">\n{inlined}\n</div>')

    OUT.mkdir(exist_ok=True)
    (OUT / "index.html").write_text(bundled, encoding="utf-8")

    # Copy assets/ alongside the bundle so image src="assets/..." resolves.
    if ASSETS.exists():
        shutil.copytree(ASSETS, OUT / "assets", dirs_exist_ok=True)

    print(f"✓ Bundled {len(manifest)} steps → {OUT / 'index.html'}")

if __name__ == "__main__":
    main()
