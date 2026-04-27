# NLP Text Analyzer API

## 🚀 Overview
This project is a FastAPI-based backend service that performs **sentiment analysis** on input text using a pretrained Transformer model from HuggingFace.

It demonstrates how to integrate machine learning models into a real-world backend system and expose them via REST APIs.

---

## ⚙️ Features
- Accepts text input via API
- Performs sentiment analysis (Positive / Negative)
- Returns confidence score
- Fast and lightweight backend using FastAPI
- Interactive API testing using Swagger UI (`/docs`)

---

## 🧠 Tech Stack
- **Python**
- **FastAPI**
- **HuggingFace Transformers**
- **Uvicorn**

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
  "confidence": 0.99
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
ML Model (HuggingFace Pipeline)
        ↓
JSON Response
```

---

## ▶️ How to Run Locally

1. Clone the repository
```bash
git clone https://github.com/gee-46/nlp-text-analyzer-api.git
cd nlp-text-analyzer-api
```

2. Install dependencies
```bash
pip install fastapi uvicorn transformers
```

3. Run the server
```bash
python -m uvicorn main:app --reload
```

4. Open in browser
- API: http://127.0.0.1:8000
- Docs: http://127.0.0.1:8000/docs

---

## 📌 Key Learnings
- Building REST APIs with FastAPI
- Integrating ML models into backend systems
- Handling JSON requests and responses
- Debugging environment and dependency issues
- Structuring a real-world AI project

---

## 🔮 Future Improvements
- Add text summarization
- Add keyword extraction
- Deploy API (Render / Railway)
- Add frontend interface

---

## 👤 Author

**Gautam Chipkar**  
AI & Data Science Student
