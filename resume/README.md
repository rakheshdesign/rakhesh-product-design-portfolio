# Résumé build

Generates the one-page and two-page PDFs from `data.py` (content) and `build.py` (layout in the portfolio design system).

```
python3 resume/build.py                       # writes one.html and two.html
NODE_PATH=$(npm root -g) node resume/render.js   # Playwright -> one.pdf, two.pdf
python3 resume/crop.py one two                # trims page boxes -> one_c.pdf, two_c.pdf  (these are the deliverables)
```

Needs Python with Pillow and pypdf, and Node with Playwright. Fonts are in `fonts/`. The photo is `portrait_c2.jpg`.
`mkportrait.py` rebuilds the photo (needs the original Collaboration photo, kept privately, and a cut-out made with rembg `isnet-general-use`).

Content edits go in `data.py` (bullets, stats, skills) and `build.py` (tagline, layout). Keep the honesty rules in `docs/working-with-rakhesh.md`.
To publish: copy `two_c.pdf` over `RK-Product_Designer.pdf` at the repo root, commit, push (only when Rakhesh says "push live").
