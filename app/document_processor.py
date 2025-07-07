from typing import List
from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema import Document


class DocumentProcessor:
    """Handles document loading and text splitting."""

    def __init__(
        self,
        chunk_size: int = 500,
        chunk_overlap: int = 50
    ):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

    def load_and_split_documents(self, doc_paths: List[str]) -> List[Document]:
        """Loads PDF documents and split them into text chunks for processing."""
        print(f"Loading and splitting {len(doc_paths)} documents...")
        all_chunks = []

        for path in doc_paths:
            if not Path(path).exists():
                print(f"Warning: Document not found at {path}")
                continue

            print(f"Processing: {path}")
            loader = PyMuPDFLoader(path)
            documents = loader.load()
            chunks = self.text_splitter.split_documents(documents)
            all_chunks.extend(chunks)
            print(f"Generated {len(chunks)} chunks")

        print(f"Total chunks created: {len(all_chunks)}")
        return all_chunks
