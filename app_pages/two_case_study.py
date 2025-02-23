# Import the Streamlit library which we'll use to create our web app
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data
def load_data(csv_file_path):
    return pd.read_csv(csv_file_path)

def case_study_body():
    # Add a main header for the overview section
    st.header("Case Study")

    # Add a subtitle that explains the app's purpose in one line
    st.subheader(
        "Exploratory Data Analysis (EDA)"
    )
    
    st.write(
    """
    The BulldozerPriceGenius app aims to help users understand the factors that influence bulldozer prices. The project has two main data science objectives under Business Requirements:

    - Analyze the distribution of sale prices to understand how bulldozer values are spread out
    - Study sales patterns over time to identify any seasonal trends or recurring patterns in bulldozer pricing

    Through these analyses, the project will provide insights that help users better understand what drives bulldozer market values.
    """
    )

    # Load the CSV file with caching
    csv_file_path = "src/data_prep/TrainAndValid_object_values_as_categories.csv"
    df = load_data(csv_file_path)

    # Add a checkbox to toggle the display of the CSV table
    if st.checkbox("Inspect dataframe"):
        st.dataframe(df)
        
    st.subheader(
        "View SalePrice distribution"
    )
    st.write(
    """
    A histogram of the SalePrice column helps visualize how bulldozer prices are distributed across different price ranges.
    """
    )

    # Add a checkbox to toggle the display of the SalePrice distribution histogram
    if st.checkbox("Visualize Sale Price Distribution Histogram"):
        st.write(
            """
            **What to Look For:**

            - Shape of distribution - whether prices are evenly spread out or clustered around certain values
            - Price ranges - identify the most common price points and any outliers
            - Skewness - whether prices tend to lean towards higher or lower values

            **Business Value:**

            - Helps understand typical price ranges for bulldozers
            - Identifies unusual or extreme prices that might need investigation
            - Provides insights for pricing strategies and market analysis

            This analysis is fundamental for understanding the target variable in this regression problem, which will help achieve the business requirement of understanding what influences bulldozer prices.
            """
        )
        fig, ax = plt.subplots()
        df.SalePrice.plot.hist(ax=ax, xlabel="Sale Price ($)")
        st.pyplot(fig)