# server.py
import contextlib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from langchain.chains import RetrievalQA
from langchain_ollama import Ollama
# Import the functions from your existing RAG script
from simple_rag import build_or_load_store, load_documents, DOCS_DIR

@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Handles startup and shutdown events.
    Loads the RAG system into app.state for use in API endpoints.
    """
    print("Loading RAG system...")
    try:
        docs = load_documents(DOCS_DIR)
        if not docs:
            print(f"Warning: No documents in '{DOCS_DIR}'. API will be unable to answer questions.")
            app.state.qa_chain = None
        else:
            retriever = build_or_load_store(docs)
            llm = Ollama(model="mistral", temperature=0)
            app.state.qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
            print("✅ RAG system loaded successfully.")
    except Exception as e:
        print(f"❌ Error loading RAG system: {e}")
        app.state.qa_chain = None
    
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

    qa_chain = app.state.qa_chain
    if not qa_chain:
        raise HTTPException(status_code=503, detail="RAG system is not loaded or failed to load.")
    
    print(f"Received question: {request.text}")
    # DEPRECATION FIX: .run() is replaced with .invoke()
    result = qa_chain.invoke({"query": request.text})
    return {"question": request.text, "answer": result['result']}

@app.get("/")
def read_root():
    return {"status": "online", "message": "Welcome to the RAG API!"}

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)