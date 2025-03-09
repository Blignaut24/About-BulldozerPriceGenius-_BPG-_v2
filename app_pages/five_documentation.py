# --------------------------------------------------------------
# BulldozerPriceGenius - Technical Documentation Module
# --------------------------------------------------------------
# Purpose: Creates a technical documentation page for the BPG application
# --------------------------------------------------------------

import streamlit as st

def documentation_body():
    """
    Renders the complete technical documentation interface for BulldozerPriceGenius.
    Includes sections on API details, system architecture, limitations, and roadmap.
    """
    # --------------------------------------------------------------
    # SECTION 1: Title and Introduction
    # --------------------------------------------------------------
    st.subheader("BulldozerPriceGenius: Technical Documentation")
    st.write("This comprehensive guide provides technical details for the \"Predicting the Sale Price of Bulldozers using Machine Learning\" project. It's designed for technical users who want to understand the inner workings of the system and potentially extend or adapt it for their own use cases.")
    
    # --------------------------------------------------------------
    # SECTION 2: API Details
    # --------------------------------------------------------------
    st.subheader("1. API Details")
    st.write("This notebook primarily leverages the APIs of the following libraries:")
    
    # Define library list with descriptions
    libraries = [
        "**`pandas:`** for data manipulation and analysis",
        "**`NumPy`**: for numerical computations", 
        "**`matplotlib`**: for data visualization",
        "**`scikit-learn`**: for machine learning modeling"
    ]
    
    # Display libraries as bullet points
    for lib in libraries:
        st.markdown(f"- {lib}")
    
    st.write("Specific functions and classes from these libraries are used throughout the notebooks. Refer to the respective library documentation for detailed API information.")
    st.write("Example: The pandas.read_csv function is used to import the dataset. To see its full documentation, you can refer to the pandas documentation by searching for \"pandas.read_csv\".")
    
    # --------------------------------------------------------------
    # SECTION 3: System Architecture
    # --------------------------------------------------------------
    st.subheader("2. System Architecture")
    st.write("BulldozerPriceGenius uses a modular architecture with these key components:")
    
    # Define architecture components
    components = [
        "**Data Processing Module:** Handles data ingestion, cleaning, and feature engineering",
        "**Machine Learning Core:** Random Forest regression model for price prediction",
        "**API Layer:** RESTful API endpoints for system integration",
        "**UI Component:** Streamlit-based interactive dashboard"
    ]
    
    # Display components as bullet points
    for component in components:
        st.markdown(f"- {component}")
    
    # --------------------------------------------------------------
    # SECTION 4: System Limitations
    # --------------------------------------------------------------
    st.subheader("3. System Limitations")
    
    # Define system limitations with detailed explanations
    limitations = [
        "**Dataset Size**: The notebook is designed to work with the provided Bluebook for Bulldozers dataset. While it handles a large dataset, performance may be affected if used with significantly larger datasets.",
        "**Memory Usage**: The `low_memory=False` parameter is used when reading the CSV data, which can potentially lead to higher memory consumption. Consider adjusting this parameter if memory is a constraint.",
        "**CSV Limitations**: Saving the preprocessed data to CSV format results in the loss of categorical data types. This is a limitation of the CSV format. For data persistence with data type preservation, consider using alternative formats like Parquet or Feather.",
        "**Model Choice**: The notebook currently uses a RandomForestRegressor model. While this model is generally effective, exploring other models may be beneficial for specific use cases.",
        "**Data Constraints:** Predictions are optimized for North American market conditions, with reduced accuracy for international markets",
        "**Model Boundaries:** Most accurate for equipment manufactured after 1990; older equipment may have wider confidence intervals",
        "**Feature Coverage:** Limited coverage for rare or specialty attachments and modifications",
        "**Market Volatility:** Predictions may have reduced accuracy during periods of unusual market volatility",
        "**Real-time Updates:** Market data refreshes weekly, not in real-time",
        "**Performance:** Batch processing limited to 500 items per request"
    ]
    
    # Display limitations as bullet points
    for limitation in limitations:
        st.markdown(f"- {limitation}")
    
    # --------------------------------------------------------------
    # SECTION 5: ML Pipeline Steps
    # --------------------------------------------------------------
    st.subheader("4. ML Pipeline Steps")
    
    st.write("Here's a detailed walkthrough of the Machine Learning (ML) pipeline we used to predict bulldozer sale prices:")

    # Problem Definition
    st.markdown("**1. Problem Definition:**")
    st.markdown("""
    - **Goal:** Predict the future sale price of a bulldozer based on its characteristics and historical sales data.
    - **Problem Type:** Regression (predicting a continuous value - sale price).
    - **Specifics:** Time series or forecasting problem (predicting future sales based on past sales).
    """)

    # Data Collection & Preparation
    st.markdown("**2. Data Collection & Preparation:**")
    st.markdown("""
    - **Data Source:** Kaggle Bluebook for Bulldozers competition dataset (TrainAndValid.csv).
    - **Data Loading:** Import data into a pandas DataFrame using `pd.read_csv()`.
    - **Data Cleaning:**
        - Parsing dates: Convert the 'saledate' column to datetime objects
        - Sorting data: Sort the DataFrame by 'saledate'
    - **Feature Engineering:**
        - Creating new features from 'saledate'
        - Enhancing predictive power with relevant features
    """)

    # EDA
    st.markdown("**3. Exploratory Data Analysis (EDA):**")
    st.markdown("""
    - **Data Visualization:** Create plots to understand feature relationships
        - Example: Scatter plots, histograms, bar charts
    - **Data Insights:** Gain insights from data to guide modeling decisions
        - Example: Identifying patterns, trends, and outliers
    """)

    # Data Preprocessing
    st.markdown("**4. Data Preprocessing:**")
    st.markdown("""
    - **Handling Missing Values:**
        - Strategies: Imputation, removal of rows/columns
    - **Feature Transformation:**
        - Convert categorical features to numerical
            - Technique: Using pandas categories and `.cat.codes`
        - Scale numerical features as needed
    """)

    # Model Selection
    st.markdown("**5. Model Selection:**")
    st.markdown("""
    - **Choosing an Algorithm:**
        - Considerations: Dataset size, problem type, algorithm characteristics
        - Example: RandomForestRegressor
    - **Model Instantiation:** Create instance of chosen model
    """)

    # Model Training
    st.markdown("**6. Model Training:**")
    st.markdown("""
    - **Splitting Data:** Divide into training and validation sets
    - **Fitting the Model:**
        - Train using training data
        - Provide input features (X) and target variable (y)
    """)

    # Model Evaluation
    st.markdown("**7. Model Evaluation:**")
    st.markdown("""
    - **Predicting on Validation Set:** Test model performance
    - **Evaluation Metric:** Calculate RMSLE
    - **Comparison with Baseline:** Compare with average predictions
    """)

    # Model Tuning
    st.markdown("**8. Model Tuning & Optimization:**")
    st.markdown("""
    - **Hyperparameter Tuning:**
        - Techniques: Grid search, randomized search, cross-validation
    - **Feature Selection:** Identify important features
    """)

    # Deployment
    st.markdown("**9. Deployment & Prediction:**")
    st.markdown("""
    - **Train on Full Data:** Use combined dataset
    - **Predict on Test Data:** Make final predictions
    """)

    # --------------------------------------------------------------
    # SECTION 6: Development Roadmap
    # --------------------------------------------------------------
    st.subheader("5. Development Roadmap")
    
    # Define future development items
    roadmap = [
        "**Feature Engineering:** Further exploration of feature engineering techniques could potentially improve model performance.",
        "**Model Selection and Tuning:** Experimenting with other machine learning models and hyperparameter tuning could lead to better predictive accuracy.",
        "**Handling Missing Values:** Implementing more robust methods for handling missing values is crucial. While current techniques convert string values into categories, more advanced imputation strategies could be applied."
    ]
    
    # Display roadmap items as bullet points
    for item in roadmap:
        st.markdown(f"- {item}")

# Entry point check
if __name__ == "__main__":
    documentation_body()