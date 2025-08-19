#!/usr/bin/env python3
"""
Heroku Environment Setup Script for BulldozerPriceGenius
Configures the Google Drive model file ID for your specific deployment
"""

import subprocess
import sys
import os

def check_heroku_cli():
    """Check if Heroku CLI is installed and user is logged in"""
    try:
        # Check if Heroku CLI is installed
        result = subprocess.run(['heroku', '--version'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode != 0:
            print("❌ Heroku CLI is not installed.")
            print("   Please install it from: https://devcenter.heroku.com/articles/heroku-cli")
            return False
        
        print(f"✅ Heroku CLI found: {result.stdout.strip()}")
        
        # Check if user is logged in
        result = subprocess.run(['heroku', 'auth:whoami'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode != 0:
            print("❌ Not logged in to Heroku.")
            print("   Please run: heroku login")
            return False
        
        print(f"✅ Logged in as: {result.stdout.strip()}")
        return True
        
    except subprocess.TimeoutExpired:
        print("❌ Heroku CLI command timed out")
        return False
    except FileNotFoundError:
        print("❌ Heroku CLI not found in PATH")
        print("   Please install it from: https://devcenter.heroku.com/articles/heroku-cli")
        return False
    except Exception as e:
        print(f"❌ Error checking Heroku CLI: {e}")
        return False

def setup_heroku_config(app_name, file_id):
    """Set up Heroku environment variables"""
    try:
        print(f"\n🔧 Setting up Heroku environment for app: {app_name}")
        print(f"   Google Drive File ID: {file_id}")
        
        # Set the environment variable
        cmd = ['heroku', 'config:set', f'GOOGLE_DRIVE_MODEL_ID={file_id}', '--app', app_name]
        
        print(f"\n⚙️ Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            print("✅ Environment variable set successfully!")
            print(result.stdout)
            return True
        else:
            print("❌ Failed to set environment variable")
            print(f"Error: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print("❌ Heroku command timed out")
        return False
    except Exception as e:
        print(f"❌ Error setting up Heroku config: {e}")
        return False

def verify_heroku_config(app_name):
    """Verify the Heroku configuration"""
    try:
        print(f"\n🔍 Verifying Heroku configuration for app: {app_name}")
        
        cmd = ['heroku', 'config', '--app', app_name]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=20)
        
        if result.returncode == 0:
            print("✅ Current Heroku configuration:")
            print(result.stdout)
            
            # Check if our variable is set
            if 'GOOGLE_DRIVE_MODEL_ID' in result.stdout:
                print("✅ GOOGLE_DRIVE_MODEL_ID is configured!")
                return True
            else:
                print("❌ GOOGLE_DRIVE_MODEL_ID not found in configuration")
                return False
        else:
            print("❌ Failed to get Heroku configuration")
            print(f"Error: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Error verifying Heroku config: {e}")
        return False

def main():
    """Main setup function"""
    print("🚀 Heroku Environment Setup for BulldozerPriceGenius")
    print("=" * 60)
    
    # Your specific Google Drive file ID
    file_id = "1mSIR9TnJvP4zpVHlrsMGm11WS-DWyyTp"
    
    print(f"""
📋 Configuration Details:
   Google Drive File ID: {file_id}
   Direct Download URL: https://drive.google.com/uc?export=download&id={file_id}
   Model Size: ~561MB
   
🎯 This script will configure your Heroku app to use external model storage.
    """)
    
    # Step 1: Check Heroku CLI
    print("\n📋 Step 1: Checking Heroku CLI")
    print("-" * 30)
    if not check_heroku_cli():
        return False
    
    # Step 2: Get app name
    print("\n📋 Step 2: Heroku App Configuration")
    print("-" * 30)
    
    # Try to detect app name from git remote
    app_name = None
    try:
        result = subprocess.run(['git', 'remote', 'get-url', 'heroku'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            # Extract app name from Heroku git URL
            url = result.stdout.strip()
            if 'heroku.com' in url:
                app_name = url.split('/')[-1].replace('.git', '')
                print(f"🔍 Detected Heroku app from git remote: {app_name}")
    except:
        pass
    
    if not app_name:
        app_name = input("Enter your Heroku app name: ").strip()
    
    if not app_name:
        print("❌ App name is required")
        return False
    
    # Step 3: Set up configuration
    print(f"\n📋 Step 3: Setting Environment Variables")
    print("-" * 30)
    if not setup_heroku_config(app_name, file_id):
        return False
    
    # Step 4: Verify configuration
    print(f"\n📋 Step 4: Verifying Configuration")
    print("-" * 30)
    if not verify_heroku_config(app_name):
        return False
    
    # Step 5: Deployment instructions
    print(f"\n📋 Step 5: Deployment Instructions")
    print("-" * 30)
    print(f"""
🚀 Your Heroku app is now configured for external model storage!

📋 Next Steps:
   1. Commit your changes:
      git add .
      git commit -m "feat: implement external model storage"
   
   2. Deploy to Heroku:
      git push heroku main
   
   3. Monitor deployment:
      heroku logs --tail --app {app_name}
   
   4. Open your app:
      heroku open --app {app_name}

⚡ Expected Deployment Behavior:
   • Slug size will be ~50MB (under 500MB limit)
   • First model load will take 30-60 seconds
   • Subsequent predictions will be instant (cached)
   • Same prediction accuracy as local version

🔧 Troubleshooting:
   • Check logs: heroku logs --tail --app {app_name}
   • Verify config: heroku config --app {app_name}
   • Test locally first: streamlit run app.py
    """)
    
    return True

if __name__ == "__main__":
    try:
        success = main()
        if success:
            print("\n🎉 Heroku environment setup completed successfully!")
        else:
            print("\n❌ Heroku environment setup failed.")
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️ Setup interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)
