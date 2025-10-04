# RAG Project - Retrieval-Augmented Generation System

A modular and extensible RAG implementation with support for multiple LLM backends, vector databases, and document processing pipelines.

## Project Structure

```
rag_project/
├── data/
│   ├── raw/                 # Raw documents (PDFs, CSVs, text)
│   ├── processed/           # Cleaned/processed data for embedding
│   └── embeddings/          # Vector embeddings stored as files (optional)
│
├── src/
│   ├── __init__.py
│   ├── config.py            # Configs like API keys, paths, DB settings
│   ├── preprocess.py        # Data cleaning and text preprocessing
│   ├── embeddings.py        # Code to generate embeddings (e.g., OpenAI, HuggingFace)
│   ├── retriever.py         # Vector DB queries, FAISS, Pinecone, Weaviate
│   ├── generator.py         # LLM interface for generation (OpenAI, Llama, etc.)
│   ├── rag_pipeline.py      # Integrates retriever + generator
│   └── utils.py             # Helper functions (logging, metrics, etc.)
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   └── 02_rag_demo.ipynb
│
├── scripts/
│   ├── ingest_data.py       # Script to load and preprocess documents
│   ├── run_rag.py           # CLI for running RAG queries
│   ├── server.py            # FastAPI server for RAG system
│   └── test_rag.py          # Test script for debugging
│
├── requirements.txt         # Python dependencies
├── README.md
└── env.template             # Environment variables template
```

## Features

- **Modular Architecture**: Clean separation of concerns with configurable components
- **Multiple LLM Support**: Ollama, OpenAI, HuggingFace models
- **Vector Database Support**: ClickHouse, FAISS (extensible for Pinecone, Weaviate)
- **Document Processing**: Automatic text cleaning, chunking, and preprocessing
- **Question Generation**: Generate multiple-choice questions from your content
- **Interactive Interface**: CLI and web API interfaces
- **Jupyter Notebooks**: Data exploration and demonstration notebooks

## Quick Start

### Prerequisites
1. **Ollama** - Install and run locally:
   ```bash
   # Install Ollama (see https://ollama.ai)
   ollama serve
   ollama pull mistral
   ```

2. **ClickHouse** - Install and run:
   ```bash
   # Using Docker (recommended)
   docker run -d --name clickhouse-server -p 8123:8123 -p 9000:9000 clickhouse/clickhouse-server
   
   # Or install locally (see https://clickhouse.com/docs/en/install)
   ```

3. **Python Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

1. **Copy environment template**:
   ```bash
   cp env.template .env
   ```

2. **Edit `.env` file** with your configuration:
   ```bash
   # ClickHouse settings
   CLICKHOUSE_HOST=localhost
   CLICKHOUSE_PORT=8123
   CLICKHOUSE_USER=default
   CLICKHOUSE_PASSWORD=your_password
   CLICKHOUSE_DATABASE=rag_db
   
   # Ollama settings
   OLLAMA_MODEL=mistral
   OLLAMA_TEMPERATURE=0.0
   ```

### Running the RAG System

1. **Test the setup**:
   ```bash
   python scripts/test_rag.py
   ```

2. **Ingest your documents**:
   ```bash
   python scripts/ingest_data.py
   ```

3. **Run interactive RAG**:
   ```bash
   python scripts/run_rag.py
   ```

4. **Start the web API server**:
   ```bash
   python scripts/server.py
   ```

5. **Explore with Jupyter notebooks**:
   ```bash
   jupyter notebook notebooks/
   ```

### Usage Examples

#### Command Line Interface
```bash
# Interactive mode
python scripts/run_rag.py

# Single question
python scripts/run_rag.py --mode question --question "What is blockchain?"

# Generate questions
python scripts/run_rag.py --mode generate --num-questions 10
```

#### Web API
```bash
# Start server
python scripts/server.py

# Test API
curl -X POST "http://localhost:8000/ask" \
     -H "Content-Type: application/json" \
     -d '{"text": "What is blockchain?"}'
```

#### Jupyter Notebooks
- `01_data_exploration.ipynb`: Explore your data and preprocessing pipeline
- `02_rag_demo.ipynb`: Interactive RAG demonstrations and testing  
