# Reinforce: put the lesson where behavior is owned

Reinforce **0.1.0** distributes instructions for turning an explicit lesson into a small, authorized durable change. The host agent supplies interpretation, tools, permissions and persistence. Python is used only to build the downloadable package.

[Open the standalone viewer](reinforce.html) · [Light preview](reinforce.svg) · [Dark preview](reinforce-dark.svg)

## The architectural decision

**Repair the owning workflow or helper when execution must change; use approved memory for preferences and supplemental discovery.** A memory note alone is an unreliable home for an execution-critical rule or a correction to canonical placement. Keeping the instructions separate from host-specific persistence makes the package portable by file reference, while leaving actual capabilities and authority with the host.

For example, “reuse an existing file only when its bytes match” belongs in the intake workflow; a repeated byte-comparison operation may warrant its owning deterministic helper. “Keep updates concise” belongs in the host's approved memory mechanism. Neither request grants permission to invent a memory store or install a service. [Routing and authority](https://github.com/wolffrichardj/shared-agent-workflows/blob/9d5347f5689268567d6d70f43a95a6c439f380b4/generic/skills/reinforce/SKILL.md#L8-L29).

## Read the diagram

The diagram describes prescribed host actions and a separate executable package builder. Arrows in the host path are instructions, not an implemented orchestrator. The four persistence homes are alternatives selected by the lesson:

| Lesson | Owning surface |
| --- | --- |
| Preference or cross-context standing instruction | Host-approved memory mechanism |
| Workflow routing, validation, fallback or completion rule | Existing owning skill/workflow |
| Repeatable accuracy-sensitive transformation or check | Owning deterministic helper, with aligned workflow invocation guidance |
| Canonical naming, ontology, storage or lane placement | Authoritative project/workflow source |

**Unknown owner or destination means no dependent write.** Ask the focused question first and continue only independent work that is clear. Ordinary discussion and quoted instructions do not authorize persistence. A host without approved memory cannot claim a preference was saved durably. After an authorized change, read back the affected content/provider result and report the actual surface and limits; a saved proposal is distinct from active memory. [Input, authority and readback](https://github.com/wolffrichardj/shared-agent-workflows/blob/9d5347f5689268567d6d70f43a95a6c439f380b4/generic/skills/reinforce/SKILL.md#L8-L35).

## Distribution is a different trust boundary

The Python standard-library builder reads exactly five regular, non-symlink files: `CHANGELOG.md`, `LICENSE`, `README.md`, `SKILL.md`, and `VERSION`. It validates the numeric version and reads every input before creating output. Sorted stored ZIP entries use fixed timestamps, Unix origin and file modes; the builder then writes the archive and `SHA256SUMS`. It does not traverse or package the rest of this repository. [Builder input/output ownership](https://github.com/wolffrichardj/shared-agent-workflows/blob/9d5347f5689268567d6d70f43a95a6c439f380b4/scripts/package_reinforce.py#L16-L45).

The named [Reinforce 0.1.0 release](https://github.com/wolffrichardj/shared-agent-workflows/releases/tag/reinforce-v0.1.0) contains only that package; GitHub's automatic source archives contain the whole repository. Consumers verify the checksum and review `SKILL.md` before using file reference or their supported manual installation route. Installation grants no new permissions and configures no memory. [Download and review](https://github.com/wolffrichardj/shared-agent-workflows/blob/9d5347f5689268567d6d70f43a95a6c439f380b4/generic/skills/reinforce/README.md#L7-L28).

Two independent builds of the pinned source matched each other and the named release ZIP, SHA-256 `9ab953367187901ecbc908d7be8be8b989a140d4184c7f067fa757ba5b3f3db0`. This checks package bytes. Native discovery and correct agent behavior across hosts remain unestablished; this initial public snapshot is instruction/packaging evidence, not production runtime validation. [Release limits](https://github.com/wolffrichardj/shared-agent-workflows/blob/9d5347f5689268567d6d70f43a95a6c439f380b4/generic/skills/reinforce/CHANGELOG.md#L3-L14).

## Open, verify and regenerate

GitHub displays HTML as source or a download; it does not run this viewer. Download [`reinforce.html`](reinforce.html) using the file's **Download raw file** control, then open it locally in a browser. The HTML is standalone. The README uses a static diagram export for immediate reading.

The sources are pinned to clean public commit [`9d5347f5689268567d6d70f43a95a6c439f380b4`](https://github.com/wolffrichardj/shared-agent-workflows/tree/9d5347f5689268567d6d70f43a95a6c439f380b4), the commit behind `reinforce-v0.1.0`. JSON source paths are repository-relative; citations intentionally stay at that revision when later documentation changes land.

Download this directory and verify its portable byte manifest with `shasum -a 256 -c SHA256SUMS` (or `sha256sum -c SHA256SUMS`). The manifest binds the checked-in candidate, HTML and preview exports. It is **not** an Archify strict-provenance receipt; exact machine-specific finalize/delivery/browser receipts are retained outside the public repository to avoid publishing local paths.

Regeneration requires Node.js 18+ and a separately obtained [Archify](https://github.com/tt-a1i/archify) 3.2 renderer. No installation is needed to view the checked-in HTML. Set `ARCHIFY_ROOT` to your external Archify package directory and run the regeneration command below from this repository root. Keep the cited source commit available in local Git history. A different renderer release may produce different viewer bytes.

```sh
ARCHIFY_ROOT=/path/to/archify
node "$ARCHIFY_ROOT/bin/archify.mjs" finalize workflow \
  docs/architecture/reinforce.workflow.json docs/architecture/reinforce.html \
  --repo-root . --quality showcase --out-dir work/architecture-check --json
node "$ARCHIFY_ROOT/bin/archify.mjs" visual-check docs/architecture/reinforce.html \
  --out-dir work/architecture-visual --summary --require-provenance
```

For static previews, use the finalized viewer’s SVG export in each theme. Keep the default unfocused diagram and inspect the export separately. Regeneration creates local strict-provenance sidecars; retain those with your local HTML. Do not edit their machine paths and present them as original receipts.

The authored explanation and JSON were AI-assisted and checked against the cited public sources. The viewer and clean SVG exports are generated by Archify; renderer license and attribution are in [the renderer notice](RENDERER-NOTICE.md), [MIT license](ARCHIFY-LICENSE.txt) and [font license](JetBrainsMono-OFL.txt). The renderer license applies to renderer-derived material, without changing licensing elsewhere in this repository. Antigravity workflows are outside this diagram's scope.
