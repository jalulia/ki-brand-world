# Render Sheet — live render library

Chris's one-pager render spec, turned into a living tool. One sheet per UK flavor
(+ a Full Line tab for group angles); every slot shows the latest render and lists
every uploaded format as a download chip.

## How it works
- **Layout** follows the `Ø — Render Sheet · One Pager` spec exactly: 01 VIEWS ·
  02 CONSTRUCTION · 03 ARTWORK · 04 SPEC, plus 05 LIBRARY for extras.
- **Files live in Google Drive** — folder `Ki Render Sheet/UK/<Flavor>/<Slot>/`.
  This is the interim home until Impossible Co stands up their own Supabase;
  the page reads `manifest.json`, so swapping the backend later only means
  regenerating the manifest.
- **Previews** (`previews/*.webp`, ~60 KB each) are committed here so slots render
  instantly and perfectly; chips download the hi-res originals from Drive.
- **Browse / download**: open to anyone with the page. Each slot: format chips
  (`PNG 3MG`, `PDF SLEEVE 9MG`, …) + `ALL FILES ↗` into the Drive folder.
- **Upload**: unlock **Manage** (footer, same passphrase as the index edit mode) →
  every slot gets `UPLOAD ↗` into its Drive folder + a `LIVE VIEW` embed that shows
  new files the moment they land. Real write-control = Drive share permissions.

## Refreshing the manifest (after new uploads)
New files appear immediately in each slot's LIVE view. To promote them to
first-class chips, rebuild `manifest.json` — the builder walks the synced Drive
folder and harvests file IDs from DriveFS xattrs (`com.google.drivefs.item-id#S`):

```bash
python3 _build/build_manifest.py   # then commit manifest.json
```

## Sources
- Renders: `_Master Ki Brand/05_Product_Renders/UK/` (+ `/Angles`)
- Label flats: `_Master Ki Brand/04_Packaging_Mechanicals/UK_Labels_{3,9}MG/`
- Spec: `Ø — Render Sheet · One Pager.pdf` (Chris, 070226, V2 identity)
