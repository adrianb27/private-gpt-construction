import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
from llama_index.vector_stores import ChromaVectorStore
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core.node_parser import SimpleNodeParser
from llama_index.core.settings import Settings
from chromadb import PersistentClient
from dotenv import load_dotenv

load_dotenv()

DATA_DIR = os.getenv("DATA_DIR", "./data")
CHROMA_DB_DIR = os.getenv("CHROMA_DB_DIR", "./chroma")

from llama_index.embeddings.huggingface import HuggingFaceEmbedding
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

parser = SimpleNodeParser()

print("Loading documents...")
documents = SimpleDirectoryReader(DATA_DIR).load_data()

nodes = parser.get_nodes_from_documents(documents)

chroma_client = PersistentClient(path=CHROMA_DB_DIR)
vector_store = ChromaVectorStore(chroma_collection=chroma_client.get_or_create_collection("construction-gpt"))

storage_context = StorageContext.from_defaults(vector_store=vector_store)

print("Building index...")
index = VectorStoreIndex(nodes, storage_context=storage_context)
index.storage_context.persist()

print("✅ Ingestion complete.")

