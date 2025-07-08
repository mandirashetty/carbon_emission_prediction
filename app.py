import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('rf_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("CO₂ Emissions Predictor")

# Example input fields (customize based on your features)
gdp = st.number_input('GDP (current US$)', min_value=0.0)
population = st.number_input('Population', min_value=0)
energy_use = st.number_input('Energy Use (kg of oil equivalent per capita)', min_value=0.0)
# Add more fields as needed

if st.button('Predict'):
    features = np.array([[gdp, population, energy_use]])  # Adjust order/features as needed
    prediction = model.predict(features)
    st.success(f"Predicted CO₂ Emissions: {prediction[0]:.2f} metric tons")
