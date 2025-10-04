"""
Main RAG pipeline that integrates retrieval and generation
"""
import logging
import json
import random
import string
from typing import List, Dict, Any, Optional
from langchain.chains import RetrievalQA
from langchain_core.documents import Document

from .config import config
from .preprocess import preprocess_documents
from .embeddings import create_embedding_manager
from .retriever import create_vector_store
from .generator import create_llm_manager

logger = logging.getLogger(__name__)


class RAGPipeline:
    """Main RAG pipeline that integrates all components"""
    
    def __init__(self, config_obj=None):
        """
        Initialize RAG pipeline
        
        Args:
            config_obj: Configuration object (uses global config if None)
        """
        self.config = config_obj or config
        self.embedding_manager = None
        self.vector_store = None
        self.llm_manager = None
        self.qa_chain = None
        self.retriever = None
        
        # Initialize components
        self._initialize_components()
    
    def _initialize_components(self):
        """Initialize all RAG components"""
        try:
            # Initialize embedding manager
            self.embedding_manager = create_embedding_manager(
                model_type="ollama",  # Default to ollama for now
                model_name=self.config.embeddings.model
            )
            
            # Initialize vector store
            if self.config.vector_store_type == "clickhouse":
                self.vector_store = create_vector_store(
                    store_type="clickhouse",
                    embedding_function=self.embedding_manager.embedding_function,
                    host=self.config.clickhouse.host,
                    port=self.config.clickhouse.port,
                    user=self.config.clickhouse.user,
                    password=self.config.clickhouse.password,
                    database=self.config.clickhouse.database,
                    table=self.config.clickhouse.table
                )
            else:
                raise ValueError(f"Unsupported vector store type: {self.config.vector_store_type}")
            
            # Initialize LLM manager
            self.llm_manager = create_llm_manager(
                llm_type=self.config.llm_type,
                model_name=self.config.ollama.model,
                temperature=self.config.ollama.temperature,
                base_url=self.config.ollama.base_url
            )
            
            logger.info("RAG pipeline components initialized successfully")
            
        except Exception as e:
            logger.error(f"Error initializing RAG components: {e}")
            raise
    
    def load_and_process_documents(self, data_dir: str = None) -> List[Document]:
        """
        Load and process documents for the RAG system
        
        Args:
            data_dir: Directory containing raw documents (uses config default if None)
            
        Returns:
            List of processed documents
        """
        if data_dir is None:
            data_dir = self.config.raw_data_dir
        
        logger.info(f"Loading and processing documents from {data_dir}")
        
        # Preprocess documents
        documents = preprocess_documents(
            data_dir=data_dir,
            chunk_size=self.config.embeddings.chunk_size,
            chunk_overlap=self.config.embeddings.chunk_overlap
        )
        
        if not documents:
            logger.warning("No documents found to process")
            return []
        
        # Add documents to vector store
        self.vector_store.add_documents(documents)
        
        # Create retriever
        self.retriever = self.vector_store.as_retriever(
            search_kwargs={"k": self.config.similarity_search_k}
        )
        
        # Create QA chain
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm_manager.llm,
            chain_type="stuff",
            retriever=self.retriever
        )
        
        logger.info(f"Successfully processed {len(documents)} documents")
        return documents
    
    def ask_question(self, question: str) -> str:
        """
        Ask a question and get an answer from the RAG system
        
        Args:
            question: Question to ask
            
        Returns:
            Answer from the RAG system
        """
        if not self.qa_chain:
            raise ValueError("RAG pipeline not initialized. Call load_and_process_documents() first.")
        
        try:
            logger.info(f"Processing question: {question}")
            result = self.qa_chain.invoke({"query": question})
            answer = result['result']
            logger.info(f"Generated answer: {answer[:100]}...")
            return answer
        except Exception as e:
            logger.error(f"Error processing question: {e}")
            raise
    
    def generate_object_id(self) -> str:
        """Generate a random 24-character hex string for MongoDB ObjectId"""
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=24))
    
    def generate_question_json(self, question_text: str, options: List[str], 
                             correct_answer: str, category: str = "", image_url: str = "") -> Dict[str, Any]:
        """Generate a single question in the specified JSON format"""
        return {
            "_id": {"$oid": self.generate_object_id()},
            "question": question_text,
            "one": options[0] if len(options) > 0 else "",
            "two": options[1] if len(options) > 1 else "",
            "three": options[2] if len(options) > 2 else "",
            "four": options[3] if len(options) > 3 else "",
            "correct": correct_answer,
            "category": category,
            "QuestionPic": image_url,
            "__v": {"$numberInt": "0"}
        }
    
    def generate_questions_from_content(self, num_questions: int = 5) -> List[Dict[str, Any]]:
        """
        Generate multiple-choice questions based on the indexed content
        
        Args:
            num_questions: Number of questions to generate
            
        Returns:
            List of question dictionaries
        """
        logger.info(f"Starting question generation process for {num_questions} questions")
        
        if not self.retriever:
            raise ValueError("RAG pipeline not initialized. Call load_and_process_documents() first.")
        
        # Get diverse chunks using multiple queries
        sample_docs = []
        queries = [
            "general knowledge content",
            "programming concepts",
            "technical documentation", 
            "tutorial content",
            "examples and code"
        ]
        
        for query in queries:
            try:
                docs = self.retriever._get_relevant_documents(query)
                sample_docs.extend(docs)
            except Exception as e:
                logger.error(f"Error executing query '{query}': {e}")
                continue
        
        # Remove duplicates
        seen = set()
        unique_docs = []
        for doc in sample_docs:
            doc_id = hash(doc.page_content)
            if doc_id not in seen:
                seen.add(doc_id)
                unique_docs.append(doc)
        
        sample_docs = unique_docs
        logger.info(f"Retrieved {len(sample_docs)} unique document chunks")
        
        if not sample_docs:
            logger.warning("No documents found to generate questions from")
            return []
        
        questions = []
        used_content_hashes = set()
        max_attempts = num_questions * 3
        attempts = 0
        
        while len(questions) < num_questions and attempts < max_attempts:
            attempts += 1
            
            # Get a random document chunk
            doc = random.choice(sample_docs)
            content = doc.page_content[:800]
            content_hash = hash(content)
            
            # Skip if we've already used this content
            if content_hash in used_content_hashes:
                continue
            used_content_hashes.add(content_hash)
            
            # Generate question using LLM
            try:
                response = self.llm_manager.generate_questions(content, 1)
                
                # Parse the response
                lines = response.strip().split('\n')
                question_text = ""
                options = []
                correct_answer = ""
                category = ""
                
                for line in lines:
                    line = line.strip()
                    if line.startswith("QUESTION:"):
                        question_text = line.replace("QUESTION:", "").strip()
                    elif line.startswith("A:"):
                        options.append(line.replace("A:", "").strip())
                    elif line.startswith("B:"):
                        options.append(line.replace("B:", "").strip())
                    elif line.startswith("C:"):
                        options.append(line.replace("C:", "").strip())
                    elif line.startswith("D:"):
                        options.append(line.replace("D:", "").strip())
                    elif line.startswith("CORRECT:"):
                        correct_letter = line.replace("CORRECT:", "").strip().upper()
                        correct_answer = {"A": "one", "B": "two", "C": "three", "D": "four"}.get(correct_letter, "one")
                    elif line.startswith("CATEGORY:"):
                        category = line.replace("CATEGORY:", "").strip()
                
                if question_text and len(options) >= 4 and correct_answer:
                    question_json = self.generate_question_json(question_text, options, correct_answer, category)
                    questions.append(question_json)
                    logger.info(f"Successfully generated question {len(questions)}: {question_text[:50]}...")
                
            except Exception as e:
                logger.error(f"Error generating question on attempt {attempts}: {e}")
                continue
        
        logger.info(f"Question generation completed. Generated {len(questions)} out of {num_questions} requested questions")
        return questions
    
    def save_questions_to_json(self, questions: List[Dict[str, Any]], filename: str = None):
        """Save questions to JSON file"""
        if filename is None:
            filename = self.config.questions_file
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(questions, f, indent=2, ensure_ascii=False)
            logger.info(f"Saved {len(questions)} questions to {filename}")
        except Exception as e:
            logger.error(f"Error saving questions: {e}")
            raise


def create_rag_pipeline(config_obj=None) -> RAGPipeline:
    """
    Factory function to create a RAG pipeline
    
    Args:
        config_obj: Configuration object (uses global config if None)
        
    Returns:
        RAGPipeline instance
    """
    return RAGPipeline(config_obj)
