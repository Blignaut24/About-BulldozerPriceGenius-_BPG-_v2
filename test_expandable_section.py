#!/usr/bin/env python3
"""
Test script to verify the expandable section functionality
"""

import streamlit as st

# Streamlit compatibility layer
def get_expander(label, expanded=False):
    """Get the appropriate expander function based on Streamlit version"""
    if hasattr(st, 'expander'):
        return st.expander(label, expanded=expanded)
    elif hasattr(st, 'beta_expander'):
        return st.beta_expander(label, expanded=expanded)
    else:
        # Fallback for very old versions - just use a container
        st.markdown(f"**{label}**")
        return st.container()

def test_expandable_section():
    st.title("🧪 Test Expandable Section")
    
    # Mock variables that would be defined in the real application
    selected_year_made = 1994
    product_size = "Large"
    state = "Texas"
    sale_year = 2005
    sale_day_of_year = 180
    selected_model_id = 4200
    enclosure = "EROPS w AC"
    fi_base_model = "D8"
    coupler_system = "Hydraulic"
    tire_size = "26.5R25"
    hydraulics_flow = "High Flow"
    grouser_tracks = "Double"
    hydraulics = "4 Valve"
    
    st.markdown("### Input Values Set:")
    st.write(f"Year Made: {selected_year_made}, Product Size: {product_size}, State: {state}")
    
    # Test the expandable section
    with get_expander("🔍 Review Selected Values - Complete Input Summary", expanded=False):
        st.markdown("**📋 Comprehensive Input Verification**")
        st.markdown("Review all values that will be passed to the Enhanced ML Model for prediction:")

        # Create three-column layout for better organization
        col_basic, col_tech, col_features = st.columns(3)

        with col_basic:
            st.markdown("**📋 Required Fields:**")
            basic_info = f"""
• **Year Made**: {selected_year_made}
• **Product Size**: {product_size}
• **State**: {state}
• **Sale Year**: {sale_year}
• **Sale Day of Year**: {sale_day_of_year}
"""
            st.markdown(basic_info)
            
            # Equipment age calculation
            equipment_age = sale_year - selected_year_made
            st.markdown(f"• **Equipment Age**: {equipment_age} years")

        with col_tech:
            st.markdown("**🔧 Technical Specifications:**")
            tech_specs = f"""
• **Model ID**: {selected_model_id}
• **Enclosure**: {enclosure}
• **Base Model**: {fi_base_model}
• **Coupler System**: {coupler_system}
• **Tire Size**: {tire_size}
"""
            st.markdown(tech_specs)

        with col_features:
            st.markdown("**⚙️ Equipment Features:**")
            equipment_features = f"""
• **Hydraulics Flow**: {hydraulics_flow}
• **Grouser Tracks**: {grouser_tracks}
• **Hydraulics**: {hydraulics}
"""
            st.markdown(equipment_features)
            
            st.markdown("**📊 Prediction Info:**")
            prediction_info = """
• **Method**: Enhanced ML Model
• **Expected Accuracy**: 85-95%
• **Confidence Level**: High
"""
            st.markdown(prediction_info)
        
        # Auto-filled defaults notification
        st.markdown("---")
        st.markdown("**🔄 Auto-filled Default Values:**")
        defaults_info = """
All optional fields have been populated with intelligent defaults based on the Year Made and Product Size selections. 
These defaults are derived from the most common configurations for similar equipment in our training dataset.
"""
        st.info(defaults_info)
    
    st.success("✅ Expandable section test completed!")

if __name__ == "__main__":
    test_expandable_section()
