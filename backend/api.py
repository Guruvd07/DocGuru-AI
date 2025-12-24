from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import os
import shutil

from pdf_loader import extract_text_from_pdf
from text_chunker import chunk_text
from embedding import generate_embeddings, model
from vector_store import create_faiss_index
from retriever import retrieve_relevant_chunks
from llm_answer import generate_answer

app = FastAPI(title="GuruDoc AI")

# CORS (future frontend ke liye)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Global in-memory store (simple version)
VECTOR_INDEX = None
TEXT_CHUNKS = None

@app.post("/upload-pdf")
def upload_pdf(file: UploadFile = File(...)):
    global VECTOR_INDEX, TEXT_CHUNKS

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Pipeline
    text = extract_text_from_pdf(file_path)
    TEXT_CHUNKS = chunk_text(text)
    embeddings = generate_embeddings(TEXT_CHUNKS)
    VECTOR_INDEX = create_faiss_index(embeddings)

    return {
        "message": "PDF uploaded and processed successfully",
        "total_chunks": len(TEXT_CHUNKS)
    }

@app.post("/ask")
def ask_question(question: str):
    if VECTOR_INDEX is None or TEXT_CHUNKS is None:
        return {"error": "Please upload a PDF first"}

    relevant_chunks = retrieve_relevant_chunks(
        query=question,
        model=model,
        index=VECTOR_INDEX,
        chunks=TEXT_CHUNKS
    )

    answer = generate_answer(question, relevant_chunks)

    return {
        "question": question,
        "answer": answer
    }
