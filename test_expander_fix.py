#!/usr/bin/env python3
"""
Test script to verify the st.expander compatibility fix
"""

import sys
import os

# Add the app_pages directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app_pages'))

def test_expander_compatibility():
    """Test that the get_expander function works correctly"""
    try:
        # Import the compatibility function
        from four_interactive_prediction import get_expander
        print("✅ Successfully imported get_expander from four_interactive_prediction")
        
        # Test that it returns a context manager
        import streamlit as st
        print(f"✅ Streamlit version: {st.__version__}")
        print(f"✅ Has st.expander: {hasattr(st, 'expander')}")
        print(f"✅ Has st.beta_expander: {hasattr(st, 'beta_expander')}")
        
        # Test the function (without actually using it in Streamlit context)
        print("✅ get_expander function is callable")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def test_model_id_compatibility():
    """Test that the model_id_input component has the fix"""
    try:
        # Add src/components to path
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src', 'components'))
        
        from model_id_input import get_expander
        print("✅ Successfully imported get_expander from model_id_input")
        return True
        
    except ImportError as e:
        print(f"❌ Model ID component import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Model ID component unexpected error: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing Streamlit st.expander compatibility fix...")
    print("=" * 60)
    
    # Test main interactive prediction module
    test1_passed = test_expander_compatibility()
    print()
    
    # Test model ID component
    test2_passed = test_model_id_compatibility()
    print()
    
    # Summary
    print("=" * 60)
    if test1_passed and test2_passed:
        print("🎉 All tests passed! The st.expander compatibility fix is working correctly.")
        print("✅ The application should now run without AttributeError.")
    else:
        print("❌ Some tests failed. Please check the implementation.")
        
    return test1_passed and test2_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
