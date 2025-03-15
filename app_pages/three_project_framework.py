# Import required libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io


def load_data(csv_file_path, nrows=None):
    """
    Function to load data from a CSV file
    """
    return pd.read_csv(csv_file_path, nrows=nrows)


def project_framework_body():
    """
    Main function to render the Project Framework page
    Displays the framework and structure of the project
    """
    st.subheader("*Forecasting Bulldozer Values Using Machine Learning*")
    st.write(
        """
        The **BulldozerPriceGenius (BPG)** project helps users predict bulldozer sale prices using machine learning. By analyzing historical sales data through a **time series regression model**, the app delivers accurate, data-driven valuations. Below is a diagram overview of the BPG project, and this page focuses on the **Cross Industry Standard Process for Data Mining (CRISP-DM)** workflow. 
        """
    )
    st.image("static/images/BPG_Framework.webp", use_column_width=True)

    # ===== NAVIGATION =====
    # Table of contents
    # FIXME: Broken links
    st.markdown(
        """
    - [1. Business Understanding](#business-understanding)
    - [2. Data Understanding](#data-understanding)
    - [3. Data Preparation](#data-preparation)
    - [4. Modeling](#modeling)
    - [5. Evaluation](#evaluation)
    - [6. Deployment](#deployment)
    """
    )

    st.write("---")

    # Add more content as needed
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

    # Business Requirements with checkboxes
    if st.checkbox("Show Business Requirements"):
        st.success(
            """
            **Business Requirement 1**: The client needs to understand what factors most significantly influence bulldozer auction prices to help optimize their auction strategies and provide better guidance to sellers and buyers.
        
            **Business Requirement 2**: The client requires a machine learning system that can accurately predict bulldozer prices based on historical auction data, with the ability to scale and adapt as new data becomes available.
        
            **Business Requirement 3**: The client needs the prediction system to be accessible through a user-friendly interface that can be used by both technical and non-technical staff.
            """
        )

    st.write("---")

    st.header("2. Data Understanding")
    st.subheader("What Data Do We Have?")
    st.write(
        """
        Our project uses three main datasets from [Kaggle](https://www.kaggle.com/c/bluebook-for-bulldozers/data):
        - **Training data**: Sales records up to `2011`
        - **Validation data**: Sales from `January to April 2012`
        - **Test data**: Sales from `May to November 2012`
        """
    )
    st.subheader("Data Quality Check")
    st.write(
        """
        The dataset has over `400,000` entries (bulldozer sales records). 
        Here's what we found:

    - **Good Points:**
        - Large dataset with detailed information
        - Covers multiple years of sales
        - Contains various machine details details
    - **Challenges:**
        - Some missing information in important fields
        - Mixed data types that need cleaning
        - Dates need to be converted to the right format
    """
    )

    # Load and display the dataset
    csv_file_path = "src/data_prep/TrainAndValid_object_values_as_categories.csv"
    df = load_data(
        csv_file_path, nrows=500
    )  # Load only the first 500 out of 10,000 rows

    # Optional dataframe inspection
    if st.checkbox("DataFrame Inspection: Missing Values"):
        st.dataframe(df)

    # Load and display the processed dataset info
    processed_file_path = "data/processed/TrainAndValid_processed.csv"
    df_processed = load_data(processed_file_path)

    if st.checkbox("DataFrame Inspection: Data Mixed Types"):
        buffer = io.StringIO()
        df_processed.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)

    st.write("---")
    st.header("3. Data Preparation")
    st.write("Details about the project framework will be displayed here.")

    st.write("---")
    st.header("4. Modeling")
    st.write("Details about the project framework will be displayed here.")

    st.write("---")
    st.header("5. Evaluation")
    st.write("Details about the project framework will be displayed here.")

    st.write("---")
    st.header("6. Deployment")
    st.write("Details about the project framework will be displayed here.")

    st.write("---")


# ===== MAIN EXECUTION =====
if __name__ == "__main__":
    project_framework_body()
