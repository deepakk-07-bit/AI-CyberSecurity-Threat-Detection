import random
from config import THREATS

def detect_threat():
    threat = random.choice(THREATS)
    confidence = random.randint(82, 99)

    return {
        "threat": threat,
        "confidence": confidence
    }