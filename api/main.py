from fastapi import FastAPI
import joblib
import os

app = FastAPI(title="AI Cyber Security Threat Detection API")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model = joblib.load(os.path.join(BASE_DIR, "models", "model.pkl"))

@app.get("/")
def home():
    return {"message": "Cyber Security Threat Detection API Running"}

@app.get("/predict")
def predict(packet_size: int, duration: int, failed_logins: int, requests_per_second: int):

    prediction = model.predict([[packet_size, duration, failed_logins, requests_per_second]])[0]

    return {
        "prediction": "Threat" if prediction == 1 else "Normal"
    }