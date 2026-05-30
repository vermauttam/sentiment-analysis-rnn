# app.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from predict import predict_sentiment

app = FastAPI(title="Sentiment Analysis RNN API")

# Allow your frontend (Vite dev server) to call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # tighten to your frontend URL later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TextIn(BaseModel):
    text: str


class PredictionOut(BaseModel):
    label: str
    confidence: float


@app.get("/")
def root():
    return {"status": "ok", "message": "Sentiment Analysis RNN API is running"}


@app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    label, confidence = predict_sentiment(payload.text)
    return {"label": label, "confidence": round(confidence, 4)}
