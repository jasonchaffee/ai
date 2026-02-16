# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Getting Started

Read `README.md` for repository purpose, structure, and external resources.

## Claude Code Assets

All Claude Code specific assets are in `claude/`:

- `commands/` - Slash commands with YAML frontmatter
- `subagents/` - Specialized agent definitions
- `skills/` - Packaged skills with SKILL.md, references/, and scripts/
- `settings/` - Configuration including custom statuslines

## Command Format

Commands are markdown files with YAML frontmatter:

```yaml
---
description: What the command does
category: Command grouping
argument-hint: Expected arguments
allowed-tools: Tool restrictions
---
```

## Skill Format

Skills are directories containing:

- `SKILL.md` - Main skill definition with frontmatter
- `README.md` - Usage documentation (optional)
- `references/` - Supporting documentation (optional)
- `scripts/` - Helper scripts (optional)

## Subagent Format

Subagents are markdown files with frontmatter:

```yaml
---
name: Agent identifier
description: When to use this agent
tools: Allowed tool list
category: Agent grouping
---
```
