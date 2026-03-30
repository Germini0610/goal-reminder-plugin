#!/usr/bin/env python3
"""
Status Line：持續在 Terminal 底部顯示當前目標
格式：🎯 目標: <你的需求>
若未設定目標則顯示提示訊息
"""
import os

GOAL_FILE = os.path.expanduser("~/.claude/plugins/goal-reminder/current_goal.txt")

def main():
    if os.path.exists(GOAL_FILE):
        try:
            with open(GOAL_FILE, "r", encoding="utf-8") as f:
                goal = f.read().strip()
            if goal:
                print(f"🎯 目標: {goal}")
                return
        except Exception:
            pass

    # 未設定目標時的提示
    print("💡 尚未設定目標（輸入第一個 prompt 後自動記錄，或使用 /goal <需求> 手動設定）")

if __name__ == "__main__":
    main()
