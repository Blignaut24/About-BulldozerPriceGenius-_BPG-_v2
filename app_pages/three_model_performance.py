import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_log_error, mean_absolute_error, r2_score

def model_performance_body():
    st.subheader("ML: Model Performance Metrics")
    st.write(
        """
        Welcome to the Model Performance page, where we demonstrate the reliability and accuracy of our bulldozer price prediction system. Our machine learning model, built using RandomForestRegressor on historical auction data, provides transparent performance metrics through industry-standard evaluations. This directly fulfills Business Requirement 2: Creating a reliable price prediction system with the following measurable objectives:
        """
    )
    # Display business objectives in a success box
    st.success(
        """
        **Measurable Objectives:**
        
        - **Model Accuracy**: Achieve optimal RMSLE (Root Mean Squared Log Error) scores through systematic training and validation
        - **Model Improvement**: Implement cross-validation and hyperparameter tuning to enhance prediction accuracy
        - **Model Comparison**: Compare multiple models to identify the best-performing one for deployment
        - **Performance Validation**: Demonstrate model reliability through comprehensive metrics including MAE, RMSLE, and R² scores
        """
    )
    
    st.subheader("**Model Accuracy:**")
    st.write("TEXT HERE")
    
    st.subheader("**Model Improvement:**")
    st.write("TEXT HERE")
    
    st.subheader("**Model Comparison:**")
    st.write("TEXT HERE")

    # Add a checkbox to display the PNG image
    if st.checkbox('Show Model Comparison Chart'):
        image_path = r'C:\Users\blign\Dropbox\1 PROJECT\VS Code Project Respository\About-BulldozerPriceGenius-_BPG-_v2\data\interim\model_comparison.png'
        st.image(image_path, caption='Model Comparison', use_container_width=True)