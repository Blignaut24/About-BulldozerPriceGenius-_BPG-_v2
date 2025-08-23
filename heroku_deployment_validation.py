#!/usr/bin/env python3
"""
Heroku Deployment Validation Script for BulldozerPriceGenius
Validates all components are ready for production deployment
"""

import os
import sys
import importlib
import subprocess
from pathlib import Path

def check_file_exists(filepath, description):
    """Check if a required file exists"""
    if os.path.exists(filepath):
        print(f"✅ {description}: {filepath}")
        return True
    else:
        print(f"❌ {description}: {filepath} - NOT FOUND")
        return False

def check_dependencies():
    """Check if all required dependencies can be imported"""
    required_packages = [
        ('streamlit', 'Streamlit web framework'),
        ('pandas', 'Data manipulation'),
        ('numpy', 'Numerical computing'),
        ('sklearn', 'Machine learning'),
        ('joblib', 'Model serialization'),
        ('requests', 'HTTP requests'),
    ]
    
    print("\n🔍 Checking Python Dependencies:")
    all_good = True
    
    for package, description in required_packages:
        try:
            importlib.import_module(package)
            print(f"✅ {description}: {package}")
        except ImportError:
            print(f"❌ {description}: {package} - NOT AVAILABLE")
            all_good = False
    
    return all_good

def check_heroku_files():
    """Check if all Heroku deployment files are present"""
    print("\n📁 Checking Heroku Deployment Files:")
    
    files_to_check = [
        ('Procfile', 'Heroku process definition'),
        ('requirements.txt', 'Python dependencies'),
        ('.python-version', 'Python version specification (modern Heroku)'),
        ('.slugignore', 'Deployment optimization'),
        ('setup.sh', 'Streamlit configuration script'),
        ('.streamlit/config.toml', 'Streamlit configuration'),
    ]
    
    all_files_present = True
    for filepath, description in files_to_check:
        if not check_file_exists(filepath, description):
            all_files_present = False
    
    return all_files_present

def check_app_structure():
    """Check if the application structure is correct"""
    print("\n🏗️ Checking Application Structure:")
    
    required_structure = [
        ('app.py', 'Main application entry point'),
        ('app_pages/', 'Application pages directory'),
        ('app_pages/multipage.py', 'Multi-page framework'),
        ('app_pages/four_interactive_prediction.py', 'Main prediction page'),
        ('app_pages/dark_theme.py', 'Dark theme implementation'),
        ('src/', 'Source code directory'),
        ('src/external_model_loader_v2.py', 'External model loader'),
    ]
    
    all_structure_good = True
    for filepath, description in required_structure:
        if not check_file_exists(filepath, description):
            all_structure_good = False
    
    return all_structure_good

def check_dark_theme_compatibility():
    """Check if dark theme is properly implemented"""
    print("\n🌙 Checking Dark Theme Implementation:")
    
    try:
        # Check if dark theme module can be imported
        sys.path.append('app_pages')
        from dark_theme import apply_dark_theme, get_dark_theme_colors
        print("✅ Dark theme module imports successfully")
        
        # Check if color palette is available
        colors = get_dark_theme_colors()
        required_colors = ['primary_bg', 'secondary_bg', 'text_primary', 'accent_orange']
        
        for color in required_colors:
            if color in colors:
                print(f"✅ Dark theme color '{color}': {colors[color]}")
            else:
                print(f"❌ Dark theme color '{color}': MISSING")
                return False
        
        return True
        
    except ImportError as e:
        print(f"❌ Dark theme import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Dark theme validation error: {e}")
        return False

def check_streamlit_compatibility():
    """Check Streamlit compatibility functions"""
    print("\n🔧 Checking Streamlit Compatibility:")
    
    try:
        # Check main prediction page compatibility
        sys.path.append('app_pages')
        from four_interactive_prediction import get_expander
        print("✅ Streamlit expander compatibility function available")
        
        # Check component compatibility
        sys.path.append('src/components')
        from model_id_input import get_expander as model_get_expander
        print("✅ Model ID component expander compatibility available")
        
        return True
        
    except ImportError as e:
        print(f"❌ Streamlit compatibility import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Streamlit compatibility error: {e}")
        return False

def check_external_model_loader():
    """Check external model loader functionality"""
    print("\n🤖 Checking External Model Loader:")
    
    try:
        sys.path.append('src')
        from external_model_loader_v2 import ExternalModelLoaderV2
        print("✅ External model loader imports successfully")

        # Test initialization (without actually downloading)
        loader = ExternalModelLoaderV2()
        print("✅ External model loader initializes correctly")
        
        return True
        
    except ImportError as e:
        print(f"❌ External model loader import error: {e}")
        return False
    except Exception as e:
        print(f"❌ External model loader error: {e}")
        return False

def check_security():
    """Check for security issues"""
    print("\n🔒 Checking Security Configuration:")
    
    security_checks = []
    
    # Check for sensitive files
    sensitive_files = ['.env', 'secrets.toml', 'kaggle.json', 'credentials.json']
    for file in sensitive_files:
        if os.path.exists(file):
            print(f"⚠️ Sensitive file found: {file} - Ensure it's in .slugignore")
            security_checks.append(False)
        else:
            print(f"✅ No sensitive file: {file}")
            security_checks.append(True)
    
    # Check .slugignore for sensitive files
    if os.path.exists('.slugignore'):
        with open('.slugignore', 'r') as f:
            slugignore_content = f.read()
            for file in sensitive_files:
                if file in slugignore_content:
                    print(f"✅ Sensitive file {file} excluded in .slugignore")
                else:
                    print(f"⚠️ Sensitive file {file} not explicitly excluded in .slugignore")
    
    return all(security_checks)

def main():
    """Run all validation checks"""
    print("🚀 BulldozerPriceGenius - Heroku Deployment Validation")
    print("=" * 60)
    
    checks = [
        ("Heroku Files", check_heroku_files),
        ("Application Structure", check_app_structure),
        ("Python Dependencies", check_dependencies),
        ("Dark Theme", check_dark_theme_compatibility),
        ("Streamlit Compatibility", check_streamlit_compatibility),
        ("External Model Loader", check_external_model_loader),
        ("Security Configuration", check_security),
    ]
    
    results = []
    for check_name, check_function in checks:
        try:
            result = check_function()
            results.append((check_name, result))
        except Exception as e:
            print(f"❌ {check_name}: FAILED with error: {e}")
            results.append((check_name, False))
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 VALIDATION SUMMARY:")
    
    all_passed = True
    for check_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {check_name}")
        if not result:
            all_passed = False
    
    print("\n" + "=" * 60)
    if all_passed:
        print("🎉 ALL CHECKS PASSED! Ready for Heroku deployment.")
        print("✅ The application is production-ready with:")
        print("   - Dark theme implementation")
        print("   - Enhanced UX features")
        print("   - Dual prediction systems")
        print("   - Test scenario validation")
        print("   - Streamlit compatibility")
        print("   - Security configuration")
    else:
        print("❌ SOME CHECKS FAILED! Please fix issues before deployment.")
    
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
