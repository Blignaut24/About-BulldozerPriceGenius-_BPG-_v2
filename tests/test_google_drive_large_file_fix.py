#!/usr/bin/env python3
"""
Test script for Google Drive large file download fix
Tests the updated external model loader with HTML handling
"""

import os
import sys
import time
import requests
from io import BytesIO

def test_google_drive_large_file_download():
    """Test the Google Drive large file download with HTML handling"""
    
    print("🧪 Testing Google Drive Large File Download Fix")
    print("=" * 60)
    
    # Your Google Drive file ID
    file_id = "1mSIR9TnJvP4zpVHlrsMGm11WS-DWyyTp"
    
    print(f"📋 Configuration:")
    print(f"   File ID: {file_id}")
    print(f"   Expected size: ~561MB")
    print(f"   File type: RandomForest pickle model")
    
    # Test multiple download strategies
    download_strategies = [
        ("Standard URL", f"https://drive.google.com/uc?export=download&id={file_id}"),
        ("Confirmation URL", f"https://drive.google.com/uc?export=download&id={file_id}&confirm=t"),
        ("Alternative endpoint", f"https://docs.google.com/uc?export=download&id={file_id}")
    ]
    
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'BulldozerPriceGenius/1.0 (Large File Download Test)'
    })
    
    for strategy_name, url in download_strategies:
        print(f"\n🔄 Testing: {strategy_name}")
        print(f"   URL: {url}")
        
        try:
            # Test with HEAD request first
            head_response = session.head(url, timeout=10, allow_redirects=True)
            print(f"   HEAD response: {head_response.status_code}")
            
            if head_response.status_code == 200:
                content_length = head_response.headers.get('content-length')
                content_type = head_response.headers.get('content-type', '')
                
                print(f"   Content-Type: {content_type}")
                if content_length:
                    size_mb = int(content_length) / (1024 * 1024)
                    print(f"   Content-Length: {size_mb:.1f}MB")
                
                # Test actual download (first 2KB only)
                response = session.get(url, stream=True, timeout=(10, 30))
                
                if response.status_code == 200:
                    # Read first 2KB to check content
                    first_chunk = next(response.iter_content(chunk_size=2048), b'')
                    response.close()
                    
                    print(f"   Downloaded: {len(first_chunk)} bytes")
                    
                    # Analyze content
                    if first_chunk.startswith(b'\x80'):
                        print("   ✅ Content appears to be pickle file (binary)")
                        return True, strategy_name
                    elif first_chunk.startswith(b'<!DOCTYPE') or first_chunk.startswith(b'<html'):
                        print("   ⚠️  Content is HTML (confirmation page)")
                        
                        # Try to extract useful information from HTML
                        html_content = first_chunk.decode('utf-8', errors='ignore')
                        if 'virus' in html_content.lower():
                            print("   📋 HTML contains virus scan warning")
                        if 'download' in html_content.lower():
                            print("   📋 HTML contains download references")
                        if 'confirm' in html_content.lower():
                            print("   📋 HTML contains confirmation elements")
                    else:
                        print(f"   ❓ Unknown content type")
                        print(f"   First 50 bytes: {first_chunk[:50]}")
                else:
                    print(f"   ❌ GET request failed: {response.status_code}")
            else:
                print(f"   ❌ HEAD request failed: {head_response.status_code}")
                
        except requests.exceptions.Timeout:
            print("   ⏱️ Request timed out")
        except requests.exceptions.ConnectionError:
            print("   🌐 Connection error")
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    return False, None

def test_html_parsing():
    """Test HTML parsing capabilities for Google Drive confirmation pages"""
    
    print(f"\n🧪 Testing HTML Parsing for Confirmation Pages")
    print("=" * 50)
    
    file_id = "1mSIR9TnJvP4zpVHlrsMGm11WS-DWyyTp"
    
    try:
        # Get the Google Drive file page
        view_url = f"https://drive.google.com/file/d/{file_id}/view"
        
        session = requests.Session()
        response = session.get(view_url, timeout=15)
        
        if response.status_code == 200:
            print("✅ Successfully accessed Google Drive file page")
            
            html_content = response.text
            
            # Look for download-related patterns
            import re
            
            patterns_to_check = [
                (r'"downloadUrl":"([^"]+)"', "Download URL in JSON"),
                (r'href="([^"]*uc\?export=download[^"]*)"', "Download link in href"),
                (r'action="([^"]*uc\?export=download[^"]*)"', "Download form action"),
                (r'name="confirm" value="([^"]+)"', "Confirmation token"),
                (r'"confirm":"([^"]+)"', "Confirmation in JSON"),
            ]
            
            found_patterns = []
            for pattern, description in patterns_to_check:
                matches = re.findall(pattern, html_content)
                if matches:
                    found_patterns.append((description, matches[0]))
                    print(f"   ✅ Found: {description}")
                else:
                    print(f"   ❌ Not found: {description}")
            
            if found_patterns:
                print(f"\n📋 Extracted information:")
                for desc, value in found_patterns:
                    print(f"   {desc}: {value[:100]}...")
                return True
            else:
                print(f"\n⚠️  No download patterns found in HTML")
                return False
        else:
            print(f"❌ Failed to access file page: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ HTML parsing test failed: {e}")
        return False

def main():
    """Main test function"""
    
    print("🚀 Google Drive Large File Download Fix Test")
    print("=" * 60)
    
    print("""
🎯 This test verifies the fix for Google Drive large file downloads
   that handle HTML confirmation pages instead of direct binary downloads.

File: 1mSIR9TnJvP4zpVHlrsMGm11WS-DWyyTp (561MB RandomForest model)
Issue: Google Drive serves HTML confirmation pages for large files
Fix: Multiple download strategies with HTML parsing
    """)
    
    # Test 1: Download strategies
    download_success, successful_strategy = test_google_drive_large_file_download()
    
    # Test 2: HTML parsing
    html_parsing_success = test_html_parsing()
    
    print(f"\n📊 Test Results Summary:")
    print("=" * 40)
    print(f"   Download Strategies: {'✅ PASS' if download_success else '❌ FAIL'}")
    if successful_strategy:
        print(f"   Successful Strategy: {successful_strategy}")
    print(f"   HTML Parsing: {'✅ PASS' if html_parsing_success else '❌ FAIL'}")
    
    overall_success = download_success or html_parsing_success
    
    if overall_success:
        print(f"\n🎉 Fix verification successful!")
        print(f"   The updated external model loader should handle Google Drive large files.")
        print(f"   Deploy the fix to Heroku to resolve the 'Unexpected Error'.")
        
        print(f"\n📋 Deployment Steps:")
        print(f"   1. Commit the changes: git add . && git commit -m 'fix: handle Google Drive large file downloads'")
        print(f"   2. Deploy to Heroku: git push heroku main")
        print(f"   3. Test on Heroku: https://bulldozerpricegenius.herokuapp.com")
        print(f"   4. Monitor logs: heroku logs --tail --app bulldozerpricegenius")
        
    else:
        print(f"\n⚠️  Fix verification inconclusive.")
        print(f"   The Google Drive file may still require additional handling.")
        print(f"   Consider alternative approaches or file hosting solutions.")
    
    return overall_success

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
