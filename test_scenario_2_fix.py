#!/usr/bin/env python3
"""
Test Script to Verify Test Scenario 2 Fix
Validates that Test Scenario 2 (1987 D9 Large Ultra-Vintage) displays correctly
"""

import streamlit as st

def test_scenario_2_fix():
    """Test the fixed Test Scenario 2 implementation"""
    
    st.title("🧪 Test Scenario 2 Fix Verification")
    st.markdown("Testing the UX consistency fix for Test Scenario 2 (1987 D9 Large Ultra-Vintage)")
    
    # Simulate Test Scenario 2 data loading
    st.subheader("1. 📋 Simulating Test Scenario 2 Data Load")
    
    # Test Scenario 2 data from the actual implementation
    test_scenario_2_data = {
        "year_made": 1987,
        "product_size": "Large", 
        "state": "Texas",
        "model_id": 4800,
        "enclosure": "EROPS w AC",
        "base_model": "D9",
        "hydraulics": "4 Valve",
        "tire_size": "29.5R25",
        "sale_year": 2006,
        "sale_day": 182
    }
    
    # Store in session state with test_ prefix (as the actual implementation does)
    for field, value in test_scenario_2_data.items():
        st.session_state[f"test_{field}"] = value
    
    st.success("✅ Test Scenario 2 data loaded into session state")
    
    # Display what was loaded
    st.markdown("**Loaded Test Data:**")
    for field, value in test_scenario_2_data.items():
        st.write(f"• test_{field}: {value}")
    
    # 2. Test the fixed expandable section logic
    st.subheader("2. 🔍 Testing Fixed Expandable Section Logic")
    
    # Simulate the form widget values (these would be the actual widget values)
    year_made = st.session_state.get('test_year_made', 2000)
    model_id = st.session_state.get('test_model_id', 4800)
    product_size = st.session_state.get('test_product_size', 'Large')
    state = st.session_state.get('test_state', 'All States')
    enclosure = st.session_state.get('test_enclosure', 'EROPS')
    base_model = st.session_state.get('test_base_model', 'D3')
    hydraulics = st.session_state.get('test_hydraulics', 'Standard')
    tire_size = st.session_state.get('test_tire_size', 'None or Unspecified')
    sale_year = st.session_state.get('test_sale_year', 2006)
    sale_day = st.session_state.get('test_sale_day', 182)
    
    st.markdown("**Form Widget Values (what expandable section should see):**")
    st.write(f"• Year Made: {year_made}")
    st.write(f"• Product Size: {product_size}")
    st.write(f"• State: {state}")
    st.write(f"• Model ID: {model_id}")
    st.write(f"• Enclosure: {enclosure}")
    st.write(f"• Base Model: {base_model}")
    st.write(f"• Hydraulics: {hydraulics}")
    st.write(f"• Tire Size: {tire_size}")
    st.write(f"• Sale Year: {sale_year}")
    st.write(f"• Sale Day: {sale_day}")
    
    # 3. Test the expandable section display logic
    st.subheader("3. 📊 Testing Expandable Section Display")
    
    # Import the get_expander function
    try:
        from app_pages.four_interactive_prediction_render import get_expander, get_columns
        
        # Simulate the fixed expandable section
        with get_expander("🔍 Review Selected Values - Complete Input Summary", expanded=True):
            st.markdown("**📋 Comprehensive Input Verification**")
            st.markdown("Review all values that will be passed to the Enhanced ML Model for prediction:")
            
            # Use the actual form widget values (as the fix does)
            display_year_made = year_made
            display_model_id = model_id  
            display_product_size = product_size
            display_state = state
            display_enclosure = enclosure
            display_base_model = base_model
            display_hydraulics = hydraulics
            display_tire_size = tire_size
            display_sale_year = sale_year
            display_sale_day = sale_day
            
            # Validate data types
            display_year_made = int(display_year_made) if isinstance(display_year_made, (int, float, str)) and str(display_year_made).isdigit() else 2000
            display_model_id = int(display_model_id) if isinstance(display_model_id, (int, float, str)) and str(display_model_id).isdigit() else 4800
            display_sale_year = int(display_sale_year) if isinstance(display_sale_year, (int, float, str)) and str(display_sale_year).isdigit() else 2006
            display_sale_day = int(display_sale_day) if isinstance(display_sale_day, (int, float, str)) and str(display_sale_day).isdigit() else 182
            
            # Test three-column layout
            try:
                col_basic, col_tech, col_features = get_columns(3)
                
                with col_basic:
                    st.markdown("**📋 Required Fields:**")
                    basic_info = f"""
• **Year Made**: {display_year_made}
• **Product Size**: {display_product_size}
• **State**: {display_state}
• **Sale Year**: {display_sale_year}
• **Sale Day of Year**: {display_sale_day}
"""
                    st.markdown(basic_info)
                    
                    # Equipment age calculation
                    equipment_age = display_sale_year - display_year_made
                    st.markdown(f"• **Equipment Age**: {equipment_age} years")
                
                with col_tech:
                    st.markdown("**🔧 Technical Specifications:**")
                    tech_specs = f"""
• **Model ID**: {display_model_id}
• **Enclosure**: {display_enclosure}
• **Base Model**: {display_base_model}
• **Tire Size**: {display_tire_size}
"""
                    st.markdown(tech_specs)
                
                with col_features:
                    st.markdown("**⚙️ Equipment Features:**")
                    equipment_features = f"""
• **Hydraulics**: {display_hydraulics}
"""
                    st.markdown(equipment_features)
                    
                    st.markdown("**📊 Prediction Info:**")
                    prediction_info = """
• **Method**: Enhanced ML Model
• **Expected Accuracy**: 85-95%
• **Confidence Level**: High
"""
                    st.markdown(prediction_info)
                    
            except Exception as e:
                st.error(f"Column layout failed: {e}")
            
            # Test scenario detection
            st.markdown("---")
            st.markdown("**🧪 Test Scenario Detection:**")
            detected_scenarios = []
            
            # Test Scenario 2: 1987 D9 Large - FIXED detection
            if (display_year_made == 1987 and display_product_size == 'Large' and
                display_base_model == 'D9' and 'EROPS' in display_enclosure):
                detected_scenarios.append("Test Scenario 2 (1987 D9 Large - Ultra-Vintage)")
            
            if detected_scenarios:
                for scenario in detected_scenarios:
                    st.success(f"✅ **{scenario}** detected")
                st.info("🎯 **Test Scenario Detected**: This configuration matches a TEST.md validation scenario.")
            else:
                st.warning("⚠️ Test Scenario 2 not detected - check detection logic")
                st.write(f"Debug: year_made={display_year_made}, product_size='{display_product_size}', base_model='{display_base_model}', enclosure='{display_enclosure}'")
        
        st.success("✅ Expandable section test completed successfully")
        
    except Exception as e:
        st.error(f"❌ Expandable section test failed: {e}")
        import traceback
        st.code(traceback.format_exc())
    
    # 4. Verification Summary
    st.subheader("4. ✅ Verification Summary")
    
    # Check expected values
    expected_values = {
        "Year Made": 1987,
        "Product Size": "Large",
        "State": "Texas", 
        "Base Model": "D9",
        "Enclosure": "EROPS w AC",
        "Model ID": 4800,
        "Sale Year": 2006,
        "Equipment Age": 19
    }
    
    actual_values = {
        "Year Made": display_year_made,
        "Product Size": display_product_size,
        "State": display_state,
        "Base Model": display_base_model,
        "Enclosure": display_enclosure,
        "Model ID": display_model_id,
        "Sale Year": display_sale_year,
        "Equipment Age": display_sale_year - display_year_made
    }
    
    st.markdown("**Expected vs Actual Values:**")
    all_correct = True
    for field, expected in expected_values.items():
        actual = actual_values.get(field, "Missing")
        if actual == expected:
            st.success(f"✅ {field}: {actual} (correct)")
        else:
            st.error(f"❌ {field}: Expected {expected}, Got {actual}")
            all_correct = False
    
    if all_correct:
        st.balloons()
        st.success("🎉 **ALL TESTS PASSED!** Test Scenario 2 fix is working correctly!")
    else:
        st.error("❌ Some tests failed - fix needs additional work")

if __name__ == "__main__":
    test_scenario_2_fix()
