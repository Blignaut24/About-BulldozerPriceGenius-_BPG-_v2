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
        
            **Business Requirement 2**: The client requires a machine learning system that can accurately predict bulldozer prices based on historical auction data, with the ability to scale and adapt as new data becomes available.
        
            **Business Requirement 3**: The client needs the prediction system to be accessible through a user-friendly interface that can be used by both technical and non-technical staff.
            """
        )
    st.write("---")

    # ===== SECTION 2: DATA UNDERSTANDING =====
    st.header("2. Data Understanding")

    # Overview of available data
    st.subheader("What Data Do We Have?")
    st.write(
        """
        Our project uses three main datasets from [Kaggle](https://www.kaggle.com/c/bluebook-for-bulldozers/data):
        - **Training data**: Sales records up to `2011`
        - **Validation data**: Sales from `January to April 2012`
        - **Test data**: Sales from `May to November 2012`
        """
    )

    # Data quality check
    st.subheader("Data Quality Check")
    st.write(
        """
        The dataset has over `400,000` entries (bulldozer sales records). 
        Here's what we found:

        - **Good Points:**
            - Large dataset with detailed information
            - Covers multiple years of sales
            - Contains various machine details
        - **Challenges:**
            - Some missing information in important fields
            - Mixed data types that need cleaning
            - Dates need to be converted to the right format
        """
    )

    # Load and display the dataset
    csv_file_path = "src/data_prep/TrainAndValid_object_values_as_categories.csv"
    df = load_data(csv_file_path, nrows=500)  # Load only the first 500 rows

    # Optional: Inspect missing values in the dataset
    if st.checkbox("DataFrame Inspection: Missing Values"):
        st.write("Load the first `500` rows from a total of `10,000` rows")
        st.dataframe(df)

    # Optional: Inspect processed dataset for mixed data types
    processed_file_path = "data/processed/TrainAndValid_processed.csv"
    df_processed = load_data(processed_file_path)
    if st.checkbox("DataFrame Inspection: Data Mixed Types"):
        buffer = io.StringIO()
        df_processed.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)

    # Explanation of dataset structure
    st.subheader("What Each Part Means")
    if st.checkbox("Main Types of Information"):
        st.write("The dataset includes these main types of information:")
        st.info(
            """
            - **Basic Details**:
                - **Sales ID**: Unique number for each sale
                - **Machine ID**: Unique number for each bulldozer
                - **Sale Price**: How much the bulldozer sold for (this is what we want to predict)
            - **Machine Information**:
                - **Year Made**: When the bulldozer was built
                - **Usage Hours**: How many hours the machine has been used
                - **Usage Level**: Low, medium, or high based on hours used
            - **Sale Details**:
                - **Sale Date**: When the bulldozer was sold
                - **State**: Where the sale happened in the USA    
            """
        )
    st.write("---")

    # ===== SECTION 3: DATA PREPARATION =====
    st.header("3. Data Preparation")

    # Data cleaning steps
    st.subheader("Data Cleaning")
    st.write(
        """
        1. **Parse Dates**
            - Convert `'saledate'` from string to datetime
            - Sort data chronologically
            
        2. **Handle Categorical Data**
            - Convert string columns to category type
            - Create numerical representations
            
        3. **Address Missing Values**
            - Identify columns with missing data
            - Apply appropriate imputation strategies
        """
    )

    # Optional: Check missing values in the dataset
    if st.checkbox("DataFrame Inspection: Identify columns with missing data"):
        parquet_file_path = (
            "data/processed/TrainAndValid_object_values_as_categories.parquet"
        )
        df_tmp = load_parquet_data(parquet_file_path)
        missing_values = df_tmp.isna().sum().sort_values(ascending=False)[:25]
        st.write(missing_values)

    # Feature engineering steps
    st.subheader("Feature Engineering")
    st.write(
        """
        1. **Date-based Features**
            - Extract year, month, day from saledate
            - Create day of week and day of year features
        2. **Categorical Encoding**
            - One-hot encoding for nominal categories
            - Label encoding for ordinal categories
        3. **Derived Features**
            - Calculate machine age at sale
            - Create usage intensity metrics
        """
    )

    # Data transformation steps
    st.subheader("Data Transformation")
    st.write(
        """
        1. **Scaling**
            - Normalize numerical features
            - Handle outliers appropriately
            
        2. **Final Processing**
            - Format data for model input
            - Split into training and validation sets
            
        3. **Quality Checks**
            - Verify data completeness
            - Validate transformations
        """
    )

    # Optional: Inspect random sample rows
    parquet_file_path = "data/processed/TrainAndValid_object_values_as_categories_and_missing_values_filled.parquet"
    df_tmp = load_parquet_data(parquet_file_path)
    if st.checkbox("Quality Checks: Inspection of Random Sample Rows"):
        st.write(df_tmp.sample(5))

    # Optional: Check total number of missing values
    if st.checkbox("Quality Checks: Total Number of Missing Values"):
        total_missing_values = df_tmp.isna().sum().sum()
        if total_missing_values == 0:
            st.success(
                f"Total missing values: {total_missing_values} - Woohoo! Let's build a model!"
            )
        else:
            st.warning(
                f"Uh oh... total missing values: {total_missing_values} - Consider retracing steps to fill the values."
            )

    st.write("---")

    # ===== SECTION 4: MODELING =====
    st.header("4. Modeling")
    st.write(
        """
        This section focuses on selecting, training, and testing a suitable machine learning model to predict bulldozer sale prices.
        """
    )
    st.subheader("""
                Choose Model Type
                """)
    st.markdown("""
                - **Model Selection:** We picked the `Random Forest` model because it has worked well for similar projects before and is known to handle this type of data well.
                - **Choosing the Right Tool:** Given that we have a lot of data (over 100,000 examples) and need to predict prices, we looked at two main options:
                    - `SGD Regressor`: A simple math model that learns by looking at one example at a time.
                    - `Random Forest`: A more advanced model that uses multiple decision trees to make better predictions.
                - **Final Choice:** We went with the Random Forest model because it has a good track record with similar projects and usually gives reliable results across many different types of data.
                """)
    st.subheader("""
                Train the Model
                """)
    st.markdown("""
                **Data Preparation**: Before we can train our model, we need to prepare our data properly:
                """)
    st.markdown("""
                    - **Convert to Numeric**: First, we need to turn all text data into numbers that our computer can understand. We do this by putting similar items into categories and giving each category a number.ber.ber.
                """)
    st.markdown("""
                    - **Handling Missing Values**: Next, we look at any missing information in our data. When we find gaps, we either fill them in with reasonable values or use special techniques to work around them.hem.hem.
                        
                """)
    st.markdown("""
                **Training Process**: The RandomForestRegressor is trained using the preprocessed data. 
                """)
    st.markdown("""
                **Hyperparameter Tuning:** Parameters like the number of trees in the Random Forest can be optimized for better performance.
                """)
    st.subheader("""
                Test the Model
                """)
    st.markdown(
        """
        - **Evaluation Metric**: We use the Root Mean Squared Log Error (RMSLE) as our evaluation metric, which aligns with the Kaggle competition and sets a target accuracy goal of under 1 RMSLE.
        """
    )
    st.markdown(
        """
        - **Validation Set**: Allows for assessment of the model's generalization performance on unseen data.
        
        """
    )
    st.markdown(
        """
        - **Performance Comparison**: The RMSLE obtained would be compared against the Kaggle leaderboard to benchmark the model's effectiveness.
        """
    )
    st.markdown(
        """
        - **Further Testing**: After we test our model on the validation data, we'll do one final test using a separate set of data we've kept aside. This helps us better understand how well our model will work in real-life situations.
        
        """
    )
    st.write("---")

    # ===== SECTION 5: EVALUATION =====
    st.header("5. Evaluation")
    
    st.write("---")

    # ===== SECTION 6: DEPLOYMENT =====
    st.header("6. Deployment")
    st.write(
        """
        *6. Deployment*
        - Put model to use
        - Monitor performance
        - Make updates as needed
        """
    )
    st.write("---")


# ===== MAIN EXECUTION =====
if __name__ == "__main__":
    project_framework_body()
