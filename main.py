from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "API is working"}

@app.post("/analyze")
def analyze(input: TextInput):
    # simple rule-based sentiment (temporary)
    text = input.text.lower()

    if "good" in text or "love" in text:
        sentiment = "POSITIVE"
    else:
        sentiment = "NEGATIVE"

    return {
        "input_text": input.text,
        "sentiment": sentiment,
        "confidence": 0.8
    }