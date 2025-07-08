#!/bin/bash
echo "Installing dependencies..."
pip install -r requirements.txt

echo "Ingesting sample documents..."
python ingest/ingest_documents.py

echo "Launching Streamlit UI..."
streamlit run app/main.py
