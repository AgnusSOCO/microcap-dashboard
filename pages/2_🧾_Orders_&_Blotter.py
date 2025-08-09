
import streamlit as st, pandas as pd
from utils.data import load_orders

st.set_page_config(layout="wide")
st.markdown("## 🧾 Orders & Blotter")
df = load_orders('sample_data/orders.csv')
status = st.multiselect("Status", options=sorted(df['status'].unique()), default=list(sorted(df['status'].unique())))
st.dataframe(df[df['status'].isin(status)], use_container_width=True)
