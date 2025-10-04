"""
LLM interface for text generation
"""
import logging
from typing import Optional, Dict, Any
from langchain_core.language_models.base import BaseLanguageModel

# Conditional imports to handle missing packages gracefully
try:
    from langchain_ollama import Ollama
except ImportError:
    Ollama = None

try:
    from langchain_openai import ChatOpenAI
except ImportError:
    ChatOpenAI = None

try:
    from langchain_community.llms import HuggingFacePipeline
except ImportError:
    HuggingFacePipeline = None

logger = logging.getLogger(__name__)


class LLMManager:
    """Manages different LLM providers and models"""
    
    def __init__(self, llm_type: str = "ollama", model_name: str = "mistral", **kwargs):
        """
        Initialize LLM manager
        
        Args:
            llm_type: Type of LLM (ollama, openai, huggingface)
            model_name: Name of the specific model to use
            **kwargs: Additional model-specific parameters
        """
        self.llm_type = llm_type
        self.model_name = model_name
        self.llm = self._initialize_llm(**kwargs)
    
    def _initialize_llm(self, **kwargs) -> BaseLanguageModel:
        """Initialize the appropriate LLM based on llm_type"""
        try:
            if self.llm_type == "ollama":
                if Ollama is None:
                    raise ImportError("langchain_ollama package not installed")
                logger.info(f"Initializing Ollama LLM with model: {self.model_name}")
                return Ollama(
                    model=self.model_name,
                    temperature=kwargs.get("temperature", 0.0),
                    base_url=kwargs.get("base_url", "http://localhost:11434")
                )
            
            elif self.llm_type == "openai":
                if ChatOpenAI is None:
                    raise ImportError("langchain_openai package not installed")
                logger.info(f"Initializing OpenAI LLM with model: {self.model_name}")
                return ChatOpenAI(
                    model=self.model_name,
                    temperature=kwargs.get("temperature", 0.0),
                    api_key=kwargs.get("api_key")
                )
            
            elif self.llm_type == "huggingface":
                if HuggingFacePipeline is None:
                    raise ImportError("langchain_community package not installed")
                logger.info(f"Initializing HuggingFace LLM with model: {self.model_name}")
                # Note: This requires additional setup for HuggingFace models
                raise NotImplementedError("HuggingFace LLM integration not yet implemented")
            
            else:
                raise ValueError(f"Unsupported LLM type: {self.llm_type}")
                
        except Exception as e:
            logger.error(f"Failed to initialize LLM: {e}")
            raise
    
    def generate(self, prompt: str, **kwargs) -> str:
        """
        Generate text from a prompt
        
        Args:
            prompt: Input prompt
            **kwargs: Additional generation parameters
            
        Returns:
            Generated text
        """
        try:
            response = self.llm.invoke(prompt)
            return response
        except Exception as e:
            logger.error(f"Error generating text: {e}")
            raise
    
    def generate_questions(self, content: str, num_questions: int = 5) -> str:
        """
        Generate multiple-choice questions from content
        
        Args:
            content: Source content to generate questions from
            num_questions: Number of questions to generate
            
        Returns:
            Generated questions in structured format
        """
        prompt = f"""
        Based on the following content, create {num_questions} multiple-choice questions with 4 options each.
        
        Content: {content}
        
        Please provide your response in this exact format for each question:
        QUESTION: [Your question here]
        A: [Option 1]
        B: [Option 2] 
        C: [Option 3]
        D: [Option 4]
        CORRECT: [A, B, C, or D]
        CATEGORY: [Category name]
        
        ---
        """
        
        try:
            response = self.generate(prompt)
            return response
        except Exception as e:
            logger.error(f"Error generating questions: {e}")
            raise


def create_llm_manager(llm_type: str = "ollama", model_name: str = "mistral", **kwargs) -> LLMManager:
    """
    Factory function to create an LLM manager
    
    Args:
        llm_type: Type of LLM
        model_name: Name of the specific model
        **kwargs: Additional model-specific parameters
        
    Returns:
        LLMManager instance
    """
    return LLMManager(llm_type, model_name, **kwargs)
