import streamlit as st

# utils
def get_openapi_access_key():
    return st.secrets["OPENAPI_KEY"]





def main():

    st.set_page_config(page_title="Chatting with PDF yo!", 
                        page_icon="🤖")
    
    st.header("Chat with multiple PDFs 📑")
    st.text_input("Ask any question about the file")

    with st.sidebar:
        st.subheader("Your documents")
        st.file_uploader("Upload your pdf here 👇")
        st.button("Process")

    


if __name__ == "__main__":
    main()