import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(
    page_title="AI Cyber Security Threat Detection",
    page_icon="🛡️",
    layout="wide"
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

dataset_path = os.path.join(BASE_DIR, "dataset", "network_traffic.csv")
model_path = os.path.join(BASE_DIR, "models", "model.pkl")

st.title("🛡️ AI-Based Cyber Security Threat Detection Dashboard")

if os.path.exists(dataset_path):

    df = pd.read_csv(dataset_path)

    st.success("Dataset Loaded Successfully ✅")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Records", len(df))
    col2.metric("Features", len(df.columns)-1)
    col3.metric("Threat Records", int(df["threat"].sum()))

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Threat Distribution")
    st.bar_chart(df["threat"].value_counts())

    st.divider()

    st.subheader("🔍 Live Threat Prediction")

    if os.path.exists(model_path):

        model = joblib.load(model_path)

        packet_size = st.number_input("Packet Size", 40, 1500, 500)
        duration = st.number_input("Duration", 1, 500, 100)
        failed_logins = st.number_input("Failed Logins", 0, 10, 1)
        requests = st.number_input("Requests Per Second", 1, 1000, 300)

        if st.button("Predict Threat"):

            sample = [[packet_size, duration, failed_logins, requests]]

            prediction = model.predict(sample)[0]

            if prediction == 1:
                st.error("🚨 Threat Detected!")
            else:
                st.success("✅ Normal Traffic")

    else:
        st.error("Model file not found!")

else:
    st.error("Dataset not found!")