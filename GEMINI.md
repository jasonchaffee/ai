# Gemini Instructions - AI Assistant Configuration

Refer to `README.md` for the project overview, repository structure, and the full list of available Gemini commands, hooks, and skills.

## Gemini Technical Context

- **Extension Path:** All local project customizations reside in the `.gemini/` directory at the project root.
- **Commands:** Defined in TOML format within `gemini/commands/`.
- **Hooks:** Executable scripts in `gemini/hooks/` triggered by lifecycle events.
- **Skills:** Directory-based with a `SKILL.md` definition (Markdown with YAML frontmatter) in `gemini/skills/`.

### Gemini Statusline Hook
The `AfterAgent` hook provides a dynamic status display after each turn.
- **Installation:** Run `./gemini/install.sh`. This links commands and configures the hook in `.gemini/settings.json`.
- **Customization:** Logic is in `gemini/hooks/statusline.py`. It parses usage from the session transcript.

## Development Guidelines

- **DRY Principle:** Before adding new logic, check if it can be implemented as a cross-assistant skill or if a similar Claude command can be adapted.
- **Testing Hooks:**
  ```bash
  # Mock a hook execution
  cat sample_hook_input.json | python3 gemini/hooks/statusline.py
  ```
- **Permissions:** Ensure all new hook scripts and installers are executable (`chmod +x`).
- **TOML Validation:** Ensure Gemini commands follow the TOML schema for steps and prompts.
