#!/usr/bin/env python3
"""
Debug script to test preprocessing components loading
"""

import os
import pickle
import sys

def test_preprocessing_load():
    """Test loading preprocessing components"""
    
    print("=== Debugging Preprocessing Components Loading ===")
    print(f"Current working directory: {os.getcwd()}")
    
    # Test the exact path used in the app
    preprocessing_path = "src/models/preprocessing_components.pkl"
    
    print(f"\nTesting path: {preprocessing_path}")
    print(f"File exists: {os.path.exists(preprocessing_path)}")
    
    if os.path.exists(preprocessing_path):
        print(f"File size: {os.path.getsize(preprocessing_path)} bytes")
        
        try:
            # Try to load the file
            with open(preprocessing_path, 'rb') as f:
                preprocessing_data = pickle.load(f)
            
            print("✅ Successfully loaded preprocessing components!")
            print(f"Type: {type(preprocessing_data)}")
            
            if isinstance(preprocessing_data, dict):
                print(f"Keys: {list(preprocessing_data.keys())}")
                
                # Check each component
                for key, value in preprocessing_data.items():
                    print(f"  {key}: {type(value)}")
                    
                    # Special handling for label_encoders
                    if key == 'label_encoders' and isinstance(value, dict):
                        print(f"    Label encoders count: {len(value)}")
                        if len(value) > 0:
                            print(f"    Sample encoder keys: {list(value.keys())[:5]}")
                    
                    # Special handling for imputer
                    if key == 'imputer':
                        print(f"    Imputer strategy: {getattr(value, 'strategy', 'unknown')}")
                        print(f"    Imputer features: {getattr(value, 'n_features_in_', 'unknown')}")
            
            return True, preprocessing_data
            
        except Exception as e:
            print(f"❌ Error loading preprocessing components: {e}")
            print(f"Error type: {type(e)}")
            return False, str(e)
    else:
        print("❌ File does not exist")
        return False, "File not found"

def test_absolute_path():
    """Test with absolute path"""
    print("\n=== Testing with absolute path ===")
    
    abs_path = os.path.abspath("src/models/preprocessing_components.pkl")
    print(f"Absolute path: {abs_path}")
    print(f"File exists: {os.path.exists(abs_path)}")
    
    if os.path.exists(abs_path):
        try:
            with open(abs_path, 'rb') as f:
                preprocessing_data = pickle.load(f)
            print("✅ Successfully loaded with absolute path!")
            return True, preprocessing_data
        except Exception as e:
            print(f"❌ Error with absolute path: {e}")
            return False, str(e)
    else:
        return False, "File not found with absolute path"

def test_from_app_pages_context():
    """Test from app_pages directory context (simulating Streamlit app)"""
    print("\n=== Testing from app_pages context ===")
    
    # Change to app_pages directory to simulate Streamlit context
    original_cwd = os.getcwd()
    
    try:
        # Simulate being in app_pages directory
        app_pages_path = os.path.join(original_cwd, "app_pages")
        if os.path.exists(app_pages_path):
            os.chdir(app_pages_path)
            print(f"Changed to: {os.getcwd()}")
            
            # Test relative path from app_pages
            preprocessing_path = "../src/models/preprocessing_components.pkl"
            print(f"Testing path: {preprocessing_path}")
            print(f"File exists: {os.path.exists(preprocessing_path)}")
            
            if os.path.exists(preprocessing_path):
                try:
                    with open(preprocessing_path, 'rb') as f:
                        preprocessing_data = pickle.load(f)
                    print("✅ Successfully loaded from app_pages context!")
                    return True, preprocessing_data
                except Exception as e:
                    print(f"❌ Error from app_pages context: {e}")
                    return False, str(e)
            else:
                return False, "File not found from app_pages context"
        else:
            print("app_pages directory not found")
            return False, "app_pages directory not found"
            
    finally:
        # Always return to original directory
        os.chdir(original_cwd)

if __name__ == "__main__":
    print("Starting preprocessing components debug test...")
    
    # Test 1: From root directory
    success1, result1 = test_preprocessing_load()
    
    # Test 2: With absolute path
    success2, result2 = test_absolute_path()
    
    # Test 3: From app_pages context
    success3, result3 = test_from_app_pages_context()
    
    print("\n=== SUMMARY ===")
    print(f"Root directory test: {'✅ PASS' if success1 else '❌ FAIL'}")
    print(f"Absolute path test: {'✅ PASS' if success2 else '❌ FAIL'}")
    print(f"App pages context test: {'✅ PASS' if success3 else '❌ FAIL'}")
    
    if not any([success1, success2, success3]):
        print("\n❌ All tests failed!")
        print("This indicates a serious issue with the preprocessing components file.")
    else:
        print("\n✅ At least one test passed - the file is loadable.")
        
        # If any test passed, show the working solution
        if success1:
            print("✅ Recommended solution: Use relative path from root directory")
        elif success2:
            print("✅ Recommended solution: Use absolute path")
        elif success3:
            print("✅ Recommended solution: Use relative path from app_pages directory")
