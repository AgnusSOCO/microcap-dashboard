
import os, streamlit as st, pandas as pd, numpy as np, datetime as dt
from utils.data import load_positions, load_orders, load_equity_curve, load_llm_logs, compute_account_kpis, calc_sector_alloc, stops_targets, has_env_creds
from utils.plotting import line_equity, pie_alloc, bar_pl

st.set_page_config(page_title="Micro-Cap LLM Trader", layout="wide", page_icon="📈")

st.markdown("# 📈 Micro‑Cap LLM Trader — Control Center")
colL, colR = st.columns([3,2])

with colL:
    eq = load_equity_curve('sample_data/equity_curve.csv')
    st.plotly_chart(line_equity(eq), use_container_width=True)
with colR:
    positions = load_positions('sample_data/positions.csv')
    k = compute_account_kpis(positions, eq)
    st.metric("Market Value", f"${k['market_value']:,.0f}")
    st.metric("Cash", f"${k['cash']:,.0f}")
    st.metric("Unrealized P/L", f"${k['unrealized_pl']:,.0f}")
    st.metric("Exposure", f"{k['exposure']*100:.1f}%")
    st.metric("Max Drawdown", f"{k['drawdown']*100:.1f}%")

st.divider()
c1, c2 = st.columns([2,3])
with c1:
    alloc = calc_sector_alloc(positions)
    st.subheader("Sector Allocation")
    if not alloc.empty:
        st.plotly_chart(pie_alloc(alloc), use_container_width=True)
    else:
        st.info("No positions loaded yet.")
with c2:
    st.subheader("Position P/L")
    if not positions.empty:
        st.plotly_chart(bar_pl(positions), use_container_width=True)
    st.dataframe(stops_targets(positions))

st.divider()
st.subheader("System Status")
live = has_env_creds()
st.write("Mode:", "🟢 Live" if live else "🧪 Paper / Sample")
st.caption("Switch to live by setting ALPACA_API_KEY and ALPACA_SECRET_KEY in environment or Streamlit secrets.")
