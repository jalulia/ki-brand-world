# Ki Social · Phase One — build kit

Regenerates the whole Phase-One social set + presentation.

- `build_social.py` — renders the 22 standard posts (SKU/RTB/brand) as HTML, then headless-render → 1080/.
  Product posts = flavour landscape + `KI_NEW_UK_*_01` puck + subtle flavour-kanji tag. No invented copy.
- `social.css` — the post type system. Display = Obviously **Medium**, Site Gold #B88448 (per uk.ki.bio type sheet).
- The range triptych is a `multi.jpg` 3240×1080 panorama sliced into 3 grid-continuous squares + 3 stories.
- `build_deck.py` — the self-contained interactive HTML deck (IG mockups + copy).
- `build_slides.py` — shared slide spec → `slides.json` (native) + `slides.html` (crisp PDF).
- `build_pptx.mjs` — PptxGenJS native rebuild from `slides.json` (real text boxes + placed images).

Fonts to install to edit/present the PPTX natively: **Obviously** (Regular, Medium, SemiBold).
Render pipeline: headless Chromium (arm64) — see the outputs `_render/` helpers.
