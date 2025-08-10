import os
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.common.logger import get_logger
from app.common.custom_exception import CustomException

from app.config.config import DATA_PATH, CHUNK_SIZE, CHUCK_OVERLAP

logger = get_logger(__name__)
 

def load_pdf_files():
    try:
        if not os.path.exists(DATA_PATH):
            raise CustomException(f"Data path {DATA_PATH} does not exist.")
        
        logger.info(f"Loading PDF files from {DATA_PATH}...")
        loader = DirectoryLoader(DATA_PATH, glob="*.pdf", loader_cls=PyPDFLoader)
        documents = loader.load()

        if not documents:
            raise CustomException("No PDF documents found in the specified directory.")
        else:
            logger.info(f"Found {len(documents)} PDF documents.")

        return documents
    
    except Exception as e:
        error_message = CustomException("Failed to load PDF files", e)
        logger.error(str(error_message))
        return []
    
def split_documents(documents):
    try:
        if not documents:
            raise CustomException("No documents to split.")

        logger.info("Splitting documents into chunks...")
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUCK_OVERLAP)
        chunks = text_splitter.split_documents(documents)

        logger.info(f"Split into {len(chunks)} chunks.")
        return chunks
    
    except Exception as e:
        error_message = CustomException("Failed to split documents", e)
        logger.error(str(error_message))
        return []
            