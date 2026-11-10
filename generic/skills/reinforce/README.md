# Reinforce

Save a reusable lesson in the place that will affect future work: preferences in approved memory, workflow rules in the owning skill, repeatable logic in a helper, and canonical-placement rules in their authoritative source.

## Use

Clone this repository, then add [SKILL.md](SKILL.md) to your agent's context using its supported file attachment or file-reference mechanism. For example:

> Use Reinforce to remember this preference: keep status updates concise.

Or:

> Use Reinforce to codify this in the intake workflow: reuse an existing file only when its bytes match, even if the filename is the same.

For hosts with native skill discovery, copy this directory into the location documented by that host, then verify discovery and use its supported invocation syntax. This package does not prescribe a host-specific installation path or claim native discovery has been tested.

The skill has no runtime dependencies. Your agent still needs the relevant read/write capabilities and an approved persistence mechanism. A host without configured memory can use workflow/tool routing, but cannot claim to save preferences durably until an approved memory destination is available. Portability depends on host capabilities and policies; compatibility with every agent is not established.

## Provenance and license

Generalized from the author's personal Reinforce workflow and introduced here as a sanitized snapshot. Existing public repository history is retained; private workflow history is not imported.

The [MIT license](LICENSE), copyright 2026 Richard Wolff, applies only to the owner-controlled material in this directory. It does not license other repository content.
