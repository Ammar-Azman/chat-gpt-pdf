import importlib
import backend.utils

import streamlit as st

importlib.reload(backend.utils)
from backend.utils import get_openapi_access_key
from components import (
    side_bar,
    initial_conversation_state,
    initial_chat_history_state,
    initial_model_state,
    handle_user_input,
)
from html_template import css

OPEN_API_KEY = get_openapi_access_key()


def main():
    st.set_page_config(page_title="Chatting with PDF yo!", page_icon="🤖")

    st.write(css, unsafe_allow_html=True)
    with st.container(border=True):
        st.header("Chat with multiple PDFs 📑")

    initial_model_state()
    initial_conversation_state()
    initial_chat_history_state()

    user_question = st.chat_input("Ask about your files!")
    if user_question:
        handle_user_input(user_question)

    side_bar()


if __name__ == "__main__":
    main()
