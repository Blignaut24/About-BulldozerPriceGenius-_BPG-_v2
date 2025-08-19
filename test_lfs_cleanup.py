#!/usr/bin/env python3
"""
Test script to verify Git LFS cleanup and Heroku deployment readiness
for BulldozerPriceGenius application.
"""

import os
import subprocess
import sys
from pathlib import Path

def run_command(cmd, capture_output=True):
    """Run a command and return the result."""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=capture_output, text=True)
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def check_lfs_status():
    """Check if any files are still tracked by Git LFS."""
    print("🔍 Checking Git LFS status...")
    
    success, stdout, stderr = run_command("git lfs ls-files")
    if success:
        if stdout.strip():
            print("❌ LFS files still tracked:")
            print(stdout)
            return False
        else:
            print("✅ No LFS files tracked")
            return True
    else:
        print(f"⚠️ Could not check LFS status: {stderr}")
        return False

def check_gitignore():
    """Check if .gitignore properly excludes large files."""
    print("\n🔍 Checking .gitignore configuration...")
    
    gitignore_path = Path(".gitignore")
    if not gitignore_path.exists():
        print("❌ .gitignore file not found")
        return False
    
    with open(gitignore_path, 'r') as f:
        content = f.read()
    
    required_patterns = [
        "data/",
        "*.csv",
        "*.pkl",
        "venv/",
        "myenv/"
    ]
    
    missing_patterns = []
    for pattern in required_patterns:
        if pattern not in content:
            missing_patterns.append(pattern)
    
    if missing_patterns:
        print(f"❌ Missing .gitignore patterns: {missing_patterns}")
        return False
    else:
        print("✅ .gitignore properly configured")
        return True

def check_external_model_loader():
    """Check if external model loader is properly configured."""
    print("\n🔍 Checking external model loader...")
    
    loader_path = Path("src/external_model_loader_v2.py")
    if not loader_path.exists():
        print("❌ External model loader V2 not found")
        return False
    
    with open(loader_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    if "gdown" in content and "GOOGLE_DRIVE_MODEL_ID" in content:
        print("✅ External model loader properly configured")
        return True
    else:
        print("❌ External model loader missing required components")
        return False

def check_heroku_files():
    """Check if all required Heroku deployment files exist."""
    print("\n🔍 Checking Heroku deployment files...")
    
    required_files = [
        "Procfile",
        "requirements.txt",
        ".python-version",
        "setup.sh",
        "app.py"
    ]
    
    missing_files = []
    for file in required_files:
        if not Path(file).exists():
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing Heroku files: {missing_files}")
        return False
    else:
        print("✅ All Heroku deployment files present")
        return True

def check_requirements():
    """Check if requirements.txt includes gdown."""
    print("\n🔍 Checking requirements.txt...")
    
    req_path = Path("requirements.txt")
    if not req_path.exists():
        print("❌ requirements.txt not found")
        return False
    
    with open(req_path, 'r') as f:
        content = f.read()
    
    if "gdown" in content:
        print("✅ gdown dependency found in requirements.txt")
        return True
    else:
        print("❌ gdown dependency missing from requirements.txt")
        return False

def check_repository_size():
    """Estimate repository size without LFS files."""
    print("\n🔍 Checking repository size...")
    
    success, stdout, stderr = run_command("git count-objects -vH")
    if success:
        print("📊 Repository size information:")
        print(stdout)
        
        # Look for size-pack line
        for line in stdout.split('\n'):
            if 'size-pack' in line:
                size_info = line.split()
                if len(size_info) >= 2:
                    size = size_info[1]
                    print(f"✅ Repository pack size: {size}")
                    return True
        
        print("✅ Repository size check completed")
        return True
    else:
        print(f"⚠️ Could not check repository size: {stderr}")
        return False

def main():
    """Run all deployment readiness checks."""
    print("BulldozerPriceGenius - Git LFS Cleanup Verification")
    print("=" * 55)
    
    checks = [
        ("Git LFS Status", check_lfs_status),
        (".gitignore Configuration", check_gitignore),
        ("External Model Loader", check_external_model_loader),
        ("Heroku Deployment Files", check_heroku_files),
        ("Requirements Dependencies", check_requirements),
        ("Repository Size", check_repository_size)
    ]
    
    passed = 0
    total = len(checks)
    
    for check_name, check_func in checks:
        try:
            if check_func():
                passed += 1
            else:
                print(f"❌ {check_name} check failed")
        except Exception as e:
            print(f"❌ {check_name} check error: {e}")
    
    print(f"\n📊 Summary: {passed}/{total} checks passed")
    
    if passed == total:
        print("🎉 All checks passed! Repository is ready for Heroku deployment.")
        print("\n🚀 Next steps:")
        print("1. Push changes to GitHub: git push origin main")
        print("2. Deploy to Heroku from the main branch")
        print("3. Set GOOGLE_DRIVE_MODEL_ID environment variable in Heroku")
        return True
    else:
        print("⚠️ Some checks failed. Please fix the issues before deploying.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
