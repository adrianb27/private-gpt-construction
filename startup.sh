#!/bin/bash
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt --no-cache-dir

echo "Ingesting sample documents..."
python ingest/ingest_documents.py

echo "Launching Streamlit UI..."
python3 -m streamlit run app/main.py --server.port=8501 --server.address=0.0.0.0
