# 📄 PDF-based Chatbot using LangChain, FAISS & OpenAI

This project is an **AI-powered chatbot** that answers questions based on the content of a PDF. It uses **LangChain** for document processing, **FAISS** for vector search, **HuggingFace embeddings** for semantic similarity, and **OpenAI GPT models** to generate answers. The chatbot ensures responses are strictly based on the uploaded PDF without relying on external sources.

---

## 🚀 Features
- 📑 Load and process PDF documents.  
- ✂️ Split large texts into smaller chunks.  
- 🧠 Generate embeddings using `sentence-transformers/all-mpnet-base-v2`.  
- 📦 Store and retrieve chunks using **FAISS**.  
- 🤖 Chat with a Flask-based API endpoint.  
- 🔒 Context-driven answers (no external search).  
- 🌍 CORS enabled for frontend integration.  

---

## 🗂 Project Structure
├── app.py # Flask API for chatbot queries
├── batch_job.py # Script to build FAISS index from PDF
├── tcsannualreport.pdf # Example PDF
├── tcs_docu_faiss_index # Local FAISS vector index
├── requirements.txt # Project dependencies

## ⚙️ How It Works
1. **Preprocessing (`batch_job.py`)**  
   - Loads a PDF file.  
   - Splits the content into chunks.  
   - Generates embeddings with HuggingFace.  
   - Saves data in a FAISS index.  

2. **Chatbot API (`app.py`)**  
   - Accepts a user question via POST request.  
   - Retrieves the most relevant chunk from FAISS.  
   - Sends the chunk as context to GPT.  
   - Returns the generated answer.  

---

## 🛠 Tech Stack
- Python  
- Flask  
- LangChain  
- HuggingFace Transformers  
- FAISS  
- OpenAI GPT  

---
