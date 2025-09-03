# -*- coding: utf-8 -*-
"""
Minimal Interactive Prediction Module for Render Compatibility Testing
"""

import streamlit as st
import pandas as pd
import numpy as np
import sys
import os
import warnings
warnings.filterwarnings('ignore')

def interactive_prediction_body():
    """
    Minimal interactive prediction function for testing Render deployment
    """
    st.title("🚜 Interactive Bulldozer Price Prediction")
    
    st.markdown("""
    ### Test Page for Render Deployment
    
    This is a minimal version to test Render platform compatibility.
    """)
    
    # Basic inputs
    year_made = st.selectbox("Year Made", range(1974, 2019), index=20)
    product_size = st.selectbox("Product Size", ["Compact", "Small", "Medium", "Large"])
    
    if st.button("Test Prediction"):
        st.success(f"Test successful! Year: {year_made}, Size: {product_size}")
        st.info("Enhanced ML Model diagnostic system would activate here.")

if __name__ == "__main__":
    interactive_prediction_body()
