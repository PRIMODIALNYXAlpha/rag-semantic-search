# ==============================
# SEMANTIC SEARCH (PINECONE + STREAMLIT) - FINAL
# ==============================

import streamlit as st
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone, ServerlessSpec
import numpy as np
import os
from dotenv import load_dotenv

# Load .env file properly
env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(env_path)

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

# Debug check (remove later)
# st.write("API KEY:", PINECONE_API_KEY)

# Load model (cached)
@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

# Load documents
def load_documents(uploaded_file):
    lines = uploaded_file.read().decode("utf-8").splitlines()
    lines = [l.strip() for l in lines if l.strip()]

    # Combine Q + A pairs
    docs = [f"{lines[i]} {lines[i+1]}" for i in range(0, len(lines), 2)]
    return docs

# Initialize Pinecone
def init_pinecone(dimension):
    if not PINECONE_API_KEY:
        st.error("❌ API key not loaded. Check your .env file.")
        st.stop()

    pc = Pinecone(api_key=PINECONE_API_KEY)
    index_name = "semantic-search"

    existing_indexes = [i.name for i in pc.list_indexes()]

    if index_name not in existing_indexes:
        pc.create_index(
            name=index_name,
            dimension=dimension,
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )
        )

    return pc.Index(index_name)

# Upload vectors
def upload_to_pinecone(index, docs, model):
    embeddings = model.encode(docs)

    vectors = [
        (str(i), embeddings[i].tolist(), {"text": docs[i]})
        for i in range(len(docs))
    ]

    index.upsert(vectors)

# Search function
def search(query, model, index):
    query_embedding = model.encode([query])[0]

    results = index.query(
        vector=query_embedding.tolist(),
        top_k=3,
        include_metadata=True
    )

    return results["matches"]

# ==============================
# STREAMLIT UI
# ==============================

def main():
    st.set_page_config(page_title="Semantic Search", layout="centered")

    st.title("🔍 Semantic Search using Pinecone")
    st.write("Upload a .txt file (Q & A pairs) and search intelligently")

    uploaded_file = st.file_uploader("Upload your .txt file", type="txt")

    if uploaded_file:
        model = load_model()
        docs = load_documents(uploaded_file)

        index = init_pinecone(dimension=384)
        upload_to_pinecone(index, docs, model)

        st.success("✅ Data uploaded successfully!")

        query = st.text_input("Enter your query")

        if query:
            results = search(query, model, index)

            st.subheader("📌 Results")
            for r in results:
                st.write(f"Score: {r['score']:.4f}")
                st.write(r["metadata"]["text"])
                st.markdown("---")

if __name__ == "__main__":
    main()