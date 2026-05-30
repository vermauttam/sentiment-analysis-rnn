# config.py
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SAVED_MODELS_DIR = os.path.join(BASE_DIR, "saved_models")
TFIDF_PATH = os.path.join(SAVED_MODELS_DIR, "tfidf.pkl")
LABEL_ENCODER_PATH = os.path.join(SAVED_MODELS_DIR, "label_encoder.pkl")
RNN_MODEL_PATH = os.path.join(SAVED_MODELS_DIR, "rnn_model.pth")

MAX_FEATURES = 5000
INPUT_SIZE = 5000
DEVICE = "cpu"
