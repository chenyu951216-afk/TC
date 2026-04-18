# TW Stock News Ranking Bot

台股消息驅動 + 市場數據評分 + OpenAI 建議層 + 持股追蹤通知系統。

## 功能
- 每日產生可下單候選股前 5 名（可調整）
- 固定顯示股票編號、股票名稱、產業、題材、理由、風險、止損止盈
- 排名產生前，先整理新聞與事件，再送 OpenAI 產出「建議層」分析
- OpenAI 僅作考量之一，不直接覆蓋系統分數
- 可勾選「我已下單」，進入持股追蹤
- 持股追蹤會監控趨勢、產業熱度、新聞變化與 thesis 是否失效
- 提供黃燈 / 橘燈 / 紅燈警示
- 內建 GitHub 可用資料夾結構，所有程式都在 `app/` 路徑底下

## 專案結構
```text
app/
  main.py
  core/
  routers/
  services/
  tasks/
  templates/
  static/
  data/
```

## 快速啟動
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

開啟：`http://127.0.0.1:8000`

## OpenAI 分析層
系統會在出排名前先整理：
- 市場摘要
- 產業強弱
- 個股候選池
- 新聞與事件

再送給 OpenAI 做：
- 市場主線
- 題材摘要
- 候選股加減分建議
- 風險提醒

預設 `USE_OPENAI_ANALYSIS=false`，若要啟用請在 `.env` 設定：
```env
OPENAI_API_KEY=你的 key
USE_OPENAI_ANALYSIS=true
OPENAI_MODEL=gpt-4.1-mini
```

本專案採用 OpenAI 官方建議的結構化輸出思路，讓模型回傳固定 JSON 欄位，比較適合接到你的評分引擎。官方文件指出 Responses API 與 function calling / structured outputs 適合這類需要可靠 JSON 的工作流程。citeturn744773search0turn744773search9

## 止損止盈設計
本專案為 3–10 天波段設計的預設規則：
- 初始止損：`min(20日低點, 收盤價 - 1.8 * ATR14)`，但風險距離至少 3%，最多 10%
- 目標一：1.5R
- 目標二：2.5R
- 目標三：4.0R
- 追蹤中若 thesis 失效，優先發出風險通知

## 後續接真實資料
目前提供：
- 可執行的完整 UI / API / 排名引擎 / 風控引擎 / watchlist
- 範例市場與新聞資料
- 真實資料接點的抽象介面

之後只要把 `app/services/news_service.py` 與 `app/services/market_service.py` 中的 sample provider 換成你要的台股資料來源即可。
