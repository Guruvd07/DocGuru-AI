import numpy as np

def retrieve_relevant_chunks(query, model, index, chunks, top_k=3):
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), top_k)

    relevant_chunks = []
    for idx in indices[0]:
        relevant_chunks.append(chunks[idx])

    return relevant_chunks
