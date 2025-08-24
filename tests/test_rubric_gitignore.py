#!/usr/bin/env python3
"""
Test that rubric files are properly excluded by .gitignore
"""

import os
import subprocess
import tempfile

def test_rubric_gitignore():
    """Test that various rubric file patterns are ignored by git"""
    
    print("Testing Rubric File .gitignore Exclusions")
    print("=" * 45)
    
    # Test patterns that should be ignored
    test_patterns = [
        "rubric",
        "rubric.txt", 
        "rubric.pdf",
        "my_rubric.doc",
        "project_rubric_v1.xlsx",
        "RUBRIC.md",
        "RUBRIC_FINAL.pdf",
        "grading_rubric.txt",
        "assessment_rubric.docx",
        "test.rubric"
    ]
    
    success_count = 0
    total_tests = len(test_patterns)
    
    for pattern in test_patterns:
        try:
            # Create a temporary test file
            with open(pattern, 'w') as f:
                f.write("Test rubric content")
            
            # Check if git ignores this file
            result = subprocess.run(
                ['git', 'check-ignore', pattern], 
                capture_output=True, 
                text=True,
                cwd='.'
            )
            
            if result.returncode == 0:
                print(f"✅ {pattern:25} - Successfully ignored")
                success_count += 1
            else:
                print(f"❌ {pattern:25} - NOT ignored (should be)")
            
            # Clean up test file
            if os.path.exists(pattern):
                os.remove(pattern)
                
        except Exception as e:
            print(f"⚠️  {pattern:25} - Test error: {e}")
            # Clean up on error
            if os.path.exists(pattern):
                os.remove(pattern)
    
    print(f"\n📊 Test Results: {success_count}/{total_tests} patterns correctly ignored")
    
    if success_count == total_tests:
        print("🎯 All rubric patterns successfully excluded!")
        return True
    else:
        print("⚠️  Some rubric patterns may not be properly excluded")
        return False

def verify_existing_rubric():
    """Verify that existing rubric file is ignored"""
    print("\n🔍 Verifying Existing Rubric File:")
    print("-" * 35)
    
    if os.path.exists('rubric'):
        try:
            result = subprocess.run(
                ['git', 'check-ignore', 'rubric'], 
                capture_output=True, 
                text=True,
                cwd='.'
            )
            
            if result.returncode == 0:
                print("✅ Existing 'rubric' file is properly ignored")
                return True
            else:
                print("❌ Existing 'rubric' file is NOT being ignored")
                return False
        except Exception as e:
            print(f"⚠️  Error checking existing rubric file: {e}")
            return False
    else:
        print("ℹ️  No existing 'rubric' file found")
        return True

def main():
    """Main test function"""
    print("🧪 BulldozerPriceGenius Rubric .gitignore Test")
    print("=" * 50)
    
    # Test 1: Pattern matching
    patterns_success = test_rubric_gitignore()
    
    # Test 2: Existing file
    existing_success = verify_existing_rubric()
    
    print(f"\n📋 Final Results:")
    print("-" * 20)
    
    if patterns_success and existing_success:
        print("✅ All rubric exclusion tests PASSED")
        print("🔒 Rubric files are properly protected from version control")
        print("🎯 Assessment criteria confidentiality maintained")
    else:
        print("❌ Some rubric exclusion tests FAILED")
        print("⚠️  Review .gitignore patterns for rubric files")

if __name__ == "__main__":
    main()
