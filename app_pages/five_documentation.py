import streamlit as st


def documentation_body():
    """
    Renders the complete technical documentation interface for BulldozerPriceGenius.
    Includes sections on API details, system architecture, limitations, and roadmap.
    """
    
    st.write("---")

    # --------------------------------------------------------------
    # SECTION 1: Title and Introduction
    # --------------------------------------------------------------
    st.subheader("*Technical Documentation*")
    st.write(
        'This comprehensive guide provides technical details for the "Predicting the Sale Price of Bulldozers using Machine Learning" project. It\'s designed for technical users who want to understand the inner workings of the system and potentially extend or adapt it for their own use cases.'
    )
    st.markdown(
        """
        - [1. API Details](#1-api-details)
        - [2. System Architecture](#2-system-architecture)
        - [3. System Limitations](#3-system-limitations)
        - [4. Development Roadmap](#4-development-roadmap)
        """
    )
    st.write("---")

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
        "**`scikit-learn`**: for machine learning modeling",
    ]

    # Display libraries as bullet points
    for lib in libraries:
        st.markdown(f"- {lib}")

    st.write(
        "Specific functions and classes from these libraries are used throughout the notebooks. Refer to the respective library documentation for detailed API information."
    )
    st.write(
        'Example: The pandas.read_csv function is used to import the dataset. To see its full documentation, you can refer to the pandas documentation by searching for "pandas.read_csv".'
    )
    st.write("---")

    # --------------------------------------------------------------
    # SECTION 3: System Architecture
    # --------------------------------------------------------------
    st.subheader("2. System Architecture")
    st.write(
        "BulldozerPriceGenius uses a modular architecture with these key components:"
    )

    # Define architecture components
    components = [
        "**Data Processing Module:** Handles data ingestion, cleaning, and feature engineering",
        "**Machine Learning Core:** Random Forest regression model for price prediction",
        "**API Layer:** RESTful API endpoints for system integration",
        "**UI Component:** Streamlit-based interactive dashboard",
    ]

    # Display components as bullet points
    for component in components:
        st.markdown(f"- {component}")
    st.write("---")

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
        "**Performance:** Batch processing limited to 500 items per request",
    ]

    # Display limitations as bullet points
    for limitation in limitations:
        st.markdown(f"- {limitation}")

    st.write("---")

    # --------------------------------------------------------------
    # SECTION 5: Development Roadmap
    # --------------------------------------------------------------
    st.subheader("4. Development Roadmap")

    # Define future development items
    roadmap = [
        "**Feature Engineering:** Further exploration of feature engineering techniques could potentially improve model performance.",
        "**Model Selection and Tuning:** Experimenting with other machine learning models and hyperparameter tuning could lead to better predictive accuracy.",
        "**Handling Missing Values:** Implementing more robust methods for handling missing values is crucial. While current techniques convert string values into categories, more advanced imputation strategies could be applied.",
    ]

    # Display roadmap items as bullet points
    for item in roadmap:
        st.markdown(f"- {item}")
    st.write("---")


# Entry point check
if __name__ == "__main__":
    documentation_body()
