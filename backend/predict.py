# predict.py
import pickle
import torch

import config
from model import RNN
from preprocess import preprocess_text


with open(config.TFIDF_PATH, "rb") as f:
    tfidf = pickle.load(f)

with open(config.LABEL_ENCODER_PATH, "rb") as f:
    label_encoder = pickle.load(f)

model = RNN(input_size=config.INPUT_SIZE)
model.load_state_dict(torch.load(config.RNN_MODEL_PATH, map_location=config.DEVICE))
model.to(config.DEVICE)
model.eval()


def predict_sentiment(text: str):
    cleaned = preprocess_text(text)
    features = tfidf.transform([cleaned]).toarray()
    x = torch.tensor(features, dtype=torch.float32, device=config.DEVICE)
    x = x.unsqueeze(1)  # (1, 5000) -> (1, 1, 5000)  matches training

    with torch.no_grad():
        logit = model(x)
        prob = torch.sigmoid(logit.squeeze()).item()

    pred_idx = 1 if prob > 0.5 else 0
    label = label_encoder.inverse_transform([pred_idx])[0]
    confidence = prob if pred_idx == 1 else (1 - prob)
    return label, float(confidence)
