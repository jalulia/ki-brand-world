# 気 — ki-brand-world

A living index of small Ki experiments — tools, toys, and type. One repo that collates the
little one-off Ki things and links them from a single clean page.

**Live:** https://jalulia.github.io/ki-brand-world/

---

## What's in here

| File | What it is |
|---|---|
| `index.html` | The directory. Type-driven, white, no fuss. Shows **only what's live**. |
| `ki-world.html` | *The World of Ki* — a scrollable artifact world (the first sublink). |
| `assets/` | Self-hosted Obviously fonts + imagery used by the pages. |
| `CATALOGUE.md` | Everything else that *could* move in here, with where it lives + status. |
| `IDEAS.md` | New little tools worth building. |

## How the index works

Intentionally minimal — it lists tools that are actually live, nothing aspirational. Two kinds of rows:

- **↗ external** — hosted in its own repo, e.g. `Ki-Landscapes`, `ki-sell-sheet`.
- **→ internal** — lives in this repo, e.g. `ki-world.html`.

The list is driven by **`data.json`** (`config` + `items`). `index.html` renders the rows from it, so
the public page never needs hand-editing. Numbers and the `N live` count are derived automatically.

## Edit the list (no code)

Add **`#edit`** to the URL and enter the passphrase:

> `https://jalulia.github.io/ki-brand-world/#edit`

The plain link stays a clean read-only list — the editor only appears with `#edit` + the passphrase.
In edit mode you can:

- **Drag** the ⠿ handle to reorder rows.
- **Click any name or subtitle** to edit the text inline.
- **Click a thumbnail** to upload a new image or point to an existing `assets/img/…` path.
- **Link** to set the URL and toggle internal → / external ↗ (a sub-page folder = drop it in the repo, link `my-tool/`).
- **+ Tool / Delete** to add or remove rows.

**Saving** (bottom toolbar):

- If you've added a **GitHub token** in *Settings*, **Save** commits `data.json` (and any uploaded
  images → `assets/img/uploads/`) straight to the repo — live in ~1 min.
- With no token, **Save** downloads an updated `data.json` for you to commit yourself (uploaded
  images ride along embedded inside it).

Token and passphrase notes: the token is stored **only in your browser** (localStorage), never written
into the site. The passphrase is stored **hashed** in `data.json`; change it in *Settings*. Default
passphrase is **`ki-edit-2026`** — change it on first use.

To make a fine-grained GitHub token: GitHub → *Settings → Developer settings → Fine-grained tokens*,
scope it to **`jalulia/ki-brand-world`** with **Contents: Read and write**.

## Publish (GitHub Pages)

```bash
git push -u origin main
```

Then on GitHub: **Settings → Pages → Source: `main` / root**. Served at
`https://jalulia.github.io/ki-brand-world/`.

## Local preview

Open `index.html` in a browser — all fonts and images are relative, so it works straight off disk.
