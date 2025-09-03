# -*- coding: utf-8 -*-
"""
Minimal test script to isolate the import issue
"""

def test_basic_imports():
    """Test basic imports that should work"""
    try:
        import streamlit as st
        print("✅ Streamlit import successful")
        
        import pandas as pd
        print("✅ Pandas import successful")
        
        import numpy as np
        print("✅ Numpy import successful")
        
        return True
    except Exception as e:
        print(f"❌ Basic imports failed: {e}")
        return False

def test_app_page_imports():
    """Test app page imports"""
    try:
        import sys
        import os
        sys.path.append('.')
        sys.path.append('app_pages')
        
        # Test the problematic import
        from app_pages.four_interactive_prediction import interactive_prediction_body
        print("✅ Interactive prediction import successful")
        
        return True
    except SyntaxError as e:
        print(f"❌ Syntax error in interactive prediction: {e}")
        print(f"   Line {e.lineno}: {e.text}")
        return False
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Other error: {e}")
        return False

def interactive_prediction_body():
    """Minimal placeholder function"""
    return "Test function"

if __name__ == "__main__":
    print("🔍 Testing imports...")
    
    if test_basic_imports():
        print("\n🔍 Testing app page imports...")
        test_app_page_imports()
    
    print("\n✅ Test completed")
