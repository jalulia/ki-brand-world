# Ki Business Cards

Standalone internal tool for approving and requesting the Japanese renderings used on Ki
business cards — **katakana** for names, **kanji** for titles, each with a one-line explainer.

Open `index.html` in a browser. No build step, no backend.

## What it does
- **+ Add Person** — enter English name, title, phone, email. As you type, the tool suggests the
  katakana name, kanji title, and an explainer note. Every field stays editable.
- **Status** — mark each entry `For review`, `Approved`, or `Draft`; filter and search the list.
- **Export CSV** — UTF-8 (BOM) file with data-merge columns: `Name_EN, Name_JP, Title_EN,
  Title_JP, Phone, Email, Note, Status, Owner`. Feeds straight into InDesign / Word mail-merge.
- **Download PDF** — styled approval sheet (uses the browser print dialog → *Save as PDF*).
  Respects the current filter, so you can print just the Approved set.

Data is saved in the browser (localStorage). Share by exporting the CSV — it is the source of truth.

## Auto-suggest (no API)
Suggestions come from built-in dictionaries, so there's nothing to set up:
- The five approved Ki leaders are seeded with their verified renderings.
- Common first/last names map to standard katakana; unknown names fall back to a phonetic
  transliteration that is flagged for review.
- Titles map to standard corporate kanji (CEO, CRO, "Director of X", "Chief X Officer", etc.).

**Always confirm before print:** each person's own name pronunciation, and a native-speaker
review of kanji titles. Suggestions are a starting point, not sign-off.

## Notes
- Self-contained page; intentionally does **not** link back to the World of Ki portal.
- Fonts (Obviously) and logo are pulled from `../assets/`.
