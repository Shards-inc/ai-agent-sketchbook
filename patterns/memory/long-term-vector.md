"""
# Long-Term Memory with Vector Databases

**Long-term memory** is a critical component for AI agents, allowing them to retain and retrieve information over extended periods, beyond the immediate context window of a Large Language Model (LLM). This is typically achieved by externalizing knowledge into specialized databases, with **vector databases** being a prominent solution for efficient semantic search.

## 🧠 Concept

The fundamental concept behind using vector databases for long-term memory is to transform raw information (text, images, audio, etc.) into numerical representations called **embeddings**. These embeddings capture the semantic meaning of the data, allowing for similarity searches based on meaning rather than exact keyword matches.

When an agent needs to recall information, its query is also converted into an embedding. The vector database then efficiently finds and returns the most semantically similar stored embeddings, providing the agent with contextually relevant knowledge. This approach enables agents to:

-   **Overcome Context Window Limitations**: Store and access vast amounts of information that would otherwise exceed an LLM's input capacity.
-   **Ground Responses**: Provide factual and up-to-date information by retrieving knowledge from external, continuously updated sources.
-   **Personalize Interactions**: Remember user preferences, past conversations, and specific domain knowledge to offer more tailored and consistent experiences.

## 🛠️ Implementation Workflow

The implementation of long-term memory using vector databases generally involves three main stages:

1.  **Embedding Generation (Ingestion)**:
    -   **Data Chunking**: Large documents or continuous streams of information are broken down into smaller, manageable chunks (e.g., paragraphs, sentences, fixed-size blocks).
    -   **Embedding Model**: Each chunk is then passed through an embedding model (e.g., OpenAI Embeddings, Sentence Transformers, Google's Universal Sentence Encoder). This model converts the text into a high-dimensional vector (embedding) that numerically represents its semantic content.
    -   **Metadata Association**: Alongside the vector, relevant metadata (e.g., source URL, creation date, document ID, author) is stored to enrich retrieval and attribution.

2.  **Vector Storage**: The generated embeddings and their associated metadata are stored in a **vector database** (e.g., Pinecone, Milvus, Chroma, Weaviate, Qdrant). These databases are optimized for storing and querying high-dimensional vectors, offering fast approximate nearest neighbor (ANN) search capabilities.

3.  **Retrieval (Querying)**:
    -   **Query Embedding**: When the agent receives a query or needs information, the query itself is first converted into an embedding using the *same* embedding model used during ingestion.
    -   **Similarity Search**: This query embedding is then sent to the vector database, which performs a similarity search to find the top-k (e.g., top 5) most semantically similar stored embeddings.
    -   **Context Augmentation**: The original text chunks corresponding to these retrieved embeddings are then passed back to the agent. This retrieved context is typically prepended or inserted into the LLM's prompt, augmenting its knowledge base before generating a response.

## 📈 Benefits

-   **Scalability**: Vector databases are designed to efficiently manage and search through massive datasets, making them suitable for enterprise-level knowledge bases.
-   **Semantic Understanding**: Agents can retrieve contextually relevant information, even if the exact keywords are not present in the query, leading to more intelligent and nuanced responses.
-   **Knowledge Augmentation**: LLMs can be augmented with up-to-date, domain-specific, or proprietary knowledge, overcoming the limitations of their training data cutoff.
-   **Source Attribution**: By storing metadata with embeddings, agents can cite the sources of their information, enhancing transparency and trustworthiness.
-   **Dynamic Learning**: New information can be continuously ingested and made available to the agent without retraining the base LLM.

## 🚀 Conceptual Implementation Example

```python
from typing import List, Dict

class MockEmbeddingModel:
    """Simulates an embedding model that converts text to vectors."""
    def embed(self, text: str) -> List[float]:
        # In a real scenario, this would be a complex model.
        # For demonstration, we use a simple hash-based vector.
        return [float(ord(c)) / 100.0 for c in text[:10]] + [0.0] * (10 - len(text[:10]))

class MockVectorDB:
    """Simulates a vector database for storing and searching embeddings."""
    def __init__(self):
        self.vectors: List[Dict[str, Any]] = []

    def add_document(self, text: str, embedding: List[float], metadata: Dict[str, Any]):
        self.vectors.append({"text": text, "embedding": embedding, "metadata": metadata})

    def search(self, query_embedding: List[float], top_k: int = 3) -> List[Dict[str, Any]]:
        """Finds the top_k most similar documents based on cosine similarity (mocked)."""
        # In a real DB, this would be optimized for high-dimensional vectors.
        # Here, we just simulate by finding exact matches or partial matches for simplicity.
        results = []
        for doc in self.vectors:
            # Simple mock similarity: if query embedding shares any values with doc embedding
            if any(q_val == d_val for q_val in query_embedding for d_val in doc["embedding"]):
                results.append(doc)
        return results[:top_k]

class LongTermMemory:
    """Manages long-term memory for an AI agent using a vector database."""
    def __init__(self, embedding_model: MockEmbeddingModel, vector_db: MockVectorDB):
        self.embedding_model = embedding_model
        self.vector_db = vector_db

    def ingest_knowledge(self, document_id: str, content: str, source: str):
        """Ingests new knowledge into long-term memory."""
        embedding = self.embedding_model.embed(content)
        self.vector_db.add_document(content, embedding, {"id": document_id, "source": source})
        print(f"Ingested document \'{document_id}\' from {source}")

    def retrieve_knowledge(self, query: str, top_k: int = 3) -> List[str]:
        """Retrieves relevant knowledge based on a query."""
        query_embedding = self.embedding_model.embed(query)
        search_results = self.vector_db.search(query_embedding, top_k)
        return [doc["text"] for doc in search_results]

if __name__ == "__main__":
    embedding_model = MockEmbeddingModel()
    vector_db = MockVectorDB()
    memory = LongTermMemory(embedding_model, vector_db)

    # Ingest some knowledge
    memory.ingest_knowledge("doc1", "The capital of France is Paris. It is famous for the Eiffel Tower.", "Wikipedia")
    memory.ingest_knowledge("doc2", "Artificial intelligence is a field of computer science that develops intelligent machines.", "Encyclopedia")
    memory.ingest_knowledge("doc3", "Renewable energy sources like solar and wind power are crucial for combating climate change.", "Environmental Report")
    memory.ingest_knowledge("doc4", "Python is a popular programming language, widely used in AI and data science.", "Programming Guide")

    # Retrieve knowledge
    print("\nRetrieving knowledge for: \"Eiffel Tower location\"")
    retrieved = memory.retrieve_knowledge("Where is the Eiffel Tower?")
    for item in retrieved:
        print(f"- {item}")

    print("\nRetrieving knowledge for: \"AI definition\"")
    retrieved = memory.retrieve_knowledge("What is AI?")
    for item in retrieved:
        print(f"- {item}")

    print("\nRetrieving knowledge for: \"sustainable power\"")
    retrieved = memory.retrieve_knowledge("What are some sustainable power options?")
    for item in retrieved:
        print(f"- {item}")

    print("\nRetrieving knowledge for: \"popular language for data science\"")
    retrieved = memory.retrieve_knowledge("Which language is often used for data science?")
    for item in retrieved:
        print(f"- {item}")
```

## 📚 Resources

-   [Pinecone: The Vector Database for AI](https://www.pinecone.io/)
-   [Chroma: The AI-Native Open-Source Vector Database](https://www.trychroma.com/)
-   [Milvus: Vector Database for AI Applications](https://milvus.io/)
-   [Weaviate: Vector Database](https://weaviate.io/)
-   [Qdrant: Vector Database & Search Engine](https://qdrant.tech/)
-   [Hugging Face: Sentence Transformers](https://www.sbert.net/)
-   [OpenAI Embeddings Documentation](https://platform.openai.com/docs/guides/embeddings)
"""
