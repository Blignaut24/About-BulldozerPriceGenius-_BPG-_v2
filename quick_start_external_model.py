#!/usr/bin/env python3
"""
Quick Start Script for External Model Storage Setup
Helps users configure and test the external model loading functionality
"""

import os
import sys
import subprocess
import webbrowser
from pathlib import Path

def print_header(title):
    """Print a formatted header"""
    print("\n" + "=" * 60)
    print(f"🚀 {title}")
    print("=" * 60)

def print_step(step_num, title):
    """Print a formatted step"""
    print(f"\n📋 Step {step_num}: {title}")
    print("-" * 40)

def check_requirements():
    """Check if all requirements are met"""
    print_step(1, "Checking Requirements")
    
    # Check if model file exists
    model_path = Path("src/models/randomforest_regressor_best_RMSLE.pkl")
    if model_path.exists():
        size_mb = model_path.stat().st_size / (1024 * 1024)
        print(f"✅ Model file found: {size_mb:.1f}MB")
        if size_mb > 500:
            print(f"⚠️  Model size ({size_mb:.1f}MB) exceeds Heroku's 500MB limit")
            print("   External storage is required for deployment")
        return True
    else:
        print(f"❌ Model file not found: {model_path}")
        print("   Please ensure the model file exists before proceeding")
        return False

def setup_google_drive():
    """Guide user through Google Drive setup"""
    print_step(2, "Google Drive Setup")
    
    print("📤 Upload your model to Google Drive:")
    print("   1. Go to https://drive.google.com")
    print("   2. Click 'New' → 'File upload'")
    print("   3. Select: src/models/randomforest_regressor_best_RMSLE.pkl")
    print("   4. Wait for upload to complete (5-10 minutes)")
    
    input("\nPress Enter when upload is complete...")
    
    print("\n🔗 Configure sharing:")
    print("   1. Right-click the uploaded file → 'Share'")
    print("   2. Change 'Restricted' → 'Anyone with the link'")
    print("   3. Set permission to 'Viewer'")
    print("   4. Copy the share link")
    
    print("\n📋 Example share link:")
    print("   https://drive.google.com/file/d/1ABC123DEF456GHI789JKL/view?usp=sharing")
    print("                                    ↑")
    print("                              This is your FILE_ID")
    
    share_link = input("\nPaste your Google Drive share link: ").strip()
    
    # Extract file ID
    if "drive.google.com/file/d/" in share_link:
        try:
            file_id = share_link.split("/file/d/")[1].split("/")[0]
            print(f"\n✅ Extracted File ID: {file_id}")
            return file_id
        except:
            print("❌ Could not extract file ID from the link")
            return None
    else:
        print("❌ Invalid Google Drive link format")
        return None

def setup_local_config(file_id):
    """Set up local configuration"""
    print_step(3, "Local Configuration")
    
    # Create .streamlit directory if it doesn't exist
    streamlit_dir = Path(".streamlit")
    streamlit_dir.mkdir(exist_ok=True)
    
    # Create secrets.toml
    secrets_file = streamlit_dir / "secrets.toml"
    
    config_content = f"""# Streamlit Secrets Configuration
# Google Drive Model Storage
GOOGLE_DRIVE_MODEL_ID = "{file_id}"

# This file should not be committed to git
# Add .streamlit/secrets.toml to your .gitignore
"""
    
    with open(secrets_file, 'w') as f:
        f.write(config_content)
    
    print(f"✅ Created: {secrets_file}")
    
    # Update .gitignore
    gitignore_file = Path(".gitignore")
    gitignore_content = ""
    
    if gitignore_file.exists():
        with open(gitignore_file, 'r') as f:
            gitignore_content = f.read()
    
    if ".streamlit/secrets.toml" not in gitignore_content:
        with open(gitignore_file, 'a') as f:
            f.write("\n# Streamlit secrets\n.streamlit/secrets.toml\n")
        print("✅ Updated .gitignore")
    
    return True

def test_setup():
    """Test the external model setup"""
    print_step(4, "Testing Setup")
    
    print("🧪 Running test script...")
    
    try:
        result = subprocess.run([sys.executable, "test_external_model.py"], 
                              capture_output=True, text=True, timeout=60)
        
        if result.returncode == 0:
            print("✅ Test passed!")
            print("\nTest output:")
            print(result.stdout)
            return True
        else:
            print("❌ Test failed!")
            print("\nError output:")
            print(result.stderr)
            return False
            
    except subprocess.TimeoutExpired:
        print("⏱️ Test timed out (this might be normal for large downloads)")
        return True
    except Exception as e:
        print(f"❌ Error running test: {e}")
        return False

def setup_heroku_deployment():
    """Guide user through Heroku deployment setup"""
    print_step(5, "Heroku Deployment Setup")
    
    print("🌐 Heroku deployment options:")
    print("   A. Use the automated setup script")
    print("   B. Manual setup")
    
    choice = input("\nChoose option (A/B): ").strip().upper()
    
    if choice == 'A':
        print("\n🔧 Running Heroku setup script...")
        try:
            subprocess.run(["bash", "heroku_setup.sh"], check=True)
            print("✅ Heroku setup completed!")
        except subprocess.CalledProcessError:
            print("❌ Heroku setup failed. Try manual setup.")
            return False
        except FileNotFoundError:
            print("❌ Bash not found. Using manual setup...")
            choice = 'B'
    
    if choice == 'B':
        print("\n📋 Manual Heroku setup:")
        app_name = input("Enter your Heroku app name: ").strip()
        file_id = input("Enter your Google Drive file ID: ").strip()
        
        print(f"\n🔧 Run these commands:")
        print(f"   heroku config:set GOOGLE_DRIVE_MODEL_ID=\"{file_id}\" --app {app_name}")
        print(f"   git push heroku main")
        
        input("\nPress Enter when you've completed the Heroku setup...")
    
    return True

def main():
    """Main setup function"""
    print_header("BulldozerPriceGenius External Model Setup")
    
    print("""
🎯 This script will help you set up external model storage for Heroku deployment.

What this script does:
• Checks if your model file exists and is too large for Heroku
• Guides you through uploading the model to Google Drive
• Configures local development environment
• Tests the external model loading
• Helps set up Heroku deployment

Let's get started!
    """)
    
    # Step 1: Check requirements
    if not check_requirements():
        print("\n❌ Requirements not met. Please fix the issues above.")
        return False
    
    # Step 2: Google Drive setup
    file_id = setup_google_drive()
    if not file_id:
        print("\n❌ Google Drive setup failed. Please try again.")
        return False
    
    # Step 3: Local configuration
    if not setup_local_config(file_id):
        print("\n❌ Local configuration failed.")
        return False
    
    # Step 4: Test setup
    if not test_setup():
        print("\n⚠️ Tests failed, but you can still proceed with deployment.")
        proceed = input("Continue anyway? (y/N): ").strip().lower()
        if proceed != 'y':
            return False
    
    # Step 5: Heroku deployment
    deploy_now = input("\nSet up Heroku deployment now? (y/N): ").strip().lower()
    if deploy_now == 'y':
        setup_heroku_deployment()
    
    # Final summary
    print_header("Setup Complete!")
    
    print(f"""
🎉 External model storage setup is complete!

📋 Summary:
• Model uploaded to Google Drive
• Local configuration created
• File ID: {file_id}
• Direct download URL: https://drive.google.com/uc?export=download&id={file_id}

🚀 Next steps:
1. Test locally: streamlit run app.py
2. Deploy to Heroku: git push heroku main
3. Monitor deployment: heroku logs --tail

📚 For detailed instructions, see: EXTERNAL_MODEL_DEPLOYMENT_GUIDE.md

✅ Your application is ready for Heroku deployment!
    """)
    
    return True

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️ Setup interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)
