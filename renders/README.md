# Render Sheet — live render library

Chris's one-pager render spec, turned into a living tool. One sheet per UK flavor
(+ a Full Line tab for group angles); every slot shows the latest render and lists
every uploaded format as a download chip.

## How it works
- **Layout** follows the `Ø — Render Sheet · One Pager` spec exactly: 01 VIEWS ·
  02 CONSTRUCTION · 03 ARTWORK · 04 SPEC, plus 05 LIBRARY for extras and
  06 WORLD (landscape brand world) at the foot of each flavour sheet.
- **Single-puck shots** live in their own flavour tab. The former "Solo tilts"
  row on Full Line is gone — each single-puck tilt now sits in that flavour's
  05 LIBRARY row (`Solo tilt`). Full Line keeps only the multi-flavour group angles.
- **World / Universe.** Every flavour ends with its landscape world
  (`worlds/<flavor>.jpg`, shown from `previews/worlds/*.webp`, downloadable as
  full JPG). Full Line's 02 UNIVERSE gathers all five worlds — tap any tile to
  jump to that flavour — with a slot reserved for the full-line hero sky shot.
  Tokyo Cola's world has two reserved slots for the floating-tin sky shots
  (blue-camo + red) — drop the hi-res files in to fill them.
- **Files live in the IMPØSSIBLE shared drive** — `01_Projects/Ki/3. Creative/
  2. Packaging/Ki Render Sheet/UK/<Flavor>/<Slot>/`. Everyone at
  impossibleoutcomes.co can upload (`everyone@` = writer); the whole domain can
  download. Interim home until Impossible stands up their own Supabase; the page
  reads `manifest.json`, so swapping backends later only means regenerating it.
- **Previews** (`previews/*.webp`, ~60 KB each) are committed here so slots render
  instantly and perfectly; chips download the hi-res originals from Drive.
- **Browse / download**: open to anyone with the page. Each slot: format chips
  (`PNG 3MG`, `PDF SLEEVE 9MG`, …) + `ALL FILES ↗` into the Drive folder.
- **Upload**: unlock **Manage** (footer, same passphrase as the index edit mode) →
  every slot gets `UPLOAD ↗` into its Drive folder + a `LIVE VIEW` embed that shows
  new files the moment they land. Real write-control = Drive share permissions.

## Refreshing the manifest (after new uploads)
New files appear immediately in each slot's LIVE view. To promote them to
first-class chips, rebuild `manifest.json`: ask Claude to "refresh the render
sheet" — it re-harvests file IDs through the Drive connector (the shared drive
isn't synced to this Mac, so the old xattr builder in `_build/` only applies to
locally-synced trees) and pushes the updated manifest.

## Sources
- Renders: `_Master Ki Brand/05_Product_Renders/UK/` (+ `/Angles`)
- Label flats: `_Master Ki Brand/04_Packaging_Mechanicals/UK_Labels_{3,9}MG/`
- Spec: `Ø — Render Sheet · One Pager.pdf` (Chris, 070226, V2 identity)
