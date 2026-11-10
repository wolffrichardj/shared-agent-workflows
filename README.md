# Shared Agent Workflows

A collection of skills and workflows for advanced AI coding agents. This repository focuses on "meta-agentic" capabilities—reasoning, synthesis, and architectural alignment.

## Philosophy

We assume the reader (and the agent) knows how to run basic commands but we also are not always technology locked. The focus is not skills for rote tasks. Instead, skills that:
1.  **Synthesize Context**: Combine multiple data sources (git, chat history, files) to generate unique insights.
2.  **Enforce Architecture**: Act as a Lead Architect to audit code against abstract principles.
3.  **Maintain Self-Consistency**: Keep documentation and project state aligned.

## Structure

The repository is organized by the **tool** or **agent** the skills are designed for, as different agents have different capabilities and context availabilities.

### `antigravity/`
Skills and workflows optimized for **Google Antigravity**. Use these if you are using the Antigravity editor or agent.
- **Skills**: `antigravity/skills/` (e.g., `daily-activity` which uses Antigravity's specific conversation history context).
- **Workflows**: `antigravity/workflows/`

## Workflows (`antigravity/workflows/`)

- **`daily-activity`**: Runs the activity summarization skill.

### `generic/`
Portable instructions that do not rely on tool-specific context blocks. Use depends on each host's capabilities and policies; see each package's requirements.

- **[Reinforce](generic/skills/reinforce/README.md)**: Persist an explicitly stated lesson in approved memory, an owning workflow, a deterministic helper, or authoritative project guidance.

The MIT license in `generic/skills/reinforce/` applies only to that package. This addition leaves the licensing of other repository material unchanged.

## Usage

Clone the repository into your project or a general code directory:

```bash
git clone https://github.com/wolffrichardj/shared-agent-workflows agent-workflows
```

To use a skill, simply add the relevant `SKILL.md` file to your AI agent's context (e.g. via `@file` reference).

**Compatibility**: Host capabilities and native skill discovery differ. See each package for requirements and usage. Existing Antigravity workflows were primarily tested with **Antigravity**; Reinforce has separate portable file-reference instructions and does not claim universal host compatibility.
