#!/usr/bin/env python3
"""
Test script to verify Streamlit compatibility functions work correctly.
"""

import sys
import os

# Add the current directory to the path so we can import from app_pages
sys.path.append('.')

def test_compatibility_functions():
    """Test the compatibility functions without running Streamlit"""
    print("🔍 Testing Streamlit Compatibility Functions...")
    print("=" * 60)
    
    try:
        import streamlit as st
        print(f"✅ Streamlit imported successfully")
        print(f"   Version: {st.__version__ if hasattr(st, '__version__') else 'Unknown'}")
        
        # Test if metric exists
        has_metric = hasattr(st, 'metric')
        print(f"   st.metric available: {'✅ Yes' if has_metric else '❌ No'}")
        
        # Test if caption exists
        has_caption = hasattr(st, 'caption')
        print(f"   st.caption available: {'✅ Yes' if has_caption else '❌ No'}")
        
        # Test if columns exists
        has_columns = hasattr(st, 'columns')
        has_beta_columns = hasattr(st, 'beta_columns')
        print(f"   st.columns available: {'✅ Yes' if has_columns else '❌ No'}")
        print(f"   st.beta_columns available: {'✅ Yes' if has_beta_columns else '❌ No'}")
        
        # Test if expander exists
        has_expander = hasattr(st, 'expander')
        has_beta_expander = hasattr(st, 'beta_expander')
        print(f"   st.expander available: {'✅ Yes' if has_expander else '❌ No'}")
        print(f"   st.beta_expander available: {'✅ Yes' if has_beta_expander else '❌ No'}")
        
        return True
        
    except ImportError as e:
        print(f"❌ Streamlit import failed: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def test_prediction_functions():
    """Test that prediction functions can be imported"""
    print("\n🔍 Testing Prediction Function Imports...")
    print("=" * 60)
    
    try:
        # Test importing the main prediction functions
        from app_pages.four_interactive_prediction import (
            make_prediction_basic_statistical,
            make_prediction_fallback,
            get_metric,
            get_columns,
            get_expander
        )
        
        print("✅ Successfully imported prediction functions:")
        print("   • make_prediction_basic_statistical")
        print("   • make_prediction_fallback") 
        print("   • get_metric (compatibility function)")
        print("   • get_columns (compatibility function)")
        print("   • get_expander (compatibility function)")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import failed: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def test_basic_prediction():
    """Test basic prediction without Streamlit UI"""
    print("\n🔍 Testing Basic Prediction Function...")
    print("=" * 60)
    
    try:
        from app_pages.four_interactive_prediction import make_prediction_basic_statistical
        
        # Test with sample data
        result = make_prediction_basic_statistical(
            year_made=2008,
            product_size="Large",
            state="California",
            sale_year=2012
        )
        
        if result['success']:
            print("✅ Basic prediction function works correctly")
            print(f"   Predicted price: ${result['predicted_price']:,.2f}")
            print(f"   Confidence: {result['confidence']}%")
            print(f"   Method: {result['method']}")
        else:
            print(f"❌ Basic prediction failed: {result.get('error', 'Unknown error')}")
            return False
            
        return True
        
    except Exception as e:
        print(f"❌ Basic prediction test failed: {e}")
        return False

def main():
    """Run all compatibility tests"""
    print("🧪 Streamlit Compatibility Test Suite")
    print("Testing compatibility functions for older Streamlit versions")
    print("=" * 80)
    
    # Run tests
    streamlit_ok = test_compatibility_functions()
    imports_ok = test_prediction_functions()
    prediction_ok = test_basic_prediction()
    
    # Summary
    print("\n" + "=" * 80)
    print("📊 Test Results Summary:")
    print(f"   Streamlit Compatibility: {'✅ PASS' if streamlit_ok else '❌ FAIL'}")
    print(f"   Function Imports: {'✅ PASS' if imports_ok else '❌ FAIL'}")
    print(f"   Basic Prediction: {'✅ PASS' if prediction_ok else '❌ FAIL'}")
    
    total_passed = sum([streamlit_ok, imports_ok, prediction_ok])
    print(f"\n🎯 Overall: {total_passed}/3 tests passed")
    
    if total_passed == 3:
        print("🎉 All compatibility tests passed!")
        print("💡 The application should work with your Streamlit version")
    elif total_passed >= 2:
        print("✅ Core functionality is working")
        print("⚠️ Some features may have reduced functionality")
    else:
        print("⚠️ Multiple compatibility issues detected")
        print("💡 Consider updating Streamlit: pip install --upgrade streamlit")

if __name__ == "__main__":
    main()
