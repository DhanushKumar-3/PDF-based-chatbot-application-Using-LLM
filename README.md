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
