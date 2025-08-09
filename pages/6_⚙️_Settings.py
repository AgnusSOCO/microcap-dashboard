
import streamlit as st, os

st.set_page_config(layout="wide")
st.markdown("## ⚙️ Settings")
st.caption("Provide API keys to enable live mode (env vars or Streamlit secrets).")

with st.expander("Environment Variables"):
    st.code("export ALPACA_API_KEY=...\nexport ALPACA_SECRET_KEY=...")

with st.form("secrets"):
    api = st.text_input("ALPACA_API_KEY", value=os.getenv("ALPACA_API_KEY",""))
    sec = st.text_input("ALPACA_SECRET_KEY", value=os.getenv("ALPACA_SECRET_KEY",""), type="password")
    submitted = st.form_submit_button("Save (session only)")
    if submitted:
        st.session_state['ALPACA_API_KEY']=api
        st.session_state['ALPACA_SECRET_KEY']=sec
        st.success("Saved in session (restart app to clear).")
