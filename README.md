# AI Knowledge Assistant (RAG-Based PDF Chatbot)

## Overview
AI Knowledge Assistant is a Retrieval-Augmented Generation (RAG) chatbot that allows users to upload PDF documents and ask questions based on their content. The system retrieves relevant information from the uploaded document using semantic search and displays context-aware answers.

## Features
- Upload PDF documents
- Extract and process document content
- Semantic search for relevant information
- Context-aware question answering
- Interactive Streamlit interface

## Technologies Used
- Python
- Streamlit
- LangChain
- ChromaDB
- HuggingFace Embeddings
- Sentence Transformers
- PyPDF

## Project Structure

```text
rag-chatbot/
│
├── app.py
├── utils.py
├── requirements.txt
├── README.md
├── data/
└── chroma_db/
```

## Installation

1. Clone the repository

```bash
git clone https://github.com/Akshaya9806/rag-chatbot.git
cd rag-chatbot
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the application

```bash
python -m streamlit run app.py
```

## How It Works

1. User uploads a PDF document.
2. The document is split into smaller chunks.
3. Text embeddings are generated.
4. Embeddings are stored in a vector database.
5. Relevant content is retrieved based on the user's query.
6. The system displays the most relevant information from the document.
