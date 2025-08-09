
import streamlit as st, pandas as pd, json
from utils.data import load_llm_logs

st.set_page_config(layout="wide")
st.markdown("## 🧠 Research (LLM Audit)")

logs = load_llm_logs('sample_data/llm_logs.jsonl')
if not logs:
    st.info("No LLM logs yet.")
else:
    sym = st.selectbox("Symbol", options=sorted(set(r['symbol'] for r in logs)))
    filtered = [r for r in logs if r['symbol']==sym]
    for r in filtered[:200]:
        with st.expander(f"{r['ts']} — {r['symbol']}"):
            st.json(r)
