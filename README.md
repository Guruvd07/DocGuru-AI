# 📄 GuruDoc AI

## RAG-Based PDF Question Answering System (API-Driven)

GuruDoc AI is a **backend, API-first AI system** that enables users to upload PDF documents and ask natural-language questions. The system returns **accurate, document-grounded answers** using a **Retrieval-Augmented Generation (RAG)** architecture.

This project focuses purely on **core AI intelligence and backend design**. There is **no frontend implementation**. All APIs are tested and validated using **Swagger UI**.

---

## 🚀 Key Features

* Upload and process PDF documents via REST APIs
* Semantic search over document content using embeddings
* Accurate question answering strictly from document context
* Hallucination prevention using RAG architecture
* Clean, scalable backend design

---

## 🧱 Project Type

* Backend AI Project
* API-first architecture
* No HTML / CSS / JavaScript
* No frontend framework

> Swagger UI is used **only for API testing and validation**, not as a frontend.

---

## 🏗️ System Architecture

```
Client (Swagger UI / Postman)
        |
        | HTTP Requests
        v
FastAPI Backend
        |
        | PDF Text Extraction
        | Text Cleaning
        | Text Chunking
        | Embedding Generation
        | Vector Search
        v
Gemini LLM
        |
        v
JSON Response
```

---

## 🔁 Workflow Overview

### 1️⃣ PDF Upload (`POST /upload-pdf`)

* PDF file is uploaded using `multipart/form-data`
* Text is extracted page-by-page
* Extracted text is cleaned and normalized
* Text is split into smaller semantic chunks
* Each chunk is converted into embeddings
* Embeddings are stored in a FAISS vector index

**Sample Response:**

```json
{
  "message": "PDF uploaded and processed successfully",
  "total_chunks": 12
}
```

---

### 2️⃣ Question Answering (`POST /ask`)

* User question is received as input
* Question is converted into an embedding
* FAISS retrieves top-k relevant document chunks
* Retrieved chunks are merged as context
* Context + question are passed to the LLM
* Answer is generated strictly from document content

**Sample Response:**

```json
{
  "question": "Does the document mention any internship?",
  "answer": "The document does not explicitly mention an internship."
}
```

---

## 🧠 Core Concept — Retrieval-Augmented Generation (RAG)

RAG is an AI architecture that combines **information retrieval** with **language generation**.

Instead of allowing the LLM to answer from its own memory:

1. Relevant information is first retrieved from the document using vector search
2. The LLM generates an answer only from the retrieved context

### Why RAG?

* Prevents hallucination
* Ensures factual accuracy
* Enterprise-grade safety
* Suitable for private and dynamic data

---

## 🛠️ Technology Stack

| Technology            | Purpose                         |
| --------------------- | ------------------------------- |
| FastAPI               | Backend REST API framework      |
| Swagger UI            | API testing and validation      |
| Sentence Transformers | Semantic text embeddings        |
| FAISS                 | Vector similarity search        |
| Gemini LLM            | Context-aware answer generation |
| RAG Architecture      | Hallucination prevention        |

---

## 🔐 Hallucination Prevention Strategy

* Retrieval-Augmented Generation pipeline
* Semantic vector search before generation
* Strict prompt instructions:

  * *Answer only from the given context*
  * *If information is not present, say it is not explicitly mentioned*

This makes the system reliable and enterprise-ready.

---

## 🧪 Testing

* All endpoints tested using Swagger UI
* Verified:

  * Successful PDF ingestion
  * Correct chunk creation
  * Accurate semantic retrieval
  * Zero hallucinated answers

---

## 🏆 Why This Project Matters

* Demonstrates real-world AI system design
* Focuses on backend and core intelligence
* Uses industry-standard RAG architecture
* Easily extensible and scalable
* Interview-ready AI project

---

## 📌 Use Cases

* Legal document analysis
* Resume screening systems
* Internal company knowledge bases
* Research paper Q&A
* Policy and compliance assistants

---

## 🔮 Future Enhancements

* Persistent vector storage
* Support for scanned PDFs using OCR
* Authentication and access control
* Multi-document querying
* UI integration (optional)

---

## 🧾 Summary

GuruDoc AI is a **production-aligned backend AI system** that demonstrates how modern enterprises build **accurate, trustworthy document question-answering solutions** using Retrieval-Augmented Generation.

---

**Auth
