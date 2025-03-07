import streamlit as st
import pandas as pd
import pickle
import numpy as np


def interactive_prediction_body():
    """Creates interactive dashboard interface and handles model predictions"""

    # -----------------------------------------------------------------------------
    # 1. DASHBOARD SETUP
    # -----------------------------------------------------------------------------
    st.header("Interactive Prediction Dashboard")

    # -----------------------------------------------------------------------------
    # 2. MODEL LOADING AND IDENTIFICATION
    # -----------------------------------------------------------------------------
    # Initialize model in session state if not already present
    if "model" not in st.session_state:
        try:
            model_path = "src/models/randomforest_regressor_best_RMSLE.pkl"
            st.info(f"📁 Loading model from: {model_path}")
            
            with open(model_path, "rb") as file:
                st.session_state["model"] = pickle.load(file)
                st.success(f"✅ Successfully loaded: {model_path.split('/')[-1]}")
        except Exception as e:
            st.error(f"Failed to load model: {e}")
            st.session_state["model"] = None

    # -----------------------------------------------------------------------------
    # 3. MODEL VERIFICATION AND DETAILS
    # -----------------------------------------------------------------------------
    if st.session_state["model"] is not None:
        try:
            # Display model type and verify it's a Random Forest Regressor
            model_type = type(st.session_state["model"])
            
            # Create an expander for model details
            with st.expander("📊 Model Details"):
                st.write("Model Type:", model_type)
                st.write("Model Name:", model_path.split('/')[-1])
                st.write("Model Parameters:", st.session_state["model"].get_params())
                st.write("Number of Features:", st.session_state["model"].n_features_in_)
                st.write("Number of Trees:", st.session_state["model"].n_estimators)
            
            if str(model_type) == "<class 'sklearn.ensemble._forest.RandomForestRegressor'>":
                st.success("✅ Model loaded successfully - confirmed as RandomForestRegressor")
                st.write("Model is loaded and ready!")

                # -----------------------------------------------------------------------------
                # 4. TEST PREDICTION
                # -----------------------------------------------------------------------------
                # Create sample data for testing
                dummy_data = pd.DataFrame({
                    "YearMade": [2000],
                    "Coupler_System": ["None or Unspecified"],
                    "saleYear": [2010],
                    "saleMonth": [5],
                    "saleDay": [10],
                    "saleDayofweek": [1],
                    "saleDayofyear": [130],
                })

                # TODO: Implement preprocessing function
                # dummy_data_processed = preprocess_data(dummy_data)

                # Make test prediction
                dummy_prediction = st.session_state["model"].predict(dummy_data)
                
                # Display results
                st.write("Test prediction successful!")
                st.write("Dummy prediction value:", dummy_prediction[0])
            else:
                st.warning("⚠️ Model loaded but is not a RandomForestRegressor")

        except Exception as e:
            st.error(f"Prediction error: {e}")
    else:
        st.error("Model not loaded. Please check the model path and file.")


# -----------------------------------------------------------------------------
# MAIN EXECUTION
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    interactive_prediction_body()
