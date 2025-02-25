import streamlit as st
import pandas as pd
import joblib
import datetime
import numpy as np

def model_performance_body():
    """Displays model performance metrics and loads the model."""

    st.subheader("Model Performance Metrics")

    # Define the absolute path to load the model here, inside the function
    bulldozer_price_prediction_model_name = "randomforest_regressor_best_RMSLE.pkl"
    model_load_path = "C:/Users/blign/Dropbox/1 PROJECT/VS Code Project Respository/About-BulldozerPriceGenius-_BPG-_v2/src/models/" + bulldozer_price_prediction_model_name

    try:
        with open(model_load_path, 'rb') as f:
            model = joblib.load(f, mmap_mode='r')  # Load model with memory mapping

        st.write(f"Model loaded from: {model_load_path}")
        st.write(f"joblib version: {joblib.__version__}")
        return model  # Return the loaded model
    except np.core._exceptions._ArrayMemoryError as e:
        st.error(f"Memory error: {e}")
        st.error("Unable to load the model due to insufficient memory. Please try closing other applications or increasing virtual memory.")
        return None  # Return None if model loading fails

def predict_price(model, input_data):
    """Predicts the price of a bulldozer using the given model and input data."""
    # Ensure input_data is a DataFrame with the correct column names
    input_df = pd.DataFrame([input_data])
    # Make prediction
    prediction = model.predict(input_df)[0]
    return prediction

def main():
    """Main function to run the Streamlit app."""
    st.title("Bulldozer Price Genius")
    st.write("Predict the price of your bulldozer!")

    # ... (model loading from your model_performance_body function) ...
    model = model_performance_body()  # Load the model
    if model is None:  # Check if model loading failed
        st.stop()  # Stop the app if model loading failed

    st.sidebar.title("Input Features")
    input_data = {}

    # Example input fields (add more as needed)
    input_data["YearMade"] = st.sidebar.number_input("Year Made", min_value=1950, max_value=datetime.datetime.now().year, value=2000)
    input_data["Coupler_System"] = st.sidebar.selectbox("Coupler System", ["None or Unspecified", "Yes", "No"])
    # ... (add more input fields for other features) ...

    # Display input data
    st.write("### Input Data")
    st.write(input_data)

    # Feature engineering (similar to your notebook)
    input_data["saleYear"] = datetime.datetime.now().year
    input_data["saleMonth"] = datetime.datetime.now().month
    input_data["saleDay"] = datetime.datetime.now().day
    input_data["saleDayofweek"] = datetime.datetime.now().weekday()
    input_data["saleDayofyear"] = datetime.datetime.now().timetuple().tm_yday

    # Preprocessing for categorical features
    for feature in ["Coupler_System"]:  # Include all categorical features
        input_data[feature] = pd.Categorical([input_data[feature]], categories=df_tmp[feature].cat.categories).codes[0]

    # Display engineered features
    st.write("### Engineered Features")
    st.write(input_data)

    # Predict button
    if st.button("Predict Price"):
        try:
            prediction = predict_price(model, input_data)
            st.success(f"Predicted Price: ${prediction:,.2f}")
        except Exception as e:
            st.error(f"Prediction failed: {e}")

if __name__ == "__main__":
    main()