# Gemini CLI Configurations

This directory contains customizations for the Gemini CLI, following the standard Gemini organization patterns.

## Repository Structure

```
gemini/
  commands/       # Custom TOML-based slash commands
  hooks/          # Executable hook scripts (e.g., AfterAgent)
  skills/         # Gemini Skills (with SKILL.md)
  install.sh      # Installation script for local setup
```

## Available Customizations

### Statusline Hook
Located in `hooks/statusline.py`. It displays a formatted status line after each turn, including:
- **Model Name**: Detected from session transcript.
- **Git Branch**: Current branch and status (dirty/clean).
- **Context Usage**: Total tokens used and percentage of limit.

## Installation

To enable these customizations in your local `.gemini/` configuration:

```bash
./gemini/install.sh
```

This will:
1. Create a `.gemini/` directory at the project root if it doesn't exist.
2. Install the statusline hook script.
3. Link all custom commands from `gemini/commands/` to `.gemini/commands/`.
4. Configure the `AfterAgent` hook in `.gemini/settings.json`.

## Development

### Adding a Command
1. Create a `.toml` file in `gemini/commands/`.
2. Follow the [Gemini Custom Commands documentation](https://gemini.google.com/cli/docs/commands).

### Adding a Skill
1. Create a subdirectory in `gemini/skills/`.
2. Add a `SKILL.md` with appropriate metadata.
3. Follow the [Gemini Skills documentation](https://gemini.google.com/cli/docs/skills).
