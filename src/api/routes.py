from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from src.models.schemas import QueryRequest, QueryResponse, UploadResponse
from src.document_processor import DocumentProcessor
from src.rag_engine import RAGEngine
from src.utils.redis_memory import RedisMemoryManager

router = APIRouter()

processor = DocumentProcessor()
rag_engine = RAGEngine()
memory_manager = RedisMemoryManager()

@router.post("/upload", response_model=UploadResponse)
async def upload_document(file: UploadFile = File(...)):
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are supported")
    
    try:
        content = await file.read()
        documents = processor.process_pdf(content, file.filename)
        rag_engine.ingest_documents(documents)
        
        return UploadResponse(
            message="Document successfully processed and indexed",
            chunks_processed=len(documents)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/query", response_model=QueryResponse)
async def query_document(request: QueryRequest):
    try:
        # Get memory for this session
        memory = memory_manager.get_memory(request.session_id)
        
        # Get the QA chain
        chain = rag_engine.get_chain(memory)
        
        # Execute query
        result = chain({"question": request.query})
        
        # Extract unique sources
        sources = list(set([doc.metadata.get("source", "Unknown") for doc in result["source_documents"]]))
        
        return QueryResponse(
            answer=result["answer"],
            source_documents=sources
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
