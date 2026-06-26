import streamlit as st
import pickle
import numpy as np

# Load saved models
kmeans = pickle.load(open("kmeans.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Cluster mapping
segment_map = {
    0: "At Risk",
    1: "Champions",
    2: "New Customers",
    3: "Lost Customers"
}

# UI
st.title("Customer Segmentation App (RFM Model)")
st.write("Enter customer RFM values")

# Text input boxes
recency = st.text_input("Recency (days since last purchase)")
frequency = st.text_input("Frequency (number of orders)")
monetary = st.text_input("Monetary (total spend)")

# Prediction
if st.button("Predict Segment"):

    try:
        # Convert inputs into numbers
        recency = float(recency)
        frequency = float(frequency)
        monetary = float(monetary)

        # Prepare input
        input_data = np.array([[recency, frequency, monetary]])

        # Scale input
        input_scaled = scaler.transform(input_data)

        # Predict cluster
        cluster = kmeans.predict(input_scaled)[0]

        # Segment label
        segment = segment_map.get(cluster, "Unknown")

        st.success(f"Predicted Segment: {segment}")

        # Business recommendation
        if segment == "Champions":
            st.info("High-value customers. Focus on retention and rewards.")
        elif segment == "At Risk":
            st.warning("Customers are becoming inactive. Use re-engagement strategies.")
        elif segment == "Lost Customers":
            st.error("Inactive customers. Try win-back campaigns.")
        else:
            st.info("New customers. Focus on onboarding and engagement.")

    except ValueError:
        st.error("Please enter valid numeric values.")