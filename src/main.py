from threat_detector import detect_threat
from logger import log_event

result = detect_threat()

print("\n===== Threat Detection Result =====")
print(f"Threat     : {result['threat']}")
print(f"Confidence : {result['confidence']}%")

log_event(result["threat"], result["confidence"])

print("\nThreat successfully logged!")