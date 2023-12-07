import streamlit as st
from backend.utils import (
    get_text_from_pdf,
    get_text_chunks,
    get_vectorstore,
    get_conversation_chain,
)
from html_template import user_template, bot_template


def side_bar():
    with st.sidebar:
        st.subheader("Hugginface LLM Model")
        hf_id = st.text_input("Hugginface ID")
        hf_token = st.text_input("Hunggingface Token")

        st.subheader("Your documents")
        pdf_docs = st.file_uploader(
            label="Upload your pdf here", accept_multiple_files=True
        )

        if st.button("Process"):
            if not pdf_docs:
                st.error("ERROR: No files uploaded")
                return

            vector_embedding = processing_input(pdf_docs)
            # conversation chain
            # initialize state
            st.session_state.conversation = get_conversation_chain(
                vector_embedding, hf_id, hf_token
            )

            if hf_id:
                st.session_state.model = hf_id
            else:
                st.session_state.model = "OpenAI Model"

            with st.spinner("Processing..."):
                st.success("Processing completed.")
                st.success("Start asking the AI!")


def processing_input(pdf_docs, hf_id=False, hf_file=False):
    # raw text
    raw_text: str = get_text_from_pdf(pdf_docs)

    # text chunks
    text_chunks: list = get_text_chunks(raw_text)

    # vector embedding
    vector_embedding = get_vectorstore(text_chunks)

    return vector_embedding


def initial_model_state():
    if "model" not in st.session_state:
        st.session_state.model = None


def initial_conversation_state():
    if "conversation" not in st.session_state:
        st.session_state.conversation = None


def initial_chat_history_state():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None


def handle_user_input(user_question: str):
    """
    Initialize state to ensure the apps
    remember the conversation.

    """
    response = st.session_state.conversation({"question": user_question})
    st.session_state.chat_history: list = response["chat_history"]

    model = st.session_state.model
    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(
                user_template.replace("{{MSG}}", f"{message.content}"),
                unsafe_allow_html=True,
            )
        else:
            st.write(
                bot_template.replace("{{MSG}}", f"<--{model}-->\n\n{message.content}"),
                unsafe_allow_html=True,
            )
