# Local Project Diary & Git Commit Architect (Phase 1 RAG)

A completely self-contained, air-gapped Retrieval-Augmented Generation (RAG) system that transforms loose, daily developer markdown logs into a searchable semantic knowledge base. 

This project demonstrates the foundational mechanics of a localized RAG architecture—handling local data ingestion, text tokenization chunking optimization, and deterministic local model context grounding using zero-cost, open-source infrastructure.

---

## 🛠️ Architectural Overview

The application is split into two decoupled, core engineering pipelines:

1. **The Ingestion Pipeline (`chunker.py`):** Ingests raw text artifacts, divides them logically using a `RecursiveCharacterTextSplitter` to maintain contextual integrity, translates text into high-dimensional geometric representations using local vector embedding models, and commits them to a persistent disk-backed vector store.
2. **The Retrieval & Generation Pipeline (`query_engine.py`):** Translates user queries into vectors, executes a Cosine Similarity search across the local database, extracts the top relevant context nodes ($k=2$), builds an engineered system instruction prompt, and routes it through a deterministic local Large Language Model to compile precise answers without hallucination risk.

---

## 🧰 Tech Stack & Prerequisites

* **LLM & Embedding Engine:** [Ollama](https://ollama.com/) executing **Llama 3.1 (8B)**
* **Orchestration Framework:** LangChain / Native Integration Packages (`langchain-ollama`)
* **Vector Database:** ChromaDB (`langchain-chroma`) via persistent local SQLite engine
* **Environment Sandbox:** Python Virtual Environment (`venv`)

---

## 🚀 Getting Started (Local Setup)

Follow these steps to run this project entirely offline on your local machine:

### 1. Initialize the AI Model Server
Download and install [Ollama](https://ollama.com). Open your system terminal and pull down the Llama 3.1 model weights:
```bash
ollama pull llama3.1

2. Sandbox Setup & Activation
Clone this repository to your local directory, navigate into it, and establish a clean virtual python environment:

Bash
# Create the environment directory
python -m venv venv

# Activate the environment
# On Windows (Command Prompt):
.\venv\Scripts\activate.bat

# On macOS / Linux:
source venv/bin/activate
3. Install Core Framework Dependencies
With your virtual environment active (venv), install the exact pinned version packages required:

Bash
pip install -r requirements.txt
4. Hydrate the Data Vault
Place your loose handwritten development markdown files inside the data_vault/ directory (e.g., data_vault/day1_notes.md). Ensure it contains your daily logs, encountered bugs, and technical choices.

🏃‍♂️ Execution Pipeline
Step 1: Ingest and Vectorize Data
Run the ingestion pipeline to parse, chunk, and embed your raw developer text documents directly to your local drive partition:

Bash
python chunker.py
Expected Output: You will observe confirmations detailing the character payload size, chunk array distribution, and a confirmation that db_storage/ was successfully compiled.

Step 2: Search Your Technical History
Launch the conversational query engine loop to safely interview your private repository data:

Bash
python query_engine.py
Example Usage Interaction:
Plaintext
Ask about your project: What did I build using FastAPI?
Searching database for context regarding: What did I build using FastAPI?..

[Found matching data in data_vault/day1_notes.md]
↳ Today I built the authentication routing using FastAPI...

LLM Answer: You built the authentication routing using FastAPI."# project_diary_rag" 
