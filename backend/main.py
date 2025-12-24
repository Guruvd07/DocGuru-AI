from pdf_loader import extract_text_from_pdf
from text_chunker import chunk_text
from embedding import generate_embeddings, model
from vector_store import create_faiss_index
from retriever import retrieve_relevant_chunks
from llm_answer import generate_answer

if __name__ == "__main__":
    pdf_path = "../data/uploads/sample.pdf"

    text = extract_text_from_pdf(pdf_path)
    chunks = chunk_text(text)

    embeddings = generate_embeddings(chunks)
    index = create_faiss_index(embeddings)

    query = "Does the document mention any internship or professional work experience?"

    relevant_chunks = retrieve_relevant_chunks(
        query=query,
        model=model,
        index=index,
        chunks=chunks
    )

    final_answer = generate_answer(query, relevant_chunks)

    print("\n🤖 FINAL AI ANSWER:\n")
    print(final_answer)
