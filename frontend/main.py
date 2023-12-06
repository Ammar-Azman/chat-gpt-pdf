import streamlit as st

import importlib
import backend.utils
importlib.reload(backend.utils)
from backend.utils import get_openapi_access_key
from components import side_bar, initialize_conversation_state, handle_user_input
from html_template import css, bot_template, user_template

OPEN_API_KEY = get_openapi_access_key()

def main():

    st.set_page_config(page_title="Chatting with PDF yo!", 
                        page_icon="🤖")
    
    st.write(css, unsafe_allow_html=True)
    
    st.header("Chat with multiple PDFs 📑")
    user_question = st.text_input("Ask any question about the file")
    if user_question:
        handle_user_input(user_question)

    st.write(user_template.replace("{{MSG}}", "Hello AI!"), unsafe_allow_html=True)
    st.write(bot_template.replace("{{MSG}}", "Hello human!"), unsafe_allow_html=True)

    initialize_conversation_state()

    side_bar()    

if __name__ == "__main__":
    main()