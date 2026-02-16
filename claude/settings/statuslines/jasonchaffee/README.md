# jasonchaffee-statusline

Emoji-rich status line for Claude Code CLI with model icons, git integration, and context usage tracking.

## Examples

```
⚡ Sonnet 4 | 📁 my-project | 🏠 main | 🟢 23% (46,000/200,000)
⚡ Sonnet 4 | 📁 my-project | 🌿 feature/auth ✹✭ | 🟡 58% (116,000/200,000)
🧠 Opus 4 | 📁 my-project | 🌿 fix/bug-123 ✚✹✖✭ | 🟠 82% (164,000/200,000)
```

## Emojis

### Models

| Model | Emoji |
|-------|-------|
| Opus | 🧠 |
| Sonnet | ⚡ |
| Haiku | 🚀 |
| Other | 🤖 |

### Directory

| Element | Emoji |
|---------|-------|
| Current folder | 📁 |

### Git Branch

| Branch | Emoji |
|--------|-------|
| main/master | 🏠 |
| Other branches | 🌿 |

### Git Status

| Status | Symbol |
|--------|--------|
| Added | ✚ |
| Modified | ✹ |
| Deleted | ✖ |
| Renamed | ➜ |
| Unmerged | ═ |
| Untracked | ✭ |

### Context Usage

| Usage | Emoji |
|-------|-------|
| 0-50% | 🟢 |
| 50-75% | 🟡 |
| 75-90% | 🟠 |
| 90%+ | 🔴 |

## Install

```bash
curl -fsSL https://raw.githubusercontent.com/jasonchaffee/ai/main/claude/settings/statuslines/jasonchaffee/install.sh | bash
```

Then add to `~/.claude/settings.json`:

```json
{
  "statusLine": {
    "type": "command",
    "command": "python3 ~/.claude/scripts/jasonchaffee-statusline.py",
    "padding": 0
  }
}
```
