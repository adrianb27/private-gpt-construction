import os
import streamlit as st
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.vector_stores import ChromaVectorStore
from chromadb import PersistentClient
from dotenv import load_dotenv

load_dotenv()

CHROMA_DB_DIR = os.getenv("CHROMA_DB_DIR", "./chroma")

st.set_page_config(page_title="PrivateGPT for Construction", layout="wide")
st.title("🏗️ PrivateGPT for Construction")

query = st.text_input("Ask something about your construction documents:")

if query:
    with st.spinner("Thinking..."):
        chroma_client = PersistentClient(path=CHROMA_DB_DIR)
        vector_store = ChromaVectorStore(chroma_collection=chroma_client.get_or_create_collection("construction-gpt"))
        storage_context = StorageContext.from_defaults(vector_store=vector_store)

        index = load_index_from_storage(storage_context)
        response = index.as_query_engine().query(query)

        st.markdown("### 🔍 Answer:")
        st.write(response.response)
