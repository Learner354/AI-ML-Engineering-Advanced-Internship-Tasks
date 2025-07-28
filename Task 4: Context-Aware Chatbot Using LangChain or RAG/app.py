import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import OpenAI as LangchainOpenAI
from openai import OpenAI
import tempfile
import os

# Configure OpenAI GitHub proxy client
client = OpenAI(
    api_key="ghp_XXXXXXXXXXXXXXX",  # Replace with your GitHub token actual removed for security reason
    base_url="https://models.github.ai/inference/v1"
)

st.set_page_config(page_title="Chat with PDF", layout="wide")
st.title("📄 RAG Chatbot with PDF + Memory")

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    # Load and split PDF
    loader = PyPDFLoader(tmp_path)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(documents)

    # Embeddings and vector DB
    embeddings = HuggingFaceEmbeddings()
    vectorstore = FAISS.from_documents(chunks, embeddings)

    # Memory for conversation history
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    # LangChain-compatible LLM using proxy
    llm = LangchainOpenAI(
        openai_api_key=client.api_key,
        base_url=client.base_url,
        model_name="gpt-4.1"
    )

    # Create Conversational RAG chain
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 4}),
        memory=memory,
        verbose=True
    )

    # Display chat messages
    for msg in st.session_state.chat_history:
        st.chat_message(msg['role']).markdown(msg['content'])

    # User input
    prompt = st.chat_input("Ask a question about the document...")
    if prompt:
        st.chat_message("user").markdown(prompt)
        st.session_state.chat_history.append({'role': 'user', 'content': prompt})

        try:
            result = qa_chain.run(prompt)
            st.chat_message("assistant").markdown(result)
            st.session_state.chat_history.append({'role': 'assistant', 'content': result})
        except Exception as e:
            error_msg = f"❌ Error: {str(e)}"
            st.chat_message("assistant").markdown(error_msg)
            st.session_state.chat_history.append({'role': 'assistant', 'content': error_msg})

    # Cleanup uploaded file
    os.remove(tmp_path)
else:
    st.info("📥 Please upload a PDF file to begin.")
