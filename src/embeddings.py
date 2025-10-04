"""
Embedding generation and management
"""
import logging
from typing import List, Optional
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings

logger = logging.getLogger(__name__)


class EmbeddingManager:
    """Manages different embedding models and providers"""
    
    def __init__(self, model_type: str = "ollama", model_name: str = "all-minilm"):
        """
        Initialize embedding manager
        
        Args:
            model_type: Type of embedding model (ollama, openai, huggingface)
            model_name: Name of the specific model to use
        """
        self.model_type = model_type
        self.model_name = model_name
        self.embedding_function = self._initialize_embedding_function()
    
    def _initialize_embedding_function(self):
        """Initialize the appropriate embedding function based on model_type"""
        try:
            if self.model_type == "ollama":
                logger.info(f"Initializing Ollama embeddings with model: {self.model_name}")
                return OllamaEmbeddings(model=self.model_name)
            
            elif self.model_type == "openai":
                logger.info(f"Initializing OpenAI embeddings with model: {self.model_name}")
                return OpenAIEmbeddings(model=self.model_name)
            
            elif self.model_type == "huggingface":
                logger.info(f"Initializing HuggingFace embeddings with model: {self.model_name}")
                return HuggingFaceEmbeddings(model_name=self.model_name)
            
            else:
                raise ValueError(f"Unsupported model type: {self.model_type}")
                
        except Exception as e:
            logger.error(f"Failed to initialize embedding function: {e}")
            raise
    
    def embed_documents(self, documents: List[Document]) -> List[List[float]]:
        """
        Generate embeddings for a list of documents
        
        Args:
            documents: List of Document objects
            
        Returns:
            List of embedding vectors
        """
        logger.info(f"Generating embeddings for {len(documents)} documents")
        
        try:
            texts = [doc.page_content for doc in documents]
            embeddings = self.embedding_function.embed_documents(texts)
            logger.info(f"Successfully generated {len(embeddings)} embeddings")
            return embeddings
        except Exception as e:
            logger.error(f"Error generating embeddings: {e}")
            raise
    
    def embed_query(self, query: str) -> List[float]:
        """
        Generate embedding for a single query
        
        Args:
            query: Query text
            
        Returns:
            Embedding vector
        """
        try:
            return self.embedding_function.embed_query(query)
        except Exception as e:
            logger.error(f"Error generating query embedding: {e}")
            raise
    
    def get_embedding_dimension(self) -> int:
        """Get the dimension of the embedding vectors"""
        try:
            # Generate a test embedding to determine dimension
            test_embedding = self.embed_query("test")
            return len(test_embedding)
        except Exception as e:
            logger.error(f"Error determining embedding dimension: {e}")
            return 0


def create_embedding_manager(model_type: str = "ollama", model_name: str = "all-minilm") -> EmbeddingManager:
    """
    Factory function to create an embedding manager
    
    Args:
        model_type: Type of embedding model
        model_name: Name of the specific model
        
    Returns:
        EmbeddingManager instance
    """
    return EmbeddingManager(model_type, model_name)
