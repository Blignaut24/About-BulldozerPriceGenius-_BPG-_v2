#!/usr/bin/env python3
"""
Test deployment configuration for BulldozerPriceGenius
"""

import os
import sys

def test_deployment_config():
    """Test all deployment configuration files"""
    
    print("BulldozerPriceGenius Deployment Configuration Test")
    print("=" * 55)
    
    # Test 1: Check required files (in parent directory)
    required_files = ['Procfile', 'requirements.txt', '.python-version', 'setup.sh', 'app.py']
    print('\nRequired Files Check:')
    all_files_present = True
    for file in required_files:
        file_path = os.path.join('..', file)
        if os.path.exists(file_path):
            print(f'✅ {file} exists')
        else:
            print(f'❌ {file} missing')
            all_files_present = False
    
    # Test 2: Check Python version in .python-version
    print('\nPython Version Check:')
    try:
        with open('../.python-version', 'r') as f:
            python_version = f.read().strip()
            print(f'✅ Python version: {python_version}')
    except:
        print('❌ Failed to read .python-version')

    # Test 3: Check gdown version in requirements.txt
    print('\nDependencies Check:')
    try:
        with open('../requirements.txt', 'r') as f:
            content = f.read()
            if 'gdown==5.2.0' in content:
                print('✅ gdown==5.2.0 specified correctly')
            else:
                print('❌ gdown version not correctly specified')
            
            if 'streamlit' in content:
                print('✅ Streamlit dependency found')
            else:
                print('❌ Streamlit dependency missing')
    except:
        print('❌ Failed to read requirements.txt')
    
    # Test 4: Check external model loader configuration
    print('\nModel Configuration Check:')
    try:
        sys.path.append('../src')
        from external_model_loader import ExternalModelLoader
        loader = ExternalModelLoader()
        file_id = loader._get_model_file_id()
        if file_id == '1mSIR9TnJvP4zpVHlrsMGm11WS-DWyyTp':
            print('✅ Model file ID configured correctly')
        else:
            print(f'❌ Model file ID incorrect: {file_id}')
    except Exception as e:
        print(f'❌ Model loader test failed: {e}')
    
    # Test 5: Check .slugignore
    print('\nDeployment Optimization Check:')
    if os.path.exists('.slugignore'):
        print('✅ .slugignore exists (deployment optimization)')
        with open('.slugignore', 'r') as f:
            content = f.read()
            if 'secrets.toml' in content:
                print('✅ secrets.toml excluded from deployment')
            else:
                print('❌ secrets.toml not excluded')
    else:
        print('❌ .slugignore missing')
    
    print('\nConfiguration test completed!')
    return all_files_present

if __name__ == "__main__":
    test_deployment_config()
