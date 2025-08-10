import os
from langchain_community.vectorstores import FAISS
from app.components.embeddings import get_embedding_model

from app.common.logger import get_logger
from app.common.custom_exception import CustomException

from app.config.config import DB_FAISS_PATH

logger = get_logger(__name__)

def load_vector_store():
    try:
        embedding_model = get_embedding_model()
        
        if os.path.exists(DB_FAISS_PATH):
            logger.info("Loading existing FAISS vector store...")
            return FAISS.load_local(
                DB_FAISS_PATH, 
                embedding_model,
                allow_dangerous_deserialization=True
            )
        else:
            logger.info("No vector store not found. Creating a new one...")
            
    except Exception as e:
        error_message =CustomException("failed to load vector store", e)
        logger.error(error_message)

#create a new vector store if it doesn't exist
def create_vector_store(text_chunks):
    try:
        if not text_chunks:
            raise CustomException("No text chunks were found.")

        logger.info("Creating new FAISS vector store...")

        embedding_model = get_embedding_model()
        
        vector_db = FAISS.from_documents(text_chunks, embedding_model)
        logger.info("Saving vector store")

        vector_db.save_local(DB_FAISS_PATH)
        logger.info("Vector store saved successfully.")
        return vector_db
    
    except Exception as e:
        error_message = CustomException("failed to create new vector store", e)
        logger.error(str(error_message))