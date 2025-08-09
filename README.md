
# Micro‑Cap LLM Trader — Dashboard

Feature‑rich Streamlit dashboard for the ChatGPT Micro‑Cap Experiment. Works out‑of‑the‑box with sample data; switches to live mode when broker credentials are present.

## Quickstart

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Pages
- **Home**: KPIs, equity curve, sector allocation, position P/L.
- **Positions**: Full positions table with stops & targets.
- **Orders & Blotter**: Filterable order history.
- **Research (LLM Audit)**: View JSONL logs of LLM decisions.
- **Risk**: Limits and per‑name risk stats.
- **Backtest**: Load equity curve and compute Sharpe/Sortino/Max DD.
- **Settings**: Configure API keys for live mode.

## Live Mode
Set `ALPACA_API_KEY` and `ALPACA_SECRET_KEY` via environment or Streamlit secrets.

## Data Contracts
- Positions: `sample_data/positions.csv`
- Orders: `sample_data/orders.csv`
- Equity curve: `sample_data/equity_curve.csv`
- LLM logs: `sample_data/llm_logs.jsonl`
