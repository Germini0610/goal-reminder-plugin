#!/usr/bin/env python3
"""
UserPromptSubmit Hook：
- 每次送出 prompt 都自動覆蓋目標
- 忽略 slash commands（/goal, /help 等）
"""
import sys
import os
import json

GOAL_DIR = os.path.expanduser("~/.claude/plugins/goal-reminder/sessions")

def get_goal_file(session_id):
    return os.path.join(GOAL_DIR, f"{session_id}.txt")

def main():
    # 讀取 hook 傳入的 JSON（stdin）
    try:
        data = json.load(sys.stdin)
        prompt = data.get("prompt", "").strip()
        session_id = data.get("session_id", "default")
    except Exception:
        prompt = ""
        session_id = "default"

    if not prompt:
        sys.exit(0)

    # 忽略 slash commands（/goal, /help 等）
    if prompt.startswith("/"):
        sys.exit(0)

    # 每次都覆蓋，永遠顯示最新的 prompt（per session）
    os.makedirs(GOAL_DIR, exist_ok=True)
    first_line = prompt.splitlines()[0].strip()
    goal_text = first_line if len(first_line) <= 80 else first_line[:77] + "..."
    with open(get_goal_file(session_id), "w", encoding="utf-8") as f:
        f.write(goal_text)

    sys.exit(0)

if __name__ == "__main__":
    main()
