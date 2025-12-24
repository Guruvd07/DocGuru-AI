from sentence_transformers import SentenceTransformer

# Load embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embeddings(text_chunks):
    """
    Convert list of text chunks into embeddings
    """
    embeddings = model.encode(text_chunks)
    return embeddings
