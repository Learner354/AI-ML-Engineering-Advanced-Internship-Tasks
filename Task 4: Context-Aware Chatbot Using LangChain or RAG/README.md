# 📄 Chat with Your PDF — RAG Chatbot with Context Memory

A conversational chatbot powered by **LangChain**, **HuggingFace embeddings**, and **OpenAI (via GitHub proxy)**. Upload any PDF and ask questions about its contents. The chatbot uses **Retrieval-Augmented Generation (RAG)** and remembers chat context during your conversation.

---

## 🚀 Features

- 🔍 **Retrieval-Augmented Generation (RAG)** with LangChain
- 🧠 **Context memory** using `ConversationBufferMemory`
- 📄 Upload and query **custom PDF documents**
- 🧾 Uses **HuggingFace embeddings** + **FAISS** for fast vector search
- 💬 Fully interactive **Streamlit** interface
- 🔐 Connects to **OpenAI-compatible GitHub proxy**

---

## 🛠️ Tech Stack

- [LangChain](https://github.com/langchain-ai/langchain)
- [HuggingFace Transformers & SentenceTransformers](https://huggingface.co/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [OpenAI API (via GitHub proxy)](https://github.com/openai/openai-python)
- [Streamlit](https://streamlit.io/)

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/Learner354/AI-ML-Engineering-Advanced-Internship-Tasks/Task 4: Context-Aware Chatbot Using LangChain or RAG/chatbot.py
cd pdf-chatbot
---
## Install dependencies

```bash
pip install -r requirements.txt
---
## Run the app

bash
Copy
Edit
streamlit run app.py
## 🔑 Configuration
Make sure you have a GitHub-proxy OpenAI API key. In the code, set:

```python

client = OpenAI(
    api_key="ghp_XXXXXXXXXXXXXXXXXXXXXXXXXXX",
    base_url="https://models.github.ai/inference/v1"
)
---

## How It Works
- User uploads a PDF via Streamlit.
- The PDF is loaded, split into chunks, and vectorized using HuggingFaceEmbeddings.
- A FAISS vectorstore is created in memory.

##LangChain ConversationalRetrievalChain uses:
- OpenAI LLM (via GitHub proxy)
- Document retriever
- Chat history memory

User interacts in real-time, asking questions that are answered using both document retrieval + chat history.
