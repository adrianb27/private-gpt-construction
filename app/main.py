import os
import shutil
import streamlit as st
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage, SimpleDirectoryReader
from llama_index.vector_stores import ChromaVectorStore
from chromadb import PersistentClient
from dotenv import load_dotenv

load_dotenv()

CHROMA_DB_DIR = os.getenv("CHROMA_DB_DIR", "./chroma")
DATA_DIR = os.getenv("DATA_DIR", "./data")

st.set_page_config(page_title="PrivateGPT for Construction", layout="wide")
st.title("🏗️ PrivateGPT for Construction")

# Drag-and-drop file uploader
uploaded_files = st.file_uploader("📄 Upload your PDFs", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        with open(os.path.join(DATA_DIR, uploaded_file.name), "wb") as f:
            f.write(uploaded_file.read())
    st.success("Files uploaded! Now embedding...")

    documents = SimpleDirectoryReader(DATA_DIR).load_data()
    chroma_client = PersistentClient(path=CHROMA_DB_DIR)
    vector_store = ChromaVectorStore(chroma_collection=chroma_client.get_or_create_collection("construction-gpt"))
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    index = VectorStoreIndex.from_documents(documents, storage_context=storage_context)
    index.storage_context.persist()
    st.success("✅ Documents ingested and ready to query!")

# Input box
query = st.text_input("Ask something about your construction documents:")

if query:
    chroma_client = PersistentClient(path=CHROMA_DB_DIR)
    vector_store = ChromaVectorStore(chroma_collection=chroma_client.get_or_create_collection("construction-gpt"))
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    index = load_index_from_storage(storage_context)
    response = index.as_query_engine().query(query)

    st.markdown("### 🔍 Answer:")
    st.write(response.response)


