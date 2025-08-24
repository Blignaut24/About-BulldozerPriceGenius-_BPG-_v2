#!/usr/bin/env python3
"""
Test the specific preprocessing logic that's causing the fallback messages.
"""

import os
import sys
import warnings
import pickle
import pandas as pd

# Suppress Streamlit warnings for testing
warnings.filterwarnings("ignore")
os.environ["STREAMLIT_SERVER_HEADLESS"] = "true"

# Add app_pages to path for imports
sys.path.insert(0, 'app_pages')
sys.path.insert(0, 'src')

def test_preprocessing_logic_directly():
    """Test the preprocessing logic directly without Streamlit context."""
    print("🧪 Testing Preprocessing Logic Directly")
    print("=" * 40)
    
    # Test data similar to Test Scenario 1
    input_data = pd.DataFrame({
        'YearMade': [1994],
        'ProductSize': ['Large'],
        'state': ['California'],
        'Enclosure': ['EROPS w AC'],
        'fiBaseModel': ['D8'],
        'Coupler_System': ['Hydraulic'],
        'Tire_Size': ['26.5R25'],
        'Hydraulics_Flow': ['High Flow'],
        'Grouser_Tracks': ['Double'],
        'Hydraulics': ['4 Valve'],
        'SaleYear': [2005],
        'saledate': [180]
    })
    
    print(f"📊 Input data shape: {input_data.shape}")
    print(f"📋 Input columns: {list(input_data.columns)}")
    
    # Test preprocessing components loading
    preprocessing_path = "src/models/preprocessing_components.pkl"
    print(f"\n📁 Testing preprocessing file: {preprocessing_path}")
    print(f"📊 File exists: {os.path.exists(preprocessing_path)}")
    
    if os.path.exists(preprocessing_path):
        try:
            with open(preprocessing_path, 'rb') as f:
                preprocessing_data = pickle.load(f)
            
            print(f"✅ File loaded successfully")
            print(f"📋 Data type: {type(preprocessing_data)}")
            print(f"🔑 Keys: {list(preprocessing_data.keys())}")
            
            # Test the preprocessing logic
            if 'label_encoders' in preprocessing_data and 'imputer' in preprocessing_data:
                label_encoders = preprocessing_data['label_encoders']
                imputer = preprocessing_data['imputer']
                
                print(f"📊 Label encoders type: {type(label_encoders)}")
                print(f"📊 Imputer type: {type(imputer)}")
                
                if isinstance(label_encoders, dict):
                    print(f"📊 Number of label encoders: {len(label_encoders)}")
                    print(f"🔑 Label encoder keys: {list(label_encoders.keys())}")
                
                # Try to apply preprocessing
                try:
                    print(f"\n🔧 Applying preprocessing...")
                    
                    # Step 1: Apply label encoding
                    input_encoded = input_data.copy()
                    
                    for column in input_encoded.columns:
                        if input_encoded[column].dtype == 'object':
                            if column in label_encoders:
                                encoder = label_encoders[column]
                                print(f"   Encoding {column} with {type(encoder).__name__}")
                                try:
                                    input_encoded[column] = encoder.transform(input_encoded[column])
                                except Exception as e:
                                    print(f"   ⚠️ Encoding failed for {column}: {e}")
                                    # Use label encoding fallback
                                    unique_values = input_encoded[column].unique()
                                    value_map = {val: idx for idx, val in enumerate(unique_values)}
                                    input_encoded[column] = input_encoded[column].map(value_map)
                            else:
                                print(f"   No encoder for {column}, using label encoding")
                                unique_values = input_encoded[column].unique()
                                value_map = {val: idx for idx, val in enumerate(unique_values)}
                                input_encoded[column] = input_encoded[column].map(value_map)
                    
                    print(f"✅ Label encoding completed")
                    print(f"📊 Encoded data shape: {input_encoded.shape}")
                    
                    # Step 2: Apply imputation
                    print(f"🔧 Applying imputation...")
                    input_final = pd.DataFrame(
                        imputer.transform(input_encoded),
                        columns=input_encoded.columns
                    )
                    
                    print(f"✅ Enhanced ML preprocessing applied successfully")
                    print(f"📊 Final data shape: {input_final.shape}")
                    print(f"📊 Final data types: {input_final.dtypes.to_dict()}")
                    
                    return True, "Enhanced ML preprocessing applied successfully"
                    
                except Exception as e:
                    print(f"❌ Preprocessing failed: {e}")
                    import traceback
                    traceback.print_exc()
                    return False, f"Enhanced preprocessing unavailable: {e}"
            else:
                print(f"❌ Missing required components in preprocessing data")
                return False, "Missing label_encoders or imputer"
                
        except Exception as e:
            print(f"❌ Failed to load preprocessing file: {e}")
            return False, f"Preprocessing components file error: {e}"
    else:
        print(f"❌ Preprocessing file does not exist")
        return False, "Preprocessing components file not found"

def test_with_streamlit_context():
    """Test with Streamlit context to see actual messages."""
    print("\n🧪 Testing with Streamlit Context")
    print("=" * 35)
    
    try:
        import streamlit as st
        
        # Mock Streamlit functions to capture messages
        messages = []
        
        def mock_success(msg):
            messages.append(('SUCCESS', msg))
            print(f"✅ SUCCESS: {msg}")
        
        def mock_warning(msg):
            messages.append(('WARNING', msg))
            print(f"⚠️ WARNING: {msg}")
        
        def mock_info(msg):
            messages.append(('INFO', msg))
            print(f"ℹ️ INFO: {msg}")
        
        # Replace Streamlit functions
        original_success = st.success
        original_warning = st.warning
        original_info = st.info
        
        st.success = mock_success
        st.warning = mock_warning
        st.info = mock_info
        
        try:
            # Test the actual preprocessing logic
            success, message = test_preprocessing_logic_directly()
            
            print(f"\n📊 Captured Streamlit messages:")
            for msg_type, msg_content in messages:
                print(f"   {msg_type}: {msg_content}")
            
            return success, messages
            
        finally:
            # Restore original functions
            st.success = original_success
            st.warning = original_warning
            st.info = original_info
            
    except Exception as e:
        print(f"❌ Streamlit context test failed: {e}")
        return False, []

def main():
    """Run preprocessing logic tests."""
    print("BulldozerPriceGenius - Preprocessing Logic Test")
    print("=" * 50)
    print("Testing the specific preprocessing logic causing fallback messages")
    print()
    
    # Test direct logic
    success1, message1 = test_preprocessing_logic_directly()
    
    # Test with Streamlit context
    success2, messages2 = test_with_streamlit_context()
    
    print("\n" + "=" * 50)
    print("📊 Test Results:")
    print(f"   Direct preprocessing test: {'✅ PASS' if success1 else '❌ FAIL'}")
    print(f"   Message: {message1}")
    print(f"   Streamlit context test: {'✅ PASS' if success2 else '❌ FAIL'}")
    
    if success1 and success2:
        print("\n🎉 Preprocessing logic is working correctly!")
        print("✅ Enhanced ML preprocessing should be available")
        print("✅ No fallback to basic preprocessing should occur")
    else:
        print("\n⚠️ Issues found in preprocessing logic")
        if not success1:
            print(f"• Direct test failed: {message1}")
        if not success2:
            print("• Streamlit context test failed")
    
    return success1 and success2

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
