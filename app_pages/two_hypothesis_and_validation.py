import streamlit as st
import os
from pathlib import Path
import matplotlib.pyplot as plt





def hypothesis_and_validation_body():
    st.image("static/images/bulldozer_ai-min.webp")
    st.subheader("*Hypothesis and Validation*")
    st.markdown(
        """
        The BulldozerPriceGenius app helps you see how accurate our price predictions are. 
        This page shows you how well our machine learning model predicts bulldozer auction prices. 
        The project has one main objective based on the project business requirements:
        """
    )
    st.success(
        """
        - **Objective 1**: A user can evaluate model performance metrics to ensure our price 
        predictions are reliable and accurate (*Business Requirement 2*)
        """
    )
    st.write("---")

    st.subheader("What We Are Testing")
    st.markdown(
        """
        This section will contain the hypothesis for the Bulldozer Price Genius project.
        1. **Price Accuracy**: We believe that our model can predict prices within an acceptable margin of error
        2. **Feature Significance**: We expect certain bulldozer features (age, condition, brand) to have stronger influence on price predictions
        3. **Model Performance**: Different machine learning models will exhibit varying performance levels in predicting bulldozer prices
        """
    )
    st.write("---")

    st.subheader("How We Validate")
    st.markdown(
        """
        - `RMSLE scores` show how close our predictions are to actual prices
        - `Model comparison` helps us choose the best performing solution
        
        All validation metrics directly support:
        """
    )
    st.info(
        """ 
        **Business Requirement 2** - developing a machine learning system that accurately predicts 
        bulldozer prices based on historical auction data, with the ability to scale and adapt 
        as new data becomes available.
        """
    )
    st.write("---")

    st.header("Validation 1: Price Accuracy")

    st.success(
        """
        **Hypothesis 1**: We believe that our model can predict prices within an acceptable 
        margin of error, with an RMSLE score less than `1.0`
        """
    )
    st.image("results/price_prediction_distribution.png")

    # Display prediction vs reality
    st.subheader("Prediction vs Reality")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Model Prediction", f"${55495.68:,.2f}")
    with col2:
        st.metric("Actual Price", f"${72600:,.2f}")

    # Display error metrics
    st.subheader("Performance Metrics")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Mean Absolute Error (MAE)", f"${17104:,.2f}")
    with col2:
        st.metric("RMSLE Score", "0.27")

    # Display analysis
    st.subheader("Analysis")
    st.write(
        """
        - RMSLE score of 0.27 indicates reasonable model performance
        - Model provides valuable pricing guidance
        - Some room for improvement exists
        """
    )

    st.write("---")
    st.subheader("Hypothesis 2: Feature Significance")

    st.write("---")
    st.subheader("Hypothesis 3: Model Performance")

    st.write("---")
    st.header("Project Success")

    st.write("---")

    # Call the function to show the prediction plot
    show_prediction_plot()


if __name__ == "__main__":
    hypothesis_and_validation_body()
