# ContextIQ

### Retrieval-Augmented Document Q&A

ContextIQ is a lightweight **Retrieval-Augmented Generation (RAG)** application that answers questions using information retrieved from a custom knowledge base.

The project demonstrates the core RAG pipeline, including **document processing, text chunking, embeddings, vector storage, semantic retrieval, context augmentation, and grounded LLM generation**, using locally hosted models through Ollama.

---

## How It Works

ContextIQ follows a straightforward retrieval-augmented generation pipeline:

```text
Knowledge Base
      ↓
Text Chunking
      ↓
Embeddings
      ↓
Chroma Vector Store
      ↓
Similarity Search
      ↓
Relevant Context
      ↓
Llama 2
      ↓
Grounded Answer
```

When a user submits a question:

1. The knowledge base is loaded and divided into smaller chunks.
2. Each chunk is converted into a numerical embedding.
3. The embeddings are stored in **Chroma**.
4. The user's question is converted into an embedding and compared against the stored vectors.
5. The most relevant chunks are retrieved from the knowledge base.
6. The retrieved information is provided to **Llama 2** as contextual information.
7. Llama 2 generates a response grounded in the retrieved context.

---

## Features

* Question answering over a custom knowledge base
* Semantic similarity-based retrieval
* Local text embeddings using `nomic-embed-text`
* Local vector storage using Chroma
* Local LLM inference using Llama 2 and Ollama
* Context-grounded responses
* No external LLM API key required
* Lightweight Python-based implementation

---

## Tech Stack

| Technology           | Purpose                                   |
| -------------------- | ----------------------------------------- |
| **Python**           | Core application and RAG pipeline         |
| **LangChain**        | RAG pipeline components and orchestration |
| **Ollama**           | Local model execution                     |
| **Llama 2**          | Response generation                       |
| **nomic-embed-text** | Text embeddings                           |
| **Chroma**           | Vector storage and similarity search      |

---

## Project Structure

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

## Installation

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd ContextIQ
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama Models

Make sure [Ollama](https://ollama.com/) is installed on your system.

Pull the Llama 2 model:

```bash
ollama pull llama2
```

Pull the embedding model:

```bash
ollama pull nomic-embed-text
```

---

## Running ContextIQ

Start the Llama 2 model through Ollama:

```bash
ollama run llama2
```

Then, in the project terminal, run:

```bash
python rag.py
```

ContextIQ will prompt you to enter a question:

```text
Ask ContextIQ a question:
```

---

## Example

### Question

```text
What is Chroma used for?
```

### Response

```text
Chroma is used as the local vector store for ContextIQ.
```

### Grounding Test

ContextIQ is designed to avoid generating unsupported information when the requested information is not present in the knowledge base.

For example, if asked:

```text
What is the population of India?
```

when that information is not included in the knowledge base, the system responds that the information is unavailable rather than intentionally generating an unsupported answer.

---

## Core RAG Components

### 1. Document Chunking

The knowledge base is divided into smaller text segments to allow relevant information to be retrieved efficiently.

### 2. Embeddings

The `nomic-embed-text` model converts text into numerical representations that capture semantic relationships between pieces of information.

### 3. Vector Store

Chroma stores the generated embeddings and enables efficient similarity-based retrieval.

### 4. Retrieval

When a question is submitted, ContextIQ performs a similarity search against the stored embeddings and retrieves the most relevant sections of the knowledge base.

### 5. Context Augmentation

The retrieved information is added to the prompt provided to the language model, giving the model relevant context for generating its response.

### 6. Generation

Llama 2 uses the retrieved context to generate the final answer.

---

## Learning Outcomes

This project was developed as a hands-on exploration of **Retrieval-Augmented Generation** and demonstrates the following concepts:

* Document processing
* Text chunking
* Text embeddings
* Vector databases
* Semantic search
* Similarity-based retrieval
* Context augmentation
* LLM-based generation
* Grounded question answering

---

## Future Improvements

Potential extensions include:

* PDF and multi-document ingestion
* Advanced text-splitting strategies
* Metadata-based filtering
* Hybrid keyword and semantic search
* Retrieval reranking
* FastAPI REST API
* Web-based chat interface
* RAG evaluation and retrieval metrics

---

## Author

**Urvee S Bettadapur**

ContextIQ was developed as a hands-on project to explore **Retrieval-Augmented Generation, semantic retrieval, vector databases, and locally hosted LLM applications**.