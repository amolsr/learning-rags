"""
Utility functions for logging, metrics, and helper operations
"""
import logging
import os
import time
from typing import Any, Dict, List, Optional
from functools import wraps


def setup_logging(log_level: str = "INFO", log_file: str = "rag_questions.log") -> logging.Logger:
    """
    Set up logging configuration
    
    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR)
        log_file: Log file path
        
    Returns:
        Configured logger
    """
    # Create logs directory if it doesn't exist
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Configure logging
    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    
    logger = logging.getLogger(__name__)
    logger.info(f"Logging configured - Level: {log_level}, File: {log_file}")
    return logger


def timing_decorator(func):
    """Decorator to measure function execution time"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        
        logger = logging.getLogger(func.__module__)
        logger.info(f"{func.__name__} executed in {execution_time:.2f} seconds")
        
        return result
    return wrapper


def validate_file_path(file_path: str, must_exist: bool = True) -> bool:
    """
    Validate if a file path exists and is accessible
    
    Args:
        file_path: Path to validate
        must_exist: Whether the file must exist
        
    Returns:
        True if valid, False otherwise
    """
    try:
        if must_exist:
            return os.path.exists(file_path) and os.path.isfile(file_path)
        else:
            # Check if parent directory exists
            parent_dir = os.path.dirname(file_path)
            return os.path.exists(parent_dir) if parent_dir else True
    except Exception:
        return False


def ensure_directory_exists(directory_path: str) -> bool:
    """
    Ensure a directory exists, create it if it doesn't
    
    Args:
        directory_path: Path to directory
        
    Returns:
        True if directory exists or was created, False otherwise
    """
    try:
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
        return True
    except Exception as e:
        logging.error(f"Error creating directory {directory_path}: {e}")
        return False


def get_file_extension(file_path: str) -> str:
    """
    Get file extension from a file path
    
    Args:
        file_path: Path to file
        
    Returns:
        File extension (including the dot)
    """
    return os.path.splitext(file_path)[1].lower()


def format_file_size(size_bytes: int) -> str:
    """
    Format file size in human-readable format
    
    Args:
        size_bytes: Size in bytes
        
    Returns:
        Formatted size string
    """
    if size_bytes == 0:
        return "0 B"
    
    size_names = ["B", "KB", "MB", "GB", "TB"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
    
    return f"{size_bytes:.1f} {size_names[i]}"


def count_tokens_approximate(text: str) -> int:
    """
    Approximate token count for text (rough estimation)
    
    Args:
        text: Text to count tokens for
        
    Returns:
        Approximate token count
    """
    # Rough estimation: 1 token ≈ 4 characters for English text
    return len(text) // 4


def clean_filename(filename: str) -> str:
    """
    Clean filename by removing invalid characters
    
    Args:
        filename: Original filename
        
    Returns:
        Cleaned filename
    """
    import re
    # Remove invalid characters for filenames
    cleaned = re.sub(r'[<>:"/\\|?*]', '_', filename)
    # Remove multiple underscores
    cleaned = re.sub(r'_+', '_', cleaned)
    # Remove leading/trailing underscores
    cleaned = cleaned.strip('_')
    return cleaned


def batch_process(items: List[Any], batch_size: int = 100):
    """
    Generator to process items in batches
    
    Args:
        items: List of items to process
        batch_size: Size of each batch
        
    Yields:
        Batches of items
    """
    for i in range(0, len(items), batch_size):
        yield items[i:i + batch_size]


def safe_json_loads(json_str: str, default: Any = None) -> Any:
    """
    Safely load JSON string with fallback
    
    Args:
        json_str: JSON string to parse
        default: Default value if parsing fails
        
    Returns:
        Parsed JSON or default value
    """
    try:
        import json
        return json.loads(json_str)
    except Exception:
        return default


def safe_json_dumps(obj: Any, default: str = "{}") -> str:
    """
    Safely dump object to JSON string with fallback
    
    Args:
        obj: Object to serialize
        default: Default string if serialization fails
        
    Returns:
        JSON string or default string
    """
    try:
        import json
        return json.dumps(obj, ensure_ascii=False)
    except Exception:
        return default


class ProgressTracker:
    """Simple progress tracking utility"""
    
    def __init__(self, total: int, description: str = "Processing"):
        self.total = total
        self.current = 0
        self.description = description
        self.start_time = time.time()
    
    def update(self, increment: int = 1):
        """Update progress"""
        self.current += increment
        self._log_progress()
    
    def _log_progress(self):
        """Log current progress"""
        if self.total > 0:
            percentage = (self.current / self.total) * 100
            elapsed_time = time.time() - self.start_time
            
            if self.current > 0:
                estimated_total_time = elapsed_time * (self.total / self.current)
                remaining_time = estimated_total_time - elapsed_time
                eta = f", ETA: {remaining_time:.1f}s"
            else:
                eta = ""
            
            logging.info(f"{self.description}: {self.current}/{self.total} ({percentage:.1f}%){eta}")
    
    def finish(self):
        """Mark as finished"""
        total_time = time.time() - self.start_time
        logging.info(f"{self.description} completed in {total_time:.2f} seconds")
