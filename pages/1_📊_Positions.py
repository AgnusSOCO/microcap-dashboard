
import streamlit as st, pandas as pd
from utils.data import load_positions, stops_targets

st.set_page_config(layout="wide")
st.markdown("## 📊 Positions")
df = load_positions('sample_data/positions.csv')
if df.empty:
    st.warning("No positions available.")
else:
    st.dataframe(stops_targets(df), use_container_width=True)
