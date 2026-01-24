---
name: daily-activity
description: Generate a summary of activity for a specified date or today.
---

# Activity Summary

Generate a comprehensive summary of Antigravity usage and project activity.

## Process

### 1. Gather Activity Data

Check if the user specified a **target date** in their request (e.g., "yesterday", "2024-01-20").
*   **Default**: If no date is specified, use **Today** (since midnight).
*   **Custom**: If a date is specified, use that date (00:00 to 23:59).

You need to gather data from two primary sources:

1.  **Conversation History**: Look at the `<conversation_summaries>` section in your **Current Context**.
    *   Identify conversations where the `Last modified` date matches the **target date**.
    *   Note the "USER Objective" and the summary of the conversation.
2.  **Git Activity**: Run the following command to see commits (adjust `--since` and `--until` for the target date):
    *   *For Today:*
        ```bash
        git log --since="midnight" --author="$(git config user.name)" --pretty=format:"%h - %s"
        ```
    *   *For a specific date (e.g., 2026-01-20):*
        ```bash
        git log --since="2026-01-20 00:00:00" --until="2026-01-20 23:59:59" --author="$(git config user.name)" --pretty=format:"%h - %s"
        ```

### 2. Analyze and Group by Theme

Read through the conversation summaries and git logs. Group them into meaningful work themes.

**Focus on substantial work.**
*   **Substantial Work**: New features, refactoring, documentation updates, complex debugging.
*   **Other**: Quick fixes, typo corrections, minor config tweaks, simple Q&A.

For each major theme, identify:
*   **Work Done**: What was actually accomplished?
*   **Key Decisions**: Did the strategy change? (e.g., "Refactoring workflow X", "Adopting Convention Y")
*   **Artefacts**: What files/components were created or heavily modified?

### 3. Output Format

Generate markdown suitable for a daily note.

```markdown
## Antigravity Activity Report - [YYYY-MM-DD]

### Day Summary
2-3 sentences giving the overall shape of the day: major focus areas, flow of work, high-level accomplishments.

### [Theme 1 Name]
- Description of work done
- Key decisions or outcomes

### [Theme 2 Name]
- Description of work done
...

### Other
- Brief summary of smaller tasks.
- Quick fixes.
```

## Key Rules

1.  **Synthesize**: Don't just list commits or conversation titles. Explain *what* was done.
2.  **Context Aware**: Use the `conversation_summaries` to understand the *intent* behind the git commits.
3.  **No Token Usage**: We do not currently have access to token usage stats, so omit that section.
