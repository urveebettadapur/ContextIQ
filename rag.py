from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_chroma import Chroma
from langchain_core.documents import Document

# Load knowledge base
with open("knowledge.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Split text into chunks
chunks = [text[i:i + 500] for i in range(0, len(text), 500)]
documents = [Document(page_content=chunk) for chunk in chunks]

# Create embeddings
embeddings = OllamaEmbeddings(model="llama2")

# Store embeddings in Chroma
vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embeddings
)

# Get user question
question = input("\nAsk ContextIQ a question: ")

# Retrieve relevant chunks
results = vectorstore.similarity_search(question, k=2)

# Build context
context = "\n\n".join(doc.page_content for doc in results)

# Create grounded prompt
prompt = f"""You are ContextIQ, a document question-answering assistant.

Answer the question using ONLY the provided context.
If the answer is not contained in the context, say:
"I don't know based on the provided knowledge."

Context:
{context}

Question:
{question}

Answer:
"""

# Generate answer
llm = ChatOllama(model="llama2")
response = llm.invoke(prompt)

print("\nContextIQ:")
print(response.content)