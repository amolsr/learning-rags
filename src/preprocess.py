"""
Document preprocessing and text cleaning utilities
"""
import os
import logging
from typing import List, Optional
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document

logger = logging.getLogger(__name__)


def load_documents(data_dir: str, file_extensions: List[str] = None) -> List[Document]:
    """
    Load documents from a directory
    
    Args:
        data_dir: Directory containing documents
        file_extensions: List of file extensions to load (default: ['.md', '.txt'])
    
    Returns:
        List of Document objects
    """
    if file_extensions is None:
        file_extensions = ['.md', '.txt']
    
    docs = []
    files_found = []
    
    # Collect all matching files
    for root, dirs, files in os.walk(data_dir):
        for fname in files:
            if any(fname.lower().endswith(ext) for ext in file_extensions):
                files_found.append(os.path.join(root, fname))
    
    logger.info(f"Found {len(files_found)} files to process")
    
    # Process files with progress indicator
    for i, path in enumerate(files_found, 1):
        try:
            logger.info(f"Loading {i}/{len(files_found)}: {os.path.basename(path)}")
            loader = TextLoader(path, encoding="utf-8")
            docs.extend(loader.load())
        except Exception as e:
            logger.error(f"Error loading {path}: {e}")
            continue
    
    logger.info(f"Successfully loaded {len(docs)} documents")
    return docs


def clean_text(text: str) -> str:
    """
    Clean and normalize text content
    
    Args:
        text: Raw text content
    
    Returns:
        Cleaned text
    """
    # Remove excessive whitespace
    text = ' '.join(text.split())
    
    # Remove special characters that might interfere with processing
    # Keep basic punctuation and alphanumeric characters
    import re
    text = re.sub(r'[^\w\s\.\,\!\?\;\:\-\(\)]', '', text)
    
    return text.strip()


def split_documents(
    documents: List[Document], 
    chunk_size: int = 800, 
    chunk_overlap: int = 100
) -> List[Document]:
    """
    Split documents into smaller chunks
    
    Args:
        documents: List of Document objects
        chunk_size: Maximum size of each chunk
        chunk_overlap: Number of characters to overlap between chunks
    
    Returns:
        List of chunked Document objects
    """
    logger.info(f"Splitting {len(documents)} documents into chunks...")
    
    # Clean text before splitting
    for doc in documents:
        doc.page_content = clean_text(doc.page_content)
    
    splitter = CharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separator="\n\n"  # Split on double newlines for better chunk boundaries
    )
    
    split_docs = splitter.split_documents(documents)
    logger.info(f"Created {len(split_docs)} chunks")
    
    return split_docs


def preprocess_documents(
    data_dir: str, 
    chunk_size: int = 800, 
    chunk_overlap: int = 100,
    file_extensions: List[str] = None
) -> List[Document]:
    """
    Complete preprocessing pipeline: load, clean, and chunk documents
    
    Args:
        data_dir: Directory containing raw documents
        chunk_size: Maximum size of each chunk
        chunk_overlap: Number of characters to overlap between chunks
        file_extensions: List of file extensions to process
    
    Returns:
        List of processed Document objects ready for embedding
    """
    logger.info(f"Starting document preprocessing from {data_dir}")
    
    # Load documents
    documents = load_documents(data_dir, file_extensions)
    
    if not documents:
        logger.warning(f"No documents found in {data_dir}")
        return []
    
    # Split into chunks
    chunked_docs = split_documents(documents, chunk_size, chunk_overlap)
    
    logger.info(f"Preprocessing complete: {len(chunked_docs)} chunks ready for embedding")
    return chunked_docs
