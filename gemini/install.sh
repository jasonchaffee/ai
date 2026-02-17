#!/bin/bash
# Install jasonchaffee statusline hook for Gemini CLI

set -e

PROJECT_ROOT=$(git rev-parse --show-toplevel 2>/dev/null || pwd)
GEMINI_DIR="$PROJECT_ROOT/.gemini"
HOOKS_DIR="$GEMINI_DIR/hooks"
SETTINGS_FILE="$GEMINI_DIR/settings.json"
SCRIPT_NAME="statusline.py"

echo "Installing Gemini statusline hook..."

# Create .gemini directories if needed
mkdir -p "$HOOKS_DIR"

# Copy the statusline script
cp "$PROJECT_ROOT/gemini/hooks/statusline.py" "$HOOKS_DIR/$SCRIPT_NAME"
chmod +x "$HOOKS_DIR/$SCRIPT_NAME"

# Link commands
mkdir -p "$GEMINI_DIR/commands"
for cmd in "$PROJECT_ROOT/gemini/commands"/*.toml; do
    if [ -f "$cmd" ]; then
        ln -sf "$cmd" "$GEMINI_DIR/commands/$(basename "$cmd")"
    fi
done

echo "Hook script installed to: $HOOKS_DIR/$SCRIPT_NAME"

# Create or update settings.json
if [ ! -f "$SETTINGS_FILE" ]; then
    echo '{"hooks": []}' > "$SETTINGS_FILE"
fi

# Use python to safely update the JSON if jq isn't available
python3 - <<EOF
import json
import os

settings_path = "$SETTINGS_FILE"
hook_path = "./hooks/$SCRIPT_NAME"

with open(settings_path, 'r') as f:
    try:
        data = json.load(f)
    except:
        data = {}

if 'hooks' not in data:
    data['hooks'] = []

# Check if hook already exists
exists = False
for hook in data['hooks']:
    if hook.get('event') == 'AfterAgent' and hook.get('command') == f"python3 {hook_path}":
        exists = True
        break

if not exists:
    data['hooks'].append({
        "event": "AfterAgent",
        "command": f"python3 {hook_path}"
    })
    with open(settings_path, 'w') as f:
        json.dump(data, f, indent=2)
    print("Added AfterAgent hook to .gemini/settings.json")
else:
    print("AfterAgent hook already configured in .gemini/settings.json")
EOF

echo "✅ Gemini installation complete!"
echo "The statusline will appear after each turn in Gemini CLI."
