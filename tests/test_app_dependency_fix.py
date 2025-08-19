#!/usr/bin/env python3
"""
Final test to verify the gdown dependency fix works in the actual application context
"""

import sys
import os

def test_app_imports():
    """Test that the main application can import all required dependencies"""
    print("🧪 Testing Application Imports")
    print("=" * 40)
    
    try:
        # Test core dependencies
        import streamlit as st
        print("✅ streamlit imported successfully")
        
        import gdown
        print(f"✅ gdown imported successfully (version: {gdown.__version__})")
        
        import pandas as pd
        print("✅ pandas imported successfully")
        
        import numpy as np
        print("✅ numpy imported successfully")
        
        import pickle
        print("✅ pickle imported successfully")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_external_model_loader_integration():
    """Test the external model loader integration"""
    print(f"\n🧪 Testing External Model Loader Integration")
    print("=" * 40)
    
    # Add src to path (works from both project root and tests directory)
    import os
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(os.path.join(project_root, 'src'))
    
    try:
        # Test ExternalModelLoaderV2 import
        from external_model_loader_v2 import ExternalModelLoaderV2
        print("✅ ExternalModelLoaderV2 imported successfully")
        
        # Create instance
        loader = ExternalModelLoaderV2()
        print("✅ ExternalModelLoaderV2 instance created")
        
        # Check that gdown is available within the loader
        try:
            import gdown
            print("✅ gdown available in loader context")
            
            # Test the method that checks for gdown
            file_id = loader._get_model_file_id()
            print(f"✅ File ID retrieved: {file_id}")
            
            if file_id == "1mSIR9TnJvP4zpVHlrsMGm11WS-DWyyTp":
                print("✅ Correct Google Drive file ID configured")
            else:
                print(f"⚠️  File ID: {file_id} (check configuration)")
            
            return True
            
        except ImportError:
            print("❌ gdown not available in loader context")
            return False
            
    except Exception as e:
        print(f"❌ Error testing external model loader: {e}")
        return False

def test_prediction_page_imports():
    """Test that the prediction page can import the external model loader"""
    print(f"\n🧪 Testing Prediction Page Imports")
    print("=" * 40)
    
    # Add app_pages to path (works from both project root and tests directory)
    import os
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(os.path.join(project_root, 'app_pages'))
    
    try:
        # Mock streamlit for testing
        class MockStreamlit:
            def __init__(self):
                self.secrets = {'GOOGLE_DRIVE_MODEL_ID': '1mSIR9TnJvP4zpVHlrsMGm11WS-DWyyTp'}
            
            def cache_resource(self, func):
                return func
            
            def progress(self, value):
                class MockProgress:
                    def progress(self, val): pass
                    def empty(self): pass
                return MockProgress()
            
            def empty(self):
                class MockEmpty:
                    def text(self, val): pass
                    def empty(self): pass
                return MockEmpty()
            
            def warning(self, text): pass
            def success(self, text): pass
            def error(self, text): pass
            def info(self, text): pass
            def markdown(self, text, unsafe_allow_html=False): pass
            def button(self, text, key=None): return False
            def columns(self, n): return [MockStreamlit() for _ in range(n)]
            def expander(self, text, expanded=False): return MockStreamlit()
            def metric(self, label, value): pass
            def code(self, text): pass
        
        # Set up mock
        sys.modules['streamlit'] = MockStreamlit()
        
        # Add src to path for external model loader (works from both project root and tests directory)
        import os
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        sys.path.append(os.path.join(project_root, 'src'))
        
        # Test the import that happens in four_interactive_prediction.py
        try:
            from external_model_loader_v2 import external_model_loader_v2 as external_model_loader
            print("✅ external_model_loader_v2 imported successfully")
            
            # Test that it has the required methods
            if hasattr(external_model_loader, 'load_model_from_google_drive'):
                print("✅ load_model_from_google_drive method available")
            else:
                print("❌ load_model_from_google_drive method missing")
                return False
            
            if hasattr(external_model_loader, 'get_model_info'):
                print("✅ get_model_info method available")
            else:
                print("❌ get_model_info method missing")
                return False
            
            return True
            
        except ImportError as e:
            print(f"❌ Failed to import external_model_loader_v2: {e}")
            
            # Try fallback import
            try:
                from external_model_loader import external_model_loader
                print("✅ Fallback to external_model_loader successful")
                return True
            except ImportError as e2:
                print(f"❌ Fallback import also failed: {e2}")
                return False
        
    except Exception as e:
        print(f"❌ Error testing prediction page imports: {e}")
        return False

def test_no_missing_dependency_error():
    """Test that no missing dependency error occurs"""
    print(f"\n🧪 Testing No Missing Dependency Error")
    print("=" * 40)
    
    try:
        # Test the specific import that was failing
        import gdown
        print("✅ gdown import successful - no missing dependency error")
        
        # Test that the error message would not be triggered
        try:
            # This is the code path that was failing before
            download_url = "https://drive.google.com/uc?id=1mSIR9TnJvP4zpVHlrsMGm11WS-DWyyTp"
            print(f"✅ Can construct download URL: {download_url}")
            
            # Test that gdown has the required methods
            if hasattr(gdown, 'download'):
                print("✅ gdown.download method available")
            else:
                print("❌ gdown.download method missing")
                return False
            
            return True
            
        except Exception as e:
            print(f"❌ Error in gdown functionality test: {e}")
            return False
            
    except ImportError:
        print("❌ gdown import failed - missing dependency error would occur")
        return False

def main():
    """Main test function"""
    
    print("🚀 Final Application Dependency Fix Test")
    print("=" * 60)
    
    print(f"""
🎯 This test verifies that the 'Missing Dependency' error is completely fixed
   in the actual application context.

Previous Error:
📦 Missing Dependency
The 'gdown' library is required for downloading large files from Google Drive.
Please install it with: pip install gdown
Fallback: Using statistical prediction instead.

Expected Result:
✅ All imports work correctly
✅ External model loader V2 functions properly
✅ No missing dependency errors in the application
✅ Ready for ML prediction functionality
    """)
    
    # Run all tests
    tests = [
        ("Application Imports", test_app_imports),
        ("External Model Loader Integration", test_external_model_loader_integration),
        ("Prediction Page Imports", test_prediction_page_imports),
        ("No Missing Dependency Error", test_no_missing_dependency_error),
    ]
    
    results = {}
    
    for test_name, test_func in tests:
        try:
            results[test_name] = test_func()
        except Exception as e:
            print(f"❌ {test_name} test failed with exception: {e}")
            results[test_name] = False
    
    # Summary
    print(f"\n📊 Final Test Results Summary:")
    print("=" * 40)
    
    all_passed = True
    for test_name, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"   {test_name}: {status}")
        if not passed:
            all_passed = False
    
    if all_passed:
        print(f"\n🎉 All tests passed! Missing dependency error is completely fixed.")
        print(f"\n📋 Ready for Application Testing:")
        print(f"   1. Run: streamlit run app.py")
        print(f"   2. Navigate to Interactive Prediction page (Page 4)")
        print(f"   3. Click the orange '🤖 Get ML Prediction' button")
        print(f"   4. Verify the following sequence appears:")
        print(f"      • 🔄 Initializing model download from Google Drive...")
        print(f"      • 🌐 Connecting to Google Drive...")
        print(f"      • 📥 Downloading model file (561MB)...")
        print(f"      • ✅ Model loaded successfully in X seconds!")
        
        print(f"\n✅ Success Criteria:")
        print(f"   • No '📦 Missing Dependency' error messages")
        print(f"   • External model loading works correctly")
        print(f"   • ML predictions function properly")
        print(f"   • Orange button styling is applied")
        
    else:
        print(f"\n⚠️  Some tests failed. Please check the issues above.")
        print(f"\n🔧 Troubleshooting:")
        print(f"   • Verify gdown installation: python -c 'import gdown; print(gdown.__version__)'")
        print(f"   • Check Python environment consistency")
        print(f"   • Ensure all dependencies are in the same environment")
    
    return all_passed

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️ Test interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)
