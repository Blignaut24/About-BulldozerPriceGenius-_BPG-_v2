"""
Complete YearMade Prediction Demo

This example demonstrates how to integrate the YearMade input component
into a complete bulldozer price prediction interface, showcasing why
YearMade is the most important feature for price prediction.

Usage:
    streamlit run examples/year_made_prediction_demo.py

Author: BulldozerPriceGenius Team
Date: 2025-07-08
"""

import streamlit as st
import pandas as pd
import numpy as np
import sys
import os
import plotly.express as px
import plotly.graph_objects as go

# Add src to path to import our components
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

# Streamlit caching compatibility layer
def get_cache_data_decorator():
    """Get the appropriate caching decorator for data caching."""
    if hasattr(st, 'cache_data'):
        return st.cache_data
    elif hasattr(st, 'experimental_memo'):
        return st.experimental_memo
    elif hasattr(st, 'cache'):
        return st.cache
    else:
        def no_cache(func):
            return func
        return no_cache

cache_data_decorator = get_cache_data_decorator()

from components.year_made_input import (
    create_year_made_input,
    preprocess_year_made_for_prediction,
    YearMadeProcessor
)


def load_sample_data():
    """Load sample data for demonstration purposes."""
    try:
        # Try to load real data if available
        data_path = "src/data_prep/TrainAndValid_object_values_as_categories.csv"
        if os.path.exists(data_path):
            data = pd.read_csv(data_path, usecols=['YearMade', 'SalePrice'], nrows=5000)
            # Filter out placeholder values
            data = data[data['YearMade'] > 1970]
            return data
    except Exception:
        pass
    
    # Create realistic sample data if real data not available
    np.random.seed(42)
    sample_data = []
    
    # Create realistic year distribution based on analysis
    years = list(range(1975, 2015))
    weights = [1 if y < 1990 else 3 if y < 2000 else 2 for y in years]  # More 90s/2000s
    
    for _ in range(1000):
        year = np.random.choice(years, p=np.array(weights)/sum(weights))
        
        # Simulate price based on year (newer = higher base price)
        base_price = 30000 + (year - 1975) * 1500  # $1500 per year newer
        
        # Add realistic variation
        variation = np.random.normal(0, 15000)
        depreciation = np.random.uniform(0.8, 1.2)  # ±20% variation
        
        price = max(10000, (base_price + variation) * depreciation)
        sample_data.append({'YearMade': year, 'SalePrice': price})
    
    return pd.DataFrame(sample_data)


@cache_data_decorator
def create_fitted_processor():
    """Create and fit a YearMade processor with sample data."""
    sample_data = load_sample_data()
    processor = YearMadeProcessor()
    processor.fit(sample_data['YearMade'])
    return processor


def simulate_price_prediction(year_made: int, processed_year: np.ndarray) -> float:
    """
    Simulate a price prediction based on YearMade.
    In a real application, this would use your trained ML model.
    
    Args:
        year_made: Original year value
        processed_year: Preprocessed year array
        
    Returns:
        Simulated predicted price
    """
    # Base price increases with newer years
    base_price = 25000 + (year_made - 1975) * 1200
    
    # Add some realistic factors
    age = 2025 - year_made
    depreciation_factor = max(0.3, 1 - (age * 0.08))  # 8% depreciation per year
    
    # Technology bonus for certain eras
    if year_made >= 2010:
        tech_bonus = 1.15  # 15% bonus for modern tech
    elif year_made >= 2000:
        tech_bonus = 1.05  # 5% bonus for recent tech
    else:
        tech_bonus = 1.0
    
    # Market demand factor (some years more popular)
    popular_years = [1995, 1998, 2000, 2005]
    demand_factor = 1.1 if year_made in popular_years else 1.0
    
    predicted_price = base_price * depreciation_factor * tech_bonus * demand_factor
    
    # Add some randomness for realism
    np.random.seed(year_made)
    noise = np.random.normal(1.0, 0.1)
    
    return max(15000, predicted_price * noise)


def create_year_impact_visualization(year_made: int, sample_data: pd.DataFrame):
    """Create visualizations showing YearMade impact on prices."""
    
    # Price by year scatter plot
    fig1 = px.scatter(
        sample_data, 
        x='YearMade', 
        y='SalePrice',
        title='Bulldozer Prices by Year Made',
        labels={'YearMade': 'Year Made', 'SalePrice': 'Sale Price ($)'},
        opacity=0.6
    )
    
    # Highlight the selected year
    selected_data = sample_data[sample_data['YearMade'] == year_made]
    if not selected_data.empty:
        fig1.add_scatter(
            x=selected_data['YearMade'],
            y=selected_data['SalePrice'],
            mode='markers',
            marker=dict(color='red', size=10),
            name=f'Year {year_made}',
            showlegend=True
        )
    
    fig1.update_layout(height=400)
    
    # Average price by year line chart
    yearly_avg = sample_data.groupby('YearMade')['SalePrice'].mean().reset_index()
    
    fig2 = px.line(
        yearly_avg,
        x='YearMade',
        y='SalePrice',
        title='Average Price Trend by Year Made',
        labels={'YearMade': 'Year Made', 'SalePrice': 'Average Sale Price ($)'}
    )
    
    # Add vertical line for selected year
    fig2.add_vline(
        x=year_made,
        line_dash="dash",
        line_color="red",
        annotation_text=f"Selected: {year_made}"
    )
    
    fig2.update_layout(height=400)
    
    return fig1, fig2


def main():
    """Main application function."""
    st.set_page_config(
        page_title="YearMade Prediction Demo",
        page_icon="📅",
        layout="wide"
    )
    
    st.title("📅 Bulldozer Price Prediction - YearMade Demo")
    st.markdown("""
    This demo showcases why **YearMade is the most important feature** for bulldozer price prediction.
    Enter a year to see how it affects price predictions and explore the relationship between age and value.
    """)
    
    # Load sample data
    sample_data = load_sample_data()
    
    # Create two columns for layout
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("📝 Input Section")
        
        # Create the YearMade input component
        year_made = create_year_made_input()
        
        if year_made is not None:
            # Show year insights
            st.subheader("📊 Year Insights")
            
            # Calculate age and era
            current_year = 2025
            age = current_year - year_made
            
            col1a, col1b = st.columns(2)
            with col1a:
                st.metric("Equipment Age", f"{age} years")
            with col1b:
                if year_made >= 2010:
                    era = "Modern Era"
                    era_color = "🟢"
                elif year_made >= 2000:
                    era = "Recent Era"
                    era_color = "🟡"
                elif year_made >= 1990:
                    era = "Mature Era"
                    era_color = "🟠"
                else:
                    era = "Vintage Era"
                    era_color = "🔴"
                
                st.metric("Technology Era", f"{era_color} {era}")
            
            # Show historical data for this year
            year_data = sample_data[sample_data['YearMade'] == year_made]
            if not year_data.empty:
                st.success(f"✅ Found {len(year_data)} bulldozers from {year_made} in dataset")
                avg_price = year_data['SalePrice'].mean()
                st.metric("Historical Avg Price", f"${avg_price:,.2f}")
            else:
                st.info(f"ℹ️ No historical data for {year_made} - using model prediction")
    
    with col2:
        st.header("🔄 Processing & Prediction")
        
        if year_made is not None:
            # Load fitted processor
            with st.spinner("Loading YearMade processor..."):
                processor = create_fitted_processor()
            
            # Preprocess the YearMade
            st.subheader("1️⃣ Preprocessing")
            processed_array, status = preprocess_year_made_for_prediction(year_made, processor)
            st.info(status)
            
            # Show preprocessing details
            with st.expander("🔍 Preprocessing Details"):
                st.write(f"**Original YearMade:** {year_made}")
                st.write(f"**Processed Value:** {processed_array[0]}")
                st.write(f"**Data Type:** {processed_array.dtype}")
                st.write(f"**Array Shape:** {processed_array.shape}")
                st.write("**Processing Method:** Direct numerical (no encoding)")
                st.write("**Imputation Strategy:** Median for missing values")
                st.write("**Feature Type:** Numerical (maintains natural ordering)")
            
            # Simulate prediction
            st.subheader("2️⃣ Price Prediction")
            with st.spinner("Generating prediction..."):
                predicted_price = simulate_price_prediction(year_made, processed_array)
            
            # Display prediction results
            st.success(f"🎯 Predicted Price: ${predicted_price:,.2f}")
            
            # Show confidence and additional metrics
            col2a, col2b = st.columns(2)
            with col2a:
                # Confidence based on training range
                if 1971 <= year_made <= 2014:
                    confidence = 0.92
                elif 1970 <= year_made <= 2020:
                    confidence = 0.78
                else:
                    confidence = 0.65
                st.metric("Prediction Confidence", f"{confidence:.1%}")
            
            with col2b:
                # Show depreciation estimate
                age = 2025 - year_made
                if age <= 5:
                    depreciation = age * 12
                elif age <= 15:
                    depreciation = 60 + (age - 5) * 8
                else:
                    depreciation = min(95, 140 + (age - 15) * 3)
                
                st.metric("Est. Depreciation", f"{depreciation:.0f}%")
    
    # Show visualizations if year is selected
    if year_made is not None:
        st.write("---")
        st.header("📈 YearMade Impact Analysis")
        
        # Create visualizations
        fig1, fig2 = create_year_impact_visualization(year_made, sample_data)
        
        col3, col4 = st.columns(2)
        with col3:
            st.plotly_chart(fig1, use_container_width=True)
        with col4:
            st.plotly_chart(fig2, use_container_width=True)
        
        # Show correlation analysis
        st.subheader("🔗 Feature Importance Analysis")
        correlation = sample_data['YearMade'].corr(sample_data['SalePrice'])
        
        col5, col6, col7 = st.columns(3)
        with col5:
            st.metric("Price Correlation", f"{correlation:.3f}")
        with col6:
            st.metric("Feature Rank", "#1 Most Important")
        with col7:
            variance_explained = correlation ** 2 * 100
            st.metric("Variance Explained", f"{variance_explained:.1f}%")
        
        # Technical implementation details
        st.write("---")
        st.header("🛠️ Technical Implementation")
        
        tab1, tab2, tab3 = st.tabs(["Why Most Important", "Processing Pipeline", "Best Practices"])
        
        with tab1:
            st.subheader("Why YearMade is the Most Important Feature")
            st.markdown(f"""
            **For your selected year {year_made}:**
            
            **🔧 Depreciation Impact:**
            - Equipment age: {2025 - year_made} years
            - Estimated depreciation: ~{min(95, (2025 - year_made) * 8):.0f}%
            - Newer equipment retains more value
            
            **⚙️ Technology Advancement:**
            - Engine efficiency improvements over time
            - Hydraulic system enhancements
            - Control system sophistication
            - Emission standard compliance
            
            **📊 Market Dynamics:**
            - Buyer preference for newer equipment
            - Financing availability for recent models
            - Warranty and support considerations
            - Resale value expectations
            
            **🔍 Data Evidence:**
            - Correlation with price: {correlation:.3f}
            - Explains {variance_explained:.1f}% of price variance
            - Consistent predictor across all price ranges
            """)
        
        with tab2:
            st.subheader("YearMade Processing Pipeline")
            st.code(f"""
# Complete YearMade processing pipeline

import numpy as np
from sklearn.impute import SimpleImputer

# 1. User Input Validation
year_input = "{year_made}"  # From Streamlit input
is_valid, year_made, warning = validate_year_made(year_input)

if is_valid:
    # 2. Load fitted processor (saved during model training)
    processor = load_fitted_processor()
    
    # 3. Preprocess YearMade (numerical feature)
    processed_year = processor.transform(year_made)
    # Result: {processed_array} (dtype: {processed_array.dtype})
    
    # 4. Key advantages of numerical treatment:
    # - No encoding needed (unlike categorical features)
    # - Preserves natural ordering relationship
    # - Direct correlation with target variable
    # - Efficient for ML algorithms
    
    # 5. Combine with other features (maintaining feature order)
    # all_features = np.array([
    #     processed_year[0],      # Position 0: YearMade
    #     other_feature_1,        # Position 1: Next feature
    #     other_feature_2,        # Position 2: Next feature
    #     ...
    # ])
    
    # 6. Make prediction
    # prediction = trained_model.predict(all_features.reshape(1, -1))
    # Result: ${predicted_price:,.2f}
            """)
        
        with tab3:
            st.subheader("Best Practices for YearMade")
            st.markdown("""
            **✅ Input Validation:**
            - Accept only integer years (no decimals)
            - Validate realistic range (1970-2025)
            - Provide warnings for years outside training range
            - Handle edge cases gracefully
            
            **✅ Preprocessing Strategy:**
            - Treat as numerical feature (no categorical encoding)
            - Use median imputation for missing values
            - Maintain int64 data type for consistency
            - Preserve feature order in pipeline
            
            **✅ Model Integration:**
            - Position YearMade consistently in feature vector
            - Document feature order for reproducibility
            - Monitor for data drift in year distributions
            - Validate predictions for extreme years
            
            **✅ User Experience:**
            - Explain why YearMade is most important
            - Show confidence levels for different year ranges
            - Provide context about equipment age and depreciation
            - Display historical data when available
            """)
    
    # Footer with additional resources
    st.write("---")
    st.markdown("""
    ### 📚 Additional Resources
    
    - **Documentation:** See `src/components/year_made_input.py` for complete implementation
    - **Testing:** Run unit tests with `pytest tests/test_year_made_input.py`
    - **Integration:** Import and use in your prediction pipeline
    
    *This demo shows a complete, production-ready YearMade input component that demonstrates
    why YearMade is the most important feature for bulldozer price prediction.*
    """)


if __name__ == "__main__":
    main()
