# server.py
import contextlib
import sys
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from rag_pipeline import create_rag_pipeline
from config import config

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

@app.get("/")
def read_root():
    return {"status": "online", "message": "Welcome to the RAG API!"}

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)