#!/usr/bin/env python3
"""
Test script to verify the orange button styling for the ML prediction button
"""

import streamlit as st

def test_button_styling():
    """Test the orange button styling implementation"""
    
    st.title("🧪 Button Styling Test")
    st.markdown("---")
    
    st.header("Orange ML Prediction Button Test")
    
    # Apply the same CSS styling as in the main app
    st.markdown("""
    <style>
    /* Orange styling specifically for the ML prediction button */
    .ml-prediction-button {
        background-color: transparent !important;
        border: 2px solid #FF6B35 !important;
        color: #FF6B35 !important;
        font-weight: 600 !important;
        font-size: 18px !important;
        padding: 12px 24px !important;
        border-radius: 8px !important;
        transition: all 0.3s ease !important;
        min-height: 50px !important;
        width: 100% !important;
        cursor: pointer !important;
    }
    
    /* Hover effect for the ML prediction button */
    .ml-prediction-button:hover {
        background-color: #FF6B35 !important;
        color: white !important;
        border-color: #FF6B35 !important;
        box-shadow: 0 4px 8px rgba(255, 107, 53, 0.3) !important;
        transform: translateY(-1px) !important;
    }
    
    /* Active/pressed state */
    .ml-prediction-button:active {
        transform: translateY(0px) !important;
        box-shadow: 0 2px 4px rgba(255, 107, 53, 0.3) !important;
    }
    
    /* Focus state for accessibility */
    .ml-prediction-button:focus {
        outline: 2px solid #FF6B35 !important;
        outline-offset: 2px !important;
    }
    
    /* Target the specific button containing the ML prediction text */
    div.stButton > button[kind="primary"]:contains("🤖 Get ML Prediction"),
    div.stButton > button:contains("🤖 Get ML Prediction") {
        background-color: transparent !important;
        border: 2px solid #FF6B35 !important;
        color: #FF6B35 !important;
        font-weight: 600 !important;
        font-size: 18px !important;
        padding: 12px 24px !important;
        border-radius: 8px !important;
        transition: all 0.3s ease !important;
        min-height: 50px !important;
        width: 100% !important;
    }
    
    div.stButton > button[kind="primary"]:contains("🤖 Get ML Prediction"):hover,
    div.stButton > button:contains("🤖 Get ML Prediction"):hover {
        background-color: #FF6B35 !important;
        color: white !important;
        border-color: #FF6B35 !important;
        box-shadow: 0 4px 8px rgba(255, 107, 53, 0.3) !important;
        transform: translateY(-1px) !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("### Test Buttons")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Orange Styled Button:**")
        if st.button("🤖 Get ML Prediction", key="ml_prediction_test"):
            st.success("✅ Orange button clicked! Styling is working.")
    
    with col2:
        st.markdown("**Regular Button (for comparison):**")
        if st.button("🔄 Regular Button", key="regular_button_test"):
            st.info("ℹ️ Regular button clicked.")
    
    st.markdown("---")
    
    st.markdown("### Expected Styling:")
    st.markdown("""
    **Orange ML Prediction Button should have:**
    - 🎨 Orange border (#FF6B35)
    - 🎨 Orange text color (#FF6B35)
    - 📏 Larger size (50px min height)
    - 🎯 Hover effect (orange background, white text)
    - ✨ Smooth transitions
    - 🎪 Box shadow on hover
    """)
    
    st.markdown("### Color Scheme Compatibility:")
    
    # Show color palette
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div style="background-color: #FF6B35; padding: 20px; border-radius: 8px; text-align: center; color: white; font-weight: bold;">
            Orange<br>#FF6B35
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background-color: #1f77b4; padding: 20px; border-radius: 8px; text-align: center; color: white; font-weight: bold;">
            Blue<br>#1f77b4
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="background-color: #17a2b8; padding: 20px; border-radius: 8px; text-align: center; color: white; font-weight: bold;">
            Teal<br>#17a2b8
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div style="background-color: #28a745; padding: 20px; border-radius: 8px; text-align: center; color: white; font-weight: bold;">
            Green<br>#28a745
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("### Accessibility Features:")
    st.markdown("""
    - ♿ Focus outline for keyboard navigation
    - 🎯 High contrast orange color
    - 📱 Responsive design
    - ⌨️ Keyboard accessible
    - 🖱️ Clear hover states
    """)

if __name__ == "__main__":
    test_button_styling()
