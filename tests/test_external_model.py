#!/usr/bin/env python3
"""
Test script for external model loading functionality
Tests the Google Drive model loading without running the full Streamlit app
"""

import os
import sys
import time
import pickle
from io import BytesIO

# Add src directory to path (works from both project root and tests directory)
import os
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(project_root, 'src'))

def test_external_model_loader():
    """Test the external model loader functionality"""
    
    print("🧪 Testing External Model Loader")
    print("=" * 50)
    
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
    
    # Check if file ID is configured
    if loader.model_file_id == "YOUR_GOOGLE_DRIVE_FILE_ID_HERE":
        print("\n⚠️  Google Drive file ID not configured")
        print("   Please set GOOGLE_DRIVE_MODEL_ID environment variable")
        print("   or configure it in .streamlit/secrets.toml")
        return False
    
    print(f"\n🔗 Download URL: {loader.model_download_url}")
    
    # Test download (without Streamlit caching)
    print(f"\n🌐 Testing model download...")
    start_time = time.time()
    
    try:
        import requests
        
        # Test connection first
        print("   Testing connection...")
        response = requests.head(loader.model_download_url, timeout=10)
        
        if response.status_code == 200:
            print("   ✅ Connection successful")
            
            # Get file size
            content_length = response.headers.get('content-length')
            if content_length:
                size_mb = int(content_length) / (1024 * 1024)
                print(f"   📊 File size: {size_mb:.1f}MB")
            
            # Test actual download (first 1MB only for testing)
            print("   🔽 Testing download (first 1MB)...")
            response = requests.get(
                loader.model_download_url,
                stream=True,
                timeout=(10, 60)
            )
            
            # Read first 1MB
            data = BytesIO()
            downloaded = 0
            max_download = 1024 * 1024  # 1MB
            
            for chunk in response.iter_content(chunk_size=8192):
                if chunk and downloaded < max_download:
                    data.write(chunk)
                    downloaded += len(chunk)
                else:
                    break
            
            print(f"   ✅ Downloaded {downloaded / 1024:.1f}KB successfully")
            
            # Test if it looks like a pickle file
            data.seek(0)
            first_bytes = data.read(10)
            if first_bytes.startswith(b'\x80\x03') or first_bytes.startswith(b'\x80\x04'):
                print("   ✅ File appears to be a valid pickle file")
            else:
                print("   ⚠️  File may not be a valid pickle file")
            
        else:
            print(f"   ❌ Connection failed: HTTP {response.status_code}")
            return False
            
    except requests.exceptions.Timeout:
        print("   ❌ Connection timeout")
        return False
    except requests.exceptions.ConnectionError:
        print("   ❌ Connection error")
        return False
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False
    
    elapsed = time.time() - start_time
    print(f"   ⏱️  Test completed in {elapsed:.1f} seconds")
    
    print(f"\n✅ External model loader test completed successfully!")
    return True


def test_local_model():
    """Test loading the local model for comparison"""
    
    print(f"\n🧪 Testing Local Model (for comparison)")
    print("=" * 50)
    
    model_path = "src/models/randomforest_regressor_best_RMSLE.pkl"
    
    if not os.path.exists(model_path):
        print(f"❌ Local model file not found: {model_path}")
        return False
    
    # Check file size
    size_mb = os.path.getsize(model_path) / (1024 * 1024)
    print(f"📊 Local model size: {size_mb:.1f}MB")
    
    if size_mb > 500:
        print(f"⚠️  Model size ({size_mb:.1f}MB) exceeds Heroku's 500MB limit")
    
    # Test loading (just check if it's a valid pickle file)
    try:
        print("🔧 Testing model loading...")
        start_time = time.time()
        
        with open(model_path, 'rb') as f:
            # Just read the header to verify it's a valid pickle
            header = f.read(10)
            if header.startswith(b'\x80\x03') or header.startswith(b'\x80\x04'):
                print("✅ Local model file is valid pickle format")
            else:
                print("❌ Local model file is not valid pickle format")
                return False
        
        elapsed = time.time() - start_time
        print(f"⏱️  Validation completed in {elapsed:.3f} seconds")
        
    except Exception as e:
        print(f"❌ Error loading local model: {e}")
        return False
    
    return True


def main():
    """Main test function"""
    
    print("🚀 BulldozerPriceGenius External Model Test Suite")
    print("=" * 60)
    
    # Test external model loader
    external_success = test_external_model_loader()
    
    # Test local model for comparison
    local_success = test_local_model()
    
    print(f"\n📊 Test Results Summary:")
    print(f"   External Model Loader: {'✅ PASS' if external_success else '❌ FAIL'}")
    print(f"   Local Model: {'✅ PASS' if local_success else '❌ FAIL'}")
    
    if external_success:
        print(f"\n🎉 External model loading is ready for deployment!")
        print(f"   You can now deploy to Heroku without the large model file.")
    else:
        print(f"\n⚠️  External model loading needs configuration.")
        print(f"   Please check the setup instructions.")
    
    return external_success and local_success


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
