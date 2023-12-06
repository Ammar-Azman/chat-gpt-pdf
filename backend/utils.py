import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.faiss import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI

def get_openapi_access_key():
    return st.secrets["OPENAPI_KEY"]

def get_text_from_pdf(pdf_docs)-> str:
    """
    Extract all characters in pdf and 
    return string. 

    Params:
    - pdf_docs: pdf_file
    
    """
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    
    return text 

def get_text_chunks(raw_text:str) -> list:
    """
    Split the string return by `get_text_from_pdf()`
    with the respect of chunk size (by character).

    Params:
    - raw_text:str - string extracted from pdf
    
    """
    text_splitter = CharacterTextSplitter(
        separator="\n", 
        chunk_size = 1_000, 
        chunk_overlap = 200, 
        length_function=len
    )
    chunks = text_splitter.split_text(raw_text)
    return chunks

def get_vectorstore(text_chunks:list):
    """
    Using OpenAIEmbedding to vectorize text chunks
    returned by `get_text_chunks()`
    
    Params:
    - text_chunks: list - list of text chunks
    """
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_texts(texts=text_chunks, 
                                    embedding=embeddings)
    return vector_store

def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation_chain  = ConversationalRetrievalChain.from_llm(
        llm = llm, 
        retriever=vectorstore.as_retriever(), 
        memory = memory, 
    )
    return conversation_chain
