import os
HF_token = os.environ.get("HF_TOKEN")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

HUGGINGFACE_REPO_ID = "mistralai/Mistral-7B-Instruct-v0.3"
DB_FAISS_PATH = "vector_store/db_faiss"
DATA_PATH = "data/"
CHUNK_SIZE = 500
CHUCK_OVERLAP = 50