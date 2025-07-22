# 🧠 Building RAG Agents with LLMs - NVIDIA

This repository contains the completed, working files for the **NVIDIA DLI course**, _"Building RAG Agents with LLMs."_ It provides a hands-on, end-to-end implementation of a **Retrieval-Augmented Generation (RAG)** pipeline, showcasing the journey from initial setup to a fully functional and evaluated AI agent.

---

## 🚀 Core Features

- **End-to-End RAG Pipeline**  
  Implements a full RAG system using **LangChain**, processing Arxiv research papers into a **FAISS** vector store for context-aware responses.

- **Robust API Deployment**  
  The RAG agent is deployed as a scalable API using **FastAPI** and **LangServe**, ready for integration.

- **Interactive Frontend**  
  A user-friendly web interface built with **Gradio** allows for real-time interaction with the RAG agent.

- **Advanced Evaluation Framework**  
  Features an **LLM-as-a-Judge** system to numerically score the agent's performance, providing a benchmark for quality.

- **Performance Tuning Showcase**  
  Demonstrates the iterative process of **prompt engineering** and **retriever optimization**, improving the evaluation score from **0.0** to a **perfect 1.00**.

---

## 🛠️ Technology Stack

| Technology        | Description                                         |
|-------------------|-----------------------------------------------------|
| Core Framework    | LangChain                                           |
| LLMs & Embeddings | NVIDIA AI Endpoints (Llama 3.1 8B/70B, nv-embed-v1) |
| Vector Store      | FAISS (Facebook AI Similarity Search)              |
| API Backend       | FastAPI & LangServe                                 |
| UI Frontend       | Gradio                                              |
| Data Handling     | Arxiv, PyMuPDF                                      |
| Language          | Python                                              |

---

## ⚙️ How to Get Your Certificate: A Step-by-Step Guide

Follow these steps **exactly** to pass the assessment using the files in this repository.

### ✅ Step 1: Prepare Your NVIDIA Environment

1. Open your **NVIDIA DLI course environment**.
2. **Delete all existing files and folders** from the file browser on the left to ensure a clean slate.
3. **Upload** all files and folders from **this repository** into your environment.

---

### ✅ Step 2: Run the Backend Server

1. Open the `09_langserve.ipynb` notebook.
2. Run **all the cells** in order from top to bottom.
3. The **last cell will start the API server**.  
   ⚠️ Leave this notebook running — it must be active for the next step.

---

### ✅ Step 3: Run the Evaluation

1. Open the `08_evaluation.ipynb` notebook.
2. Run **all the cells** in order.
3. A link to the **Gradio UI** will appear.
4. Click the link to open the user interface.
5. In the UI, click the **"🎓 Evaluate"** button.
6. After the evaluation, you will see:  
   ✅ **"Congrats! You've passed the assessment!!"**

You can then return to the course and click the **"Assess Task"** button to receive your **certificate**.

---

## 📄 License

This project is licensed under the **MIT License**.

You are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software. See the [LICENSE](./LICENSE) file for full details.

---

> ⭐️ Star this repository if you found it useful, and good luck earning your certification!
