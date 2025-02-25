import streamlit as st
import pandas as pd
import numpy as np
import joblib

def model_performance_body():
    st.subheader("Model Performance Metrics")
    
    # Define the absolute path to load the model
    bulldozer_price_prediction_model_name = "randomforest_regressor_best_RMSLE.pkl"
    model_load_path = "C:/Users/blign/Dropbox/1 PROJECT/VS Code Project Respository/About-BulldozerPriceGenius-_BPG-_v2/src/models/" + bulldozer_price_prediction_model_name

    try:
        # Load model from file using memory mapping
        model = joblib.load(model_load_path, mmap_mode='r')
        st.write(f"Model loaded from: {model_load_path}")
        st.write(f"joblib version: {joblib.__version__}")
    except numpy.core._exceptions._ArrayMemoryError as e:
        st.error(f"Memory error: {e}")
        st.error("Unable to load the model due to insufficient memory. Please try closing other applications or increasing virtual memory.")