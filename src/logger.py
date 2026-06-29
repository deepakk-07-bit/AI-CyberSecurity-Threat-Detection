import csv
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGS_DIR = os.path.join(BASE_DIR, "logs")
LOG_FILE = os.path.join(LOGS_DIR, "threat_logs.csv")


def log_event(threat, confidence):

    os.makedirs(LOGS_DIR, exist_ok=True)

    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Time", "Threat", "Confidence"])

        writer.writerow([
            datetime.now(),
            threat,
            confidence
        ])