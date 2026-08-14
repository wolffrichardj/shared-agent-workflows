---
name: document-acquisition-bakeoff
description: Use when an operator wants to add a new user-owned document source (statements, invoices, receipts, portal exports they already have an account on). Rank and bake off a short set of acquisition attempts while building the deterministic path for that user under code_root.
---

# Document Acquisition Bake-off

Rank and “bake off” a short set of acquisition attempts **while building the deterministic path** for a user-owned document source. The winning route becomes secret-free code under `code_root`, not a one-off scrape.

## Required input

- **`code_root`**: filesystem path where this skill must write/update the deterministic collector code (manifest, connector module, sanitized fixture).

If `code_root` is missing, ask once. Do **not** invent a default that points at anyone’s private repo.

## Intent

For a provider the user already authenticates to (their own account), compare a few acquisition routes on the host-supplied authenticated session, pick a winner, and persist that winner as reusable, secret-free code under `code_root`.

Documents must be **user-owned**. Operators use their own authenticated session. Scraping is a fallback.

## Route precedence (auditable order)

Always consider routes in this exact order, named explicitly:

1. **API** — documented or discovered first-party API
2. **direct** — direct first-party endpoint (download URL / binary fetch without UI)
3. **page-context** — page-context fetch in an existing authenticated session
4. **UI** — UI click/download in the authenticated browser session
5. **email** — targeted email (provider-sent record as provenance/lead)
6. **manual** — user-only steps (MFA, CAPTCHA, legal ack)

## Process

### 1. Preflight `code_root`

1. Confirm `code_root` is provided. If not, ask once and stop until it is given.
2. Search `code_root` (and any existing manifest) before live discovery.
3. If a connector is already registered for this provider + route, **reuse it**. Do not start from scraping.
4. Inventory host-supplied transport capabilities (browser session, mail access, filesystem sink). **Fail closed** if the capability set is empty. An empty capability set is not “try everything.”

### 2. Unknown provider: plan first

For an unknown provider:

1. Search history and dependencies under `code_root` (and local project context the operator points at).
2. Return a **ranked plan** using the route precedence above.
3. Do **not** authorize immediate scraping from an unknown-provider plan alone.

Synthetic provider ids only in examples and fixtures (e.g. `example-utility`, `example-bank`).

### 3. Short bake-off (2–3 paths)

On the **already authenticated** session the host supplies:

1. Select up to 2–3 candidate routes from the precedence list that the current capability set can actually run.
2. Compare candidates on:
   - **Native bytes vs reconstructed data** (prefer provider-native bytes)
   - **Stability** (repeatable request shape / UI path)
   - **Same-content proof** (identity markers: period/order id, MIME/magic, checksum where applicable)
   - **Pagination / archive depth** (can the route reach historical documents?)
3. Any downgrade from provider-native bytes to reconstructed data must be **explicit** in the bake-off record and in the written manifest entry.
4. **Scraping is a fallback.** Prefer every higher-precedence route the capabilities allow before considering scrape-like extraction.

### 4. Record the winner as the deterministic route

Write (or update) under `code_root` a secret-free record that includes:

- **request shape** (no secrets, cookies, tokens, or account numbers)
- **same-content identity markers**
- **fixture_ref** pointing at a sanitized fixture
- **refresh triggers** (what should cause a re-run)
- **blockers** (MFA, CAPTCHA, legal ack, missing capability)

### 5. Persist connector + sanitized fixture

1. Write connector module code into `code_root` for the winning route.
2. Write a **sanitized** fixture (synthetic ids only; no real institutions, account numbers, or provider PDFs).
3. Update the manifest so the harness can load this route later without rediscovery.
4. Never write cookies, tokens, PATs, account numbers, or provider PDFs into `code_root`.

### 6. Hand off

Summarize for the operator:

- Ranked candidates tried
- Winner and why
- Paths written under `code_root` (manifest, connector, fixture)
- Remaining blockers (if any)

The runtime skill `document-acquisition-harness` loads this path later; this skill does not re-run acquisition beyond the bake-off.

## Key Rules

1. **Required `code_root`**: ask once if missing; never invent a private-repo default.
2. **Deterministic path over one-off scrape**: the product of this skill is code + fixture under `code_root`.
3. **Route precedence is fixed**: API → direct → page-context → UI → email → manual.
4. **Reuse before rediscovery**: registered connectors win over new exploration.
5. **Scraping is a fallback.**
6. **Fail closed** on empty transport capabilities.
7. **Explicit downgrades**: native bytes → reconstructed data must be called out.
8. **Public-safe artifacts**: no cookies, tokens, account numbers, provider PDFs, or real institution names in `code_root` outputs from this skill’s examples/guidance.
9. **No attack content**: do not include exploit PoCs, cookie theft, session hijack, CAPTCHA solving, or provider-specific attack steps.
