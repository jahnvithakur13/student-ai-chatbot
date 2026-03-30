import streamlit as st
from chatbot import get_ai_response
from database import save_chat, get_chats

st.set_page_config(page_title="Student AI Chatbot", layout="centered")

st.title("🎓 Student AI Assistant Chatbot")
st.write("Ask your academic doubts!")
user_input = st.text_input("You:")

if st.button("Send"):
    if user_input:
        response = get_ai_response(user_input)
        save_chat(user_input, response)

        st.success("Bot: " + response)

st.sidebar.title("📜 Chat History")

history = get_chats()

for user, bot in history:
    st.sidebar.write("🧑 You:", user)
    st.sidebar.write("🤖 Bot:", bot)
    st.sidebar.write("---")