#!/usr/bin/env python3
"""
Test script to debug RAG issues with ClickHouse
"""
import os
import sys

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

def test_imports():
    """Test if all required packages are available"""
    print("Testing imports...")
    try:
        from langchain.text_splitter import CharacterTextSplitter
        print("✓ CharacterTextSplitter imported")
    except ImportError as e:
        print(f"✗ CharacterTextSplitter import failed: {e}")
        return False
    
    try:
        from langchain.document_loaders import TextLoader
        print("✓ TextLoader imported")
    except ImportError as e:
        print(f"✗ TextLoader import failed: {e}")
        return False
    
    try:
        import clickhouse_connect
        print("✓ clickhouse_connect imported")
    except ImportError as e:
        print(f"✗ clickhouse_connect import failed: {e}")
        return False
    
    try:
        from langchain.chains import RetrievalQA
        print("✓ RetrievalQA imported")
    except ImportError as e:
        print(f"✗ RetrievalQA import failed: {e}")
        return False
    
    try:
        from langchain_community.embeddings import OllamaEmbeddings
        print("✓ OllamaEmbeddings imported")
    except ImportError as e:
        print(f"✗ OllamaEmbeddings import failed: {e}")
        return False
    
    try:
        from langchain_community.llms import Ollama
        print("✓ Ollama imported")
    except ImportError as e:
        print(f"✗ Ollama import failed: {e}")
        return False
    
    return True

def test_ollama_connection():
    """Test if Ollama is accessible"""
    print("\nTesting Ollama connection...")
    try:
        from langchain_community.llms import Ollama
        llm = Ollama(model="mistral", temperature=0)
        # Try a simple test
        response = llm("Hello")
        print(f"✓ Ollama connection successful: {response[:50]}...")
        return True
    except Exception as e:
        print(f"✗ Ollama connection failed: {e}")
        return False

def test_embeddings():
    """Test if embeddings work"""
    print("\nTesting embeddings...")
    try:
        from langchain_community.embeddings import OllamaEmbeddings
        embeddings = OllamaEmbeddings(model="mistral")
        test_text = "This is a test"
        result = embeddings.embed_query(test_text)
        print(f"✓ Embeddings working: {len(result)} dimensions")
        return True
    except Exception as e:
        print(f"✗ Embeddings failed: {e}")
        return False

def test_clickhouse_connection():
    """Test ClickHouse connection"""
    print("\nTesting ClickHouse connection...")
    try:
        import clickhouse_connect
        
        # Get connection details from environment or user
        host = os.getenv("CLICKHOUSE_HOST", "localhost")
        port = int(os.getenv("CLICKHOUSE_PORT", "8123"))
        user = os.getenv("CLICKHOUSE_USER", "default")
        password = os.getenv("CLICKHOUSE_PASSWORD", "")
        
        if not password:
            print("⚠️  No ClickHouse password provided. Set CLICKHOUSE_PASSWORD environment variable or provide it interactively.")
            password = input("ClickHouse password: ").strip()
        
        client = clickhouse_connect.get_client(
            host=host,
            port=port,
            username=user,
            password=password
        )
        
        # Test basic query
        result = client.query("SELECT 1 as test")
        print(f"✓ ClickHouse connection successful: {result.result_rows[0][0]}")
        return True
    except Exception as e:
        print(f"✗ ClickHouse connection failed: {e}")
        print("Make sure ClickHouse is running and accessible")
        return False

def test_file_loading():
    """Test loading a single file"""
    print("\nTesting file loading...")
    try:
        from preprocess import load_documents
        from config import config
        
        # Test loading from data/raw directory
        data_dir = config.raw_data_dir
        if not os.path.exists(data_dir):
            print(f"✗ Data directory does not exist: {data_dir}")
            return False
        
        docs = load_documents(data_dir)
        if docs:
            print(f"✓ File loaded: {len(docs)} documents, {len(docs[0].page_content)} characters")
            return True
        else:
            print("✗ No .md files found")
            return False
    except Exception as e:
        print(f"✗ File loading failed: {e}")
        return False

def main():
    print("RAG Debug Test with ClickHouse")
    print("=" * 50)
    
    if not test_imports():
        print("\n❌ Import test failed. Install required packages:")
        print("pip install langchain clickhouse-connect ollama")
        return
    
    if not test_clickhouse_connection():
        print("\n❌ ClickHouse test failed. Make sure ClickHouse is running and accessible.")
        return
    
    if not test_ollama_connection():
        print("\n❌ Ollama test failed. Make sure Ollama is running:")
        print("ollama serve")
        print("ollama pull mistral")
        return
    
    if not test_embeddings():
        print("\n❌ Embeddings test failed.")
        return
    
    if not test_file_loading():
        print("\n❌ File loading test failed.")
        return
    
    print("\n✅ All tests passed! The RAG system with ClickHouse should work.")

if __name__ == "__main__":
    main()
