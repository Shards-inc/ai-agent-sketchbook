
import os
from typing import List, Dict, Any

class MockVectorDB:
    """A mock vector database for demonstration purposes."""
    def __init__(self, documents: Dict[str, str]):
        self.documents = documents

    def search(self, query: str, top_k: int = 1) -> List[str]:
        """Simulates semantic search to retrieve relevant document chunks."""
        print(f"Searching vector DB for query: \'{query}\'")
        # In a real scenario, this would involve embedding the query and searching for similar vectors.
        # For this mock, we'll return a document if the query is a substring of its content.
        results = []
        for doc_id, content in self.documents.items():
            if query.lower() in content.lower():
                results.append(content)
            if len(results) >= top_k:
                break
        return results if results else ["No relevant documents found."]

class MockLLM:
    """A mock Large Language Model for demonstration purposes."""
    def generate(self, prompt: str) -> str:
        print(f"LLM generating response for prompt: \'{prompt[:100]}...\'")
        if "context:" in prompt.lower():
            context = prompt.split("context:")[-1].strip()
            if "no relevant documents" in context.lower():
                return "Final Answer: I couldn't find enough information to answer your question based on the available documents."
            return f"Final Answer: Based on the provided context: \"{context}\", I can tell you that... [simulated answer based on context]."
        return "Final Answer: I am an AI assistant and can help with many tasks."

class RAGAgent:
    """A Retrieval-Augmented Generation (RAG) agent."""
    def __init__(self, vector_db: MockVectorDB, llm: MockLLM):
        self.vector_db = vector_db
        self.llm = llm

    def query(self, question: str) -> str:
        """Queries the RAG agent with a question."""
        # Step 1: Retrieve relevant documents from the vector database
        retrieved_context = self.vector_db.search(question, top_k=2)
        context_str = "\n".join(retrieved_context)

        # Step 2: Augment the prompt with the retrieved context and generate a response
        prompt = (
            f"You are a helpful assistant. Answer the following question based on the provided context.\n"
            f"If you cannot find the answer in the context, state that you don't have enough information.\n\n"
            f"Question: {question}\n"
            f"Context: {context_str}\n\n"
            f"Answer:"
        )
        response = self.llm.generate(prompt)
        return response

if __name__ == "__main__":
    # Sample documents for the mock vector database
    sample_documents = {
        "doc1": "The capital of France is Paris. Paris is known for its Eiffel Tower.",
        "doc2": "Artificial intelligence is a rapidly developing field. Large Language Models are a subset of AI.",
        "doc3": "The best way to learn programming is by doing. Python is a popular language for AI development.",
        "doc4": "Climate change is a global issue. Renewable energy sources are key to combating it."
    }

    mock_db = MockVectorDB(sample_documents)
    mock_llm = MockLLM()

    rag_agent = RAGAgent(mock_db, mock_llm)

    print("\n--- RAG Agent Query 1 (Known fact) ---")
    result1 = rag_agent.query("What is the capital of France?")
    print(f"Agent Result: {result1}")

    print("\n--- RAG Agent Query 2 (AI related) ---")
    result2 = rag_agent.query("What are Large Language Models?")
    print(f"Agent Result: {result2}")

    print("\n--- RAG Agent Query 3 (Unknown fact) ---")
    result3 = rag_agent.query("What is the highest mountain in Africa?")
    print(f"Agent Result: {result3}")

    print("\n--- RAG Agent Query 4 (Programming related) ---")
    result4 = rag_agent.query("What is a popular language for AI development?")
    print(f"Agent Result: {result4}")
