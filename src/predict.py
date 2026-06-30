import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "models", "model.pkl")

model = joblib.load(MODEL_PATH)


def predict_threat(packet_size, duration, failed_logins, requests_per_second):

    sample = [[
        packet_size,
        duration,
        failed_logins,
        requests_per_second
    ]]

    prediction = model.predict(sample)[0]
    probability = model.predict_proba(sample)[0]

    confidence = float(round(max(probability) * 100, 2))

    if confidence >= 90:
        severity = "High"
    elif confidence >= 70:
        severity = "Medium"
    else:
        severity = "Low"

    return {
        "prediction": "Threat" if prediction == 1 else "Normal",
        "confidence": confidence,
        "severity": severity
    }