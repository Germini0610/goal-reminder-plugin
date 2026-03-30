# 🎯 goal-reminder — Claude Code Plugin

將你的**原始需求**固定顯示在 Terminal 底部 Status Line，
避免執行長任務時忘記自己的目標。

## 功能

| 功能 | 說明 |
|------|------|
| **自動更新** | 每次送出 prompt 都自動更新目標，永遠顯示最新需求 |
| **Status Line** | 目標持續顯示在 Terminal 底部 |
| `/goal` | 查看目前目標 |
| `/goal <新需求>` | 手動設定/覆蓋目標 |
| `/goal clear` | 清除目標（下次 prompt 重新捕捉） |

## 安裝步驟

### 1. 複製 plugin 到 Claude 設定目錄

```bash
cp -r goal-reminder ~/.claude/plugins/goal-reminder
```

### 2. 加入 Plugin Marketplace（本地）

```bash
claude plugin marketplace add ~/.claude/plugins/goal-reminder/.claude-plugin
```

### 3. 安裝並啟用

在 Claude Code 中輸入：
```
/plugins
```
找到 `goal-reminder` 並啟用，或執行：
```bash
claude plugin install goal-reminder
```

### 4. 重新載入

```
/reload-plugins
```

### 5. 設定 Status Line（若未自動套用）

編輯 `~/.claude/settings.json`，加入：

```json
{
  "statusLine": {
    "type": "command",
    "command": "python3 ~/.claude/plugins/goal-reminder/hooks/status_line.py"
  }
}
```

## 使用方式

```
# 直接輸入你的需求，自動記錄
> 幫我重構 src/api/ 下所有的 service 檔案，改成 async/await 模式

# 底部立即顯示：
🎯 目標: 幫我重構 src/api/ 下所有的 service 檔案，改成 async/await 模式

# 之後不管做了多少步，底部都會持續提醒你
```

## 指令範例

```bash
/goal                          # 查看目前目標
/goal 新增使用者登入功能        # 覆蓋設定新目標
/goal clear                    # 清除，準備開始新任務
```

## 檔案結構

```
goal-reminder/
├── .claude-plugin/
│   └── plugin.json          # Plugin 定義
├── hooks/
│   ├── capture_goal.py      # UserPromptSubmit Hook（自動捕捉）
│   └── status_line.py       # Status Line 顯示腳本
├── commands/
│   └── goal_cmd.py          # /goal 指令處理
└── README.md
```

## 需求

- Claude Code 已安裝（`npm install -g @anthropic-ai/claude-code`）
- Python 3.x（通常已內建）
