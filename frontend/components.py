import streamlit as st
from backend.utils import (
    get_text_from_pdf,
    get_text_chunks,
    get_vectorstore,
    get_conversation_chain,
)


def side_bar():
    with st.sidebar:
        st.subheader("Your documents")

        pdf_docs = st.file_uploader(
            label="Upload your pdf here", accept_multiple_files=True
        )

        if st.button("Process"):
            if not pdf_docs:
                st.error("ERROR: No files uploaded")
                return

            with st.spinner("Processing..."):
                # raw text
                raw_text: str = get_text_from_pdf(pdf_docs)

                # text chunks
                text_chunks: list = get_text_chunks(raw_text)

                # vector embedding
                vector_embedding = get_vectorstore(text_chunks)

                # conversation chain
                # initialize state
                st.session_state.conversation = get_conversation_chain(vector_embedding)


def initialize_conversation_state():
    if "conversation" not in st.session_state:
        st.session_state.conversation = None


def handle_user_input(user_question: str):
    """
    Initialize state to ensure the apps
    remember the conversation.

    """
    response = st.session_state.conversation({"question": user_question})
    st.write(response)
