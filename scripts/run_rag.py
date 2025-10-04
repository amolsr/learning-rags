#!/usr/bin/env python3
"""
RAG execution script

This script provides a command-line interface for running the RAG system,
including question answering and question generation.
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


def interactive_mode(rag):
    """Run interactive Q&A mode"""
    print("Interactive RAG System")
    print("=" * 50)
    print("Commands:")
    print("  - Ask questions normally")
    print("  - Type 'generate' to create questions from your content")
    print("  - Type 'exit' to quit")
    print("=" * 50)
    
    while True:
        try:
            question = input("\nQuestion> ").strip()
            
            if question.lower() in ("exit", "quit"):
                print("Goodbye!")
                break
            elif question.lower() == "generate":
                # Generate questions from content
                num_questions = input("How many questions to generate? (default: 5): ").strip()
                try:
                    num_questions = int(num_questions) if num_questions else 5
                except ValueError:
                    num_questions = 5
                
                print(f"Generating {num_questions} questions...")
                questions = rag.generate_questions_from_content(num_questions)
                
                if questions:
                    print(f"\nGenerated {len(questions)} questions:")
                    for i, q in enumerate(questions, 1):
                        print(f"\n{i}. {q['question']}")
                        print(f"   A) {q['one']}")
                        print(f"   B) {q['two']}")
                        print(f"   C) {q['three']}")
                        print(f"   D) {q['four']}")
                        print(f"   Correct: {q['correct']}")
                        print(f"   Category: {q['category']}")
                    
                    # Save questions
                    rag.save_questions_to_json(questions)
                    print(f"\nQuestions saved to {config.questions_file}")
                else:
                    print("No questions were generated.")
                continue
            elif not question:
                continue
            
            print("Thinking...")
            answer = rag.ask_question(question)
            print(f"\nAnswer:\n{answer}")
            
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"Error processing question: {e}")
            continue


def single_question_mode(rag, question):
    """Run single question mode"""
    try:
        print(f"Question: {question}")
        print("Thinking...")
        answer = rag.ask_question(question)
        print(f"\nAnswer:\n{answer}")
        return 0
    except Exception as e:
        print(f"Error processing question: {e}")
        return 1


def generate_questions_mode(rag, num_questions, output_file):
    """Run question generation mode"""
    try:
        print(f"Generating {num_questions} questions...")
        questions = rag.generate_questions_from_content(num_questions)
        
        if questions:
            print(f"\nGenerated {len(questions)} questions:")
            for i, q in enumerate(questions, 1):
                print(f"\n{i}. {q['question']}")
                print(f"   A) {q['one']}")
                print(f"   B) {q['two']}")
                print(f"   C) {q['three']}")
                print(f"   D) {q['four']}")
                print(f"   Correct: {q['correct']}")
                print(f"   Category: {q['category']}")
            
            # Save questions
            rag.save_questions_to_json(questions, output_file)
            print(f"\nQuestions saved to {output_file}")
            return 0
        else:
            print("No questions were generated.")
            return 1
            
    except Exception as e:
        print(f"Error generating questions: {e}")
        return 1


def main():
    """Main RAG execution function"""
    parser = argparse.ArgumentParser(description='Run the RAG system')
    parser.add_argument('--mode', type=str, default='interactive',
                       choices=['interactive', 'question', 'generate'],
                       help='Execution mode')
    parser.add_argument('--question', type=str,
                       help='Question to ask (for question mode)')
    parser.add_argument('--num-questions', type=int, default=5,
                       help='Number of questions to generate (for generate mode)')
    parser.add_argument('--output', type=str,
                       help='Output file for generated questions (for generate mode)')
    parser.add_argument('--data-dir', type=str, default=None,
                       help='Directory containing raw documents (default: from config)')
    parser.add_argument('--log-level', type=str, default='INFO',
                       choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
                       help='Logging level')
    
    args = parser.parse_args()
    
    # Set up logging
    logger = setup_logging(args.log_level, config.log_file)
    
    try:
        # Create RAG pipeline
        logger.info("Initializing RAG pipeline...")
        rag = create_rag_pipeline()
        
        # Load and process documents
        data_dir = args.data_dir or config.raw_data_dir
        logger.info(f"Loading documents from: {data_dir}")
        documents = rag.load_and_process_documents(data_dir)
        
        if not documents:
            logger.error("No documents were loaded. Check your data directory.")
            return 1
        
        logger.info(f"Successfully loaded {len(documents)} documents")
        
        # Run in specified mode
        if args.mode == 'interactive':
            interactive_mode(rag)
        elif args.mode == 'question':
            if not args.question:
                print("Error: --question is required for question mode")
                return 1
            return single_question_mode(rag, args.question)
        elif args.mode == 'generate':
            output_file = args.output or config.questions_file
            return generate_questions_mode(rag, args.num_questions, output_file)
        
        return 0
        
    except Exception as e:
        logger.error(f"RAG execution failed: {e}")
        return 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
