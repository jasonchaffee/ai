# Claude Code Statuslines

Custom statusline implementations for Claude Code CLI.

## Prerequisites

- **Python 3.6+** - Script uses f-strings and subprocess
- **Git** - For branch and status detection
- **Claude Code CLI** - The statusline integrates with Claude Code

## Claude Code Settings

- **Settings file**: `~/.claude/settings.json`
- **Scripts directory**: `~/.claude/scripts/`

## Quick Install

```bash
curl -fsSL https://raw.githubusercontent.com/jasonchaffee/ai/main/claude/settings/statuslines/jasonchaffee/install.sh | bash
```

After running, add the statusLine config to `~/.claude/settings.json` as shown in the output.

## Available Statuslines

### jasonchaffee

Emoji-rich status line with:
- **Model icons**: 🧠 Opus, ⚡ Sonnet, 🚀 Haiku
- **Directory**: 📁 current folder name
- **Git branch**: 🏠 main/master, 🌿 feature branches
- **Git status**: ✚ added, ✹ modified, ✖ deleted, ➜ renamed, ═ unmerged, ✭ untracked
- **Context usage**: 🟢 0-50%, 🟡 50-75%, 🟠 75-90%, 🔴 90%+

**Example output:**
```
⚡ Sonnet 4 | 📁 my-project | 🏠 main | 🟢 23% (46,000/200,000)
🧠 Opus 4 | 📁 my-project | 🌿 feature/auth ✹✭ | 🟡 58% (116,000/200,000)
```

## Manual Installation

1. Copy the statusline script to `~/.claude/scripts/`:

```bash
mkdir -p ~/.claude/scripts
cp statuslines/jasonchaffee/statusline.py ~/.claude/scripts/jasonchaffee-statusline.py
chmod +x ~/.claude/scripts/jasonchaffee-statusline.py
```

2. Add to `~/.claude/settings.json`:

```json
{
  "statusLine": {
    "type": "command",
    "command": "python3 ~/.claude/scripts/jasonchaffee-statusline.py",
    "padding": 0
  }
}
```

## Structure

```
statuslines/
├── README.md              # This file
└── jasonchaffee/
    ├── install.sh         # Curl-able install script
    └── statusline.py      # Python script that generates the status line
```

## Creating a New Statusline

1. Create a new directory with your name/identifier
2. Add a `statusline.py` (or other script) that:
   - Reads JSON from stdin
   - Prints the formatted statusline to stdout
3. Add an `install.sh` for easy installation

### Input Format

Your script receives JSON via stdin:

```json
{
  "model": {
    "display_name": "Sonnet 4"
  },
  "workspace": {
    "current_dir": "/path/to/project"
  },
  "transcript_path": "/path/to/transcript.jsonl"
}
```

### Output

Print a single line to stdout. Keep it concise - it appears at the bottom of the terminal.
