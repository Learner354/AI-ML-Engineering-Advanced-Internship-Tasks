# Context-Aware PDF Chatbot using LangChain + RAG

A conversational chatbot that remembers context and retrieves external information from PDF documents using Retrieval-Augmented Generation (RAG), powered by LangChain, HuggingFace embeddings, and OpenAI (via GitHub proxy).

---

## 📥 Clone the Repository

```bash
git clone https://github.com/Learner354/AI-ML-Engineering-Advanced-Internship-Tasks.git
cd AI-ML-Engineering-Advanced-Internship-Tasks/Task\ 4:\ Context-Aware\ Chatbot\ Using\ LangChain\ or\ RAG
```

---

## 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the App

```bash
streamlit run chatbot.py
```

---

## 🔑 Configuration

Make sure you have a GitHub-proxy OpenAI API key. In the code, set:

```python
client = OpenAI(
    api_key="ghp_XXXXXXXXXXXXXXXXXXXXXXXXXXX",  # Replace with your token
    base_url="https://models.github.ai/inference/v1"
)
```

---

## How It Works

- User uploads a PDF via Streamlit.
- The PDF is loaded, split into chunks, and vectorized using `HuggingFaceEmbeddings`.
- A `FAISS` vectorstore is created in memory.

### LangChain `ConversationalRetrievalChain` uses:
- OpenAI LLM (via GitHub proxy)
- Document retriever
- Chat history memory

The user can interact in real-time, and the chatbot answers using both:
- Retrieved document context
- Previous conversation memory

---

## Technologies Used

- LangChain
- HuggingFace Transformers & SentenceTransformers
- FAISS (Facebook AI Similarity Search)
- Streamlit
- OpenAI API (GitHub proxy)
- PyPDFLoader

---

## 📁 Project Structure

```bash
.
├── chatbot.py           # Streamlit app with full chatbot logic
├── requirements.txt     # All Python dependencies
└── README.md            # This file
```

---
