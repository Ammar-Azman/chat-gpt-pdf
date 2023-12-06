import streamlit as st

import importlib
import backend.utils
importlib.reload(backend.utils)
from backend.utils import (get_openapi_access_key, 
                            get_text_from_pdf, 
                            get_text_chunks, 
                            get_vectorstore, 
                            get_conversation_chain)

OPEN_API_KEY = get_openapi_access_key()



def side_bar():
    with st.sidebar:
        st.subheader("Your documents")

        pdf_docs = st.file_uploader("Upload your pdf here 👇", 
                                    accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing..."):
                # raw text
                raw_text:str = get_text_from_pdf(pdf_docs)

                # text chunks
                text_chunks:list = get_text_chunks(raw_text)

                # vector embedding
                vector_embedding = get_vectorstore(text_chunks)

                # conversation chain
                # initialize state
                st.session_state.conversation = get_conversation_chain(vector_embedding)

def initialize_conversation_state():
    if "conversation" not in st.session_state:
        st.session_state.conversation = None

def main():

    st.set_page_config(page_title="Chatting with PDF yo!", 
                        page_icon="🤖")
    
    st.header("Chat with multiple PDFs 📑")
    st.text_input("Ask any question about the file")

    initialize_conversation_state()

    side_bar()    

if __name__ == "__main__":
    main()