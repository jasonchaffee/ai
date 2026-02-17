# ai

Unified configuration for AI coding assistants: Claude, Gemini, ChatGPT, Copilot - CLI and IDE.

## Marketplaces

- [AI Templates (aitmpl.com)](https://www.aitmpl.com)
- [Skills Marketplace (skillsmp.com)](https://skillsmp.com)
- [MCP Market (mcpmarket.com)](https://mcpmarket.com)
- [Claude Marketplaces (claudemarketplaces.com)](https://claudemarketplaces.com)
- [FastMCP (fastmcp.me)](https://fastmcp.me)

## Skill Collections

- [awesome-claude-skills (travisvn)](https://github.com/travisvn/awesome-claude-skills)
- [claude-code-templates (davila7)](https://github.com/davila7/claude-code-templates)
- [awesome-claude-skills (ComposioHQ)](https://github.com/ComposioHQ/awesome-claude-skills)
- [agent37-skills-collection](https://github.com/Agent-3-7/agent37-skills-collection)

## Repository Structure

```
claude/
  commands/       # Claude slash commands (Markdown)
  subagents/      # Specialized Claude agent definitions
  skills/         # Claude packaged skills
  settings/
    statuslines/  # Claude statusline implementations
gemini/
  commands/       # Gemini custom commands (TOML)
  hooks/          # Gemini lifecycle hooks (Python/Bash)
  skills/         # Gemini packaged skills (SKILL.md)
```

## Commands

### Claude Commands
Markdown files with YAML frontmatter. Refer to `CLAUDE.md` for format details.

| Command | Description |
|---------|-------------|
| `architecture-review` | Comprehensive architecture review |
| `claude-commander` | Manage custom Claude commands |
| `comprehensive-code-review` | Detailed code review |
| `e2e-status-reporting` | End-to-end status reporting |
| `feature-planning` | Plan feature implementation |
| `fix-issue` | Analyze and fix Jira/GitHub issues with PR creation |
| `generate-service-presentation` | Generate service presentations |
| `implement-jira-task` | Implement a Jira task |
| `jira-worktree` | Create worktree for Jira issue |
| `llm-task-log` | Log LLM task progress |
| `plan-jira-task` | Plan implementation for Jira task |
| `prompt-plan-execution` | Execute planned prompts |
| `review-pr-comments` | Review PR comments |
| `score-issue` | Score issue complexity |
| `smart-commit` | Intelligent commit message generation |
| `sprint-review` | Generate sprint review |
| `story-draft` | Draft Jira stories |
| `tdd-implementation` | Test-driven development workflow |
| `tldr` | Analyze and improve technical documents |
| `weekly-changes-summary` | Summarize weekly merged changes |
| `write-epic` | Write Jira epics |

### Gemini Commands
TOML files defining steps and prompts. Refer to `GEMINI.md` for format details.

| Command | Description |
|---------|-------------|
| `status` | Show project status, git info, and context usage |

## Skills

Packaged skills containing a `SKILL.md` definition file.

| Skill | Description |
|-------|-------------|
| `ai-image-generator` | Generate images using Gemini AI |
| `anonymize-feedback` | Anonymize feedback content |
| `claude-troubleshooting` | Troubleshoot Claude Code issues |
| `clipboard` | Cross-platform clipboard operations |
| `data-explorer` | Exploratory data analysis on CSV/Parquet/BigQuery |
| `plantuml-confluence` | PlantUML diagrams for Confluence |
| `promptfoo` | LLM testing and evaluation |
| `rapid-risk-assessment` | Mozilla RRA methodology for service risk |
| `security-analysis` | Quick logical vulnerability assessment |
| `security-code-review` | Comprehensive OWASP-based code review |
| `survey-designer` | Design surveys and questionnaires |

## Hooks

### Gemini Hooks
Executable scripts triggered by Gemini CLI lifecycle events.

| Hook | Event | Description |
|------|-------|-------------|
| `statusline` | `AfterAgent` | Displays emoji-rich status line after each turn |

## Settings

### Claude Statuslines

Custom statusline implementations for Claude Code CLI. See `claude/settings/statuslines/README.md` for details.

Available implementations:
- `jasonchaffee` - Emoji-rich status with model icons, git status, and context usage
