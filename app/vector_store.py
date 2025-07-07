from pathlib import Path
from typing import Dict, Any, Optional
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.schema import Document


class VectorStoreManager:
    """Manages ChromaDB vector store operations."""

    def __init__(self, persist_dir: str = "../data/chroma_db",
                 embedding_model: str = "all-MiniLM-L6-v2"):
        self.persist_dir = persist_dir
        self.embedding_model = self._initialize_embeddings(embedding_model)
        self.db: Optional[Chroma] = None

    def _initialize_embeddings(self, model_name: str) -> HuggingFaceEmbeddings:
        """Initialize HuggingFace embeddings with Windows compatibility."""
        print(f"Loading embedding model: {model_name}")

        model_kwargs = {
            'device': 'cpu',
            'trust_remote_code': True
        }

        encode_kwargs = {
            'normalize_embeddings': True,
            'batch_size': 32
        }

        embeddings = HuggingFaceEmbeddings(
            model_name=model_name,
            model_kwargs=model_kwargs,
            encode_kwargs=encode_kwargs
        )
        print("✓ Embedding model loaded successfully")
        return embeddings

    def build_index(self, documents: list[Document]):
        """Create and persist vector index from document chunks."""
        print("Building ChromaDB index...")

        # Create the persist directory if it doesn't exist
        Path(self.persist_dir).mkdir(parents=True, exist_ok=True)

        self.db = Chroma.from_documents(
            documents,
            self.embedding_model,
            persist_directory=self.persist_dir
        )
        print(f"✓ Index built and saved to {self.persist_dir}")

    def load_index(self) -> None:
        """Load existing vector index from disk."""
        print("Loading existing ChromaDB index...")

        try:
            self.db = Chroma(
                persist_directory=self.persist_dir,
                embedding_function=self.embedding_model
            )

            print(f"✓ ChromaDB index loaded successfully from '{self.persist_dir}'")

        except Exception as e:
            print(f"Failed to load ChromaDB index: {e}")
            raise

    def get_retriever(self, search_kwargs: Dict[str, Any] = None):
        """Get retriever for similarity search."""
        if not self.db:
            raise ValueError("ChromaDB is not initialized. Call build_index() or load_index() first")
        if search_kwargs is None:
            search_kwargs = {"k": 3}

        return self.db.as_retriever(search_kwargs=search_kwargs)

    def index_exists(self) -> bool:
        """Check if vector index exists on disk."""
        persist_path = Path(self.persist_dir)

        return persist_path.exists() and any(persist_path.iterdir())
