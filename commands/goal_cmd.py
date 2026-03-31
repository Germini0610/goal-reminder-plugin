#!/usr/bin/env python3
"""
/goal 指令處理器
用法：
  /goal <新需求>   → 設定/覆蓋目標
  /goal            → 顯示目前目標
  /goal clear      → 清除目標（下次輸入 prompt 會重新捕捉）
"""
import sys
import os

GOAL_DIR = os.path.expanduser("~/.claude/plugins/goal-reminder/sessions")

def get_goal_file():
    session_id = os.environ.get("CLAUDE_SESSION_ID", "default")
    return os.path.join(GOAL_DIR, f"{session_id}.txt")

def main():
    args = " ".join(sys.argv[1:]).strip() if len(sys.argv) > 1 else ""

    os.makedirs(GOAL_DIR, exist_ok=True)
    goal_file = get_goal_file()

    # /goal clear → 清除
    if args.lower() == "clear":
        if os.path.exists(goal_file):
            os.remove(goal_file)
        print("✅ 目標已清除。下次輸入 prompt 時將自動記錄為新目標。")
        return

    # /goal <文字> → 設定
    if args:
        goal_text = args if len(args) <= 120 else args[:117] + "..."
        with open(goal_file, "w", encoding="utf-8") as f:
            f.write(goal_text)
        print(f"✅ 目標已設定：{goal_text}")
        return

    # /goal（無參數）→ 顯示
    if os.path.exists(goal_file):
        with open(goal_file, "r", encoding="utf-8") as f:
            goal = f.read().strip()
        print(f"🎯 當前目標：{goal}")
    else:
        print("💡 尚未設定目標。使用 /goal <你的需求> 來設定，或直接輸入第一個 prompt 自動捕捉。")

if __name__ == "__main__":
    main()
