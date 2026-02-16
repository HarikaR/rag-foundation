# RAG Foundation

Building Retrieval-Augmented Generation (RAG) systems from scratch in a clean, modular, and production-oriented way.

This repository is focused on understanding the **core engineering components** behind RAG systems — not just using frameworks.

---

## Goal

To deeply understand and implement:

- Document loading
- Text cleaning
- Chunking strategies
- Embedding generation
- Vector similarity search
- Top-K retrieval
- Evaluation of retrieval quality

All implemented step-by-step in Python.

---

## Project Structure

rag-foundation/
│
├── data/ # Sample documents
├── src/
│ ├── loader.py # Document loading logic
│ ├── chunker.py # Chunking strategies
│ └── (future) embedder.py
│
└── main.py # Pipeline execution
