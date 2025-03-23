# Import required libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io


# ===== HELPER FUNCTIONS =====
# Function to load data from a CSV file
def load_data(csv_file_path, nrows=None):
    return pd.read_csv(csv_file_path, nrows=nrows)


# Function to load data from a Parquet file
def load_parquet_data(parquet_file_path, nrows=None):
    return pd.read_parquet(parquet_file_path)


# ===== MAIN PAGE FUNCTION =====
# Main function to render the Project Framework page
def project_framework_body():
    # ===== PAGE HEADER =====
    # Display the project title and description
    st.subheader("*Forecasting Bulldozer Values Using Machine Learning*")
    st.write(
        """
        The **BulldozerPriceGenius (BPG)** project helps users predict bulldozer sale prices using machine learning. By analyzing historical sales data through a **time series regression model**, the app delivers accurate, data-driven valuations. Below is a diagram overview of the BPG project, and this page focuses on the **Cross Industry Standard Process for Data Mining (CRISP-DM)** workflow.
        """
    )
    st.image("static/images/BPG_Framework.webp", use_column_width=True)

    # ===== NAVIGATION =====
    # Table of contents for easy navigation
    st.markdown(
        """
        - [1. Business Understanding](#1-business-understanding)
        - [2. Data Understanding](#2-data-understanding)
        - [3. Data Preparation](#3-data-preparation)
        - [4. Modeling](#4-modeling)
        - [5. Evaluation](#5-evaluation)
        - [6. Deployment](#6-deployment)
        - [Conclusion](#conclusion)
        """
    )
    st.write("---")

    # ===== SECTION 1: BUSINESS UNDERSTANDING =====
    st.header("1. Business Understanding")

    # Core business requirements
    st.subheader("Business Requirements")
    st.write(
        "The core business requirement for the BPG project that drives all decisions concerning the machine learning model is:"
    )
    st.success(
        """
        **Core Business Requirement**: Develop a machine learning model to accurately predict future sale prices of bulldozers with a Root Mean Squared Log Error (RMSLE) below 1.0.
        """
    )

    # Optional: Display detailed business requirements
    if st.checkbox("Show Business Requirements"):
        st.success(
            """
            **Business Requirement 1**: The client needs to understand what factors most significantly influence bulldozer auction prices to help optimize their auction strategies and provide better guidance to sellers and buyers.

            **Business Requirement 2**: The client requires a machine learning system that can accurately predict bulldozer prices based on historical auction data with a Root Mean Squared Log Error (RMSLE) score of below 1.0.

            **Business Requirement 3**: The client needs the prediction system to be accessible through a user-friendly interface that can be used by both technical and non-technical staff.
            """
        )

    st.subheader(
        "Here's a breakdown of how different stakeholders will be impacted by BulldozerPriceGenius:"
    )
    st.markdown(
        """
    **Buyers**:
    - Make more informed purchasing decisions by understanding fair market values
    - Filter and browse listings across U.S. states based on location and predicted prices
    - Reduce risk of overpaying for equipment

    **Sellers**:
    - Price bulldozers more accurately for auctions
    - Optimize timing and strategy for selling equipment
    - Avoid leaving money on the table through data-driven pricing

    **Auctioneers (Fast Iron)**:
    - Create a standardized pricing reference similar to Kelly Blue Book for bulldozers
    - Increase market transparency and efficiency
    - Improve buyer and seller confidence in auction processes

    **App Owner and Developers**:
    - Establish a valuable market position by providing essential pricing intelligence
    - Build trust through accurate predictions using comprehensive auction data analysis
    - Create recurring value through continuous model updates and market insights
    """
    )
    st.write("---")


# ===== MAIN EXECUTION =====
if __name__ == "__main__":
    project_framework_body()
