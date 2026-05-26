from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.ai_service import rag_chat, semantic_search, store_document

app = FastAPI(title="Oracle 26ai RAG Service", version="1.0")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Models ──────────────────────────────────────────────────────
class ChatRequest(BaseModel):
    question: str

class ChatResponse(BaseModel):
    answer: str
    sources: list[str]
    context_used: bool

class SearchRequest(BaseModel):
    query: str
    top_k: int = 5

class SearchResult(BaseModel):
    chunk: str
    title: str
    score: float

class DocumentRequest(BaseModel):
    title: str
    content: str
    doc_type: str = "general"

# ── Endpoints ───────────────────────────────────────────────────
@app.get("/health")
async def health():
    return {"status": "healthy", "service": "Oracle 26ai RAG API"}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        result = rag_chat(request.question)
        return ChatResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/search", response_model=list[SearchResult])
async def search(request: SearchRequest):
    try:
        results = semantic_search(request.query, top_k=request.top_k)
        return [SearchResult(**r) for r in results]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/documents")
async def upload_document(request: DocumentRequest):
    try:
        doc_id = store_document(request.title, request.content, request.doc_type)
        return {"doc_id": doc_id, "status": "stored"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
