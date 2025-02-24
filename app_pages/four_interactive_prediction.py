import streamlit as st
import joblib
import pandas as pd
from datetime import datetime
import os

# load pipeline files with error handling
try:
    price_model = joblib.load(
        f"./src/models/randomforest_regressor_best_RMSLE.pkl")
except KeyError as e:
    st.error(f"Failed to load the model. KeyError: {e}")
    price_model = None
except Exception as e:
    st.error(f"An unexpected error occurred while loading the model: {e}")
    price_model = None

# load prediction features with error handling
try:
    prediction_features = pd.read_csv(
        f"./data/processed/TrainAndValid_object_values_as_categories.csv", dtype={'column_name': 'category'})
except FileNotFoundError as e:
    st.error(f"Failed to load prediction features. FileNotFoundError: {e}")
    prediction_features = None
except MemoryError as e:
    st.error(f"MemoryError: Unable to allocate memory for prediction features: {e}")
    prediction_features = None
except Exception as e:
    st.error(f"An unexpected error occurred while loading prediction features: {e}")
    prediction_features = None

# Define the interactive_prediction_body function
def interactive_prediction_body():
    st.title("Interactive Prediction")
    # Add your interactive prediction code here

# Ensure the function is defined before importing
if __name__ == "__main__":
    interactive_prediction_body()