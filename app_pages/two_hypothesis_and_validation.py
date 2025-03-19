import streamlit as st
import os


def hypothesis_and_validation_body():
    """
    Main function to render the Hypothesis & Validation page
    Displays model performance metrics and validation results
    """

    # ===== PAGE HEADER =====
    st.subheader("*Hypothesis and Validation*")

    # ===== INTRODUCTION =====
    # Display project overview and objectives
    st.markdown(
        """
        The BulldozerPriceGenius app helps you see how accurate our price predictions are. 
        This page shows you how well our machine learning model predicts bulldozer auction prices. 
        The project has one main objective based on the project business requirements:
        """
    )

    # Display main objective
    st.success(
        """
        - **Objective 1**: A user can evaluate model performance metrics to ensure our price 
        predictions are reliable and accurate (*Business Requirement 2*)..
        """
    )

    # ===== NAVIGATION =====
    # Table of contents for easy navigation for easy navigation
    st.markdown(
        """
        - [What We Are Testing](#what-we-are-testing)
        - [How We Validate](#how-we-validate)
        - [Validation 1: Price Accuracy](#validation-1-price-accuracy)
        - [Validation 2: Feature Significance](#validation-2-feature-significance)
        - [Validation 3: Model Performance](#validation-3-model-performance)
        """
    )
    st.write("---")

    # ===== HYPOTHESES =====
    # Section 1: Project Hypotheses
    st.subheader("What We Are Testing")
    st.markdown(
        """
        This section will contain the hypothesis for the Bulldozer Price Genius project.
        1. **Price Accuracy**: We believe that our model can predict prices within an acceptable 
        margin of error, with an RMSLE score less than 1.0..
        2. **Feature Significance**: We expect these five bulldozer features (year made, product size, sale year, model description, and model ID) to have a stronger influence on price predictions..
        3. **Model Performance**: We predict that different machine learning models will show varying levels of prediction accuracy, but both ideal and fast models will maintain acceptable performance below the target `RMSLE` threshold.
        """
    )
    st.write("---")

    # ===== VALIDATION METHODOLOGY =====
    # Section 2: Validation Methods
    st.subheader("How We Validate")
    st.markdown(
        """
        - `RMSLE scores` show how close our predictions are to actual prices..
        - `Model comparison` helps us choose the best performing solution..
        
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

    # ===== PRICE ACCURACY VALIDATION =====
    # Section 3: Price Accuracy Results
    st.header("Validation 1: Price Accuracy")
    st.success(
        """
        **Hypothesis 1**: We believe that our model can predict prices within an acceptable 
        margin of error, with an RMSLE score less than `1.0`..
        """
    )
    st.image("results/sale_price.webp")

    # Display price comparison metrics
    st.subheader("Prediction vs Reality")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Model Prediction", f"${55495.68:,.2f}")
    with col2:
        st.metric("Actual Price", f"${72600:,.2f}")

    # Show error metrics
    st.subheader("Performance Metrics")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Mean Absolute Error (MAE)", f"${17104:,.2f}")
    with col2:
        st.metric("RMSLE Score", "0.27")

    # Analysis of results
    st.subheader("Analysis")
    st.write(
        """
        - RMSLE score of 0.27 indicates reasonable model performance..
        - Model provides valuable pricing guidance..
        - Some room for improvement exists..
        """
    )

    # Price accuracy conclusions
    st.subheader("Conclusion")
    st.write(
        """
        Yes, our hypothesis was validated. Our target **RMSLE score** was below `1.0`, and we achieved `0.27` — **significantly exceeding our expectations**. While we've met our goal, we can still work on reducing the `$17,104` average error to make our predictions even more precise. Users can trust the model's price estimates.
        
        **What does this mean?**
        - Our predictions are more accurate than expected..
        - Users can trust our model for pricing guidance..
        - The system is ready for real-world use..
        """
    )
    st.write("---")

    # ===== FEATURE SIGNIFICANCE VALIDATION =====
    # Section 4: Feature Importance Analysis
    st.header("Validation 2: Feature Significance")
    st.success(
        """
        **Hypothesis 2**: We expect these five bulldozer features (year made, product size, sale year, model description, and model ID) to have a stronger influence on price predictions..
        """
    )
    st.image("results/feature_importance.webp")

    # Feature importance breakdown
    st.subheader("Analysis of Top Features")
    st.write(
        """
        **Primary Features:**
        - **Year Made** (`19.9%`): The most significant factor, with newer bulldozers commanding higher prices..
        - **Product Size** (`15.5%`): Second most important, larger machines typically cost more..
        
        **Secondary Features:**
        - **Sale Year** (`7.7%`): Reflects market conditions at time of sale..
        - **Model Description** (`5.7%`): Specific model features impact pricing..
        - **Model ID** (`5.6%`): Different models have varying base prices..
        """
    )

    # Feature significance conclusions
    st.subheader("Conclusion")
    st.write(
        """
        Our analysis validates the hypothesis regarding feature importance: bulldozer **age** and **size** together influence approximately `35%` of the price predictions, confirming these as the most significant features.
        """
    )
    st.write("---")

    # ===== MODEL PERFORMANCE VALIDATION =====
    # Section 5: Model Comparison Results
    st.header("Validation 3: Model Performance")
    st.success(
        """
        **Hypothesis 3**: We predict that different machine learning models will show varying levels of prediction accuracy, but both ideal and fast models will maintain acceptable performance below the target RMSLE threshold.
        """
    )
    st.image("results/model_comparison.webp")    st.image("results/model_comparison.webp")

    # Performance analysis conclusions    # Performance analysis conclusions
    st.subheader("Conclusion")
    st.write(
        """
        Yes, Hypothesis 3 is validated. Our analysis shows distinct variations in model performance, with all models maintaining acceptable RMSLE scores:, Hypothesis 3 is validated. Our analysis shows distinct variations in model performance, with all models maintaining acceptable RMSLE scores:

        - The **ideal model** achieves the best performance with a `Valid RMSLE` of `0.313` and `Valid R²` of `0.836`.        - The **ideal model** achieves the best performance with a `Valid RMSLE` of `0.313` and `Valid R²` of `0.836`.
        - The **fast model** performs similarly well, with a `Valid RMSLE` of `0.318` and `Valid R²` of `0.830`.
        - The **default and random search models** achieve acceptable `RMSLE scores` of `0.358` and `0.349`, respectively.     spectively.     

        **Key findings**:        **Key findings**:

        - All models maintain `RMSLE scores` well below our target of `1.0`, demonstrating reliable performance.        - All models maintain `RMSLE scores` well below our target of `1.0`, demonstrating reliable performance.
        - The **ideal and fast models** show exceptional results with negligible differences, making both viable choices based on speed requirements.e choices based on speed requirements.
        - `High R²` values, particularly in the **ideal and fast models**, demonstrate strong predictive accuracy.
        """
    )
    st.write("---")t.write("---")


# ===== MAIN EXECUTION =====# ===== MAIN EXECUTION =====
if __name__ == "__main__":
    hypothesis_and_validation_body()ion_body()
