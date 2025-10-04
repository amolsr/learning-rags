"""
Vector database retrieval and similarity search
"""
import json
import logging
from typing import List, Optional, Dict, Any
from abc import ABC, abstractmethod
import clickhouse_connect
from langchain_core.documents import Document
from langchain_core.retrievers import BaseRetriever
from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores import Chroma

logger = logging.getLogger(__name__)


class VectorStore(ABC):
    """Abstract base class for vector stores"""
    
    @abstractmethod
    def add_documents(self, documents: List[Document], embeddings: List[List[float]]):
        """Add documents and their embeddings to the vector store"""
        pass
    
    @abstractmethod
    def similarity_search(self, query: str, k: int = 4) -> List[Document]:
        """Search for similar documents"""
        pass
    
    @abstractmethod
    def as_retriever(self, search_kwargs: Dict[str, Any] = None) -> BaseRetriever:
        """Return a retriever object"""
        pass


class ClickHouseVectorStore(VectorStore):
    """ClickHouse-based vector store for RAG"""
    
    def __init__(self, host: str, port: int, user: str, password: str, 
                 database: str, table: str, embedding_function):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.table = table
        self.embedding_function = embedding_function
        self.client = None
        self._connect()
        self._create_database()
        self._create_table()
    
    def _connect(self):
        """Connect to ClickHouse"""
        try:
            self.client = clickhouse_connect.get_client(
                host=self.host,
                port=self.port,
                username=self.user,
                password=self.password
            )
            logger.info(f"Connected to ClickHouse at {self.host}:{self.port}")
        except Exception as e:
            logger.error(f"Error connecting to ClickHouse: {e}")
            raise
    
    def _create_database(self):
        """Create database if it doesn't exist"""
        try:
            self.client.command(f"CREATE DATABASE IF NOT EXISTS {self.database}")
            self.client.command(f"USE {self.database}")
            logger.info(f"Database {self.database} ready")
        except Exception as e:
            logger.error(f"Error creating database: {e}")
            raise
    
    def _create_table(self):
        """Create table for storing documents and embeddings"""
        try:
            create_table_sql = f"""
            CREATE TABLE IF NOT EXISTS {self.table} (
                id String,
                content String,
                metadata String,
                source String,
                embedding Array(Float32),
                created_at DateTime DEFAULT now()
            ) ENGINE = MergeTree()
            ORDER BY id
            """
            self.client.command(create_table_sql)
            logger.info(f"Table {self.table} ready")
        except Exception as e:
            logger.error(f"Error creating table: {e}")
            raise
    
    def add_documents(self, documents: List[Document], embeddings: List[List[float]] = None):
        """Add documents to the vector store"""
        try:
            logger.info(f"Adding {len(documents)} documents to ClickHouse...")
            
            # Generate embeddings if not provided
            if embeddings is None:
                embeddings = self.embedding_function.embed_documents(documents)
            
            # Prepare data for batch insert
            data = []
            for i, doc in enumerate(documents):
                # Prepare metadata
                metadata = json.dumps(doc.metadata) if doc.metadata else "{}"
                
                data.append([
                    f"{doc.metadata.get('source', 'unknown')}_{hash(doc.page_content)}",  # id
                    doc.page_content,  # content
                    metadata,  # metadata
                    doc.metadata.get('source', 'unknown'),  # source
                    embeddings[i]  # embedding
                ])
            
            # Batch insert
            self.client.insert(self.table, data, column_names=['id', 'content', 'metadata', 'source', 'embedding'])
            logger.info(f"Successfully added {len(documents)} documents")
            
        except Exception as e:
            logger.error(f"Error adding documents: {e}")
            raise
    
    def similarity_search(self, query: str, k: int = 4) -> List[Document]:
        """Search for similar documents using cosine similarity"""
        try:
            # Generate query embedding
            query_embedding = self.embedding_function.embed_query(query)
            
            # Use ClickHouse's cosineDistance function for similarity search
            search_sql = f"""
            SELECT 
                id,
                content,
                metadata,
                source,
                cosineDistance(embedding, {query_embedding}) as distance
            FROM {self.table}
            ORDER BY distance ASC
            LIMIT {k}
            """
            
            result = self.client.query(search_sql)
            
            documents = []
            for row in result.result_rows:
                doc_id, content, metadata_str, source, distance = row
                metadata = json.loads(metadata_str) if metadata_str else {}
                metadata['distance'] = distance
                
                doc = Document(
                    page_content=content,
                    metadata=metadata
                )
                documents.append(doc)
            
            return documents
            
        except Exception as e:
            logger.error(f"Error in similarity search: {e}")
            return []
    
    def as_retriever(self, search_kwargs: Dict[str, Any] = None) -> BaseRetriever:
        """Return a retriever object"""
        if search_kwargs is None:
            search_kwargs = {"k": 4}
        
        class ClickHouseRetriever(BaseRetriever):
            vector_store: ClickHouseVectorStore
            search_kwargs: Dict[str, Any]
            
            def __init__(self, vector_store, search_kwargs):
                super().__init__(vector_store=vector_store, search_kwargs=search_kwargs)
            
            def _get_relevant_documents(self, query: str) -> List[Document]:
                """Get relevant documents for a query"""
                return self.vector_store.similarity_search(query, self.search_kwargs.get("k", 4))
            
            @property
            def vectorstore(self):
                """Return the vector store for compatibility"""
                return self.vector_store
        
        retriever = ClickHouseRetriever(self, search_kwargs)
        logger.info(f"Created ClickHouse retriever with search_kwargs: {search_kwargs}")
        return retriever


class FAISSVectorStore(VectorStore):
    """FAISS-based vector store for RAG"""
    
    def __init__(self, embedding_function, persist_directory: str = None):
        self.embedding_function = embedding_function
        self.persist_directory = persist_directory
        self.vectorstore = None
    
    def add_documents(self, documents: List[Document], embeddings: List[List[float]] = None):
        """Add documents to FAISS vector store"""
        try:
            logger.info(f"Adding {len(documents)} documents to FAISS...")
            
            if self.vectorstore is None:
                # Create new FAISS vectorstore
                if embeddings is None:
                    embeddings = self.embedding_function.embed_documents(documents)
                
                self.vectorstore = FAISS.from_embeddings(
                    text_embeddings=list(zip([doc.page_content for doc in documents], embeddings)),
                    embedding=self.embedding_function,
                    metadatas=[doc.metadata for doc in documents]
                )
            else:
                # Add to existing vectorstore
                if embeddings is None:
                    embeddings = self.embedding_function.embed_documents(documents)
                
                self.vectorstore.add_embeddings(
                    text_embeddings=list(zip([doc.page_content for doc in documents], embeddings)),
                    metadatas=[doc.metadata for doc in documents]
                )
            
            # Save if persist directory is specified
            if self.persist_directory:
                self.vectorstore.save_local(self.persist_directory)
            
            logger.info(f"Successfully added {len(documents)} documents to FAISS")
            
        except Exception as e:
            logger.error(f"Error adding documents to FAISS: {e}")
            raise
    
    def similarity_search(self, query: str, k: int = 4) -> List[Document]:
        """Search for similar documents in FAISS"""
        try:
            if self.vectorstore is None:
                logger.warning("FAISS vectorstore not initialized")
                return []
            
            docs = self.vectorstore.similarity_search(query, k=k)
            return docs
            
        except Exception as e:
            logger.error(f"Error in FAISS similarity search: {e}")
            return []
    
    def as_retriever(self, search_kwargs: Dict[str, Any] = None) -> BaseRetriever:
        """Return a FAISS retriever object"""
        if search_kwargs is None:
            search_kwargs = {"k": 4}
        
        if self.vectorstore is None:
            raise ValueError("FAISS vectorstore not initialized")
        
        retriever = self.vectorstore.as_retriever(search_kwargs=search_kwargs)
        logger.info(f"Created FAISS retriever with search_kwargs: {search_kwargs}")
        return retriever


def create_vector_store(store_type: str, embedding_function, **kwargs) -> VectorStore:
    """
    Factory function to create vector stores
    
    Args:
        store_type: Type of vector store (clickhouse, faiss, chroma)
        embedding_function: Embedding function to use
        **kwargs: Additional arguments for specific vector store types
    
    Returns:
        VectorStore instance
    """
    if store_type == "clickhouse":
        return ClickHouseVectorStore(
            host=kwargs.get("host", "localhost"),
            port=kwargs.get("port", 8123),
            user=kwargs.get("user", "default"),
            password=kwargs.get("password", ""),
            database=kwargs.get("database", "rag_db"),
            table=kwargs.get("table", "documents"),
            embedding_function=embedding_function
        )
    
    elif store_type == "faiss":
        return FAISSVectorStore(
            embedding_function=embedding_function,
            persist_directory=kwargs.get("persist_directory")
        )
    
    else:
        raise ValueError(f"Unsupported vector store type: {store_type}")
