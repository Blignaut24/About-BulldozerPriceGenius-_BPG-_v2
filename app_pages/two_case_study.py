# Import required libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cache the data loading function to improve performance
@st.cache_data
def load_data(nrows=None):
    # Specify data types to optimize memory usage
    dtype = {
        'saleprice': 'float32',
        'salemonth': 'int8',
        'state': 'category'
    }
    # Convert Google Drive sharing link to direct download link
    file_id = "1vB55Lhr46ISb57kWN16ULHyRrUpZHXJr"
    url = f"https://drive.google.com/uc?id={file_id}"
    
    try:
        df = pd.read_csv(url, dtype=dtype, nrows=nrows, encoding='utf-8')
        # Print column names for debugging
        st.write("Available columns:", list(df.columns))
        return df
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None

def case_study_body():
    # Display main header 
    st.header("Case Study: Bulldozer Price Analysis and Visualization")
    
    # Introduction text
    st.write(
        "The BulldozerPriceGenius app aims to help users understand the factors that influence bulldozer prices."
    )
    
    # Load and display the dataset from Google Drive
    df = load_data(nrows=10000)  # Load only the first 10,000 rows
    
    if df is not None:
        # Optional dataframe inspection
        if st.checkbox("Inspect dataframe"):
            st.dataframe(df)
        
        # SECTION 1: Sale Price Distribution Analysis
        st.subheader("View Sale Price distribution")   
        if st.checkbox("Visualize Sale Price Distribution Histogram"):
            try:
                fig, ax = plt.subplots()
                # Try different possible column names
                if 'SalePrice' in df.columns:
                    price_col = 'SalePrice'
                elif 'saleprice' in df.columns:
                    price_col = 'saleprice'
                else:
                    # Find any column containing 'price' (case insensitive)
                    price_cols = [col for col in df.columns if 'price' in col.lower()]
                    if price_cols:
                        price_col = price_cols[0]
                    else:
                        st.error("Could not find price column")
                        return
                
                df[price_col].plot.hist(ax=ax)
                ax.set_xlabel("Sale Price ($)")
                st.pyplot(fig)
            except Exception as e:
                st.error(f"Error creating histogram: {str(e)}")
        
        # SECTION 2: Monthly Price Trends
        st.subheader("View Median Sale Price by Month")
        if st.checkbox("Visualize Median Sale Price by Month"):
            try:
                fig, ax = plt.subplots()
                month_col = 'saleMonth' if 'saleMonth' in df.columns else 'salemonth'
                df.groupby([month_col])[price_col].median().plot(ax=ax)
                ax.set_xlabel("Month")
                ax.set_ylabel("Median Sale Price ($)")
                st.pyplot(fig)
            except Exception as e:
                st.error(f"Error creating line plot: {str(e)}")

if __name__ == "__main__":
    case_study_body()
