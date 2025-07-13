#!/usr/bin/env python3
"""
Security Audit Script for Heroku Deployment
Checks for sensitive information that should not be deployed.
"""

import os
import re
import sys
from pathlib import Path

def check_sensitive_patterns():
    """Check for sensitive patterns in files"""
    print("🔍 Scanning for sensitive patterns...")
    
    # Patterns that indicate sensitive information
    sensitive_patterns = [
        (r'api[_-]?key\s*[=:]\s*["\']?[a-zA-Z0-9]{20,}', "API Key"),
        (r'secret[_-]?key\s*[=:]\s*["\']?[a-zA-Z0-9]{20,}', "Secret Key"),
        (r'password\s*[=:]\s*["\']?[a-zA-Z0-9]{8,}', "Password"),
        (r'token\s*[=:]\s*["\']?[a-zA-Z0-9]{20,}', "Token"),
        (r'[a-zA-Z0-9]{32,}', "Long string (potential key)"),
        (r'mongodb://.*', "MongoDB connection string"),
        (r'postgres://.*', "PostgreSQL connection string"),
        (r'mysql://.*', "MySQL connection string"),
        (r'redis://.*', "Redis connection string"),
    ]
    
    # File extensions to check
    check_extensions = ['.py', '.js', '.json', '.toml', '.yaml', '.yml', '.sh', '.env']
    
    # Directories to skip
    skip_dirs = {'.git', '__pycache__', 'node_modules', '.vscode', '.idea', 'venv', 'env', 'myenv'}
    
    issues_found = []
    
    for root, dirs, files in os.walk('.'):
        # Skip sensitive directories
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        
        for file in files:
            file_path = os.path.join(root, file)
            file_ext = os.path.splitext(file)[1].lower()
            
            # Skip binary files and non-text files
            if file_ext not in check_extensions:
                continue
            
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    
                for pattern, description in sensitive_patterns:
                    matches = re.finditer(pattern, content, re.IGNORECASE)
                    for match in matches:
                        # Skip very common false positives
                        matched_text = match.group()
                        if any(fp in matched_text.lower() for fp in ['example', 'placeholder', 'your_key_here', 'xxx', '123']):
                            continue
                        
                        issues_found.append({
                            'file': file_path,
                            'pattern': description,
                            'match': matched_text[:50] + '...' if len(matched_text) > 50 else matched_text,
                            'line': content[:match.start()].count('\n') + 1
                        })
                        
            except Exception as e:
                print(f"⚠️ Could not read {file_path}: {e}")
    
    return issues_found

def check_sensitive_files():
    """Check for sensitive files that should not be deployed"""
    print("\n📁 Checking for sensitive files...")
    
    sensitive_files = [
        '.env',
        '.env.local',
        '.env.production',
        'secrets.toml',
        '.streamlit/secrets.toml',
        'credentials.json',
        'kaggle.json',
        'cloudinary_python.txt',
        '.vscode/uptime.sh',
        '.vscode/heroku_config.sh',
        'config.ini',
        'local_settings.py',
    ]
    
    sensitive_patterns = [
        '*.key',
        '*.pem',
        '*.p12',
        '*.pfx',
        '*api_key*',
        '*secret*',
        '*password*',
        '*token*',
    ]
    
    found_files = []
    
    # Check specific files
    for file_path in sensitive_files:
        if os.path.exists(file_path):
            found_files.append(file_path)
    
    # Check pattern-based files
    for root, dirs, files in os.walk('.'):
        # Skip sensitive directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['__pycache__', 'node_modules', 'venv', 'env', 'myenv']]
        
        for file in files:
            file_path = os.path.join(root, file)
            for pattern in sensitive_patterns:
                import fnmatch
                if fnmatch.fnmatch(file.lower(), pattern):
                    found_files.append(file_path)
    
    return found_files

def check_slugignore_coverage():
    """Check if .slugignore properly excludes sensitive files"""
    print("\n🛡️ Checking .slugignore coverage...")
    
    if not os.path.exists('.slugignore'):
        return False, "No .slugignore file found"
    
    with open('.slugignore', 'r') as f:
        slugignore_content = f.read()
    
    required_exclusions = [
        '.env',
        '.vscode/',
        '*.key',
        '*secret*',
        '*api_key*',
        'secrets.toml',
    ]
    
    missing_exclusions = []
    for exclusion in required_exclusions:
        if exclusion not in slugignore_content:
            missing_exclusions.append(exclusion)
    
    if missing_exclusions:
        return False, f"Missing exclusions: {', '.join(missing_exclusions)}"
    
    return True, "All required exclusions present"

def check_gitignore_coverage():
    """Check if .gitignore properly excludes sensitive files"""
    print("\n🔒 Checking .gitignore coverage...")
    
    if not os.path.exists('.gitignore'):
        return False, "No .gitignore file found"
    
    with open('.gitignore', 'r') as f:
        gitignore_content = f.read()
    
    required_exclusions = [
        '.env',
        '*.key',
        '*secret*',
        '*api_key*',
        '.streamlit/secrets.toml',
        '.vscode/',
    ]
    
    missing_exclusions = []
    for exclusion in required_exclusions:
        if exclusion not in gitignore_content:
            missing_exclusions.append(exclusion)
    
    if missing_exclusions:
        return False, f"Missing exclusions: {', '.join(missing_exclusions)}"
    
    return True, "All required exclusions present"

def main():
    """Main security audit function"""
    print("🔒 SECURITY AUDIT FOR HEROKU DEPLOYMENT")
    print("=" * 70)
    
    # Check for sensitive patterns in code
    sensitive_patterns = check_sensitive_patterns()
    
    # Check for sensitive files
    sensitive_files = check_sensitive_files()
    
    # Check .slugignore coverage
    slugignore_ok, slugignore_msg = check_slugignore_coverage()
    
    # Check .gitignore coverage
    gitignore_ok, gitignore_msg = check_gitignore_coverage()
    
    # Report results
    print("\n" + "=" * 70)
    print("📋 SECURITY AUDIT RESULTS")
    print("=" * 70)
    
    # Sensitive patterns
    if sensitive_patterns:
        print("❌ SENSITIVE PATTERNS FOUND:")
        for issue in sensitive_patterns[:10]:  # Show first 10
            print(f"   📄 {issue['file']}:{issue['line']} - {issue['pattern']}")
            print(f"      Match: {issue['match']}")
        if len(sensitive_patterns) > 10:
            print(f"   ... and {len(sensitive_patterns) - 10} more issues")
    else:
        print("✅ No sensitive patterns found in code")
    
    # Sensitive files
    if sensitive_files:
        print("\n❌ SENSITIVE FILES FOUND:")
        for file_path in sensitive_files:
            print(f"   📁 {file_path}")
    else:
        print("\n✅ No sensitive files found")
    
    # .slugignore check
    print(f"\n{'✅' if slugignore_ok else '❌'} .slugignore: {slugignore_msg}")
    
    # .gitignore check
    print(f"{'✅' if gitignore_ok else '❌'} .gitignore: {gitignore_msg}")
    
    # Overall assessment
    total_issues = len(sensitive_patterns) + len(sensitive_files)
    config_issues = (not slugignore_ok) + (not gitignore_ok)
    
    print("\n" + "=" * 70)
    print("🎯 OVERALL SECURITY ASSESSMENT")
    print("=" * 70)
    
    if total_issues == 0 and config_issues == 0:
        print("🎉 SECURE FOR DEPLOYMENT!")
        print("✅ No sensitive information found")
        print("✅ Proper exclusion files configured")
        print("✅ Ready for Heroku deployment")
        return True
    elif total_issues == 0 and config_issues > 0:
        print("⚠️ MOSTLY SECURE")
        print("✅ No sensitive data found")
        print("🔧 Fix exclusion file issues before deployment")
        return False
    else:
        print("🚨 SECURITY ISSUES FOUND")
        print(f"❌ {total_issues} sensitive data issues")
        print(f"❌ {config_issues} configuration issues")
        print("🔧 MUST FIX before deployment")
        
        print("\n💡 RECOMMENDED ACTIONS:")
        if sensitive_patterns:
            print("1. Move hardcoded secrets to environment variables")
            print("2. Use Heroku config vars for sensitive data")
        if sensitive_files:
            print("3. Remove or exclude sensitive files")
            print("4. Update .gitignore and .slugignore")
        if not slugignore_ok:
            print("5. Fix .slugignore exclusions")
        if not gitignore_ok:
            print("6. Fix .gitignore exclusions")
        
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
