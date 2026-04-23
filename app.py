import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Voice Study Buddy", layout="wide")
st.title("🎤 Voice Study Buddy")
st.write("Your AI-powered study partner powered by Claude!")

VAPI_ASSISTANT_ID = os.getenv("VAPI_ASSISTANT_ID")

st.info("""
### 📞 How to Use Voice Study Buddy

You have **two ways** to chat with your AI study buddy:
""")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🎙️ Voice Call")
    st.write("Call your personal study buddy via phone or web")
    if st.button("📱 Start Voice Call"):
        st.markdown(f"""
        [Click here to start a voice call](https://app.vapi.ai/{VAPI_ASSISTANT_ID})
        """)

with col2:
    st.subheader("💬 Text Chat")
    st.write("Ask questions via text in this app")
    user_input = st.chat_input("Ask a study question...")
    
    if user_input:
        st.write(f"**You:** {user_input}")
        st.write("**Study Buddy:** Great question! Claude is thinking...")

st.divider()
st.caption("🚀 Voice Study Buddy | Powered by Claude + Vapi")