from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import shutil
import os

CHROMA_PATH = "chroma_db"


def create_vector_db(chunks, reset=False):
    # Delete old DB so previous paper's data doesn't bleed in
    if reset and os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

    embedding = HuggingFaceEmbeddings()
    db = Chroma.from_texts(
        chunks,
        embedding,
        persist_directory=CHROMA_PATH
    )
    return db