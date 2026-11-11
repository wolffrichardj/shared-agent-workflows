# Reinforce

Save a reusable lesson in the place that will affect future work: preferences in approved memory, workflow rules in the owning skill, repeatable logic in a helper, and canonical-placement rules in their authoritative source.

Version **0.1.0** · [Release notes](CHANGELOG.md) · [MIT license](LICENSE)

## Requirements and scope

Reinforce is an instruction-only skill with no runtime dependencies. Your agent needs the relevant read/write capabilities and an approved persistence mechanism. A host without configured memory can use workflow/tool routing, but cannot claim to save preferences durably until an approved memory destination is available. Installation does not grant new permissions or configure memory.

This initial 0.x release packages the public sanitized snapshot. Native discovery and behavior across hosts have not been independently established; archive and isolated copy-install checks establish file integrity only.

## Download and verify

Download **reinforce-0.1.0.zip** and **SHA256SUMS** from the [Reinforce 0.1.0 release](https://github.com/wolffrichardj/shared-agent-workflows/releases/tag/reinforce-v0.1.0). Use the named ZIP asset, which contains only this package. GitHub's automatic repository source archives include other repository content with separate provenance and licensing.

On macOS or Linux with `curl` and `unzip`, use a new working directory:

```sh
mkdir reinforce-download
cd reinforce-download
curl -fLO https://github.com/wolffrichardj/shared-agent-workflows/releases/download/reinforce-v0.1.0/reinforce-0.1.0.zip
curl -fLO https://github.com/wolffrichardj/shared-agent-workflows/releases/download/reinforce-v0.1.0/SHA256SUMS
shasum -a 256 -c SHA256SUMS
unzip reinforce-0.1.0.zip
```

On systems without `shasum`, use `sha256sum -c SHA256SUMS`. Continue only when the checksum passes. Review `reinforce/SKILL.md` before installation.

## Use by file reference

Add [SKILL.md](SKILL.md) to your agent's context using its supported file attachment or file-reference mechanism, then ask:

> Use Reinforce to remember this preference: keep status updates concise.

Or:

> Use Reinforce to codify this in the intake workflow: reuse an existing file only when its bytes match, even if the filename is the same.

## Manual local installation in Codex

For local experimentation, Codex supports skill folders at `.agents/skills/` in a repository and `~/.agents/skills/` for a user. See the [official OpenAI skill documentation](https://learn.chatgpt.com/docs/build-skills) for current discovery rules, invocation, and plugin distribution guidance. This ZIP is a standalone skill folder, not a plugin or marketplace listing.

From the download directory, install in an existing project (replace the example destination):

```sh
project_dir=/path/to/your/project
mkdir -p "$project_dir/.agents/skills"
# Stop if this destination already exists; review an update separately.
test ! -e "$project_dir/.agents/skills/reinforce" && cp -R reinforce "$project_dir/.agents/skills/reinforce"
```

For user-wide local installation, use `"$HOME/.agents/skills"` as the parent directory instead. Avoid installing a second skill with the same name in another discovery location. In Codex CLI or the IDE extension, check `/skills`, then invoke `$reinforce` with your explicit lesson. If the skill does not appear, restart Codex and check the current host documentation. Verify the resulting destination and readback before treating a lesson as saved.

For other agents, use their documented discovery location and invocation syntax or the file-reference route. Universal compatibility is not claimed.

## Update or remove

Read the new version's release notes, verify its checksum, and review the instructions. Keep a backup of any local changes before replacing the installed `reinforce` directory. Check `VERSION` and `SKILL.md` afterward. To uninstall, remove only the `reinforce` directory you installed; lessons already saved in memory or other workflows remain in their owning destinations.

## Build from source

From a checkout of the release tag, run with Python 3:

```sh
python3 scripts/package_reinforce.py --output-dir dist/reinforce
```

The builder includes only `SKILL.md`, `README.md`, `LICENSE`, `VERSION`, and `CHANGELOG.md` under `reinforce/`, with fixed ZIP metadata and sorted paths. It writes the ZIP and `SHA256SUMS`. Identical source bytes produce identical archives. Python is needed only to build the archive, not to use the skill.

## Provenance and license

Generalized from the author's personal Reinforce workflow and introduced here as a sanitized snapshot. Existing public repository history is retained; private workflow history is not imported.

The [MIT license](LICENSE), copyright 2026 Richard Wolff, applies only to the owner-controlled material in this directory. It does not license other repository content.
