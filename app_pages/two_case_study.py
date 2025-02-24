# Import required libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cache the data loading function to improve performance
@st.cache_data
def load_data(csv_file_path, nrows=None):
    # Specify data types to optimize memory usage
    dtype = {
        'SalePrice': 'float32',
        'saleMonth': 'int8',
        'state': 'category'
    }
    return pd.read_csv(csv_file_path, dtype=dtype, nrows=nrows)

def case_study_body():
    # Display main header 
    st.header("Case Study: Bulldozer Price Analysis and Visualization")
    
    # Introduction text explaining the app's purpose
    st.write(
        """
        The BulldozerPriceGenius app aims to help users understand the factors that influence bulldozer prices. The project has two main data science objectives under **Business Requirements**:
        """
    )
    
    # Display business objectives in a success box
    st.success(
        """
        - **Objective 1**: Analyze the distribution of sale prices to understand how bulldozer values are spread out
        - **Objective 2**: Study sales patterns over time to identify any seasonal trends or recurring patterns in bulldozer pricing
        """
    )
    
    # Load and display the dataset
    csv_file_path = "src/data_prep/TrainAndValid_object_values_as_categories.csv"
    df = load_data(csv_file_path, nrows=10000)  # Load only the first 10,000 rows
    
    # Optional dataframe inspection
    if st.checkbox("Inspect dataframe"):
        st.dataframe(df)
    
    # SECTION 1: Sale Price Distribution Analysis
    st.subheader("View SalePrice distribution")
    st.write("""[Description of histogram visualization]""")
    
    if st.checkbox("Visualize Sale Price Distribution Histogram"):
        st.write("""[Analysis guidance and business value]""")
        # Create and display histogram
        fig, ax = plt.subplots()
        df.SalePrice.plot.hist(ax=ax, xlabel="Sale Price ($)")
        st.pyplot(fig)
    
    # SECTION 2: Monthly Price Trends
    st.subheader("View Median SalePrice by Month")
    st.write("""[Description of line plot visualization]""")
    
    if st.checkbox("Visualize Median Sale Price by Month"):
        # Create and display line plot
        fig, ax = plt.subplots()
        df.groupby(["saleMonth"])["SalePrice"].median().plot(ax=ax)
        ax.set_xlabel("Month")
        ax.set_ylabel("Median Sale Price ($)")
        st.pyplot(fig)
    
    # SECTION 3: Price vs Month Scatter Plot
    st.subheader("View SalePrice against SaleMonth (First 10,000 samples)")
    
    if st.checkbox("Visualize Sale Price against Sale Month"):
        # Create and display scatter plot
        fig, ax = plt.subplots()
        ax.scatter(x=df["saleMonth"][:10000], y=df["SalePrice"][:10000])
        ax.set_xlabel("Sale Month")
        ax.set_ylabel("Sale Price ($)")
        st.pyplot(fig)
    
    # SECTION 4: Geographic Price Analysis
    st.subheader("View Median SalePrice by State")
    
    if st.checkbox("Visualize Median Sale Price by State"):
        # Calculate median prices
        median_prices_by_state = df.groupby(["state"])["SalePrice"].median()
        median_sale_price = df["SalePrice"].median()
        
        # Create and display bar plot with reference line
        fig, ax = plt.subplots(figsize=(10, 7))
        ax.bar(x=median_prices_by_state.index, height=median_prices_by_state.values)
        ax.set_xlabel("State")
        ax.set_ylabel("Median Sale Price ($)")
        plt.xticks(rotation=90, fontsize=7)
        ax.axhline(y=median_sale_price, color="red", linestyle="--", 
                  label=f"Median Sale Price: ${median_sale_price:,.0f}")
        ax.legend()
        st.pyplot(fig)