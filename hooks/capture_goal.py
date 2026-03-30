#!/usr/bin/env python3
"""
UserPromptSubmit Hook：
- 每次送出 prompt 都自動覆蓋目標
- 忽略 slash commands（/goal, /help 等）
"""
import sys
import os
import json

GOAL_FILE = os.path.expanduser("~/.claude/plugins/goal-reminder/current_goal.txt")

def main():
    # 讀取 hook 傳入的 JSON（stdin）
    try:
        data = json.load(sys.stdin)
        prompt = data.get("prompt", "").strip()
    except Exception:
        prompt = ""

    if not prompt:
        sys.exit(0)

    # 忽略 slash commands（/goal, /help 等）
    if prompt.startswith("/"):
        sys.exit(0)

    # 每次都覆蓋，永遠顯示最新的 prompt
    os.makedirs(os.path.dirname(GOAL_FILE), exist_ok=True)
    goal_text = prompt if len(prompt) <= 120 else prompt[:117] + "..."
    with open(GOAL_FILE, "w", encoding="utf-8") as f:
        f.write(goal_text)

    sys.exit(0)

if __name__ == "__main__":
    main()
