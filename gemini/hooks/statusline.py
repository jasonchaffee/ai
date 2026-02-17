#!/usr/bin/env python3
import json
import sys
import os
import subprocess

# =============================================================================
# Configuration
# =============================================================================
CONTEXT_LIMIT = 2000000 # Gemini 1.5 Pro limit (approx)

# Model emojis
MODEL_EMOJIS = {
    'gemini-1.5-pro': '🧠',
    'gemini-1.5-flash': '⚡',
    'gemini-2.0-flash-exp': '🚀',
}

# Context thresholds and colors
CONTEXT_COLORS = [
    (50, '🟢'),   # 0-50%: healthy
    (75, '🟡'),   # 50-75%: caution
    (90, '🟠'),   # 75-90%: warning
    (100, '🔴'),  # 90%+: critical
]

# =============================================================================
# Helper Functions
# =============================================================================
def get_model_emoji(model_name):
    """Get emoji for model based on name."""
    model_lower = model_name.lower()
    for key, emoji in MODEL_EMOJIS.items():
        if key in model_lower:
            return emoji
    return '🤖'  # Default

def get_context_color(percentage):
    """Get color emoji based on context percentage."""
    for threshold, emoji in CONTEXT_COLORS:
        if percentage <= threshold:
            return emoji
    return '🔴'

def get_git_info(cwd):
    """Get git branch and status indicators."""
    # Check if in a git repo
    try:
        result = subprocess.run(
            ['git', 'rev-parse', '--is-inside-work-tree'],
            cwd=cwd, capture_output=True, text=True, timeout=2
        )
        if result.returncode != 0:
            return None, None
    except:
        return None, None

    branch = None
    # Get branch name
    try:
        result = subprocess.run(
            ['git', 'branch', '--show-current'],
            cwd=cwd, capture_output=True, text=True, timeout=2
        )
        if result.returncode == 0:
            branch = result.stdout.strip()
    except:
        pass

    if not branch:
        return None, None

    is_main = branch in ('main', 'master')

    # Get git status indicators
    status_indicators = ""
    try:
        result = subprocess.run(
            ['git', 'status', '--porcelain'],
            cwd=cwd, capture_output=True, text=True, timeout=5
        )
        if result.returncode == 0 and result.stdout.strip():
            statuses = set()
            for line in result.stdout.strip().split('
'):
                if len(line) >= 2:
                    index_status = line[0]
                    work_status = line[1]
                    if index_status == 'A': statuses.add('added')
                    elif index_status == 'M': statuses.add('modified')
                    elif index_status == 'D': statuses.add('deleted')
                    if work_status == 'M': statuses.add('modified')
                    elif work_status == 'D': statuses.add('deleted')
                    if index_status == '?' and work_status == '?': statuses.add('untracked')

            if 'added' in statuses: status_indicators += '✚'
            if 'modified' in statuses: status_indicators += '✹'
            if 'deleted' in statuses: status_indicators += '✖'
            if 'untracked' in statuses: status_indicators += '✭'
    except:
        pass

    branch_emoji = '🏠' if is_main else '🌿'
    branch_str = f"{branch_emoji} {branch}"
    if status_indicators:
        branch_str += f" {status_indicators}"

    return branch_str, is_main

def get_usage_info(transcript_path):
    """Parse transcript to get usage info."""
    context_used = 0
    model_name = "Gemini"

    try:
        if not os.path.exists(transcript_path):
            return context_used, model_name

        with open(transcript_path, 'r') as f:
            data = json.load(f)

        # Gemini transcript is typically a JSON array of messages
        # Find the last model message with usage_metadata
        for message in reversed(data):
            if message.get('role') == 'model' and 'usage_metadata' in message:
                usage = message['usage_metadata']
                context_used = usage.get('total_tokens', 0)
                model_name = usage.get('model_name', model_name)
                break
    except Exception as e:
        # If it's JSONL (older/different format), try reading last line
        try:
            with open(transcript_path, 'r') as f:
                for line in reversed(f.readlines()):
                    if not line.strip(): continue
                    obj = json.loads(line)
                    if obj.get('role') == 'model' and 'usage_metadata' in obj:
                        usage = obj['usage_metadata']
                        context_used = usage.get('total_tokens', 0)
                        model_name = usage.get('model_name', model_name)
                        break
        except:
            pass

    return context_used, model_name

# =============================================================================
# Main
# =============================================================================
def main():
    try:
        # Read hook input from stdin
        input_data = json.load(sys.stdin)
        cwd = input_data.get('cwd', os.getcwd())
        transcript_path = input_data.get('transcript_path')

        if not transcript_path:
            # Fallback for common locations if not provided
            print(json.dumps({"systemMessage": "Error: transcript_path not provided to hook"}))
            return

        # Get usage and model info
        context_used, model_name = get_usage_info(transcript_path)
        
        # Get git info
        git_branch, _ = get_git_info(cwd)

        # Calculate percentage
        context_percentage = (context_used / CONTEXT_LIMIT) * 100
        context_color = get_context_color(context_percentage)
        model_emoji = get_model_emoji(model_name)
        current_dir = os.path.basename(cwd)

        # Build status line
        parts = [
            f"{model_emoji} {model_name}",
            f"📁 {current_dir}",
        ]
        if git_branch:
            parts.append(git_branch)
        parts.append(f"{context_color} {context_percentage:.1f}% ({context_used:,}/{CONTEXT_LIMIT:,})")

        status_line = " | ".join(parts)

        # Output to Gemini via systemMessage
        output = {
            "systemMessage": f"
{status_line}
"
        }
        print(json.dumps(output))

    except Exception as e:
        # Don't break the agent on hook errors, but log silently
        # print(f"Hook error: {e}", file=sys.stderr)
        print(json.dumps({}))

if __name__ == '__main__':
    main()
