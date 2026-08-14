# Generic skills

Agent-agnostic skills that work on Cursor, Claude Code, Codex, Antigravity, and similar agents that can follow a `SKILL.md` recipe and act on a filesystem path.

These skills do **not** depend on tool-specific context blocks. The operator supplies inputs (especially `code_root`) and the host supplies transport (authenticated browser session, mail, filesystem sink).

## Skills

| Skill | Path | Role |
| --- | --- | --- |
| **document-acquisition-bakeoff** | [`skills/document-acquisition-bakeoff/SKILL.md`](skills/document-acquisition-bakeoff/SKILL.md) | Rank routes and **write** the deterministic path under `code_root` |
| **document-acquisition-harness** | [`skills/document-acquisition-harness/SKILL.md`](skills/document-acquisition-harness/SKILL.md) | **Load** the winning route from `code_root` at acquisition time |

### How they pair

1. **`bakeoff`** compares a short set of acquisition attempts (API → direct → page-context → UI → email → manual) on the operator’s already authenticated session and persists secret-free connector code + sanitized fixtures under `code_root`.
2. **`harness`** reads that manifest later, selects the highest-precedence route available for the run’s capabilities, and reuses the registered connector—no rediscovery, no silent scrape.

## Provenance (strategy only)

The ranking and harness strategy is extracted from a private, user-owned document acquisition practice. **This repo contains the reusable ranking/harness, not anyone’s provider catalog.** Do not expect real institution connectors here; synthetic examples use names like `example-utility` and `example-bank`.

## Safety

- Documents must be **user-owned**.
- Operators use **their own authenticated session**; credentials and sessions stay in the host, never in `code_root`.
- **Scraping is a fallback.** Prefer API / first-party / session page-context routes first.
- Fail closed when transport capabilities are empty or the provider is unknown to the harness.
