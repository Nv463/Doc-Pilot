from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
import PyPDF2
import io

class DocumentProcessor:
    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )

    def process_pdf(self, file_content: bytes, filename: str) -> List[Document]:
        """Extracts text from PDF and splits it into chunks."""
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(file_content))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"

        # Create document with metadata
        doc = Document(
            page_content=text,
            metadata={"source": filename, "type": "pdf"}
        )

        return self.text_splitter.split_documents([doc])
