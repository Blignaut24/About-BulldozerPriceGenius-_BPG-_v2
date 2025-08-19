#!/usr/bin/env python3
"""
Test script for the gdown-based Google Drive fix
Tests the simplified external model loader V2
"""

import os
import sys
import subprocess

def install_gdown():
    """Install gdown library if not available"""
    try:
        import gdown
        print("✅ gdown library is already installed")
        return True
    except ImportError:
        print("📦 Installing gdown library...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "gdown>=4.6.0"])
            print("✅ gdown library installed successfully")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install gdown: {e}")
            return False

def test_gdown_download():
    """Test gdown download functionality"""
    
    print("\n🧪 Testing gdown Download Functionality")
    print("=" * 50)
    
    file_id = "1mSIR9TnJvP4zpVHlrsMGm11WS-DWyyTp"
    
    try:
        import gdown
        import tempfile
        
        # Create temporary file
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.pkl')
        temp_file.close()
        
        print(f"📋 Configuration:")
        print(f"   File ID: {file_id}")
        print(f"   Temp file: {temp_file.name}")
        print(f"   Download URL: https://drive.google.com/uc?id={file_id}")
        
        print(f"\n🔄 Starting download (this may take 1-2 minutes for 561MB)...")
        
        # Download with gdown
        download_url = f"https://drive.google.com/uc?id={file_id}"
        success = gdown.download(download_url, temp_file.name, quiet=False, fuzzy=True)
        
        if success and os.path.exists(temp_file.name):
            file_size = os.path.getsize(temp_file.name)
            size_mb = file_size / (1024 * 1024)
            
            print(f"✅ Download successful!")
            print(f"   File size: {size_mb:.1f}MB")
            
            if file_size > 500 * 1024 * 1024:  # > 500MB
                print(f"✅ File size looks correct for the 561MB model")
                
                # Test if it's a valid pickle file
                try:
                    import pickle
                    with open(temp_file.name, 'rb') as f:
                        # Just read the header to verify it's pickle
                        header = f.read(10)
                        if header.startswith(b'\x80'):
                            print(f"✅ File appears to be a valid pickle file")
                            success_result = True
                        else:
                            print(f"⚠️  File may not be a valid pickle file")
                            print(f"   Header: {header}")
                            success_result = False
                except Exception as e:
                    print(f"❌ Error reading file: {e}")
                    success_result = False
            else:
                print(f"⚠️  File size ({size_mb:.1f}MB) is smaller than expected (561MB)")
                print(f"   This might indicate a download issue or HTML error page")
                success_result = False
            
            # Clean up
            os.unlink(temp_file.name)
            return success_result
            
        else:
            print(f"❌ Download failed or file not created")
            if os.path.exists(temp_file.name):
                os.unlink(temp_file.name)
            return False
            
    except Exception as e:
        print(f"❌ gdown test failed: {e}")
        return False

def test_external_loader_v2():
    """Test the external model loader V2"""
    
    print("\n🧪 Testing External Model Loader V2")
    print("=" * 50)
    
    # Mock Streamlit for testing
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
                def text(self, val): print(f"   Status: {val}")
                def empty(self): pass
            return MockEmpty()
        
        def warning(self, text): print(f"⚠️  {text}")
        def success(self, text): print(f"✅ {text}")
        def error(self, text): print(f"❌ {text}")
    
    # Set up mock
    sys.modules['streamlit'] = MockStreamlit()
    
    # Add src to path (from tests directory)
    sys.path.append('../src')
    
    try:
        from external_model_loader_v2 import ExternalModelLoaderV2
        
        print("✅ External model loader V2 imported successfully")
        
        # Create loader
        loader = ExternalModelLoaderV2()
        
        # Check configuration
        info = loader.get_model_info()
        print(f"\n📋 Loader Configuration:")
        for key, value in info.items():
            print(f"   {key}: {value}")
        
        # Verify file ID
        if loader.model_file_id == "1mSIR9TnJvP4zpVHlrsMGm11WS-DWyyTp":
            print(f"✅ File ID configured correctly")
            return True
        else:
            print(f"❌ File ID mismatch: {loader.model_file_id}")
            return False
            
    except ImportError as e:
        print(f"❌ Failed to import external model loader V2: {e}")
        return False
    except Exception as e:
        print(f"❌ Error testing loader: {e}")
        return False

def main():
    """Main test function"""
    
    print("🚀 Google Drive Large File Fix Test (gdown method)")
    print("=" * 60)
    
    print("""
🎯 This test verifies the gdown-based fix for Google Drive large file downloads.

The gdown library is specifically designed to handle Google Drive downloads
and automatically bypasses virus scan warnings and confirmation pages.

File: 1mSIR9TnJvP4zpVHlrsMGm11WS-DWyyTp (561MB RandomForest model)
Method: gdown library with fuzzy matching
    """)
    
    # Test 1: Install gdown
    gdown_available = install_gdown()
    
    # Test 2: Test gdown download (only if gdown is available)
    gdown_download_success = False
    if gdown_available:
        print("\n⚠️  WARNING: The next test will download 561MB from Google Drive.")
        print("   This may take 1-2 minutes and use significant bandwidth.")
        
        proceed = input("\nProceed with download test? (y/N): ").strip().lower()
        if proceed == 'y':
            gdown_download_success = test_gdown_download()
        else:
            print("⏭️  Skipping download test")
            gdown_download_success = None  # Skipped
    
    # Test 3: Test external loader V2
    loader_success = test_external_loader_v2()
    
    # Summary
    print(f"\n📊 Test Results Summary:")
    print("=" * 40)
    print(f"   gdown Installation: {'✅ PASS' if gdown_available else '❌ FAIL'}")
    
    if gdown_download_success is None:
        print(f"   gdown Download: ⏭️  SKIPPED")
    else:
        print(f"   gdown Download: {'✅ PASS' if gdown_download_success else '❌ FAIL'}")
    
    print(f"   External Loader V2: {'✅ PASS' if loader_success else '❌ FAIL'}")
    
    # Overall assessment
    if gdown_available and loader_success:
        print(f"\n🎉 Fix is ready for deployment!")
        print(f"   The gdown-based external model loader should resolve the HTML error.")
        
        print(f"\n📋 Deployment Steps:")
        print(f"   1. Commit changes: git add . && git commit -m 'fix: use gdown for Google Drive large files'")
        print(f"   2. Deploy to Heroku: git push heroku main")
        print(f"   3. Test on Heroku: https://bulldozerpricegenius.herokuapp.com")
        print(f"   4. Monitor logs: heroku logs --tail --app bulldozerpricegenius")
        
        if gdown_download_success:
            print(f"\n✅ Download test passed - the fix should work on Heroku!")
        elif gdown_download_success is None:
            print(f"\n⚠️  Download test was skipped - deploy and test on Heroku")
        
        return True
    else:
        print(f"\n⚠️  Fix needs attention before deployment.")
        if not gdown_available:
            print(f"   • Install gdown library")
        if not loader_success:
            print(f"   • Fix external loader V2 configuration")
        return False

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
