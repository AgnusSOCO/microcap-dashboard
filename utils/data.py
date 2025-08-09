
import os, json, pandas as pd, numpy as np, datetime as dt

def has_env_creds():
    # Placeholder switches to 'live' if ALPACA_ creds exist
    required = ["ALPACA_API_KEY","ALPACA_SECRET_KEY"]
    return all(os.getenv(k) for k in required)

def load_positions(path='sample_data/positions.csv'):
    if os.path.exists(path):
        df = pd.read_csv(path)
        return df
    return pd.DataFrame(columns=["symbol","sector","price","avg_cost","shares","market_value","unrealized_pl","atr","adv","spread_bps","stop_pct","target_pct"])

def load_orders(path='sample_data/orders.csv'):
    if os.path.exists(path):
        return pd.read_csv(path)
    return pd.DataFrame(columns=["order_id","symbol","side","type","qty","limit_price","status","submitted_at"])

def load_equity_curve(path='sample_data/equity_curve.csv'):
    if os.path.exists(path):
        df = pd.read_csv(path, parse_dates=["date"])
        return df
    return pd.DataFrame(columns=["date","equity","benchmark"])

def load_llm_logs(path='sample_data/llm_logs.jsonl', max_rows=500):
    rows = []
    if os.path.exists(path):
        with open(path, "r") as f:
            for i, line in enumerate(f):
                if i>=max_rows: break
                rows.append(json.loads(line))
    return rows

def compute_account_kpis(positions_df, equity_df):
    mv = float(positions_df["market_value"].sum()) if not positions_df.empty else 0.0
    cash = 100000 - mv if equity_df.empty else float(equity_df.iloc[-1]["equity"]) - mv
    pl_unreal = float(positions_df["unrealized_pl"].sum()) if not positions_df.empty else 0.0
    exposure = mv / max(mv+cash,1e-6)
    dd = 0.0
    if not equity_df.empty:
        cummax = equity_df["equity"].cummax()
        dd = float(((equity_df["equity"] - cummax) / cummax).min())
    return {
        "market_value": mv,
        "cash": cash,
        "unrealized_pl": pl_unreal,
        "exposure": exposure,
        "drawdown": dd
    }

def calc_sector_alloc(positions_df):
    if positions_df.empty: return pd.DataFrame(columns=["sector","alloc"])
    alloc = positions_df.groupby("sector")["market_value"].sum().reset_index()
    alloc["alloc"] = alloc["market_value"] / alloc["market_value"].sum()
    return alloc[["sector","alloc"]]

def stops_targets(positions_df):
    if positions_df.empty: return positions_df
    df = positions_df.copy()
    df["stop_price"] = df["price"] * (1 - df["stop_pct"])
    df["target_price"] = df["price"] * (1 + df["target_pct"])
    return df
