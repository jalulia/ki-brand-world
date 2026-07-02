# Ki · Emails

A World of Ki tool: the WooCommerce transactional email suite for ki.bio — library, mockups & handoff.
**Copy source:** "Ki — Website review · Emails" deck (June 2026). **Design:** sell-sheet register (Ki_SellSheet_StyleGuide V0.2 palette/type) on a 600px table-based email shell.

## What it does
- **Library** — every email from the review deck, organized by the customer's actual journey
  (Account → Order lifecycle → Service → Admin → Open decisions), with live scaled previews
  and status per deck decision: designed · no change · cut · open question.
- **Mockups** — click any email: full-size render, Typographic ⇄ Landscape header toggle
  (each email has its own assigned brand-world painting), "show template areas" outlines
  every `{placeholder}` region with its Woo mapping.
- **Handoff (Woo, two layers)** — top-right **⬇ Woo handoff bundle** downloads a zip:
  - `html/typographic/` + `html/landscape/` — standalone table-based HTML per email, `{placeholders}` intact
  - `php/email-header.php` + `php/email-footer.php` — the shared wrapper as Woo template overrides
  - `strings.json` — per-email subject / heading / body copy for a settings-level pass
  - `assets/` — the real brand binaries used (crest, logos, landscape bands, tin renders)
  - `README.md` — build notes incl. the cancelled/failed customer-email caveat (Woo core sends those to admin only)
- Per-email downloads + Copy HTML live in the detail rail. Deep links: `#e=completed`;
  standalone mock render: `?mock=completed&v=land`.

## Flags carried from the deck (confirm before build)
- Subjects weren't covered in the deck — Woo defaults shown, marked.
- "Completed" copy reads pre-shipment — confirm trigger mapping.
- Two grammar fixes rendered + flagged (new account "We're looking…", failed "a different payment method").
- `customer_invoice` is cut per deck but doubles as the "pay for this order" email — dev note in-tool.
- POS completed/refunded: open questions, kept as decision cards.

## Structure
```
emails/
  index.html    the whole tool (library, renderer, exports, zip builder)
  assets/       crest.png · logo-black/white.png · land/*.webp (7 painting bands) · pucks/*.webp
                (fonts come from ../assets/fonts/)
```

## Fidelity
Palette/type per the sell-sheet system: paper #FCFBF8 · ink #15110D · body #3B362F ·
mute #706B63 · gold #B88448 · Obviously. Landscape bands cropped from canonical
`Ki Brand/04_Source-Assets/Backgrounds/` (KI_BACK 01·02·04·05·07·08·17). Tin renders =
the marketing-materials pucks (production 3 MG face-on set). Kanji per client-approved set.
