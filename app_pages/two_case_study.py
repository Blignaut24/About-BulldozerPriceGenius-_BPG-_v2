import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cache the data loading function to improve performance
@st.cache_data
def load_data(nrows=None):
    try:
        # Use os.path to handle paths correctly across platforms
        csv_file_path = os.path.join("data", "TrainAndValid_object_values_as_categories.csv")
        
        if not os.path.exists(csv_file_path):
            st.error(f"Data file not found at: {csv_file_path}")
            return None
            
        # Specify data types to optimize memory usage
        dtype = {
            'SalePrice': 'float32',
            'saleMonth': 'int8',
            'state': 'category'
        }
        return pd.read_csv(csv_file_path, dtype=dtype, nrows=nrows)
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None

# Define checkboxes outside the main function
inspect_dataframe = st.checkbox("Inspect dataframe")
visualize_hist = st.checkbox("Visualize Sale Price Distribution Histogram")
visualize_line = st.checkbox("Visualize Median Sale Price by Month")
visualize_scatter = st.checkbox("Visualize Sale Price against Sale Month")
visualize_bar = st.checkbox("Visualize Median Sale Price by State")

def case_study_body():
    # Display main header 
    st.header("Case Study: Bulldozer Price Analysis and Visualization")
    
    # Introduction text
    st.write("""
        The BulldozerPriceGenius app aims to help users understand the factors that influence bulldozer prices. 
        The project has two main data science objectives under **Business Requirements**:
    """)
    
    # Display business objectives
    st.success("""
        - **Objective 1**: Analyze the distribution of sale prices to understand how bulldozer values are spread out.
        - **Objective 2**: Study sales patterns over time to identify any seasonal trends or recurring patterns in bulldozer pricing.
    """)
    
    # Load data
    df = load_data(nrows=10000)
    if df is None:
        return
    
    # Optional dataframe inspection
    if inspect_dataframe:
        st.dataframe(df)
    
    # SECTION 1: Sale Price Distribution Analysis
    st.subheader("View SalePrice distribution")
    if visualize_hist:
        fig, ax = plt.subplots()
        df.SalePrice.plot.hist(ax=ax, xlabel="Sale Price ($)")
        st.pyplot(fig)
    
    # SECTION 2: Monthly Price Trends
    st.subheader("View Median SalePrice by Month")
    if visualize_line:
        fig, ax = plt.subplots()
        df.groupby(["saleMonth"])["SalePrice"].median().plot(ax=ax)
        ax.set_xlabel("Month")
        ax.set_ylabel("Median Sale Price ($)")
        st.pyplot(fig)
    
    # SECTION 3: Price vs Month Scatter Plot
    st.subheader("View SalePrice against SaleMonth")
    if visualize_scatter:
        fig, ax = plt.subplots()
        ax.scatter(x=df["saleMonth"][:10000], y=df["SalePrice"][:10000])
        ax.set_xlabel("Sale Month")
        ax.set_ylabel("Sale Price ($)")
        st.pyplot(fig)
    
    # SECTION 4: Geographic Price Analysis
    st.subheader("View Median SalePrice by State")
    if visualize_bar:
        median_prices_by_state = df.groupby(["state"])["SalePrice"].median()
        median_sale_price = df["SalePrice"].median()
        
        fig, ax = plt.subplots(figsize=(10, 7))
        ax.bar(x=median_prices_by_state.index, height=median_prices_by_state.values)
        ax.set_xlabel("State")
        ax.set_ylabel("Median Sale Price ($)")
        plt.xticks(rotation=90, fontsize=7)
        ax.axhline(y=median_sale_price, color="red", linestyle="--", 
                  label=f"Median Sale Price: ${median_sale_price:,.0f}")
        ax.legend()
        st.pyplot(fig)

# Call the main function
if __name__ == "__main__":
    case_study_body()