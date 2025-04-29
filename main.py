import streamlit as st
from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
import os
import time

load_dotenv()
agent = Agent(
    model=Groq(id="compound-beta", api_key=os.getenv("GROQ_API_KEY")),
    markdown=True,
    instructions=["Answer user queries using real-time info."]
)

st.set_page_config(page_title="Agno Chat")
st.title("💬 Chat with Compound-Beta")

if "history" not in st.session_state:
    st.session_state.history = []

# ✅ Show chat history
for role, msg in st.session_state.history:
    with st.chat_message(role):
        st.markdown(msg)

# ✅ Handle user input
user_input = st.chat_input("Ask something...")
if user_input:
    st.session_state.history.append(("user", user_input))
    with st.chat_message("user"):  
        st.markdown(user_input)

    with st.chat_message("assistant"):
        response_obj = agent.run(user_input)
        response = response_obj.content or ""
        placeholder = st.empty()
        streamed = ""
        for ch in response:
            streamed += ch
            placeholder.markdown(streamed + "▌")
            time.sleep(0.01)
        placeholder.markdown(streamed)
        st.session_state.history.append(("assistant", streamed))
