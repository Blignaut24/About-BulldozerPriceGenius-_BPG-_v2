#!/usr/bin/env python3
"""
Debug script to reproduce Test Scenario 1 and identify preprocessing issues.
"""

import os
import sys
import warnings

# Suppress Streamlit warnings for testing
warnings.filterwarnings("ignore")
os.environ["STREAMLIT_SERVER_HEADLESS"] = "true"

# Add app_pages to path for imports
sys.path.insert(0, 'app_pages')
sys.path.insert(0, 'src')

def debug_preprocessing_components():
    """Debug the preprocessing components loading."""
    print("🔍 Debugging Preprocessing Components Loading")
    print("=" * 50)
    
    preprocessing_path = "src/models/preprocessing_components.pkl"
    
    print(f"📁 File path: {preprocessing_path}")
    print(f"📊 File exists: {os.path.exists(preprocessing_path)}")
    
    if os.path.exists(preprocessing_path):
        file_size = os.path.getsize(preprocessing_path)
        print(f"📊 File size: {file_size:,} bytes")
        
        try:
            import pickle
            with open(preprocessing_path, 'rb') as f:
                preprocessing_data = pickle.load(f)
            print(f"✅ File loads successfully")
            print(f"📋 Data type: {type(preprocessing_data)}")
            if isinstance(preprocessing_data, dict):
                print(f"🔑 Keys: {list(preprocessing_data.keys())}")
            return preprocessing_data
        except Exception as e:
            print(f"❌ Failed to load: {e}")
            return None
    else:
        print("❌ File does not exist")
        return None

def debug_external_model_loader():
    """Debug the external model loader."""
    print("\n🔍 Debugging External Model Loader")
    print("=" * 40)
    
    try:
        from external_model_loader import ExternalModelLoader
        
        loader = ExternalModelLoader()
        print(f"📁 Loader preprocessing path: {loader.preprocessing_path}")
        
        # Try to load model and preprocessing data
        print("🌐 Loading model and preprocessing data...")
        model, preprocessing_data, error = loader.load_model_from_google_drive()
        
        print(f"📊 Model loaded: {model is not None}")
        print(f"📊 Preprocessing data loaded: {preprocessing_data is not None}")
        
        if error:
            print(f"⚠️ Error: {error}")
        
        if preprocessing_data:
            print(f"📋 Preprocessing data type: {type(preprocessing_data)}")
            if isinstance(preprocessing_data, dict):
                print(f"🔑 Keys: {list(preprocessing_data.keys())}")
        
        return model, preprocessing_data, error
        
    except Exception as e:
        print(f"❌ External model loader failed: {e}")
        import traceback
        traceback.print_exc()
        return None, None, str(e)

def test_scenario_1_prediction():
    """Test Test Scenario 1 prediction with debugging."""
    print("\n🧪 Testing Scenario 1 Prediction")
    print("=" * 35)
    
    try:
        from four_interactive_prediction import make_prediction, external_model_loader
        
        # Load model and preprocessing data
        print("🌐 Loading model and preprocessing data...")
        model, preprocessing_data, error = external_model_loader.load_model_from_google_drive()
        
        if model is None:
            print(f"❌ Model loading failed: {error}")
            return False
        
        print(f"✅ Model loaded: {type(model)}")
        print(f"📊 Preprocessing data: {preprocessing_data is not None}")
        
        if preprocessing_data:
            print(f"📋 Preprocessing data keys: {list(preprocessing_data.keys()) if isinstance(preprocessing_data, dict) else 'Not a dict'}")
        
        # Test Scenario 1 configuration
        config = {
            'year_made': 1994,
            'model_id': 4200,
            'product_size': 'Large',
            'state': 'California',
            'enclosure': 'EROPS w AC',
            'fi_base_model': 'D8',
            'coupler_system': 'Hydraulic',
            'tire_size': '26.5R25',
            'hydraulics_flow': 'High Flow',
            'grouser_tracks': 'Double',
            'hydraulics': '4 Valve',
            'sale_year': 2005,
            'sale_day_of_year': 180
        }
        
        print("\n📋 Running Test Scenario 1 prediction...")
        print("Configuration:")
        for key, value in config.items():
            print(f"   {key}: {value}")
        
        # Capture Streamlit output by redirecting
        import io
        from contextlib import redirect_stdout, redirect_stderr
        
        stdout_capture = io.StringIO()
        stderr_capture = io.StringIO()
        
        with redirect_stdout(stdout_capture), redirect_stderr(stderr_capture):
            result = make_prediction(
                model=model,
                preprocessing_data=preprocessing_data,
                **config
            )
        
        # Print captured output
        stdout_output = stdout_capture.getvalue()
        stderr_output = stderr_capture.getvalue()
        
        if stdout_output:
            print(f"\n📝 Stdout output:\n{stdout_output}")
        if stderr_output:
            print(f"\n⚠️ Stderr output:\n{stderr_output}")
        
        if result and result.get('success', False):
            print(f"\n✅ Prediction successful!")
            print(f"   Price: ${result['predicted_price']:,.2f}")
            print(f"   Confidence: {result['confidence_level']*100:.1f}%")
            print(f"   Method: {result.get('method', 'Unknown')}")
            return True
        else:
            print(f"\n❌ Prediction failed: {result.get('error', 'Unknown error') if result else 'No result'}")
            return False
            
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Run comprehensive debugging."""
    print("BulldozerPriceGenius - Test Scenario 1 Preprocessing Debug")
    print("=" * 60)
    print("Investigating preprocessing components error")
    print()
    
    # Debug steps
    preprocessing_data = debug_preprocessing_components()
    model, ext_preprocessing_data, error = debug_external_model_loader()
    test_success = test_scenario_1_prediction()
    
    print("\n" + "=" * 60)
    print("📊 Debug Summary:")
    print(f"   Preprocessing file exists: {'✅' if preprocessing_data else '❌'}")
    print(f"   External loader works: {'✅' if model else '❌'}")
    print(f"   External preprocessing data: {'✅' if ext_preprocessing_data else '❌'}")
    print(f"   Test Scenario 1 prediction: {'✅' if test_success else '❌'}")
    
    if not test_success:
        print("\n🔍 Potential Issues:")
        if not preprocessing_data:
            print("• Preprocessing components file cannot be loaded")
        if not ext_preprocessing_data:
            print("• External model loader not providing preprocessing data")
        if error:
            print(f"• External loader error: {error}")
    
    return test_success

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
