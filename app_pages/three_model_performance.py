

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


# Define the prediction function
def predict_price(input_data):
    # Convert object columns to category
    for label, content in input_data.items():
        if pd.api.types.is_object_dtype(content):
            input_data[label] = pd.Categorical(
                content,
                categories=data[label].cat.categories,
                ordered=True,
            )
    # Make prediction
    prediction = model.predict(input_data)
    return prediction[0]

# Create the Streamlit app
st.title("Bulldozer Price Prediction")

# Get unique values for categorical features for dropdown options
product_sizes = data["ProductSize"].unique()
enclosures = data["Enclosure"].unique()

# Create input widgets for prediction
year_made = st.slider("Year Made", 1950, datetime.now().year, 2000)
product_size = st.selectbox("Product Size", product_sizes)
enclosure = st.selectbox("Enclosure", enclosures)
sale_year = st.slider("Sale Year", 2010, datetime.now().year, 2012)

# Create a dictionary with the input values
input_data = {
    "YearMade": [year_made],
    "ProductSize": [product_size],
    "Enclosure": [enclosure],
    "saleYear": [sale_year],
}

# Create a DataFrame from the input data
input_df = pd.DataFrame(input_data)

# Make prediction if button is clicked
if st.button("Predict"):
    prediction = predict_price(input_df)
    st.success(f"Predicted Bulldozer Price: ${prediction:,.2f}")