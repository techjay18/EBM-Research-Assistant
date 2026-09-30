# EBM Research Assistant

## Purpose
An AI-powered Evidence-Based Medicine (EBM) research assistant that enables healthcare professionals and researchers to retrieve relevant oncology research papers and obtain AI-generated answers based on scientific literature.

## Problem Statement
Medical researchers often spend significant time searching through numerous research papers to find relevant evidence. This process is time-consuming and makes it difficult to quickly obtain accurate, literature-backed information.

## Solution
The application combines semantic search using BioBERT embeddings with Retrieval-Augmented Generation (RAG) to retrieve relevant oncology papers and generate context-aware responses from biomedical literature.

## Why this project was made
The project was developed to simplify evidence retrieval from oncology research papers while demonstrating the integration of vector databases, biomedical language models, and AI-powered question answering.

## Features
- Upload and index oncology research papers
- Semantic search using BioBERT embeddings
- FAISS vector database for fast retrieval
- AI-generated evidence-based responses
- Context-aware Retrieval-Augmented Generation (RAG)
- Interactive React-based user interface

## Technologies Used
- React
- FastAPI
- Python
- PostgreSQL
- FAISS
- BioBERT
- BioMistral-7B
- Hugging Face


## Dependencies
- Python 3.10+
- Node.js v20+
- PostgreSQL
- FAISS
- Transformers
- Sentence Transformers
- PyTorch

## Installation

### Backend
```bash
pip install -r requirements.txt
```

### Frontend
```bash
npm install
```

## Run the Project

### Backend
```bash
cd backend
uvicorn app:app --reload
```

### Frontend
```bash
npm run dev
```

## Author

Jay Desai