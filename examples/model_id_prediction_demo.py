"""
Complete ModelID Prediction Demo

This example demonstrates how to integrate the ModelID input component
into a complete bulldozer price prediction interface.

Usage:
    streamlit run examples/model_id_prediction_demo.py

Author: BulldozerPriceGenius Team
Date: 2025-07-08
"""

import streamlit as st
import pandas as pd
import numpy as np
import sys
import os

# Add src to path to import our components
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from components.model_id_input import (
    create_model_id_input,
    preprocess_model_id_for_prediction,
    ModelIDProcessor
)


def load_sample_data():
    """Load sample data for demonstration purposes."""
    try:
        # Try to load real data if available
        data_path = "src/data_prep/TrainAndValid_object_values_as_categories.csv"
        if os.path.exists(data_path):
            data = pd.read_csv(data_path, usecols=['ModelID', 'SalePrice'], nrows=1000)
            return data
    except Exception:
        pass
    
    # Create sample data if real data not available
    np.random.seed(42)
    sample_model_ids = [4605, 3538, 3170, 4604, 3362, 3537, 3171, 4603, 3357, 3178]
    sample_data = []
    
    for _ in range(100):
        model_id = np.random.choice(sample_model_ids)
        # Simulate price based on ModelID (for demo only)
        base_price = 50000 + (model_id % 1000) * 50
        noise = np.random.normal(0, 10000)
        price = max(10000, base_price + noise)
        sample_data.append({'ModelID': model_id, 'SalePrice': price})
    
    return pd.DataFrame(sample_data)


@st.cache_data
def create_fitted_processor():
    """Create and fit a ModelID processor with sample data."""
    sample_data = load_sample_data()
    processor = ModelIDProcessor()
    processor.fit(sample_data['ModelID'])
    return processor


def simulate_price_prediction(processed_model_id: np.ndarray, model_id: int) -> float:
    """
    Simulate a price prediction for demonstration purposes.
    In a real application, this would use your trained ML model.
    
    Args:
        processed_model_id: Preprocessed ModelID array
        model_id: Original ModelID value
        
    Returns:
        Simulated predicted price
    """
    # Simple simulation based on ModelID
    base_price = 45000
    model_factor = (model_id % 1000) * 75
    processed_factor = processed_model_id[0] * 5000
    
    # Add some randomness for realism
    np.random.seed(model_id)  # Consistent results for same ModelID
    noise = np.random.normal(0, 8000)
    
    predicted_price = base_price + model_factor + processed_factor + noise
    return max(15000, predicted_price)  # Minimum reasonable price


def main():
    """Main application function."""
    st.set_page_config(
        page_title="ModelID Prediction Demo",
        page_icon="🚜",
        layout="wide"
    )
    
    st.title("🚜 Bulldozer Price Prediction - ModelID Demo")
    st.markdown("""
    This demo shows how the ModelID input component works in a complete prediction pipeline.
    Enter a ModelID to see how it's processed and used for price prediction.
    """)
    
    # Create two columns for layout
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("📝 Input Section")
        
        # Create the ModelID input component
        model_id = create_model_id_input()
        
        if model_id is not None:
            # Show data insights for the entered ModelID
            st.subheader("📊 ModelID Insights")
            sample_data = load_sample_data()
            
            if model_id in sample_data['ModelID'].values:
                model_data = sample_data[sample_data['ModelID'] == model_id]
                avg_price = model_data['SalePrice'].mean()
                count = len(model_data)
                st.success(f"✅ ModelID {model_id} found in training data!")
                st.metric("Average Historical Price", f"${avg_price:,.2f}")
                st.metric("Number of Records", count)
            else:
                st.info(f"ℹ️ ModelID {model_id} is new - will use imputation strategy")
                st.write("This ModelID wasn't seen during training, but our model can handle it!")
    
    with col2:
        st.header("🔄 Processing & Prediction")
        
        if model_id is not None:
            # Load fitted processor
            with st.spinner("Loading ModelID processor..."):
                processor = create_fitted_processor()
            
            # Preprocess the ModelID
            st.subheader("1️⃣ Preprocessing")
            processed_array, status = preprocess_model_id_for_prediction(model_id, processor)
            st.info(status)
            
            # Show preprocessing details
            with st.expander("🔍 Preprocessing Details"):
                st.write(f"**Original ModelID:** {model_id}")
                st.write(f"**Processed Value:** {processed_array[0]:.6f}")
                st.write(f"**Array Shape:** {processed_array.shape}")
                st.write(f"**Data Type:** {processed_array.dtype}")
                
                # Show encoding information
                if hasattr(processor, 'ordinal_encoder'):
                    st.write("**Encoding Method:** OrdinalEncoder with unknown value handling")
                    st.write("**Imputation Strategy:** Most frequent value")
            
            # Simulate prediction
            st.subheader("2️⃣ Price Prediction")
            with st.spinner("Generating prediction..."):
                predicted_price = simulate_price_prediction(processed_array, model_id)
            
            # Display prediction results
            st.success(f"🎯 Predicted Price: ${predicted_price:,.2f}")
            
            # Show confidence and additional info
            col2a, col2b = st.columns(2)
            with col2a:
                # Simulate confidence based on whether ModelID was seen
                confidence = 0.92 if model_id in processor.known_model_ids else 0.78
                st.metric("Prediction Confidence", f"{confidence:.1%}")
            
            with col2b:
                # Show price range with better formatting
                price_range = predicted_price * 0.15  # ±15% range
                lower = predicted_price - price_range
                upper = predicted_price + price_range

                # Create shorter display format
                def format_price_short(price):
                    if price >= 1000000:
                        return f"${price/1000000:.1f}M"
                    elif price >= 1000:
                        return f"${price/1000:.0f}K"
                    else:
                        return f"${price:,.0f}"

                short_range = f"{format_price_short(lower)} - {format_price_short(upper)}"
                full_range = f"${lower:,.0f} - ${upper:,.0f}"

                st.metric("Estimated Range",
                         short_range,
                         help=f"Full range: {full_range} (±15%)")
    
    # Show technical details section
    if model_id is not None:
        st.write("---")
        st.header("🛠️ Technical Implementation")
        
        tab1, tab2, tab3 = st.tabs(["Pipeline Code", "Error Handling", "Best Practices"])
        
        with tab1:
            st.subheader("Complete Pipeline Implementation")
            st.code(f"""
# Complete ModelID processing pipeline

import numpy as np
from sklearn.preprocessing import OrdinalEncoder
from sklearn.impute import SimpleImputer

# 1. User Input Validation
model_id_input = "{model_id}"  # From Streamlit input
is_valid, model_id, error = validate_model_id(model_id_input)

if is_valid:
    # 2. Load fitted processor (saved during model training)
    processor = load_fitted_processor()
    
    # 3. Preprocess ModelID
    processed_model_id = processor.transform(model_id)
    # Result: {processed_array}
    
    # 4. Combine with other features
    # all_features = np.concatenate([
    #     processed_model_id,
    #     other_processed_features
    # ])
    
    # 5. Make prediction
    # prediction = trained_model.predict(all_features.reshape(1, -1))
    # Result: ${predicted_price:,.2f}
            """)
        
        with tab2:
            st.subheader("Error Handling Strategies")
            st.markdown("""
            **Input Validation:**
            - ✅ Checks for integer values only
            - ✅ Validates reasonable range (1-100,000)
            - ✅ Handles empty/invalid inputs gracefully
            
            **Preprocessing Robustness:**
            - ✅ OrdinalEncoder with `handle_unknown='use_encoded_value'`
            - ✅ SimpleImputer for missing/unknown values
            - ✅ Fallback to default values on errors
            
            **Prediction Safety:**
            - ✅ Try-catch blocks around all operations
            - ✅ Logging for debugging and monitoring
            - ✅ Graceful degradation with informative messages
            """)
        
        with tab3:
            st.subheader("Best Practices Implemented")
            st.markdown("""
            **Data Preprocessing:**
            - 🎯 Categorical encoding preserves ordinal relationships
            - 🎯 Imputation strategy handles unseen values
            - 🎯 Feature scaling and normalization ready
            
            **Code Quality:**
            - 📝 Comprehensive documentation and type hints
            - 🧪 Modular design for easy testing
            - 🔄 Reusable components across the application
            
            **User Experience:**
            - 💡 Clear validation messages and help text
            - 📊 Visual feedback on processing status
            - 🎨 Intuitive interface with expandable details
            
            **Production Readiness:**
            - 🚀 Caching for performance optimization
            - 📈 Logging and error monitoring
            - 🔒 Input sanitization and validation
            """)
    
    # Footer with additional resources
    st.write("---")
    st.markdown("""
    ### 📚 Additional Resources
    
    - **Documentation:** See `src/components/model_id_input.py` for complete implementation
    - **Testing:** Run unit tests with `pytest tests/test_model_id_input.py`
    - **Integration:** Import and use in your prediction pipeline
    
    *This demo shows a complete, production-ready ModelID input component with proper validation, 
    preprocessing, and error handling for bulldozer price prediction.*
    """)


if __name__ == "__main__":
    main()
