# Import required libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cache the data loading function to improve performance
@st.cache_data
def load_data(csv_file_path, nrows=None):
    # Specify data types to optimize memory usage
    dtype = {
        'SalePrice': 'float32',
        'saleMonth': 'int8',
        'state': 'category'
    }
    return pd.read_csv(csv_file_path, dtype=dtype, nrows=nrows)

def model_performance_body():
    # Display main header 
    st.header("Model Performance: Tracking Bulldozer Price Prediction Accuracy.")
    
    # Introduction text explaining the app's purpose
    st.write(
        """
        The BulldozerPriceGenius app helps you see how accurate our price predictions are. This page shows you how well our machine learning model predicts bulldozer auction prices. The project has one main objective base on the project **business requirements**:
        """
    )
    
    # Display business objectives in a success box
    st.success(
        """
        - **Objective 1**: A user can evaluate model performance metrics to ensure our price predictions are reliable and accurate (**Business Requirement 2**).
        """
    )