# Ki · Social

A World of Ki tool: a **gallery** of expertly-composed social assets — posts & stories, shown *in situ* in minimal Instagram mockups. Present from it, download from it. Plus a standalone **PPTX** showcase for presenting.

**Content:** the Phase One social deck (pp. 2–4 — SKU posts, RTB posts, Range shot). **Type:** the uk.ki.bio web voice — **Obviously Regular (400) + Semibold (600) only, never Black**; tight uppercase Semibold display (−0.02em, line-height ~1.0); body Regular 1.6; katakana in Site Gold; white type on imagery. Fonts self-hosted in `assets/fonts/` (Regular + Semibold woff2).

## What it is
- **`index.html` — the gallery.** Each post is self-contained in a minimal IG mockup (avatar · ki.bio · actions · caption). A per-post **Feed ⇄ Story** toggle flips it between the 1:1 feed post and the 9:16 story (in a phone frame). Download both sizes per post; copy caption. Not grouped by size.
- **`Ki_Social_Showcase.pptx` — the deck.** 11 slides (cover + 10 posts), each post presented in situ in a clean mockup with its label, at the deck's feed size. For presenting.

## The assets (10 posts × 2 sizes = 20 PNGs)
- **SKU Posts (5)** — one flavour hero (tin angle `_01`, 3MG) grounded on its own landscape.
- **Reasons to Believe (4)** — *Ingredients* (real Yuzu ingredient still composited on the Yuzu landscape) + three typographic proof points (*Hired a Chef*, *Sweetened by Nature*, *Regular Sized Can* — the last carries the Hokkaido tin). Headlines are Obviously **Semibold**, uppercase, white, tight.
- **Range / Hero (1)** — the whole line cascading across the extended panorama.

Every asset is exactly **1080 × 1080** (feed) and **1080 × 1920** (story). No crests/overlays on the product posts; no dark scrims; stories use the painting's own sky/ground (not a zoom-crop).

## Sourcing
Backgrounds: `KI_BACK` paintings — cola 01 · hokkaido 02 · maple 07 · satsuma 04 · yuzu 05 · panorama 17_Ext. Tins: `KI_NEW_UK_{FLAVOUR}_01`. Yuzu ingredient still: **frame 080** (`SCROLL_KI_01_0080`), chosen from the ingredient-stills Drive folder. Type per the attached `Ki_Website_Typography_Style_Sheet`.

## Drive-swappable
Finals live in the shared **_Social Asset Library** folder (`1hs4Lpmqhat8o0GMu…`). Register a final's file IDs in the `DRIVE` map at the top of `index.html` and that card swaps preview + download to the Drive version automatically.

## Structure
```
social/
  index.html                 the gallery
  Ki_Social_Showcase.pptx    the presentation deck
  assets/library/            full-res PNGs (1080² feed · 1080×1920 story)
  assets/prev/               webp previews for the gallery
  assets/fonts/              Obviously Regular + Semibold woff2
  README.md
```

## Rebuild
Composites: `_social_build/rebuild.py` (SKU/RTB/Range via Pillow) + in-browser comp for the Yuzu ingredient still. Slides: `_social_build/build_slides.py` → headless render → `python-pptx`.
