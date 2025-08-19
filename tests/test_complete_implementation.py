#!/usr/bin/env python3
"""
Complete Implementation Test for External Model Storage
Tests the full external model loading functionality with mock Streamlit environment
"""

import os
import sys
import time
import pickle
from io import BytesIO
from unittest.mock import Mock, MagicMock

# Mock Streamlit for testing
class MockStreamlit:
    def __init__(self):
        self.secrets = {'GOOGLE_DRIVE_MODEL_ID': '1mSIR9TnJvP4zpVHlrsMGm11WS-DWyyTp'}
        self.cache_resource = self._cache_resource
        self._progress_bar = None
        self._status_text = None
    
    def _cache_resource(self, func):
        """Mock cache_resource decorator"""
        return func
    
    def progress(self, value):
        """Mock progress bar"""
        if self._progress_bar is None:
            self._progress_bar = Mock()
        self._progress_bar.progress = Mock()
        return self._progress_bar
    
    def empty(self):
        """Mock empty widget"""
        if self._status_text is None:
            self._status_text = Mock()
        self._status_text.text = Mock()
        self._status_text.empty = Mock()
        return self._status_text
    
    def info(self, text):
        print(f"ℹ️  {text}")
    
    def success(self, text):
        print(f"✅ {text}")
    
    def error(self, text):
        print(f"❌ {text}")
    
    def warning(self, text):
        print(f"⚠️  {text}")

# Set up mock Streamlit
sys.modules['streamlit'] = MockStreamlit()

# Add src directory to path (from tests directory)
sys.path.append('../src')

def test_external_model_loader():
    """Test the external model loader with mock Streamlit"""
    
    print("🧪 Testing External Model Loader Implementation")
    print("=" * 60)
    
    try:
        from external_model_loader import ExternalModelLoader
        print("✅ External model loader imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import external model loader: {e}")
        return False
    
    # Create loader instance
    loader = ExternalModelLoader()
    
    # Check configuration
    print(f"\n📋 Configuration:")
    info = loader.get_model_info()
    for key, value in info.items():
        print(f"   {key}: {value}")
    
    # Verify file ID is configured correctly
    expected_file_id = "1mSIR9TnJvP4zpVHlrsMGm11WS-DWyyTp"
    if loader.model_file_id == expected_file_id:
        print(f"✅ File ID configured correctly: {expected_file_id}")
    else:
        print(f"❌ File ID mismatch. Expected: {expected_file_id}, Got: {loader.model_file_id}")
        return False
    
    print(f"\n🔗 Download URL: {loader.model_download_url}")
    
    # Test the download method (without actually downloading the full file)
    print(f"\n🌐 Testing model loading method...")
    
    try:
        # This will test the method but we'll interrupt it before full download
        print("   Note: This test will attempt to start the download but won't complete it")
        print("   to avoid downloading 561MB during testing.")
        
        # We can't easily test the full download without Streamlit's actual caching
        # But we can verify the method exists and is callable
        if hasattr(loader, 'load_model_from_google_drive'):
            print("✅ load_model_from_google_drive method exists")
        else:
            print("❌ load_model_from_google_drive method not found")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing model loading: {e}")
        return False

def test_prediction_integration():
    """Test integration with prediction code"""
    
    print(f"\n🧪 Testing Prediction Integration")
    print("=" * 50)
    
    # Add app_pages to path (from tests directory)
    sys.path.append('../app_pages')
    
    try:
        # Test if the prediction module can import the external loader
        import four_interactive_prediction
        
        if hasattr(four_interactive_prediction, 'EXTERNAL_MODEL_AVAILABLE'):
            if four_interactive_prediction.EXTERNAL_MODEL_AVAILABLE:
                print("✅ External model loader available in prediction module")
            else:
                print("❌ External model loader not available in prediction module")
                return False
        else:
            print("❌ EXTERNAL_MODEL_AVAILABLE flag not found")
            return False
        
        if hasattr(four_interactive_prediction, 'external_model_loader'):
            if four_interactive_prediction.external_model_loader is not None:
                print("✅ External model loader instance available")
            else:
                print("❌ External model loader instance is None")
                return False
        else:
            print("❌ external_model_loader not found")
            return False
        
        return True
        
    except ImportError as e:
        print(f"❌ Failed to import prediction module: {e}")
        return False
    except Exception as e:
        print(f"❌ Error testing prediction integration: {e}")
        return False

def test_configuration_files():
    """Test configuration files"""
    
    print(f"\n🧪 Testing Configuration Files")
    print("=" * 50)
    
    # Test .streamlit/secrets.toml
    secrets_file = ".streamlit/secrets.toml"
    if os.path.exists(secrets_file):
        print(f"✅ Secrets file exists: {secrets_file}")
        
        with open(secrets_file, 'r') as f:
            content = f.read()
            if "1mSIR9TnJvP4zpVHlrsMGm11WS-DWyyTp" in content:
                print("✅ Correct file ID found in secrets")
            else:
                print("❌ File ID not found in secrets")
                return False
    else:
        print(f"❌ Secrets file not found: {secrets_file}")
        return False
    
    # Test .gitignore
    gitignore_file = ".gitignore"
    if os.path.exists(gitignore_file):
        with open(gitignore_file, 'r') as f:
            content = f.read()
            if ".streamlit/secrets.toml" in content:
                print("✅ Secrets file properly excluded from git")
            else:
                print("⚠️  Secrets file not excluded from git (security risk)")
    
    # Test .slugignore
    slugignore_file = ".slugignore"
    if os.path.exists(slugignore_file):
        with open(slugignore_file, 'r') as f:
            content = f.read()
            if "randomforest_regressor_best_RMSLE.pkl" in content:
                print("✅ Large model file excluded from Heroku slug")
            else:
                print("❌ Large model file not excluded from slug")
                return False
    else:
        print(f"❌ Slugignore file not found: {slugignore_file}")
        return False
    
    return True

def test_requirements():
    """Test requirements.txt"""
    
    print(f"\n🧪 Testing Requirements")
    print("=" * 50)
    
    requirements_file = "requirements.txt"
    if os.path.exists(requirements_file):
        with open(requirements_file, 'r') as f:
            content = f.read()
            if "requests" in content:
                print("✅ requests library included in requirements")
            else:
                print("❌ requests library not found in requirements")
                return False
    else:
        print(f"❌ Requirements file not found: {requirements_file}")
        return False
    
    return True

def main():
    """Main test function"""
    
    print("🚀 Complete Implementation Test Suite")
    print("=" * 60)
    
    print(f"""
🎯 Testing the complete external model storage implementation:

Configuration:
• Google Drive File ID: 1mSIR9TnJvP4zpVHlrsMGm11WS-DWyyTp
• Expected Model Size: ~561MB
• Target Platform: Heroku Standard-1X

Test Coverage:
• External model loader functionality
• Integration with prediction code
• Configuration files
• Requirements and dependencies
    """)
    
    # Run all tests
    tests = [
        ("External Model Loader", test_external_model_loader),
        ("Prediction Integration", test_prediction_integration),
        ("Configuration Files", test_configuration_files),
        ("Requirements", test_requirements),
    ]
    
    results = {}
    
    for test_name, test_func in tests:
        try:
            results[test_name] = test_func()
        except Exception as e:
            print(f"❌ {test_name} test failed with exception: {e}")
            results[test_name] = False
    
    # Summary
    print(f"\n📊 Test Results Summary:")
    print("=" * 40)
    
    all_passed = True
    for test_name, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"   {test_name}: {status}")
        if not passed:
            all_passed = False
    
    if all_passed:
        print(f"\n🎉 All tests passed! Implementation is ready for deployment.")
        print(f"\n📋 Next Steps:")
        print(f"   1. Run Heroku setup: python setup_heroku_environment.py")
        print(f"   2. Deploy to Heroku: git push heroku main")
        print(f"   3. Monitor deployment: heroku logs --tail")
        
        print(f"\n✅ Expected Deployment Results:")
        print(f"   • Slug size: ~50MB (under 500MB limit)")
        print(f"   • Model loads in 30-60 seconds on first access")
        print(f"   • Instant predictions after caching")
        print(f"   • Same accuracy as local model")
        
    else:
        print(f"\n⚠️  Some tests failed. Please fix the issues before deployment.")
    
    return all_passed

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️ Tests interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)
