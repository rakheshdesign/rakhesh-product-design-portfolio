# CLAUDE.md: Rakhesh Karnati's product design portfolio

Read this first. It is the map; the details are in `docs/`. Keep it current (see "Keep this alive").

## What this is
- Rakhesh Karnati's Product Designer portfolio: live at https://rakhesh-design.vercel.app, repo `rakheshdesign/rakhesh-product-design-portfolio` (branch `main`, auto-deploys to Vercel project `rakhesh-design`, team `team_mzv1F3v3Ce4SsV5UOh32qwo2`).
- He is a Product Designer at American Express (Bangalore), aiming for Senior Product Designer roles with an AI angle. Headline title is always "Product Designer".
- The editable source is a Claude Design canvas (`.dc.html` pages + `canvas.json`). A copy of that source is in `source/`. The canvas is a private artifact tied to his Claude account (https://claude.ai/artifact/EBFMeGiz81xzmDbPAM92Wi, owner access only). A new account cannot open it: ask him to share it, or rebuild the canvas from `source/`.
- The site is the exported static copy of the canvas pages. `RK-Product_Designer.pdf` is the live résumé (two-page).

## Non-negotiables
1. **Never push live** unless he says "push live" or "push". Publishing to the canvas is always fine.
2. Run `python3 tools/lint.py` before every export and push. It must PASS. Rules are in `tools/rules.json`.
3. Never invent a metric. Label targets, estimates and concepts. Never turn a target into a result.
4. Follow the design system in `docs/design-system.md` and his preferences in `docs/working-with-rakhesh.md` (solid chart fills, max two text styles per line, no strokes, X-Y-Z impact statements, scannable copy, no internal team names).
5. Crisp answers. Tell him the plan before big changes.

## Layout of this repo
- `index.html`, `work/`, `mechanical-design/`: the live site (generated, do not hand-edit; change `source/` then export).
- `source/`: backup of the canvas pages, identical to the live pages. Source of truth for edits made outside the canvas.
- `tools/`: `lint.py` + `rules.json` + `lint-baseline.json` (design-rule checker), `export.py` + `build.py` (canvas pages to static site).
- `docs/`: `design-system.md` (tokens, type, components, voice), `working-with-rakhesh.md` (preferences and rules), `decisions.md` (decisions, open items, canvas gotchas).
- `resume/`: build files for the one-page and two-page résumé (`resume/README.md`).
- `api/likes.js`: Like counter (Upstash Redis through Vercel env vars `KV_REST_API_URL` / `KV_REST_API_TOKEN`; key `portfolio:likes`; CORS `*`).
- `tools`, `docs`, `source`, `resume` and this file are hidden from the public site by rewrites in `vercel.json` (404) and `.vercelignore`. Check this still holds after any change to `vercel.json`.

## Everyday workflow
1. Make the change in the canvas (read the latest published files first: a hand edit makes a stale publish fail) or in `source/`.
2. `python3 tools/lint.py` (add `--verbose` for line numbers). Fix errors. Do not let ratchet counts rise; after cleaning a page run `python3 tools/lint.py --update-baseline`.
3. Publish to the canvas and show him. Keep `canvas.json` board heights real (autosave can reset to 8000; lint catches it).
4. Only on "push live": `python3 tools/build.py` (preview what changes), `python3 tools/build.py --write`, check `git diff --stat`, commit with the attribution trailers, `git push origin main`, then confirm the Vercel deployment is READY (Vercel MCP `list_deployments` / `get_deployment`). The sandbox cannot curl the live site; use the Vercel MCP fetch.
5. QA before shipping: 1280 px and 390 px, light and dark, mobile menu open, links work (Projects goes to Work, AI builds goes to #ai), no console errors, Like count loads.

## Site structure
Home: Hero (portrait stage), Moments, Outcomes (metrics, before projects), Selected work, Working Method flow, Proposal, AI builds, Leadership, Range, About, Like, Footer.
Other pages: Work; cases Manage Credit Limit, Digital Charge Verification, Financial Relief Program, Canada Experience Gap, Financial Verification, Plan It Promo Pricing, Payments Mexico, Generic Medicine, Bulk Payment, Onboarding; proposals Localization Automation and Design System Usage; AI builds SourcX, ShubhViva, Gravity; Mechanical Design (engineering side, behind one secondary button).
Header on every page: Impact, Work, Proposals, AI builds, About, plus a 3 px reading-progress line. Details in `docs/decisions.md`.
Removed on purpose, do not bring back: "How I design AI behaviour" block, Financial Verification outcome card, hero cursor hint, hero "More about me" button, project list in the mobile menu, CAD or mechanical chips in About.

## Status and open items
See `docs/decisions.md` ("Open items"). Last updated: 28 Nov 2026. Live commit before this pack was added: e7dabfd (résumé tagline). Check `git log` for newer.

## What is NOT in this public repo
Private source notes (career facts, project inventory, metrics, facts-and-gaps with confidentiality rules) are kept by Rakhesh in a private handover zip, not here, because the repo is public. If a new Claude needs them, ask him to attach the zip. Until then, use only what is on the live site and in `docs/`, and ask before stating any new claim. Never put internal American Express project names, code names or unreleased details in this repo or the portfolio.

## Keep this alive
At the end of every session that changes the site or résumé: update "Status and open items" and `docs/decisions.md`, run lint, update the baseline if pages were cleaned, and commit these files with the change. Rakhesh expects this pack to stay current so any Claude account can continue from it.
