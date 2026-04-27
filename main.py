from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

class TextInput(BaseModel):
    text: str

# ❗ DON'T load model here
model = None

@app.get("/")
def home():
    return {"message": "API is working"}

@app.post("/analyze")
def analyze(input: TextInput):
    global model

    # ✅ Lazy load model (first request only)
    if model is None:
        model = pipeline("sentiment-analysis")

    result = model(input.text)[0]

    return {
        "input_text": input.text,
        "sentiment": result["label"],
        "confidence": result["score"]
    }