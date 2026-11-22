from pydantic import BaseModel
from typing import List, Optional

class QueryRequest(BaseModel):
    session_id: str
    query: str

class QueryResponse(BaseModel):
    answer: str
    source_documents: List[str]

class UploadResponse(BaseModel):
    message: str
    chunks_processed: int
