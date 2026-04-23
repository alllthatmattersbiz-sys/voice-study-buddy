import streamlit as st
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Voice Study Buddy", layout="wide")
st.title("🎓 Voice Study Buddy")
st.write("Ask me anything and I'll help you learn!")

API_KEY = os.getenv("ANTHROPIC_API_KEY")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display conversation
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Input box
user_input = st.chat_input("Ask a question...")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.write(user_input)
    
    # Call Claude via HTTP
    try:
        response = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "x-api-key": API_KEY,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json"
            },
            json={
                "model": "claude-haiku-4-5-20251001",
                "max_tokens": 500,
                "system": "You are a helpful study buddy. Explain concepts clearly.",
                "messages": st.session_state.messages
            }
        )
        
        data = response.json()
        assistant_message = data['content'][0]['text']
        st.session_state.messages.append({"role": "assistant", "content": assistant_message})
        
        with st.chat_message("assistant"):
            st.write(assistant_message)
    
    except Exception as e:
        st.error(f"Error: {str(e)}")