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

### `generic/` (current)
Universal skills that work across any agent (Cursor, Claude Code, Codex, Antigravity, etc.) that acts on the file system or standard git commands, without relying on tool-specific context blocks. See [`generic/README.md`](generic/README.md).

- **[`document-acquisition-bakeoff`](generic/skills/document-acquisition-bakeoff/SKILL.md)**: Rank acquisition routes and write a deterministic, secret-free collector path under operator-supplied `code_root`.
- **[`document-acquisition-harness`](generic/skills/document-acquisition-harness/SKILL.md)**: Load the baked winning route from `code_root` at acquisition time (no rediscovery).

## Usage

Clone the repository into your project or a general code directory:

```bash
git clone https://github.com/wolffrichardj/shared-agent-workflows agent-workflows
```

To use a skill, simply add the relevant `SKILL.md` file to your AI agent's context (e.g. via `@file` reference).

**Compatibility**: These workflows are designed to work with **any** advanced AI coding assistant (like Cursor or Claude Code). They are currently tested and validated primarily with **Antigravity**.
