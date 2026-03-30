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

GOAL_FILE = os.path.expanduser("~/.claude/plugins/goal-reminder/current_goal.txt")

def main():
    args = " ".join(sys.argv[1:]).strip() if len(sys.argv) > 1 else ""

    os.makedirs(os.path.dirname(GOAL_FILE), exist_ok=True)

    # /goal clear → 清除
    if args.lower() == "clear":
        if os.path.exists(GOAL_FILE):
            os.remove(GOAL_FILE)
        print("✅ 目標已清除。下次輸入 prompt 時將自動記錄為新目標。")
        return

    # /goal <文字> → 設定
    if args:
        goal_text = args if len(args) <= 120 else args[:117] + "..."
        with open(GOAL_FILE, "w", encoding="utf-8") as f:
            f.write(goal_text)
        print(f"✅ 目標已設定：{goal_text}")
        return

    # /goal（無參數）→ 顯示
    if os.path.exists(GOAL_FILE):
        with open(GOAL_FILE, "r", encoding="utf-8") as f:
            goal = f.read().strip()
        print(f"🎯 當前目標：{goal}")
    else:
        print("💡 尚未設定目標。使用 /goal <你的需求> 來設定，或直接輸入第一個 prompt 自動捕捉。")

if __name__ == "__main__":
    main()
