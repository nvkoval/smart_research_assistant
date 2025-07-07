from typing import List

from app.config import Config
from app.document_processor import DocumentProcessor
from app.vector_store import VectorStoreManager
from app.rag_chain import QAChainBuilder
from app.formatter import ResponseFormatter


class SmartResearchAssistant:
    """Main class that orchestrates the RAG pipeline."""

    def __init__(self, config: Config = None):
        self.config = config or Config()
        self.document_processor = DocumentProcessor()
        self.vector_store = VectorStoreManager()
        self.qa_builder = QAChainBuilder()
        self.formatter = ResponseFormatter()
        self.qa_chain = None
        self.chat_history = []

    def setup(self, document_paths: List[str]):
        """Set up research assistant with documents."""
        # Process documents
        chunks = self.document_processor.load_and_split_documents(
            document_paths
        )

        if not chunks:
            raise ValueError("No documents were successfully processed")

        # Setup vector store
        if self.vector_store.index_exists():
            self.vector_store.load_index()
        else:
            self.vector_store.build_index(chunks)

        # Build QA chain
        retriever = self.vector_store.get_retriever()
        self.qa_chain = self.qa_builder.build_chain(retriever)
        print("Smart Research Assistant is ready!")

    def ask_question(self, question: str) -> str:
        """Ask a question and get an answer with sources."""
        if not self.qa_chain:
            raise ValueError("Assistant not set up. Call setup() first.")

        print(f"\nProcessing question: {question}")

        result = self.qa_chain.invoke({
            "question": question,
            "chat_history": self.chat_history
        })

        # Update chat history
        self.chat_history.append((question, result['answer']))
        return self.formatter.format_answer_with_sources(result)

    def clear_history(self):
        """Clear chat history."""
        self.chat_history = []
        print("Chat history cleared")
