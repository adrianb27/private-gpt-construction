# 🏗️ PrivateGPT for Construction

A fully self-hosted GPT system built for construction companies. Uses LLaMA 3, ChromaDB, and Streamlit to allow teams to drag-and-drop PDF files (blueprints, contracts, RFIs) and ask natural language questions like:

- “What’s the square footage for lot 6?”
- “Show me subcontractor info from April”
- “What change orders were submitted for the foundation pour?”

---

### ⚙️ Tech Stack
- LLaMA 3 (via vLLM or Ollama)
- ChromaDB for vector storage
- LlamaIndex for retrieval
- Streamlit for secure local UI
- Private RunPod deployment

---

### 🛠️ How to Use
1. Clone this repo inside your RunPod instance
2. Load your model into `/workspace/models`
3. Add PDFs to `/workspace/data`
4. Update `.env` if needed
5. Run `./startup.sh`

---

### 🔐 No OpenAI. No Anthropic. 100% private.
Built for businesses that need secure, internal AI systems — no cloud APIs, no data leaks.

---

### 👷 Use Cases
- General contractors
- Architecture firms
- Real estate developers
- Permitting and inspection teams
