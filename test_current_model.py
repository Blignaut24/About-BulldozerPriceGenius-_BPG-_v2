#!/usr/bin/env python3
"""
Test script to verify the current model loading behavior and fallback system.
This will help us understand what's working and what needs improvement.
"""

import pickle
import numpy as np
import os
import sys

def test_model_loading():
    """Test the current model loading behavior"""
    print("🔍 Testing Current Model Loading Behavior")
    print("=" * 60)
    
    model_path = "src/models/randomforest_regressor_best_RMSLE.pkl"
    
    # Check if model file exists
    if not os.path.exists(model_path):
        print(f"❌ Model file not found at: {model_path}")
        return False
    
    print(f"✅ Model file found: {model_path}")
    print(f"📁 File size: {os.path.getsize(model_path):,} bytes")
    
    # Try to load the model
    try:
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        
        print(f"✅ Model loaded successfully")
        print(f"📊 Object type: {type(model)}")
        
        # Check if it has predict method
        has_predict = hasattr(model, 'predict')
        print(f"🎯 Has predict method: {has_predict}")
        
        if isinstance(model, np.ndarray):
            print(f"📐 Array shape: {model.shape}")
            print(f"📋 Array dtype: {model.dtype}")
            if len(model) > 0:
                print(f"🔍 First few elements: {model[:3]}")
        
        # Test prediction capability
        if has_predict:
            print("✅ Model can make predictions - ML model is working!")
            return True
        else:
            print("⚠️ Model cannot make predictions - fallback system will be used")
            return False
            
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return False

def test_fallback_system():
    """Test the intelligent fallback system"""
    print("\n🧠 Testing Intelligent Fallback System")
    print("=" * 60)
    
    # Import the fallback function from the prediction page
    sys.path.append('app_pages')
    
    try:
        from four_interactive_prediction import make_prediction_fallback
        
        # Test with sample data
        test_result = make_prediction_fallback(
            year_made=2005,
            model_id=4605,
            product_size="Medium",
            state="California",
            enclosure="EROPS",
            fi_base_model="D7",
            coupler_system="None or Unspecified",
            tire_size="None or Unspecified",
            hydraulics_flow="Standard",
            grouser_tracks="None or Unspecified",
            hydraulics="Standard",
            sale_year=2008,
            sale_day_of_year=182
        )
        
        if test_result['success']:
            print("✅ Fallback system working correctly!")
            print(f"💰 Predicted price: ${test_result['predicted_price']:,.2f}")
            print(f"📊 Confidence level: {test_result['confidence_level']:.1%}")
            print(f"📈 Price range: ${test_result['confidence_lower']:,.0f} - ${test_result['confidence_upper']:,.0f}")
            return True
        else:
            print(f"❌ Fallback system failed: {test_result.get('error', 'Unknown error')}")
            return False
            
    except ImportError as e:
        print(f"❌ Could not import fallback system: {e}")
        return False
    except Exception as e:
        print(f"❌ Error testing fallback system: {e}")
        return False

def main():
    """Main test function"""
    print("🚜 Bulldozer Price Prediction - Model Testing")
    print("=" * 80)
    
    # Test model loading
    model_works = test_model_loading()
    
    # Test fallback system
    fallback_works = test_fallback_system()
    
    # Summary
    print("\n📋 Test Summary")
    print("=" * 60)
    
    if model_works:
        print("🤖 ML Model Status: ✅ Working (predictions will use trained model)")
    else:
        print("🤖 ML Model Status: ❌ Not working (will use fallback)")
    
    if fallback_works:
        print("🧠 Fallback System: ✅ Working (intelligent statistical predictions)")
    else:
        print("🧠 Fallback System: ❌ Not working")
    
    print("\n🎯 Overall Status:")
    if model_works:
        print("✅ EXCELLENT: ML model is working - highest accuracy predictions available")
    elif fallback_works:
        print("✅ GOOD: Fallback system is working - reliable predictions available")
    else:
        print("❌ PROBLEM: Neither system is working - predictions may fail")
    
    print("\n💡 Next Steps:")
    if not model_works and fallback_works:
        print("• The app will work well with the intelligent fallback system")
        print("• Users will see clear notifications about prediction method")
        print("• Consider fixing the ML model for even higher accuracy")
    elif model_works:
        print("• The app will work excellently with the ML model")
        print("• Users will get the highest accuracy predictions")
    else:
        print("• Both systems need attention - check error messages above")

if __name__ == "__main__":
    main()
