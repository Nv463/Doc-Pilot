from langchain.memory import ConversationBufferMemory
from langchain.memory.chat_message_histories import RedisChatMessageHistory
from src.config import settings

class RedisMemoryManager:
    def __init__(self):
        self.redis_url = settings.REDIS_URL

    def get_memory(self, session_id: str) -> ConversationBufferMemory:
        """Retrieves or creates a conversational memory backed by Redis."""
        message_history = RedisChatMessageHistory(
            url=self.redis_url,
            ttl=3600,
            session_id=session_id
        )
        
        return ConversationBufferMemory(
            memory_key="chat_history",
            chat_memory=message_history,
            return_messages=True,
            output_key="answer"
        )
