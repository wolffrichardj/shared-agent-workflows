---
name: document-acquisition-harness
description: Use when running an acquisition against a provider that already has a baked deterministic path under code_root. Identify which deterministic code to load during acquisition (runtime harness, not a second bake-off).
---

# Document Acquisition Harness

Identify **which deterministic code to load** from `code_root` during acquisition. This is the runtime harness, not a second bake-off.

## Required input

- **`code_root`**: filesystem path that holds the manifest, connector modules, and sanitized fixtures written by `document-acquisition-bakeoff`.
- **Provider id**, *or* an **email lead** (sender / subject / snippet) that maps to a registered provider.

If `code_root` is missing, ask once. Do **not** invent a default that points at anyone’s private repo.

## Intent

Load the already-baked deterministic path for a user-owned document source and execute the highest-precedence route the current run’s capabilities allow. Do not rediscover. Do not scrape.

Documents must be **user-owned**. Operators use their own authenticated session. Credentials and sessions stay in the host, never in `code_root`.

## Route precedence (auditable order)

Select among registered routes using this order:

1. **API**
2. **direct** (first-party endpoint)
3. **page-context**
4. **UI** (click/download)
5. **email** (provider-sent record as provenance/lead)
6. **manual** (user-only: MFA, CAPTCHA, legal ack)

## Process

### 1. Load the manifest

1. Confirm `code_root` is provided. If not, ask once and stop until it is given.
2. Load the manifest from `code_root`.
3. Resolve the target:
   - If a **provider id** is given, look it up directly.
   - If an **email lead** is given, map sender/subject/snippet to a registered provider via manifest metadata.
4. If the provider is **unknown** in the manifest, **fail closed**. Do not start a bake-off or scrape from this skill—point the operator at `document-acquisition-bakeoff` instead.

### 2. Select the highest-precedence available route

1. Inventory this run’s host-injected transport capabilities (browser / mail / filesystem).
2. **Fail closed** when the capability set is empty. Empty is not “try everything.”
3. From the provider’s registered routes, pick the highest-precedence route that is both:
   - listed in the manifest for this provider, and
   - runnable with the current capabilities.
4. **Email** is a discovery lead / provenance. Prefer the portal or first-party endpoint unless the manifest says email is the strongest available route for this provider.

### 3. Load and reuse the connector

1. If a connector module is registered for that route, **load that module and reuse it**.
2. Do **not** rediscover endpoints.
3. Do **not** scrape.
4. Host injects transport (browser session, mail access, filesystem sink). Never read or write cookies, tokens, or credentials into `code_root`.

### 4. Acquire, verify same-content, land via sink

1. Execute the connector’s request shape using host-injected transport.
2. Verify **same-content** using the manifest’s identity markers:
   - document identity (period / order id as applicable)
   - MIME / magic
   - checksum where applicable
3. Land via a sink that treats:
   - **identical bytes** as duplicates
   - **different bytes** as a checksum-variant sibling
4. Never persist cookies, tokens, account numbers, or raw provider secrets into `code_root`.

### 5. Drift handling

If the route has **drifted** (request shape fails, identity markers no longer match, endpoint gone):

1. **Stop.**
2. Update a **temporal note** under `code_root` (or the operator-designated notes location) describing what failed and when.
3. Do **not** silently switch to scraping.
4. Advise re-running `document-acquisition-bakeoff` if a new deterministic path is needed.

## Key Rules

1. **Harness, not bake-off**: load existing deterministic code; do not rediscover.
2. **Required `code_root`**: ask once if missing; never invent a private-repo default.
3. **Fail closed** on empty capabilities or unknown provider.
4. **Reuse registered connectors** for the selected route.
5. **Email is a lead**, not a default download path, unless the manifest ranks it highest among available routes.
6. **Host holds secrets**: sessions and credentials never live in `code_root`.
7. **Same-content before land**: verify identity / MIME / checksum; sink handles duplicates vs variants.
8. **Drift → stop + temporal note**; never silent scrape fallback.
9. **Scraping is a fallback** reserved for bake-off redesign, not silent runtime improvisation.
