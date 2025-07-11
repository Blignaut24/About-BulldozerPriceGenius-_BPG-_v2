#!/usr/bin/env python3
"""
Demo Streamlit app to show the improved error handling for the bulldozer price prediction model.
Run with: streamlit run demo_error_handling.py
"""

import streamlit as st
import pickle
import numpy as np
import os

def load_model_with_error_handling():
    """Demonstrate the improved model loading with error handling"""
    try:
        model_path = "src/models/randomforest_regressor_best_RMSLE.pkl"
        with open(model_path, 'rb') as f:
            model = pickle.load(f)

        # Check if the loaded object has a predict method
        if hasattr(model, 'predict'):
            return model, None
        else:
            # The pickle file contains something else (like numpy array of trees)
            if isinstance(model, np.ndarray):
                error_msg = (
                    f"🔍 **What we found:** The file contains a numpy array with {model.shape[0]} elements, "
                    f"not a complete trained model.\n\n"
                    f"🎓 **Simple explanation:** Think of this like getting a box of calculator parts "
                    f"instead of a working calculator! The file has the 'ingredients' of a model "
                    f"(individual trees/components) but not the complete 'recipe' (trained model) "
                    f"that can make predictions.\n\n"
                    f"🔧 **What happens next:** Don't worry! The app will automatically use a "
                    f"backup prediction system based on bulldozer market data and depreciation curves."
                )
            else:
                error_msg = (
                    f"🔍 **What we found:** The file contains {type(model)} instead of a trained model.\n\n"
                    f"🎓 **Simple explanation:** We expected a 'smart calculator' that can predict prices, "
                    f"but got something else instead.\n\n"
                    f"🔧 **What happens next:** The app will use a backup prediction system."
                )
            return None, error_msg

    except FileNotFoundError:
        error_msg = (
            f"📁 **File not found:** The model file doesn't exist at the expected location.\n\n"
            f"🎓 **Simple explanation:** It's like looking for a book in the library but "
            f"finding an empty shelf.\n\n"
            f"🔧 **What happens next:** The app will use a backup prediction system."
        )
        return None, error_msg
    except Exception as e:
        error_msg = (
            f"⚠️ **Unexpected error:** {str(e)}\n\n"
            f"🔧 **What happens next:** The app will use a backup prediction system."
        )
        return None, error_msg

def main():
    st.set_page_config(
        page_title="Error Handling Demo",
        page_icon="🚜",
        layout="wide"
    )
    
    st.title("🚜 Bulldozer Price Prediction - Error Handling Demo")
    st.write("This demo shows how the app handles model loading errors gracefully.")
    
    st.header("🔍 Model Loading Test")
    
    # Load model and demonstrate error handling
    model, model_error = load_model_with_error_handling()
    
    if model_error:
        st.error("❌ **Model Loading Issue**")
        st.markdown(model_error)
        st.info("💡 **Good news!** The app will automatically use a backup prediction system that works well for basic price estimates.")
        st.warning("⚠️ **Note:** Predictions will use statistical estimation instead of the trained machine learning model.")
        
        # Show what the backup system would do
        st.header("🔧 Backup Prediction System Demo")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            year_made = st.number_input("Year Made", min_value=1974, max_value=2011, value=2005)
        
        with col2:
            product_size = st.selectbox("Product Size", ["Mini", "Small", "Compact", "Medium", "Large"], index=3)
        
        with col3:
            state = st.selectbox("State", ["California", "Texas", "Florida", "All States"], index=0)
        
        if st.button("🔮 Get Backup Prediction", type="primary"):
            # Simple fallback calculation
            size_base_prices = {
                'Large': 180000, 'Medium': 120000, 'Small': 80000, 
                'Compact': 60000, 'Mini': 40000
            }
            
            base_price = size_base_prices.get(product_size, 100000)
            current_year = 2012
            age = current_year - year_made
            depreciation_rate = 0.10
            age_factor = (1 - depreciation_rate) ** age
            
            estimated_price = base_price * age_factor
            
            # State adjustment
            state_multipliers = {
                'California': 1.15, 'Texas': 1.10, 'Florida': 1.05, 'All States': 1.0
            }
            estimated_price *= state_multipliers.get(state, 1.0)
            
            st.success(f"🎯 **Estimated Price: ${estimated_price:,.2f}**")
            
            col_result1, col_result2, col_result3 = st.columns(3)
            
            with col_result1:
                st.metric("Base Price", f"${base_price:,}")
            
            with col_result2:
                st.metric("Age", f"{age} years")
            
            with col_result3:
                st.metric("Confidence", "~60%", help="Lower confidence due to backup system")
            
            st.info("""
            💡 **How the backup system works:**
            - Uses bulldozer depreciation curves (10% per year)
            - Adjusts for product size and state
            - Provides reasonable estimates even without ML model
            - Less accurate than trained model but still useful
            """)
    
    else:
        st.success("✅ **Advanced ML Model loaded successfully!** You'll get the most accurate predictions.")
    
    # Educational section
    st.header("🎓 What Students Learn From This")
    
    st.markdown("""
    ### 🏆 **Good Programming Practices Demonstrated:**
    
    1. **Error Detection:** Always check if loaded objects work as expected
    2. **Graceful Degradation:** Have backup systems when main features fail  
    3. **Clear Communication:** Explain problems in simple, understandable terms
    4. **User Experience:** Keep the app functional even when parts break
    5. **Transparency:** Tell users what's happening and what to expect
    
    ### 🔧 **Technical Skills:**
    
    - **File I/O:** Loading and validating pickle files
    - **Type Checking:** Using `isinstance()` and `hasattr()` 
    - **Exception Handling:** Try/except blocks with specific error types
    - **Fallback Systems:** Statistical estimation when ML models fail
    - **User Interface:** Informative error messages and status indicators
    
    ### 💡 **Real-World Application:**
    
    This approach is used in production systems where:
    - Models might be corrupted or incomplete
    - Network connections to model servers fail
    - New model versions have compatibility issues
    - Systems need to stay operational during maintenance
    """)

if __name__ == "__main__":
    main()
