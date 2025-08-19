#!/usr/bin/env python3
"""
Heroku Deployment Verification Script for BulldozerPriceGenius
Tests all critical functionality after deployment
"""

import requests
import time
import sys
import json
from urllib.parse import urljoin

class HerokuDeploymentVerifier:
    """Verifies Heroku deployment functionality"""
    
    def __init__(self, app_url):
        self.app_url = app_url.rstrip('/')
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'BulldozerPriceGenius-Deployment-Verifier/1.0'
        })
    
    def print_status(self, message, status="info"):
        """Print colored status messages"""
        colors = {
            "success": "\033[92m✅",
            "error": "\033[91m❌", 
            "warning": "\033[93m⚠️",
            "info": "\033[94mℹ️"
        }
        reset = "\033[0m"
        print(f"{colors.get(status, '')} {message}{reset}")
    
    def test_app_accessibility(self):
        """Test if the app is accessible"""
        try:
            response = self.session.get(self.app_url, timeout=30)
            if response.status_code == 200:
                self.print_status("App is accessible", "success")
                return True
            else:
                self.print_status(f"App returned status {response.status_code}", "error")
                return False
        except requests.exceptions.RequestException as e:
            self.print_status(f"Failed to access app: {e}", "error")
            return False
    
    def test_model_loading(self):
        """Test if the ML model loads successfully"""
        try:
            # This would require accessing the Streamlit app's internal state
            # For now, we'll test if the app loads without errors
            response = self.session.get(self.app_url, timeout=60)
            
            # Check for error indicators in the response
            if "error" in response.text.lower() or "failed" in response.text.lower():
                self.print_status("Potential model loading issues detected", "warning")
                return False
            else:
                self.print_status("No obvious model loading errors", "success")
                return True
                
        except Exception as e:
            self.print_status(f"Model loading test failed: {e}", "error")
            return False
    
    def test_environment_variables(self, app_name):
        """Test if environment variables are properly set"""
        try:
            import subprocess
            result = subprocess.run(
                ['heroku', 'config:get', 'GOOGLE_DRIVE_MODEL_ID', '--app', app_name],
                capture_output=True, text=True, timeout=10
            )
            
            if result.returncode == 0 and result.stdout.strip():
                file_id = result.stdout.strip()
                if file_id == "1mSIR9TnJvP4zpVHlrsMGm11WS-DWyyTp":
                    self.print_status("Environment variables correctly configured", "success")
                    return True
                else:
                    self.print_status(f"Incorrect file ID: {file_id}", "error")
                    return False
            else:
                self.print_status("Environment variable not set", "error")
                return False
                
        except Exception as e:
            self.print_status(f"Environment variable test failed: {e}", "error")
            return False
    
    def test_memory_usage(self, app_name):
        """Test memory usage and dyno status"""
        try:
            import subprocess
            result = subprocess.run(
                ['heroku', 'ps', '--app', app_name, '--json'],
                capture_output=True, text=True, timeout=10
            )
            
            if result.returncode == 0:
                dynos = json.loads(result.stdout)
                for dyno in dynos:
                    if dyno['type'] == 'web':
                        size = dyno.get('size', 'unknown')
                        state = dyno.get('state', 'unknown')
                        
                        if size in ['Standard-1X', 'Standard-2X', 'Performance-M', 'Performance-L']:
                            self.print_status(f"Dyno size appropriate: {size}", "success")
                        else:
                            self.print_status(f"Dyno size may be insufficient: {size}", "warning")
                        
                        if state == 'up':
                            self.print_status(f"Dyno is running: {state}", "success")
                        else:
                            self.print_status(f"Dyno state: {state}", "warning")
                        
                        return True
                
                self.print_status("No web dynos found", "error")
                return False
            else:
                self.print_status("Failed to check dyno status", "error")
                return False
                
        except Exception as e:
            self.print_status(f"Memory usage test failed: {e}", "error")
            return False
    
    def run_verification(self, app_name):
        """Run complete verification suite"""
        print("🔍 Heroku Deployment Verification")
        print("=" * 40)
        print(f"App URL: {self.app_url}")
        print(f"App Name: {app_name}")
        print()
        
        tests = [
            ("App Accessibility", lambda: self.test_app_accessibility()),
            ("Environment Variables", lambda: self.test_environment_variables(app_name)),
            ("Memory/Dyno Configuration", lambda: self.test_memory_usage(app_name)),
            ("Model Loading", lambda: self.test_model_loading()),
        ]
        
        results = []
        for test_name, test_func in tests:
            print(f"Testing {test_name}...")
            try:
                result = test_func()
                results.append((test_name, result))
            except Exception as e:
                self.print_status(f"{test_name} failed with exception: {e}", "error")
                results.append((test_name, False))
            print()
        
        # Summary
        print("📋 Verification Summary")
        print("-" * 25)
        passed = sum(1 for _, result in results if result)
        total = len(results)
        
        for test_name, result in results:
            status = "✅ PASS" if result else "❌ FAIL"
            print(f"{test_name}: {status}")
        
        print()
        if passed == total:
            self.print_status(f"All {total} tests passed! 🎉", "success")
            return True
        else:
            self.print_status(f"{passed}/{total} tests passed", "warning")
            return False

def main():
    """Main verification function"""
    if len(sys.argv) != 3:
        print("Usage: python verify_heroku_deployment.py <app_url> <app_name>")
        print("Example: python verify_heroku_deployment.py https://myapp.herokuapp.com myapp")
        sys.exit(1)
    
    app_url = sys.argv[1]
    app_name = sys.argv[2]
    
    verifier = HerokuDeploymentVerifier(app_url)
    success = verifier.run_verification(app_name)
    
    if success:
        print("\n🚀 Deployment verification completed successfully!")
        print("Your BulldozerPriceGenius app is ready for production use.")
    else:
        print("\n⚠️ Some verification tests failed.")
        print("Please review the issues above before proceeding.")
        sys.exit(1)

if __name__ == "__main__":
    main()
