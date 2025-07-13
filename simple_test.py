#!/usr/bin/env python3
"""
Simple test script that can run without external dependencies.
Tests basic functionality and file structure.
"""

import os
import sys

def test_file_structure():
    """Test that all required files exist"""
    print("📁 Testing File Structure")
    print("=" * 50)
    
    required_files = [
        "app.py",
        "app_pages/four_interactive_prediction.py",
        "src/models/randomforest_regressor_best_RMSLE.pkl",
        "src/data_prep/TrainAndValid_object_values_as_categories_and_missing_values_filled.parquet"
    ]
    
    all_files_exist = True
    
    for file_path in required_files:
        if os.path.exists(file_path):
            size = os.path.getsize(file_path)
            print(f"✅ {file_path} ({size:,} bytes)")
        else:
            print(f"❌ {file_path} - NOT FOUND")
            all_files_exist = False
    
    return all_files_exist

def test_model_file():
    """Test the model file specifically"""
    print("\n🤖 Testing Model File")
    print("=" * 50)
    
    model_path = "src/models/randomforest_regressor_best_RMSLE.pkl"
    
    if not os.path.exists(model_path):
        print("❌ Model file not found")
        return False
    
    try:
        # Try to load without external dependencies
        with open(model_path, 'rb') as f:
            # Read first few bytes to check if it's a valid pickle file
            header = f.read(10)
            
        if header.startswith(b'\x80\x03') or header.startswith(b'\x80\x04'):
            print("✅ Model file appears to be a valid pickle file")
            print(f"📁 File size: {os.path.getsize(model_path):,} bytes")
            return True
        else:
            print("⚠️ Model file may not be a valid pickle file")
            return False
            
    except Exception as e:
        print(f"❌ Error reading model file: {e}")
        return False

def test_prediction_page():
    """Test that the prediction page can be imported"""
    print("\n📄 Testing Prediction Page Import")
    print("=" * 50)
    
    try:
        sys.path.append('app_pages')
        
        # Try to import the prediction page
        import four_interactive_prediction
        
        # Check if key functions exist
        functions_to_check = [
            'interactive_prediction_body',
            'make_prediction_fallback',
            'display_prediction_results'
        ]
        
        all_functions_exist = True
        for func_name in functions_to_check:
            if hasattr(four_interactive_prediction, func_name):
                print(f"✅ Function {func_name} exists")
            else:
                print(f"❌ Function {func_name} missing")
                all_functions_exist = False
        
        return all_functions_exist
        
    except ImportError as e:
        print(f"❌ Could not import prediction page: {e}")
        return False
    except Exception as e:
        print(f"❌ Error testing prediction page: {e}")
        return False

def test_app_structure():
    """Test the main app structure"""
    print("\n🚀 Testing App Structure")
    print("=" * 50)
    
    try:
        # Try to import the main app
        import app
        
        print("✅ Main app can be imported")
        
        # Check if it has the expected structure
        if hasattr(app, 'app'):
            print("✅ App object exists")
        else:
            print("⚠️ App object not found")
        
        return True
        
    except ImportError as e:
        print(f"❌ Could not import main app: {e}")
        return False
    except Exception as e:
        print(f"❌ Error testing app structure: {e}")
        return False

def main():
    """Main test function"""
    print("🚜 Bulldozer Price Prediction - Simple System Test")
    print("=" * 80)
    print("This test checks basic file structure and imports without external dependencies")
    print("=" * 80)
    
    # Run all tests
    tests = [
        ("File Structure", test_file_structure),
        ("Model File", test_model_file),
        ("Prediction Page", test_prediction_page),
        ("App Structure", test_app_structure)
    ]
    
    results = {}
    
    for test_name, test_func in tests:
        try:
            results[test_name] = test_func()
        except Exception as e:
            print(f"❌ {test_name} test failed with exception: {e}")
            results[test_name] = False
    
    # Summary
    print("\n" + "=" * 80)
    print("📋 TEST SUMMARY")
    print("=" * 80)
    
    passed_tests = sum(results.values())
    total_tests = len(results)
    
    for test_name, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{test_name}: {status}")
    
    print(f"\nOverall: {passed_tests}/{total_tests} tests passed")
    
    if passed_tests == total_tests:
        print("\n🎉 ALL TESTS PASSED!")
        print("✅ System appears to be properly structured")
        print("✅ Ready for enhanced functionality testing")
    elif passed_tests >= total_tests * 0.75:
        print("\n⚠️ MOST TESTS PASSED")
        print("✅ Core system is functional")
        print("🔧 Some components may need attention")
    else:
        print("\n❌ MULTIPLE TEST FAILURES")
        print("🚨 System needs significant attention")
        print("🔧 Check file structure and dependencies")
    
    print("\n💡 Next Steps:")
    if results.get("File Structure", False) and results.get("Prediction Page", False):
        print("• ✅ Core system is ready")
        print("• 🧪 Run enhanced testing with: python test_enhanced_system.py")
        print("• 🚀 Start Streamlit app with: streamlit run app.py")
    else:
        print("• 🔧 Fix basic file structure issues first")
        print("• 📞 Check installation and file paths")

if __name__ == "__main__":
    main()
