#!/bin/bash
export PATH=$PATH:/root/.local/bin

echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt --no-cache-dir

echo "Ingesting sample documents..."
python ingest/ingest_documents.py

echo "Launching Streamlit UI..."
streamlit run app/main.py --server.port=8501 --server.address=0.0.0.0
