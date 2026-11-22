import os
from typing import List
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain_community.vectorstores import Pinecone as PineconeVectorStore
from pinecone import Pinecone
from src.config import settings

class RAGEngine:
    def __init__(self):
        # Initialize Pinecone
        self.pc = Pinecone(api_key=settings.PINECONE_API_KEY)
        self.index = self.pc.Index(settings.PINECONE_INDEX_NAME)
        
        self.embeddings = OpenAIEmbeddings(openai_api_key=settings.OPENAI_API_KEY)
        self.llm = ChatOpenAI(
            model_name="gpt-3.5-turbo",
            temperature=0.1,
            streaming=True,
            openai_api_key=settings.OPENAI_API_KEY
        )

    def get_vectorstore(self):
        return PineconeVectorStore(
            index=self.index,
            embedding=self.embeddings,
            text_key="text"
        )

    def ingest_documents(self, documents: List):
        """Embeds documents and stores them in Pinecone."""
        vectorstore = self.get_vectorstore()
        vectorstore.add_documents(documents)

    def get_chain(self, memory):
        """Returns the conversational retrieval chain."""
        vectorstore = self.get_vectorstore()
        
        return ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=vectorstore.as_retriever(search_kwargs={"k": 5}),
            memory=memory,
            return_source_documents=True
        )
