# server.py
import contextlib
import sys
import os
import shutil
import json
import threading
import time
from datetime import datetime
from fastapi import FastAPI, HTTPException, UploadFile, File, BackgroundTasks
from pydantic import BaseModel
import uvicorn

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from rag_pipeline import create_rag_pipeline
from config import config

# Global storage for processing status (in production, use a database)
processing_status = {}
processing_lock = threading.Lock()

@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Handles startup and shutdown events.
    Loads the RAG system into app.state for use in API endpoints.
    """
    print("Loading RAG system...")
    try:
        # Create RAG pipeline
        rag = create_rag_pipeline()
        
        # Load and process documents
        docs = rag.load_and_process_documents()
        if not docs:
            print(f"Warning: No documents in '{config.raw_data_dir}'. API will be unable to answer questions.")
            app.state.rag_pipeline = None
        else:
            app.state.rag_pipeline = rag
            print("✅ RAG system loaded successfully.")
    except Exception as e:
        print(f"❌ Error loading RAG system: {e}")
        app.state.rag_pipeline = None
    
    yield
    
    print("RAG system shutting down.")


app = FastAPI(
    title="RAG API Server",
    description="An API to interact with the RAG system.",
    version="1.0.0",
    lifespan=lifespan
)

class QuestionRequest(BaseModel):
    text: str


class UploadResponse(BaseModel):
    filename: str
    original_filename: str
    file_size: int
    upload_timestamp: str
    file_path: str
    status: str
    processing_status: str = "pending"
    document_id: str = ""

class ProcessingStatus(BaseModel):
    document_id: str
    filename: str
    status: str  # pending, processing, completed, failed
    upload_timestamp: str
    processing_start_time: str = ""
    processing_end_time: str = ""
    error_message: str = ""
    chunks_created: int = 0
    documents_indexed: int = 0

class ProcessingStatusResponse(BaseModel):
    document_id: str
    status: str

@app.post("/ask")
def ask_question(request: QuestionRequest):
    """
    Receives a question, gets an answer from the RAG system, and returns it.
    """
    rag_pipeline = app.state.rag_pipeline
    if not rag_pipeline:
        raise HTTPException(status_code=503, detail="RAG system is not loaded or failed to load.")
    
    print(f"Received question: {request.text}")
    try:
        answer = rag_pipeline.ask_question(request.text)
        return {"question": request.text, "answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing question: {str(e)}")

@app.post("/upload", response_model=UploadResponse)
async def upload_markdown_file(file: UploadFile = File(...)):
    """
    Upload a markdown file to the RAG system.

    Args:
        file: The markdown file to upload

    Returns:
        UploadResponse with file details

    Raises:
        HTTPException: If file validation fails or upload error occurs
    """
    # Validate file extension
    allowed_extensions = {'.md', '.markdown'}
    file_extension = os.path.splitext(file.filename.lower())[1]

    if file_extension not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid file type. Only markdown files are allowed. Got: {file_extension}"
        )

    # Validate file size (10MB limit)
    max_file_size = 10 * 1024 * 1024  # 10MB in bytes
    file_size = 0

    # Read file content to validate and get size
    content = await file.read()
    file_size = len(content)

    if file_size == 0:
        raise HTTPException(
            status_code=400,
            detail="Empty file. Please upload a valid markdown file."
        )

    if file_size > max_file_size:
        raise HTTPException(
            status_code=413,
            detail=f"File too large. Maximum size is 10MB. Got: {file_size / (1024*1024):.2f}MB"
        )

    # Generate unique filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_filename = f"{os.path.splitext(file.filename)[0]}_{timestamp}.md"
    file_path = os.path.join(config.raw_data_dir, safe_filename)

    try:
        # Ensure directory exists
        os.makedirs(config.raw_data_dir, exist_ok=True)

        # Write file to disk
        with open(file_path, "wb") as buffer:
            buffer.write(content)

        print(f"✅ File uploaded successfully: {safe_filename}")

        return UploadResponse(
            filename=safe_filename,
            original_filename=file.filename,
            file_size=file_size,
            upload_timestamp=datetime.now().isoformat(),
            file_path=file_path,
            status="success"
        )

    except Exception as e:
        print(f"❌ Error saving file: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to save file: {str(e)}"
        )


@app.get("/")
def read_root():
    return {"status": "online", "message": "Welcome to the RAG API!"}

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)