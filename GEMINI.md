# Gemini Instructions - AI Assistant Configuration

Refer to `README.md` for the project overview, repository structure, and a comprehensive list of available commands and skills.

## Gemini Specific Instructions

- **Context Awareness:** Always check `README.md` and `CLAUDE.md` to understand the established formats for commands, skills, and subagents before creation.
- **Project Goal:** This repository centralizes configurations for multiple AI assistants. Ensure any new features or configurations consider cross-assistant compatibility where applicable.

## Development & Extension

### Statusline Development
When creating or modifying statuslines in `claude/settings/statuslines/`:
- **Input:** Scripts receive JSON via `stdin` (see `README.md` in the statuslines directory for the schema).
- **Output:** Must be a single line of text to `stdout`.
- **Testing:**
  ```bash
  cat sample_context.json | python3 claude/settings/statuslines/<name>/statusline.py
  ```

### New Components
- **Commands:** Follow the YAML frontmatter format described in `CLAUDE.md` and `README.md`.
- **Skills:** Must include a `SKILL.md` and should be placed in `claude/skills/` (create the directory if it doesn't exist).
- **Subagents:** Defined in `claude/subagents/` with appropriate tool sets.

## Verification
- Ensure all scripts are executable (`chmod +x`).
- Validate YAML frontmatter in markdown files for consistency with the documented schema.
- Use `python3` for statusline logic to maintain compatibility with the provided installation scripts.
