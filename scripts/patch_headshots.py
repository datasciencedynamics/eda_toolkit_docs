"""Replace hot-linked maintainer photos in built docs with the local copies.

Releases before v0.0.31 referenced headshots on external sites that no longer
serve those files. The tagged sources cannot change, and sphinx-multiversion
rebuilds them on every run, so run this after each build:

    python scripts/patch_headshots.py
"""

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
DOCS = ROOT / "docs"

REPLACEMENTS = {
    "https://www.leonshpaner.com/author/leon-shpaner/"
    "avatar_hu48de79c369d5f7d4ff8056a297b2c4c5_1681850_270x270_fill_q90_lanczos_center.jpg":
    "leon_shpaner.jpg",
    "https://oscargildata.com/portfolio_content/images/Oscar_LinkedIn_Pic.jpeg":
    "oscar_gil.jpg",
}


def main() -> None:
    patched = 0
    for page in DOCS.glob("**/contributors.html"):
        html = page.read_text(encoding="utf-8")
        if not any(url in html for url in REPLACEMENTS):
            continue
        images = page.parent / "_images"
        images.mkdir(exist_ok=True)
        for url, name in REPLACEMENTS.items():
            html = html.replace(url, f"_images/{name}")
            shutil.copy2(ASSETS / name, images / name)
        page.write_text(html, encoding="utf-8")
        patched += 1
        print(f"patched {page.relative_to(ROOT)}")
    print(f"{patched} page(s) patched")


if __name__ == "__main__":
    main()
