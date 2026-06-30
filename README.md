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

## Add a tool to the index

1. Publish the tool — either its own `jalulia.github.io/<repo>`, or drop the file into this repo.
2. In `index.html`, copy a `<a class="row">…</a>` block, point `href` at it, set a thumbnail from
   `assets/img/`, and bump the number + the `N live` count in the header.

That's the whole workflow. When a catalogued tool goes live, it graduates from `CATALOGUE.md` to a row.

## Publish (GitHub Pages)

```bash
git push -u origin main
```

Then on GitHub: **Settings → Pages → Source: `main` / root**. Served at
`https://jalulia.github.io/ki-brand-world/`.

## Local preview

Open `index.html` in a browser — all fonts and images are relative, so it works straight off disk.
