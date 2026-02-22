---
name: rag-agent
description: Provides a template for building Retrieval-Augmented Generation (RAG) agents. Use for: creating agents that can access and reason over external knowledge bases, semantic search, and contextual retrieval.
---

# RAG Agent Skill

The **Retrieval-Augmented Generation (RAG)** Agent template is designed for building agents that can access and reason over external knowledge bases.

## Key Features

-   **Semantic Search**: Integration with vector databases (e.g., Pinecone, Milvus, Chroma) for efficient and relevant information retrieval.
-   **Contextual Retrieval**: Dynamic retrieval of relevant documents based on user queries, ensuring the agent has the most pertinent information.
-   **Source Attribution**: Mechanisms to ensure the agent cites its sources for transparency and verifiability.

## Usage Instructions

To utilize this RAG agent skill, follow these steps:

1.  **Ingest Data**: Load and chunk your documents into manageable pieces.
2.  **Generate Embeddings**: Convert text chunks into vector representations suitable for semantic search.
3.  **Query Agent**: The agent will automatically retrieve relevant context from the knowledge base before generating a response to a user query.

## Example Implementation Sketch

```python
class RAGAgent:
    def __init__(self, vector_db, llm):
        self.vector_db = vector_db
        self.llm = llm

    def query(self, question):
        context = self.vector_db.search(question)
        return self.llm.generate(question, context)
```

## Resources

-   [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)
