#!/usr/bin/env python3
"""
Data ingestion script for the RAG system

This script loads documents from the raw data directory, processes them,
and stores them in the vector database.
"""

import sys
import os
import argparse
import logging
from pathlib import Path

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from config import config
from rag_pipeline import create_rag_pipeline
from utils import setup_logging


def main():
    """Main data ingestion function"""
    parser = argparse.ArgumentParser(description='Ingest data into the RAG system')
    parser.add_argument('--data-dir', type=str, default=None,
                       help='Directory containing raw documents (default: from config)')
    parser.add_argument('--log-level', type=str, default='INFO',
                       choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
                       help='Logging level')
    parser.add_argument('--force-rebuild', action='store_true',
                       help='Force rebuild of vector store even if it exists')
    
    args = parser.parse_args()
    
    # Set up logging
    logger = setup_logging(args.log_level, config.log_file)
    
    try:
        # Determine data directory
        data_dir = args.data_dir or config.raw_data_dir
        data_path = Path(data_dir)
        
        if not data_path.exists():
            logger.error(f"Data directory does not exist: {data_path}")
            return 1
        
        logger.info(f"Starting data ingestion from: {data_path}")
        
        # Create RAG pipeline
        logger.info("Initializing RAG pipeline...")
        rag = create_rag_pipeline()
        
        # Load and process documents
        logger.info("Loading and processing documents...")
        documents = rag.load_and_process_documents(data_dir)
        
        if not documents:
            logger.warning("No documents were processed")
            return 1
        
        logger.info(f"Successfully ingested {len(documents)} documents")
        logger.info("Data ingestion completed successfully")
        
        return 0
        
    except Exception as e:
        logger.error(f"Data ingestion failed: {e}")
        return 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
