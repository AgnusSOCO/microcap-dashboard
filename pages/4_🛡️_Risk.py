
import streamlit as st, pandas as pd, numpy as np
from utils.data import load_positions

st.set_page_config(layout="wide")
st.markdown("## 🛡️ Risk Dashboard")
df = load_positions('sample_data/positions.csv')
if df.empty:
    st.info("No positions to evaluate risk.")
else:
    caps = {
        "max_pos_weight": 0.10,
        "daily_loss_cap": 0.06,
        "warn_1": 0.045,
        "warn_2": 0.054
    }
    st.json(caps)
    df['weight'] = df['market_value'] / df['market_value'].sum()
    df['atr_risk_$'] = df['atr'] * df['price'] * df['shares']
    st.dataframe(df[['symbol','weight','atr','atr_risk_$','spread_bps','adv']], use_container_width=True)
