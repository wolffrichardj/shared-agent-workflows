# Shared Agent Workflows

A collection of skills and workflows for advanced AI coding agents. This repository focuses on "meta-agentic" capabilities—reasoning, synthesis, and architectural alignment.

## Philosophy

We assume the reader (and the agent) knows how to run basic commands but we also are not always technology locked. The focus is not skills for rote tasks. Instead, skills that:
1.  **Synthesize Context**: Combine multiple data sources (git, chat history, files) to generate unique insights.
2.  **Enforce Architecture**: Act as a Lead Architect to audit code against abstract principles.
3.  **Maintain Self-Consistency**: Keep documentation and project state aligned.

## Available Skills (`skills/`)

- **`activity-summary`**:  Generates a human-readable "Daily Standup" report by synthesizing git logs and conversation history to infer *intent* and *themes* of work, not just a list of commits.

## Workflows (`workflows/`)

- **`summary`**: Runs the activity summarization.

## Usage

Clone the repository into your project or a general code directory:

```bash
git clone https://github.com/wolffrichardj/shared-agent-workflows agent-workflows
```

To use a skill, simply add the relevant `SKILL.md` file to your AI agent's context (e.g. via `@file` reference).

**Compatibility**: These workflows are designed to work with **any** advanced AI coding assistant (like Cursor or Claude Code). They are currently tested and validated primarily with **Antigravity**.
