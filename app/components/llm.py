from langchain_groq import ChatGroq
from app.config.config import GROQ_API_KEY

from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

def load_llm(model_name: str = "llama-3.1-8b-instant", groq_api_key: str = GROQ_API_KEY):
    try:
        logger.info("loading LLM from Hugging Face...")

        llm = ChatGroq(
            groq_api_key = groq_api_key,
            model_name=model_name,
            temperature = 0.1,  
            max_tokens = 256,
        )

        logger.info("LLM loaded successfully.")

        return llm
    
    except Exception as e:
        error_message = CustomException("Failed to load LLM from Hugging Face", e)
        logger.error(str(error_message))