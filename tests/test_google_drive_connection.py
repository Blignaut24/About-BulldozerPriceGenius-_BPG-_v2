#!/usr/bin/env python3
"""
Simple test script for Google Drive model connection
Tests the Google Drive download without requiring Streamlit
"""

import os
import sys
import time
import requests
from io import BytesIO

def test_google_drive_connection():
    """Test connection to Google Drive and model download"""
    
    print("🧪 Testing Google Drive Model Connection")
    print("=" * 50)
    
    # Your Google Drive file ID
    file_id = "1mSIR9TnJvP4zpVHlrsMGm11WS-DWyyTp"
    download_url = f"https://drive.google.com/uc?export=download&id={file_id}"
    
    print(f"📋 Configuration:")
    print(f"   File ID: {file_id}")
    print(f"   Download URL: {download_url}")
    
    try:
        print(f"\n🌐 Testing connection to Google Drive...")
        start_time = time.time()
        
        # Test connection with HEAD request first
        print("   Checking if file is accessible...")
        response = requests.head(download_url, timeout=10, allow_redirects=True)
        
        print(f"   Response status: {response.status_code}")
        
        if response.status_code == 200:
            print("   ✅ File is accessible!")
            
            # Get file size if available
            content_length = response.headers.get('content-length')
            if content_length:
                size_mb = int(content_length) / (1024 * 1024)
                print(f"   📊 File size: {size_mb:.1f}MB")
            else:
                print("   📊 File size: Unknown (Google Drive doesn't always provide content-length)")
            
        else:
            print(f"   ❌ File not accessible: HTTP {response.status_code}")
            return False
        
        # Test actual download (first 1MB only)
        print(f"\n🔽 Testing download (first 1MB for validation)...")
        response = requests.get(download_url, stream=True, timeout=(10, 60))

        if response.status_code != 200:
            print(f"   ❌ Download failed: HTTP {response.status_code}")
            return False

        # Check if Google Drive is serving HTML (download confirmation page)
        content_type = response.headers.get('content-type', '')
        if 'text/html' in content_type:
            print("   🔄 Google Drive requires download confirmation for large files")
            print("   Trying alternative download URL...")
            response.close()

            # Try the confirmation URL for large files
            confirm_url = f"https://drive.google.com/uc?export=download&id={file_id}&confirm=t"
            response = requests.get(confirm_url, stream=True, timeout=(10, 60))

            if response.status_code != 200:
                print(f"   ❌ Confirmation download failed: HTTP {response.status_code}")
                return False
        
        # Read first 1MB to test
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
            print(f"   First bytes: {first_bytes}")
        
        elapsed = time.time() - start_time
        print(f"   ⏱️  Test completed in {elapsed:.1f} seconds")
        
        return True
        
    except requests.exceptions.Timeout:
        print("   ❌ Connection timeout")
        return False
    except requests.exceptions.ConnectionError:
        print("   ❌ Connection error - check internet connection")
        return False
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

def test_local_model_comparison():
    """Test local model for comparison"""
    
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
        print("   External storage is required for deployment")
    
    # Test file format
    try:
        print("🔧 Testing model file format...")
        with open(model_path, 'rb') as f:
            header = f.read(10)
            if header.startswith(b'\x80\x03') or header.startswith(b'\x80\x04'):
                print("✅ Local model file is valid pickle format")
                return True
            else:
                print("❌ Local model file is not valid pickle format")
                return False
    except Exception as e:
        print(f"❌ Error reading local model: {e}")
        return False

def main():
    """Main test function"""
    
    print("🚀 Google Drive Model Connection Test")
    print("=" * 60)
    
    print("""
🎯 This test verifies that your Google Drive model file is accessible
   and can be downloaded for the BulldozerPriceGenius application.

File ID: 1mSIR9TnJvP4zpVHlrsMGm11WS-DWyyTp
Expected size: ~561MB
    """)
    
    # Test Google Drive connection
    gdrive_success = test_google_drive_connection()
    
    # Test local model for comparison
    local_success = test_local_model_comparison()
    
    print(f"\n📊 Test Results Summary:")
    print(f"   Google Drive Connection: {'✅ PASS' if gdrive_success else '❌ FAIL'}")
    print(f"   Local Model: {'✅ PASS' if local_success else '❌ FAIL'}")
    
    if gdrive_success:
        print(f"\n🎉 Google Drive model is accessible and ready!")
        print(f"   Your external model storage setup is working correctly.")
        print(f"   You can now proceed with Heroku deployment.")
        
        print(f"\n📋 Next Steps:")
        print(f"   1. Set Heroku environment variable:")
        print(f"      heroku config:set GOOGLE_DRIVE_MODEL_ID=\"1mSIR9TnJvP4zpVHlrsMGm11WS-DWyyTp\" --app your-app-name")
        print(f"   2. Deploy to Heroku:")
        print(f"      git push heroku main")
        print(f"   3. Monitor deployment:")
        print(f"      heroku logs --tail --app your-app-name")
        
    else:
        print(f"\n⚠️  Google Drive connection failed.")
        print(f"   Please check:")
        print(f"   1. Internet connection")
        print(f"   2. Google Drive file sharing is set to 'Anyone with the link'")
        print(f"   3. File ID is correct: 1mSIR9TnJvP4zpVHlrsMGm11WS-DWyyTp")
    
    return gdrive_success

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
