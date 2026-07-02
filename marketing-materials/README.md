# Ki · Marketing Materials

A World of Ki tool: the sell-sheet library + WYSIWYG editor.
**Live set:** 2026 UK Launch · The Origin Collection — 2 line sheets (Columns / Rows, V08) +
5 individual **front/back trade sheets** (V07: original full-bleed flavour front + rebuilt trade back
with Aroma/Taste, Features & Benefits, spec panel, RRP, dual-strength order codes).

## What it does
- **Library** — every approved document with live previews, filters, and one-click download of the
  print-ready PDFs in `pdf/` (these are the exact finalised files from `Ki Sell Sheets/`).
- **Editor** — click any text on the sheet to edit (WYSIWYG, per-field size nudge in the right rail),
  click the hero/pucks to replace images, edit codes and the EAN-13 / ITF-14 barcodes re-render live
  (check digits auto-corrected).
- **Versions** — edits autosave as a working copy; “Save version” pins immutable D01, D02… snapshots.
  Officials are never overwritten — “Revert” always returns to the approved state.
- **New documents** — “+ New document” builds from the approved templates with any flavour/strength
  combination (future 1 mg / 6 mg, “Introducing” one-offs, master line sheet). Duplicates work too.
- **Print / PDF** — prints at exact size (Letter, margins None, background graphics ON → Save as PDF).

## Storage & sharing
Edits persist in `localStorage` (`ki-marketing-materials/v1`) — per browser, per machine.
Handoff today: **Export JSON → Import JSON** (single doc or whole workspace).
Planned quickturn for shared saves: a small Supabase table behind the same save/load functions
(`loadStore`/`save` in `index.html` are the only two touch points).

## Structure
```
marketing-materials/
  index.html      the whole app (library, editor, templates, barcode generators)
  assets/         crest.png · hero-1d.jpg · pucks/*.webp   (fonts come from ../assets/fonts/)
  pdf/            the approved print-ready PDFs (source of truth for downloads)
```

## Fidelity lineage
Sheet templates are 1:1 ports of the finalised build pipeline in
`Ki Sell Sheets/UK Launch - July 2026/_build/` (`build_back.py` → line backs V08,
`build_back3.py` + `backdata.py` → individual trade backs V07, `assets.py` → SKU data/copy).
Individual fronts are Julia's original full-bleed design (V07 pages are flattened 300 dpi
rasters, so the editor treats the front as a replaceable image page; the trade back is fully
editable). Palette + type per `Ki_SellSheet_StyleGuide.pdf` (V0.2 · July 2026).
If the canonical sheets change, re-port the geometry and drop the new PDFs into `pdf/`.

## Adding a campaign later (e.g. new market, new strengths)
1. Add products/SKUs to `PRODUCTS` in `index.html` (or extend an existing product's `skus`).
2. Add entries to `OFFICIALS` + drop approved PDFs into `pdf/`.
3. The library groups, filters, previews and “New document” picker follow the data automatically.
