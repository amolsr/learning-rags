"""
Configuration settings for the RAG system
"""
import os
from typing import Optional
from dataclasses import dataclass


@dataclass
class ClickHouseConfig:
    """ClickHouse database configuration"""
    host: str = "localhost"
    port: int = 8123
    user: str = "default"
    password: str = ""
    database: str = "rag_db"
    table: str = "documents"


@dataclass
class OllamaConfig:
    """Ollama LLM configuration"""
    model: str = "mistral"
    temperature: float = 0.0
    base_url: str = "http://localhost:11434"


@dataclass
class EmbeddingConfig:
    """Embedding model configuration"""
    model: str = "all-minilm"
    chunk_size: int = 800
    chunk_overlap: int = 100


@dataclass
class RAGConfig:
    """Main RAG system configuration"""
    # Data paths
    raw_data_dir: str = "data/raw"
    processed_data_dir: str = "data/processed"
    embeddings_dir: str = "data/embeddings"
    
    # Vector store settings
    vector_store_type: str = "clickhouse"  # clickhouse, faiss, pinecone, weaviate
    similarity_search_k: int = 4
    
    # LLM settings
    llm_type: str = "ollama"  # ollama, openai, huggingface
    
    # Logging
    log_level: str = "INFO"
    log_file: str = "rag_questions.log"
    
    # Question generation
    questions_file: str = "generated_questions.json"
    
    def __post_init__(self):
        """Load configuration from environment variables"""
        # ClickHouse settings
        self.clickhouse = ClickHouseConfig(
            host=os.getenv("CLICKHOUSE_HOST", self.clickhouse.host),
            port=int(os.getenv("CLICKHOUSE_PORT", str(self.clickhouse.port))),
            user=os.getenv("CLICKHOUSE_USER", self.clickhouse.user),
            password=os.getenv("CLICKHOUSE_PASSWORD", self.clickhouse.password),
            database=os.getenv("CLICKHOUSE_DATABASE", self.clickhouse.database),
            table=os.getenv("CLICKHOUSE_TABLE", self.clickhouse.table)
        )
        
        # Ollama settings
        self.ollama = OllamaConfig(
            model=os.getenv("OLLAMA_MODEL", self.ollama.model),
            temperature=float(os.getenv("OLLAMA_TEMPERATURE", str(self.ollama.temperature))),
            base_url=os.getenv("OLLAMA_BASE_URL", self.ollama.base_url)
        )
        
        # Embedding settings
        self.embeddings = EmbeddingConfig(
            model=os.getenv("EMBEDDING_MODEL", self.embeddings.model),
            chunk_size=int(os.getenv("CHUNK_SIZE", str(self.embeddings.chunk_size))),
            chunk_overlap=int(os.getenv("CHUNK_OVERLAP", str(self.embeddings.chunk_overlap)))
        )
        
        # Other settings
        self.vector_store_type = os.getenv("VECTOR_STORE_TYPE", self.vector_store_type)
        self.llm_type = os.getenv("LLM_TYPE", self.llm_type)
        self.similarity_search_k = int(os.getenv("SIMILARITY_SEARCH_K", str(self.similarity_search_k)))
        self.log_level = os.getenv("LOG_LEVEL", self.log_level)


# Global configuration instance
config = RAGConfig()
