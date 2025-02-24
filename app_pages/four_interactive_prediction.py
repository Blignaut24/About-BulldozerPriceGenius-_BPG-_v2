<<<<<<< HEAD
# Import required libraries
import streamlit as st  # For creating web interface
import joblib          # For loading ML models
import pandas as pd    # For data manipulation
from datetime import datetime  # For date handling
import os             # For file operations

# Try to load the machine learning model
try:
    price_model = joblib.load(
        f"./src/models/randomforest_regressor_best_RMSLE.pkl")
    st.success("Model loaded successfully.")
except FileNotFoundError as e:
    st.error(f"Failed to load the model. FileNotFoundError: {e}")
=======
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
>>>>>>> c016c02868c32638616fbbb6d268be79ce84ea35
    price_model = None
except Exception as e:
    st.error(f"An unexpected error occurred while loading the model: {e}")
    price_model = None

<<<<<<< HEAD
# Try to load the feature dataset
try:
    prediction_features = pd.read_csv(
        f"./data/processed/TrainAndValid_object_values_as_categories.csv", 
        dtype={'column_name': 'category'})
    st.success("Prediction features loaded successfully.")
=======
# load prediction features with error handling
try:
    prediction_features = pd.read_csv(
        f"./data/processed/TrainAndValid_object_values_as_categories.csv", dtype={'column_name': 'category'})
>>>>>>> c016c02868c32638616fbbb6d268be79ce84ea35
except FileNotFoundError as e:
    st.error(f"Failed to load prediction features. FileNotFoundError: {e}")
    prediction_features = None
except MemoryError as e:
    st.error(f"MemoryError: Unable to allocate memory for prediction features: {e}")
    prediction_features = None
except Exception as e:
    st.error(f"An unexpected error occurred while loading prediction features: {e}")
    prediction_features = None

<<<<<<< HEAD
# Main function for the prediction interface
def interactive_prediction_body():
    st.title("Interactive Prediction")

    # Verify model is loaded properly
    if price_model is None:
        st.warning("The model did not load correctly. Please check the model file.")
        return

    # Verify features are loaded properly
    if prediction_features is None:
        st.warning("The prediction features did not load correctly. Please check the data file.")
        return

    # Get unique values for dropdown menus
    product_sizes = prediction_features["ProductSize"].unique()
    enclosures = prediction_features["Enclosure"].unique()

    # Create input widgets for user interaction
    year_made = st.slider("Year Made", 1950, datetime.now().year, 2000)
    product_size = st.selectbox("Product Size", product_sizes)
    enclosure = st.selectbox("Enclosure", enclosures)
    sale_year = st.slider("Sale Year", 2010, datetime.now().year, 2012)

    # Prepare input data structure
    input_data = {
        "YearMade": [year_made],
        "ProductSize": [product_size],
        "Enclosure": [enclosure],
        "saleYear": [sale_year],
    }

    # Convert input to DataFrame
    input_df = pd.DataFrame(input_data)

    # Handle prediction when button is clicked
    if st.button("Predict"):
        try:
            # Convert categorical columns to proper format
            for label, content in input_df.items():
                if pd.api.types.is_object_dtype(content):
                    input_df[label] = pd.Categorical(
                        content,
                        categories=prediction_features[label].cat.categories,
                        ordered=True,
                    )

            # Make prediction and display result
            prediction = price_model.predict(input_df)
            st.success(
                f"Predicted Bulldozer Price: ${prediction[0]:,.2f}")

        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")

# Entry point of the application
=======
# Define the interactive_prediction_body function
def interactive_prediction_body():
    st.title("Interactive Prediction")
    # Add your interactive prediction code here

# Ensure the function is defined before importing
>>>>>>> c016c02868c32638616fbbb6d268be79ce84ea35
if __name__ == "__main__":
    interactive_prediction_body()