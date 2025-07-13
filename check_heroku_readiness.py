#!/usr/bin/env python3
"""
Heroku Deployment Readiness Checker
Verifies that all required files and configurations are in place for Heroku deployment.
"""

import os
import sys

def check_file_exists(filepath, description):
    """Check if a file exists and return status"""
    if os.path.exists(filepath):
        size = os.path.getsize(filepath)
        print(f"✅ {description}: {filepath} ({size:,} bytes)")
        return True
    else:
        print(f"❌ {description}: {filepath} - NOT FOUND")
        return False

def check_requirements_txt():
    """Check requirements.txt for common issues"""
    print("\n📦 Checking requirements.txt...")
    
    if not os.path.exists("requirements.txt"):
        print("❌ requirements.txt not found")
        return False
    
    with open("requirements.txt", "r") as f:
        content = f.read()
        lines = [line.strip() for line in content.split('\n') if line.strip() and not line.startswith('#')]
    
    # Check for duplicates
    packages = [line.split('==')[0] for line in lines if '==' in line]
    duplicates = set([pkg for pkg in packages if packages.count(pkg) > 1])
    
    if duplicates:
        print(f"⚠️ Duplicate packages found: {', '.join(duplicates)}")
    else:
        print("✅ No duplicate packages found")
    
    # Check for Windows-specific packages
    windows_packages = ['pywin32', 'pyzmq']
    found_windows = [pkg for pkg in windows_packages if any(pkg in line for line in lines)]
    
    if found_windows:
        print(f"⚠️ Windows-specific packages found (may cause Heroku issues): {', '.join(found_windows)}")
    else:
        print("✅ No Windows-specific packages found")
    
    # Check for essential packages
    essential_packages = ['streamlit', 'pandas', 'numpy', 'scikit-learn']
    missing_essential = [pkg for pkg in essential_packages if not any(pkg in line for line in lines)]
    
    if missing_essential:
        print(f"❌ Missing essential packages: {', '.join(missing_essential)}")
        return False
    else:
        print("✅ All essential packages present")
    
    print(f"📊 Total packages: {len(lines)}")
    return True

def check_procfile():
    """Check Procfile configuration"""
    print("\n🚀 Checking Procfile...")
    
    if not os.path.exists("Procfile"):
        print("❌ Procfile not found")
        return False
    
    with open("Procfile", "r") as f:
        content = f.read().strip()
    
    if "streamlit run app.py" in content:
        print("✅ Streamlit command found in Procfile")
    else:
        print("❌ Streamlit command not found in Procfile")
        return False
    
    if "$PORT" in content:
        print("✅ PORT variable found in Procfile")
    else:
        print("⚠️ PORT variable not found in Procfile (may cause issues)")
    
    if "0.0.0.0" in content:
        print("✅ Address binding found in Procfile")
    else:
        print("⚠️ Address binding not found in Procfile (may cause issues)")
    
    return True

def check_runtime_txt():
    """Check runtime.txt for Python version"""
    print("\n🐍 Checking runtime.txt...")
    
    if not os.path.exists("runtime.txt"):
        print("⚠️ runtime.txt not found (Heroku will use default Python version)")
        return True
    
    with open("runtime.txt", "r") as f:
        content = f.read().strip()
    
    if content.startswith("python-"):
        print(f"✅ Python version specified: {content}")
        return True
    else:
        print(f"❌ Invalid runtime.txt format: {content}")
        return False

def check_app_structure():
    """Check essential app files"""
    print("\n📁 Checking app structure...")
    
    essential_files = [
        ("app.py", "Main application file"),
        ("app_pages/four_interactive_prediction.py", "Prediction page"),
        ("src/models/randomforest_regressor_best_RMSLE.pkl", "Model file"),
        ("setup.sh", "Streamlit setup script")
    ]
    
    all_present = True
    for filepath, description in essential_files:
        if not check_file_exists(filepath, description):
            all_present = False
    
    return all_present

def estimate_slug_size():
    """Estimate deployment slug size"""
    print("\n📏 Estimating slug size...")
    
    total_size = 0
    file_count = 0
    
    # Walk through directory and calculate size
    for root, dirs, files in os.walk("."):
        # Skip directories that should be ignored
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['__pycache__', 'node_modules']]
        
        for file in files:
            filepath = os.path.join(root, file)
            try:
                size = os.path.getsize(filepath)
                total_size += size
                file_count += 1
            except OSError:
                pass
    
    total_mb = total_size / (1024 * 1024)
    print(f"📊 Estimated total size: {total_mb:.1f} MB ({file_count:,} files)")
    
    if total_mb > 500:
        print("⚠️ Large slug size - consider adding more files to .slugignore")
    elif total_mb > 300:
        print("⚠️ Moderate slug size - deployment may be slow")
    else:
        print("✅ Good slug size for fast deployment")
    
    return total_mb < 500

def check_security():
    """Check for basic security issues"""
    print("\n🔒 Checking security...")

    # Check for common sensitive files
    sensitive_files = [
        '.env',
        '.vscode/uptime.sh',
        '.vscode/heroku_config.sh',
        'secrets.toml',
        '.streamlit/secrets.toml'
    ]

    found_sensitive = []
    for file_path in sensitive_files:
        if os.path.exists(file_path):
            found_sensitive.append(file_path)

    if found_sensitive:
        print(f"⚠️ Sensitive files found: {', '.join(found_sensitive)}")
        print("🔧 These should be excluded from deployment")
        return False
    else:
        print("✅ No obvious sensitive files found")

    # Check if .slugignore exists and has security exclusions
    if os.path.exists('.slugignore'):
        with open('.slugignore', 'r') as f:
            slugignore_content = f.read()

        security_patterns = ['.env', '.vscode/', '*secret*']
        missing_patterns = [p for p in security_patterns if p not in slugignore_content]

        if missing_patterns:
            print(f"⚠️ .slugignore missing security patterns: {', '.join(missing_patterns)}")
            return False
        else:
            print("✅ .slugignore has security exclusions")
    else:
        print("⚠️ No .slugignore file found")
        return False

    return True

def main():
    """Main checker function"""
    print("🚀 Heroku Deployment Readiness Checker")
    print("=" * 60)
    
    checks = [
        ("Requirements", check_requirements_txt),
        ("Procfile", check_procfile),
        ("Runtime", check_runtime_txt),
        ("App Structure", check_app_structure),
        ("Slug Size", estimate_slug_size),
        ("Security", check_security)
    ]
    
    results = {}
    
    for check_name, check_func in checks:
        try:
            results[check_name] = check_func()
        except Exception as e:
            print(f"❌ {check_name} check failed: {e}")
            results[check_name] = False
    
    # Summary
    print("\n" + "=" * 60)
    print("📋 HEROKU READINESS SUMMARY")
    print("=" * 60)
    
    passed_checks = sum(results.values())
    total_checks = len(results)
    
    for check_name, passed in results.items():
        status = "✅ READY" if passed else "❌ NEEDS ATTENTION"
        print(f"{check_name}: {status}")
    
    print(f"\nOverall: {passed_checks}/{total_checks} checks passed")
    
    if passed_checks == total_checks:
        print("\n🎉 READY FOR HEROKU DEPLOYMENT!")
        print("✅ All checks passed - you can deploy now")
        print("\n🚀 Next steps:")
        print("1. git add . && git commit -m 'feat: Ready for Heroku deployment'")
        print("2. heroku create your-app-name")
        print("3. git push heroku main")
        print("4. heroku open")
    elif passed_checks >= total_checks * 0.8:
        print("\n⚠️ MOSTLY READY")
        print("✅ Core requirements met")
        print("🔧 Address warnings for optimal deployment")
    else:
        print("\n❌ NOT READY FOR DEPLOYMENT")
        print("🚨 Multiple issues need to be resolved")
        print("📖 Check HEROKU_DEPLOYMENT_GUIDE.md for detailed instructions")
    
    print(f"\n📖 For detailed deployment instructions, see: HEROKU_DEPLOYMENT_GUIDE.md")

if __name__ == "__main__":
    main()
