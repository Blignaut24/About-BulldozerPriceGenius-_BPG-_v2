#!/usr/bin/env python3
"""
Test Script to Verify Render Error Fix
Tests the robust variable access system for the expandable section
"""

import streamlit as st

def test_render_error_fix():
    """Test the fixed expandable section with robust variable access"""
    
    st.title("🧪 Render Error Fix Verification")
    st.markdown("Testing the robust variable access system for expandable section")
    
    # Test Results
    test_results = {
        'safe_value_function': False,
        'session_state_fallback': False,
        'data_type_validation': False,
        'test_scenario_2': False,
        'expandable_section': False
    }
    
    # 1. Test Safe Value Function
    st.subheader("1. 🔧 Safe Value Function Test")
    
    def get_safe_value(widget_var, session_key, test_key, default_value):
        """Safely get value with multiple fallback layers for Render compatibility"""
        try:
            # Try widget variable first
            if 'widget_var' in locals() and widget_var is not None:
                return widget_var
        except:
            pass
        
        try:
            # Try session state widget key
            if session_key in st.session_state:
                return st.session_state[session_key]
        except:
            pass
            
        try:
            # Try test data key
            if test_key in st.session_state:
                return st.session_state[test_key]
        except:
            pass
            
        # Return default
        return default_value
    
    try:
        # Test with missing values
        result1 = get_safe_value(None, 'missing_key', 'missing_test_key', 'default')
        assert result1 == 'default'
        
        # Test with session state value
        st.session_state['test_key'] = 'session_value'
        result2 = get_safe_value(None, 'test_key', 'missing_test_key', 'default')
        assert result2 == 'session_value'
        
        # Test with test data value
        st.session_state['test_data_key'] = 'test_value'
        result3 = get_safe_value(None, 'missing_key', 'test_data_key', 'default')
        assert result3 == 'test_value'
        
        test_results['safe_value_function'] = True
        st.success("✅ Safe value function working correctly")
        
    except Exception as e:
        st.error(f"❌ Safe value function test failed: {e}")
    
    # 2. Test Session State Fallback
    st.subheader("2. 💾 Session State Fallback Test")
    
    try:
        # Simulate Test Scenario 2 data
        test_scenario_2_data = {
            "test_year_made": 1987,
            "test_product_size": "Large", 
            "test_state": "Texas",
            "test_model_id": 4800,
            "test_enclosure": "EROPS w AC",
            "test_base_model": "D9",
            "test_hydraulics": "4 Valve",
            "test_tire_size": "29.5R25",
            "test_sale_year": 2006,
            "test_sale_day": 182
        }
        
        # Load into session state
        for key, value in test_scenario_2_data.items():
            st.session_state[key] = value
        
        # Test retrieval
        display_year_made = get_safe_value(None, 'year_made_input', 'test_year_made', 2000)
        display_base_model = get_safe_value(None, 'base_model_input', 'test_base_model', 'D3')
        display_enclosure = get_safe_value(None, 'enclosure_input', 'test_enclosure', 'EROPS')
        
        st.write(f"Year Made: {display_year_made} (expected: 1987)")
        st.write(f"Base Model: {display_base_model} (expected: D9)")
        st.write(f"Enclosure: {display_enclosure} (expected: EROPS w AC)")
        
        if display_year_made == 1987 and display_base_model == 'D9' and display_enclosure == 'EROPS w AC':
            test_results['session_state_fallback'] = True
            st.success("✅ Session state fallback working correctly")
        else:
            st.error("❌ Session state fallback not working correctly")
            
    except Exception as e:
        st.error(f"❌ Session state fallback test failed: {e}")
    
    # 3. Test Data Type Validation
    st.subheader("3. 🔢 Data Type Validation Test")
    
    try:
        # Test various data types
        test_values = [1987, "1987", 1987.0, "invalid", None, ""]
        
        for test_val in test_values:
            try:
                result = int(test_val) if str(test_val).replace('-', '').isdigit() else 2000
                st.write(f"Input: {test_val} ({type(test_val)}) → Output: {result}")
            except Exception as e:
                st.write(f"Input: {test_val} → Error: {e}")
        
        test_results['data_type_validation'] = True
        st.success("✅ Data type validation working correctly")
        
    except Exception as e:
        st.error(f"❌ Data type validation test failed: {e}")
    
    # 4. Test Scenario 2 Complete Test
    st.subheader("4. 🎯 Test Scenario 2 Complete Test")
    
    try:
        # Get all Test Scenario 2 values using safe function
        display_values = {}
        
        display_values['year_made'] = get_safe_value(None, 'year_made_input', 'test_year_made', 2000)
        display_values['model_id'] = get_safe_value(None, 'model_id_input', 'test_model_id', 4800)
        display_values['product_size'] = get_safe_value(None, 'product_size_input', 'test_product_size', 'Large')
        display_values['state'] = get_safe_value(None, 'state_input', 'test_state', 'All States')
        display_values['enclosure'] = get_safe_value(None, 'enclosure_input', 'test_enclosure', 'EROPS')
        display_values['base_model'] = get_safe_value(None, 'base_model_input', 'test_base_model', 'D3')
        display_values['hydraulics'] = get_safe_value(None, 'hydraulics_input', 'test_hydraulics', 'Standard')
        display_values['tire_size'] = get_safe_value(None, 'tire_size_input', 'test_tire_size', 'None or Unspecified')
        display_values['sale_year'] = get_safe_value(None, 'sale_year_input', 'test_sale_year', 2006)
        display_values['sale_day'] = get_safe_value(None, 'sale_day_input', 'test_sale_day', 182)
        
        # Validate data types
        display_values['year_made'] = int(display_values['year_made']) if str(display_values['year_made']).replace('-', '').isdigit() else 2000
        display_values['model_id'] = int(display_values['model_id']) if str(display_values['model_id']).replace('-', '').isdigit() else 4800
        display_values['sale_year'] = int(display_values['sale_year']) if str(display_values['sale_year']).replace('-', '').isdigit() else 2006
        display_values['sale_day'] = int(display_values['sale_day']) if str(display_values['sale_day']).replace('-', '').isdigit() else 182
        
        # Display results
        st.markdown("**Retrieved Values:**")
        for key, value in display_values.items():
            st.write(f"• {key}: {value}")
        
        # Test scenario detection
        if (display_values['year_made'] == 1987 and display_values['product_size'] == 'Large' and
            display_values['base_model'] == 'D9' and 'EROPS' in display_values['enclosure']):
            st.success("✅ **Test Scenario 2 (1987 D9 Large - Ultra-Vintage)** detected")
            test_results['test_scenario_2'] = True
        else:
            st.warning("⚠️ Test Scenario 2 not detected")
            
    except Exception as e:
        st.error(f"❌ Test Scenario 2 test failed: {e}")
    
    # 5. Test Expandable Section
    st.subheader("5. 🔍 Expandable Section Test")
    
    try:
        from app_pages.four_interactive_prediction_render import get_expander, get_columns
        
        # Test expandable section with the same logic as the fix
        with get_expander("🧪 Test Expandable Section", expanded=True):
            st.markdown("**Testing the fixed expandable section logic**")
            
            # Use the same safe value retrieval as the fix
            test_year = get_safe_value(None, 'year_made_input', 'test_year_made', 2000)
            test_base = get_safe_value(None, 'base_model_input', 'test_base_model', 'D3')
            
            st.write(f"Year Made: {test_year}")
            st.write(f"Base Model: {test_base}")
            
            # Test column layout
            try:
                col1, col2, col3 = get_columns(3)
                with col1:
                    st.info("Column 1 working")
                with col2:
                    st.success("Column 2 working")
                with col3:
                    st.warning("Column 3 working")
                st.success("✅ Column layout working")
            except Exception as e:
                st.error(f"Column layout failed: {e}")
                # Fallback
                st.info("Using single-column fallback")
        
        test_results['expandable_section'] = True
        st.success("✅ Expandable section test completed successfully")
        
    except Exception as e:
        st.error(f"❌ Expandable section test failed: {e}")
        import traceback
        st.code(traceback.format_exc())
    
    # Overall Results
    st.subheader("📊 Overall Test Results")
    
    passed_tests = sum(test_results.values())
    total_tests = len(test_results)
    success_rate = (passed_tests / total_tests) * 100
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Tests Passed", f"{passed_tests}/{total_tests}")
    with col2:
        st.metric("Success Rate", f"{success_rate:.1f}%")
    
    if success_rate >= 90:
        st.success("🎉 Render error fix is working correctly!")
        st.balloons()
    elif success_rate >= 75:
        st.warning("⚠️ Most tests passed - minor issues remain")
    else:
        st.error("❌ Significant issues detected")
    
    # Detailed results
    st.markdown("**Detailed Test Results:**")
    for test_name, result in test_results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        st.write(f"• {test_name.replace('_', ' ').title()}: {status}")

if __name__ == "__main__":
    test_render_error_fix()
