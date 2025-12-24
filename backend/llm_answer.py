import os
from dotenv import load_dotenv
from google import genai

# Load env vars
load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in .env file")

client = genai.Client(api_key=API_KEY)

# FREE TIER SAFE MODEL
MODEL_NAME = "models/gemini-flash-lite-latest"

def generate_answer(question, context_chunks):
    # 🔒 LIMIT CONTEXT (very important for free tier)
    limited_chunks = context_chunks[:2]
    context = "\n\n".join(limited_chunks)

    prompt = f"""
Answer ONLY using the context below.
If answer is not present, say "Not found".

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text
