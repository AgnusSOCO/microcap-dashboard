
import streamlit as st, pandas as pd, numpy as np
from utils.metrics import sharpe, sortino, max_drawdown

st.set_page_config(layout="wide")
st.markdown("## 🧪 Backtest Review")
uploaded = st.file_uploader("Upload equity curve CSV (date,equity,benchmark optional)", type=['csv'])
if uploaded:
    df = pd.read_csv(uploaded, parse_dates=['date'])
else:
    df = pd.read_csv('sample_data/equity_curve.csv', parse_dates=['date'])

df = df.sort_values('date')
df['ret'] = df['equity'].pct_change().fillna(0.0)
st.line_chart(df.set_index('date')[['equity','benchmark']])
col1, col2, col3 = st.columns(3)
col1.metric("Sharpe", f"{sharpe(df['ret']):.2f}")
col2.metric("Sortino", f"{sortino(df['ret']):.2f}")
col3.metric("Max DD", f"{max_drawdown(df['equity'])*100:.1f}%")
