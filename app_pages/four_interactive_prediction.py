import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Set page configuration
st.set_page_config(
    page_title="Bulldozer Price Predictor",
    page_icon="🚜",
    layout="wide"
)

def interactive_prediction_body():
    """Creates interactive dashboard interface and handles model predictions"""
    
    # Custom CSS styling
    st.markdown("""
        <style>
        .main {padding: 2rem;}
        .stButton>button {width: 100%; margin-top: 20px;}
        </style>
    """, unsafe_allow_html=True)

    st.header("🚜 Interactive Bulldozer Price Predictor")
    st.markdown("---")

    # ----------------------------------------------------------------------------- 
    # 2. MODEL LOADING AND IDENTIFICATION
    # -----------------------------------------------------------------------------
    if "model" not in st.session_state:
        try:
            model_path = "src/models/randomforest_regressor_best_RMSLE.pkl"
            st.info(f"📁 Loading model from: {model_path}")
            with open(model_path, "rb") as file:
                # Load the actual model object, not just the array
                st.session_state["model"] = pickle.load(file) 
                st.success(f"✅ Successfully loaded: {model_path.split('/')[-1]}")
        except Exception as e:
            st.error(f"Failed to load model: {e}")
            st.session_state["model"] = None

    # ----------------------------------------------------------------------------- 
    # 3. USER INPUT INTERFACE
    # -----------------------------------------------------------------------------
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📋 Basic Information")
        # Set YearMade input range (replace with actual min/max values)
        year_made = st.number_input("Year Made", value=2000, min_value=1950, max_value=2011) 
        product_size = st.selectbox("Product Size", options=["Mini", "Small", "Medium", "Large"])
        fi_base_model = st.text_input("Base Model", value="D6")
        
    with col2:
        st.subheader("🔧 Technical Specifications")
        fi_secondary_desc = st.text_input("Secondary Description", value="N")
        fi_model_desc = st.text_input("Full Model Description", value="D6N")
        enclosure = st.selectbox("Enclosure", options=["EROPS", "OROPS"])
    
    with st.expander("📅 Sale Information", expanded=False):
        sale_col1, sale_col2, sale_col3 = st.columns(3)
        with sale_col1:
            # Set saleYear input range (replace with actual min/max values)
            sale_year = st.number_input("Sale Year", value=2012, min_value=2012)
        with sale_col2:
            sale_month = st.number_input("Sale Month", value=1, min_value=1, max_value=12)
        with sale_col3:
            sale_day = st.number_input("Sale Day", value=1, min_value=1, max_value=31)
        state = st.selectbox("State", options=["Florida", "Texas", "California", "Other"])

    # ----------------------------------------------------------------------------- 
    # 4. PREDICTION AND RESULTS
    # -----------------------------------------------------------------------------
    st.markdown("---")
    if st.button("🔮 Predict Price", help="Click to get the predicted price based on your inputs"):
        with st.spinner("Calculating prediction..."):
            # Create input DataFrame
            input_data = pd.DataFrame({
                "YearMade": [year_made],
                "ProductSize": [product_size],
                "fiBaseModel": [fi_base_model],
                "fiSecondaryDesc": [fi_secondary_desc],
                "fiModelDesc": [fi_model_desc],
                "Enclosure": [enclosure],
                "state": [state],
                "saleYear": [sale_year],
                "saleMonth": [sale_month],
                "saleDay": [sale_day]
            })
            
            try:
                # Make prediction
                prediction = st.session_state["model"].predict(input_data)
                
                # Display prediction
                st.balloons()
                st.success(f"### Predicted Price: ${prediction[0]:,.2f}")
                
                # Show input summary
                with st.expander("View Input Summary", expanded=False):
                    st.json(input_data.to_dict('records')[0])
                    
            except Exception as e:
                st.error(f"❌ Prediction failed: {str(e)}")
                st.info("Please check your inputs and try again.")

if __name__ == "__main__":
    interactive_prediction_body()
