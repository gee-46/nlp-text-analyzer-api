# NLP Text Analyzer API

## 🚀 Overview
This project is a FastAPI-based backend service that performs **sentiment analysis** on input text and exposes it via REST APIs.

It demonstrates how to build, deploy, and test an AI-powered backend system in a production-like environment.

---

## 🌐 Live Demo
👉 https://nlp-text-analyzer-api.onrender.com/  
👉 https://nlp-text-analyzer-api.onrender.com/docs

---

## ⚙️ Features
- Accepts text input via API
- Performs sentiment analysis (rule-based for lightweight deployment)
- Returns structured JSON response
- Built using FastAPI
- Deployed on Render
- Interactive API testing via Swagger UI

---

## 🧠 Tech Stack
- **Python**
- **FastAPI**
- **Uvicorn**
- **Render (Deployment)**

---

## 📡 API Endpoint

### `POST /analyze`

#### Request Body:
```json
{
  "text": "I love this product"
}
```

#### Response:
```json
{
  "input_text": "I love this product",
  "sentiment": "POSITIVE",
  "confidence": 0.8
}
```

---

## 🏗️ System Architecture
```
Client (User / App)
        ↓
FastAPI Endpoint (/analyze)
        ↓
Input Validation (Pydantic)
        ↓
Sentiment Logic (Lightweight Rule-Based)
        ↓
JSON Response
```

---

## ▶️ How to Run Locally

### Clone the repository
```bash
git clone https://github.com/gee-46/nlp-text-analyzer-api.git
cd nlp-text-analyzer-api
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run the server
```bash
python -m uvicorn main:app --reload
```

### Open in browser
- API: http://127.0.0.1:8000
- Docs: http://127.0.0.1:8000/docs

---

## 📌 Key Learnings
- Building REST APIs using FastAPI
- Deploying backend services on cloud (Render)
- Handling JSON-based APIs
- Understanding system constraints (memory, deployment limits)
- Designing scalable AI system architecture

---

## 🔮 Future Improvements
- Integrate real ML models via external APIs (HuggingFace / OpenAI)
- Add text summarization
- Add authentication & rate limiting
- Add frontend UI
- Convert into a RAG-based system

---

## 👤 Author

**Gautam Chipkar**  
AI & Data Science Student