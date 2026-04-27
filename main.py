from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Only sentiment (stable)
sentiment_pipeline = pipeline("sentiment-analysis")

class TextInput(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "API is working"}

@app.post("/analyze")
def analyze(input: TextInput):
    sentiment = sentiment_pipeline(input.text)[0]

    return {
        "input_text": input.text,
        "sentiment": sentiment["label"],
        "confidence": sentiment["score"]
    }