from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq


# load the env variables
load_dotenv()

# streamlit page setup
st.set_page_config(
    page_title="Chatbot",
    page_icon="🤖",
    layout="centered",
)
# Remove default top padding (optional)
st.markdown(
    """
    <style>
    .main { padding-top: 0rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <h1 style="text-align:center;">
        
        <span style="color:#1E90FF;">KunAI:</span>
        <span style="color:#32CD32;">Samvaad</span>
        <span style="color:#FF4B4B;">💬</span>
    </h1>
    """,
    unsafe_allow_html=True,
)
# Change full app background color
st.markdown(
    """
    <style>
    .stApp {
        # background: linear-gradient(to bottom right, #0f172a, #1e293b); /* dark blue gradient */
        background: linear-gradient(to bottom right, #e0f7df, #b2f2bb); /* light green gradient */
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
# st.title("💬Kundan Ki Kalam se: Up for an AI flavored Samvaad ?")

# initiate chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# show chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# llm initiate
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.0,
)

# input box
user_prompt = st.chat_input("Let's chat...")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    response = llm.invoke(
        input = [{"role": "system", "content": "You are a helpful assistant"}, *st.session_state.chat_history]
    )
    assistant_response = response.content
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    with st.chat_message("assistant"):
        st.markdown(assistant_response)
