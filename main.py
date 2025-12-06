import sys
import os

# Add src to path so imports work correctly when running `streamlit run main.py`
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

import streamlit as st
from src.chains import ask_gemini  # now imported from src/chains.py

st.set_page_config(page_title="Gemini Python Copilot", page_icon="💻")
st.title("Gemini Python Copilot")

st.caption("Built with LangChain, Google Gemini, and Streamlit.")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask anything (Related to Python Only..)")

if user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer = ask_gemini(user_input)
            st.markdown(answer)

    st.session_state["messages"].append({"role": "assistant", "content": answer})
