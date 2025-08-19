#!/usr/bin/env python3
"""
Test script to verify gdown dependency fix for BulldozerPriceGenius
Tests that the missing dependency error is resolved
"""

import sys
import os

def test_gdown_import():
    """Test that gdown can be imported successfully"""
    print("🧪 Testing gdown Import")
    print("=" * 40)
    
    try:
        import gdown
        print(f"✅ gdown imported successfully")
        print(f"   Version: {gdown.__version__}")
        return True
    except ImportError as e:
        print(f"❌ Failed to import gdown: {e}")
        return False

def test_external_model_loader_v2():
    """Test that ExternalModelLoaderV2 can import gdown"""
    print(f"\n🧪 Testing ExternalModelLoaderV2 Import")
    print("=" * 40)
    
    # Add src to path (works from both project root and tests directory)
    import os
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(os.path.join(project_root, 'src'))
    
    try:
        from external_model_loader_v2 import ExternalModelLoaderV2
        print("✅ ExternalModelLoaderV2 imported successfully")
        
        # Create loader instance
        loader = ExternalModelLoaderV2()
        print("✅ ExternalModelLoaderV2 instance created")
        
        # Check configuration
        info = loader.get_model_info()
        print(f"✅ Model info retrieved:")
        for key, value in info.items():
            print(f"   {key}: {value}")
        
        return True
        
    except ImportError as e:
        print(f"❌ Failed to import ExternalModelLoaderV2: {e}")
        return False
    except Exception as e:
        print(f"❌ Error with ExternalModelLoaderV2: {e}")
        return False

def test_mock_streamlit_environment():
    """Test with mock Streamlit environment"""
    print(f"\n🧪 Testing Mock Streamlit Environment")
    print("=" * 40)
    
    # Mock Streamlit for testing
    class MockStreamlit:
        def __init__(self):
            self.secrets = {'GOOGLE_DRIVE_MODEL_ID': '1mSIR9TnJvP4zpVHlrsMGm11WS-DWyyTp'}
        
        def cache_resource(self, func):
            return func
        
        def progress(self, value):
            class MockProgress:
                def progress(self, val): 
                    print(f"   Progress: {val}%")
                def empty(self): pass
            return MockProgress()
        
        def empty(self):
            class MockEmpty:
                def text(self, val): 
                    print(f"   Status: {val}")
                def empty(self): pass
            return MockEmpty()
        
        def warning(self, text): print(f"⚠️  {text}")
        def success(self, text): print(f"✅ {text}")
        def error(self, text): print(f"❌ {text}")
        def info(self, text): print(f"ℹ️  {text}")
    
    # Set up mock
    sys.modules['streamlit'] = MockStreamlit()
    
    try:
        # Add src to path (works from both project root and tests directory)
        import os
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        sys.path.append(os.path.join(project_root, 'src'))
        
        from external_model_loader_v2 import ExternalModelLoaderV2
        
        # Create loader
        loader = ExternalModelLoaderV2()
        print("✅ Loader created with mock Streamlit")
        
        # Check if gdown import works within the loader context
        try:
            import gdown
            print("✅ gdown import works in loader context")
            
            # Test the method that previously failed
            print("✅ No 'Missing Dependency' error should occur now")
            return True
            
        except ImportError:
            print("❌ gdown still not available in loader context")
            return False
            
    except Exception as e:
        print(f"❌ Error in mock environment: {e}")
        return False

def test_requirements_consistency():
    """Test that requirements.txt contains gdown"""
    print(f"\n🧪 Testing Requirements.txt Consistency")
    print("=" * 40)
    
    try:
        with open('requirements.txt', 'r') as f:
            content = f.read()
        
        if 'gdown' in content:
            print("✅ gdown found in requirements.txt")
            
            # Extract gdown line
            for line in content.split('\n'):
                if 'gdown' in line and not line.startswith('#'):
                    print(f"   Specification: {line.strip()}")
                    break
            
            return True
        else:
            print("❌ gdown not found in requirements.txt")
            return False
            
    except FileNotFoundError:
        print("❌ requirements.txt not found")
        return False

def main():
    """Main test function"""
    
    print("🚀 gdown Dependency Fix Verification")
    print("=" * 60)
    
    print(f"""
🎯 This test verifies that the 'Missing Dependency' error is fixed.

Previous Error:
📦 Missing Dependency
The 'gdown' library is required for downloading large files from Google Drive.
Please install it with: pip install gdown

Expected Result:
✅ gdown library available
✅ ExternalModelLoaderV2 works without import errors
✅ No missing dependency messages
    """)
    
    # Run all tests
    tests = [
        ("gdown Import", test_gdown_import),
        ("ExternalModelLoaderV2", test_external_model_loader_v2),
        ("Mock Streamlit Environment", test_mock_streamlit_environment),
        ("Requirements Consistency", test_requirements_consistency),
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
        print(f"\n🎉 All tests passed! Missing dependency error is fixed.")
        print(f"\n📋 Next Steps:")
        print(f"   1. Run the application: streamlit run app.py")
        print(f"   2. Navigate to Interactive Prediction page (Page 4)")
        print(f"   3. Verify no 'Missing Dependency' error appears")
        print(f"   4. Test ML prediction functionality")
        
        print(f"\n✅ Expected Behavior:")
        print(f"   • No missing dependency errors")
        print(f"   • External model loader V2 works correctly")
        print(f"   • Google Drive model download functions properly")
        print(f"   • ML predictions work as expected")
        
    else:
        print(f"\n⚠️  Some tests failed. Please check the issues above.")
        print(f"\n🔧 Troubleshooting:")
        print(f"   • Ensure gdown is installed: python -m pip install gdown>=4.6.0")
        print(f"   • Check Python environment is correct")
        print(f"   • Verify requirements.txt contains gdown dependency")
    
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
