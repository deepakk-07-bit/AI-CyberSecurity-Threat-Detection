from predict import predict_threat

result = predict_threat(
    packet_size=1200,
    duration=300,
    failed_logins=5,
    requests_per_second=700
)

print(result)