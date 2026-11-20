<a href="https://github.com/datasciencedynamics/eda_toolkit"><img src="assets/eda_toolkit_logo.svg" width="300" alt="eda_toolkit"></a>

# EDA Toolkit Documentation

Source for the [`eda_toolkit`](https://github.com/datasciencedynamics/eda_toolkit) documentation, published at
**https://datasciencedynamics.com/eda_toolkit_docs/**

The site is built with [Sphinx](https://www.sphinx-doc.org/) and the Read the Docs theme, and versioned with
[sphinx-multiversion](https://github.com/sphinx-contrib/multiversion): every `v0.0.x` tag in this repository
becomes a selectable version on the site, and the root of the site mirrors the latest tag.

## Layout

```
eda_toolkit_docs/
├── source/            # reStructuredText pages and conf.py (edit these)
├── assets/            # logo, figures, and headshots referenced from source/
├── docs/              # built HTML, served by GitHub Pages (do not edit by hand)
│   ├── index.html     # latest version
│   ├── main/          # build of the main branch
│   └── v0.0.*/        # one directory per released version
├── scripts/           # post-build fixes (patch_headshots.py)
├── src/eda_toolkit/   # copy of the library at the documented version
├── requirements.txt   # library and example dependencies
└── requirements_docs.txt
```

## Building locally

```bash
# activate a Python 3.8+ environment first
pip install -r requirements.txt -r requirements_docs.txt

# single version, quick preview
sphinx-build -b html source build/html
# or live-reload while editing
sphinx-autobuild source build/html
```

## Publishing a new version

1. Edit `source/` for the release (version banner in `index.rst` and `getting_started.rst`,
   `release` in `conf.py`, `changelog.rst`, `citations.rst`, any API pages), sync `src/eda_toolkit/`
   with the released library, and commit.
2. Tag the commit and push the tag: `git tag v0.0.X && git push origin v0.0.X`.
   The tag must match `smv_tag_whitelist` in `conf.py`.
3. Build all versions and refresh the root copy:
   ```bash
   sphinx-multiversion source docs
   cp -r docs/v0.0.X/. docs/
   python scripts/patch_headshots.py   # older versions hot-linked photos that no longer exist
   ```
4. Commit `docs/` and push. GitHub Pages redeploys within a few minutes.

## Maintainers

<img align="left" width="120" src="assets/leon_shpaner.jpg" alt="Leonid Shpaner">

[Leonid Shpaner](https://github.com/lshpaner) is a Data Scientist at UCLA Health and an adjunct professor
in the University of San Diego's M.S. in Applied Artificial Intelligence program, where he teaches statistics
and machine learning using Python. He holds a Master of Science in Applied Data Science from the University of
San Diego.

<br clear="left">

<img align="left" width="120" src="assets/oscar_gil.jpg" alt="Oscar Gil">

[Oscar Gil](https://github.com/Oscar-Gil-Data) is a Data Scientist at the University of California, Riverside,
with over ten years of experience in education data management, data warehousing, analytics, and machine
learning. He holds a Master of Science in Applied Data Science from the University of San Diego.

<br clear="left">

## Contributing

Corrections and additions to the documentation are welcome through issues and pull requests on this repository.
Library issues belong in [`eda_toolkit`](https://github.com/datasciencedynamics/eda_toolkit/issues).

## License

MIT. See [LICENSE.md](LICENSE.md).
