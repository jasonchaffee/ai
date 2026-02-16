#!/bin/bash
# Install jasonchaffee statusline for Claude Code
# Usage: curl -fsSL https://raw.githubusercontent.com/jasonchaffee/ai/main/claude/settings/statuslines/jasonchaffee/install.sh | bash

set -e

SCRIPT_DIR="$HOME/.claude/scripts"
SETTINGS_FILE="$HOME/.claude/settings.json"
SCRIPT_NAME="jasonchaffee-statusline.py"
RAW_BASE="https://raw.githubusercontent.com/jasonchaffee/ai/main/claude/settings/statuslines/jasonchaffee"

echo "Installing jasonchaffee statusline for Claude Code..."

# Create scripts directory if needed
mkdir -p "$SCRIPT_DIR"

# Download the statusline script
echo "Downloading statusline script..."
curl -fsSL "$RAW_BASE/statusline.py" -o "$SCRIPT_DIR/$SCRIPT_NAME"
chmod +x "$SCRIPT_DIR/$SCRIPT_NAME"

echo "Script installed to: $SCRIPT_DIR/$SCRIPT_NAME"

# Check if settings.json exists
if [ -f "$SETTINGS_FILE" ]; then
    # Check if statusLine is already configured
    if grep -q '"statusLine"' "$SETTINGS_FILE" 2>/dev/null; then
        echo ""
        echo "⚠️  statusLine already configured in $SETTINGS_FILE"
        echo "To use this statusline, update your settings.json with:"
    else
        echo ""
        echo "Add this to your $SETTINGS_FILE:"
    fi
else
    echo ""
    echo "Create $SETTINGS_FILE with:"
fi

echo ""
echo '  "statusLine": {'
echo '    "type": "command",'
echo "    \"command\": \"python3 $SCRIPT_DIR/$SCRIPT_NAME\","
echo '    "padding": 0'
echo '  }'
echo ""

echo "✅ Installation complete!"
echo ""
echo "Example output:"
echo "  ⚡ Sonnet 4 | 📁 my-project | 🏠 main | 🟢 23% (46,000/200,000)"
echo "  🧠 Opus 4 | 📁 my-project | 🌿 feature/auth ✹✭ | 🟡 58% (116,000/200,000)"
