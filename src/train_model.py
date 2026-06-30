import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

# Random dataset generate
np.random.seed(42)

rows = 1000

df = pd.DataFrame({
    "packet_size": np.random.randint(40, 1500, rows),
    "duration": np.random.randint(1, 500, rows),
    "failed_logins": np.random.randint(0, 10, rows),
    "requests_per_second": np.random.randint(1, 1000, rows),
    "threat": np.random.randint(0, 2, rows)
})

# Dataset Save
os.makedirs("../dataset", exist_ok=True)
df.to_csv("../dataset/network_traffic.csv", index=False)

# Features
X = df.drop("threat", axis=1)
y = df["threat"]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Accuracy
pred = model.predict(X_test)
accuracy = accuracy_score(y_test, pred)

print(f"Model Accuracy: {accuracy:.2f}")

# Save Model
os.makedirs("../models", exist_ok=True)
joblib.dump(model, "../models/model.pkl")

print("Model saved successfully!")
print("Dataset generated successfully!")