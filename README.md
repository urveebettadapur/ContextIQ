# 🧠 ContextIQ

### Retrieval-Augmented Document Q&A

ContextIQ is a lightweight **Retrieval-Augmented Generation (RAG)** application that answers questions using information retrieved from a custom knowledge base.

The project demonstrates the fundamental RAG pipeline — **document processing, embeddings, vector storage, semantic retrieval, and context-grounded LLM generation** — using locally hosted models through Ollama.

---

## 🚀 How It Works

ContextIQ follows a simple RAG pipeline:

```text
📄 Knowledge Base
       ↓
✂️ Text Chunking
       ↓
🔢 Embeddings
       ↓
🗄️ Chroma Vector Store
       ↓
🔎 Similarity Search
       ↓
📚 Relevant Context
       ↓
🤖 Llama 2
       ↓
💬 Grounded Answer
```

When a user asks a question:

1. The knowledge base is loaded and divided into smaller chunks.
2. Each chunk is converted into a numerical embedding.
3. The embeddings are stored in **Chroma**.
4. The user's question is compared against the stored embeddings.
5. The most relevant chunks are retrieved.
6. The retrieved information is provided to **Llama 2** as context.
7. Llama 2 generates an answer based on the retrieved information.

---

## ✨ Features

* 📚 Question answering over a custom knowledge base
* 🔎 Semantic similarity-based retrieval
* 🧠 Local text embeddings using `nomic-embed-text`
* 🗄️ Local vector storage using Chroma
* 🤖 Local LLM inference using Llama 2 and Ollama
* 🛡️ Context-grounded responses
* 🔐 No external LLM API key required
* 🐍 Simple Python-based implementation

---

## 🛠️ Tech Stack

| Technology           | Purpose                              |
| -------------------- | ------------------------------------ |
| **Python**           | Core application                     |
| **LangChain**        | RAG pipeline components              |
| **Ollama**           | Local model execution                |
| **Llama 2**          | Response generation                  |
| **nomic-embed-text** | Text embeddings                      |
| **Chroma**           | Vector storage and similarity search |

---

## 📁 Project Structure

```text
ContextIQ/
│
├── knowledge.txt       # Custom knowledge base
├── rag.py              # RAG pipeline
├── requirements.txt    # Python dependencies
├── .gitignore          # Ignored files
└── README.md           # Project documentation
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd ContextIQ
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Install the Ollama models

Make sure [Ollama](https://ollama.com/) is installed.

Pull the Llama 2 model:

```bash
ollama pull llama2
```

Pull the embedding model:

```bash
ollama pull nomic-embed-text
```

---

## ▶️ Running ContextIQ

Start Ollama's Llama 2 model:

```bash
ollama run llama2
```

Then, in the project terminal, run:

```bash
python rag.py
```

ContextIQ will prompt you for a question:

```text
Ask ContextIQ a question:
```

---

## 💡 Example

### Question

```text
What is Chroma used for?
```

### Response

```text
Chroma is used as the local vector store for ContextIQ.
```

### Grounding Test

If the system is asked something that isn't contained in the knowledge base, such as:

```text
What is the population of India?
```

ContextIQ responds that the information isn't available in the provided knowledge rather than intentionally generating an unsupported answer.

---

## 🧩 Core RAG Components

### 1. Document Chunking

The knowledge base is divided into smaller pieces so that relevant information can be retrieved efficiently.

### 2. Embeddings

The `nomic-embed-text` model converts text into numerical representations that capture semantic meaning.

### 3. Vector Store

Chroma stores the embeddings and enables similarity-based retrieval.

### 4. Retrieval

When a question is asked, ContextIQ performs a similarity search and retrieves the most relevant chunks from the knowledge base.

### 5. Context Augmentation

The retrieved chunks are inserted into the prompt provided to the language model.

### 6. Generation

Llama 2 uses the retrieved context to generate the final response.

---

## 📚 Learning Outcomes

This project was built to understand the fundamentals of **Retrieval-Augmented Generation** and demonstrates:

* Document processing
* Text chunking
* Text embeddings
* Vector databases
* Semantic search
* Similarity retrieval
* Context augmentation
* LLM-based generation
* Grounded question answering

---

## 🔮 Future Improvements

Possible extensions include:

* 📄 PDF and multi-document ingestion
* ✂️ More advanced text splitting
* 🏷️ Metadata filtering
* 🔎 Hybrid keyword + semantic search
* 🎯 Retrieval reranking
* 🌐 FastAPI REST API
* 💻 Web-based chat interface
* 📊 RAG evaluation and retrieval metrics

---

## 👩‍💻 Author

**Urvee Bettadapur**

Built as a hands-on project to explore **Retrieval-Augmented Generation, semantic retrieval, vector databases, and local LLM applications**.
