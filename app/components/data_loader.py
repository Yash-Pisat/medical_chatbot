import os

from app.components.pdf_loader import load_pdf_files, split_documents
from app.components.vector_store import save_vector_store
from app.config.config import DB_FAISS_PATH

from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

def process_and_store_pdfs():
    try:
        logger.info("Creating vector store")
        documents = load_pdf_files()

        logger.info
        text_chunks = split_documents(documents)

        save_vector_store(text_chunks)
        logger.info("Vector store created successfully.")
    
    except CustomException as e:
        error_message = CustomException("Failed to load data from directory", e)
        logger.error(str(error_message))

if __name__ == "__main__":
    process_and_store_pdfs()
