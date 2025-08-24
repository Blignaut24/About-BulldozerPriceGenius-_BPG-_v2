#!/usr/bin/env python3
"""
Test script to verify UI color changes in four_interactive_prediction.py
"""

import sys
import os

# Add paths for imports
sys.path.append('app_pages')
sys.path.append('src')

def test_color_imports():
    """Test that the color imports work correctly"""
    try:
        from app_pages.dark_theme import get_dark_theme_colors
        colors = get_dark_theme_colors()
        
        print("✅ Dark theme colors imported successfully")
        print(f"   - Info background: {colors['info_bg']}")
        print(f"   - Info text: {colors['info_text']}")
        print(f"   - Warning background: {colors['warning_bg']}")
        print(f"   - Warning text: {colors['warning_text']}")
        print(f"   - Accent blue: {colors['accent_blue']}")
        print(f"   - Accent orange: {colors['accent_orange']}")
        print(f"   - Border color: {colors['border_color']}")
        
        return True
    except Exception as e:
        print(f"❌ Error importing colors: {e}")
        return False

def test_file_syntax():
    """Test that the modified file has valid Python syntax"""
    try:
        import py_compile
        py_compile.compile('app_pages/four_interactive_prediction.py', doraise=True)
        print("✅ four_interactive_prediction.py syntax is valid")
        return True
    except Exception as e:
        print(f"❌ Syntax error in four_interactive_prediction.py: {e}")
        return False

def test_color_values():
    """Test that the color values are appropriate for dark theme"""
    try:
        from app_pages.dark_theme import get_dark_theme_colors
        colors = get_dark_theme_colors()
        
        # Test blue colors for Enhanced ML Model and sale timing sections
        assert colors['info_bg'] == '#0c4a6e', f"Expected #0c4a6e, got {colors['info_bg']}"
        assert colors['info_text'] == '#cce7ff', f"Expected #cce7ff, got {colors['info_text']}"
        assert colors['accent_blue'] == '#17a2b8', f"Expected #17a2b8, got {colors['accent_blue']}"
        
        # Test orange colors for section headers
        assert colors['warning_bg'] == '#7c2d12', f"Expected #7c2d12, got {colors['warning_bg']}"
        assert colors['warning_text'] == '#fed7aa', f"Expected #fed7aa, got {colors['warning_text']}"
        assert colors['accent_orange'] == '#FF6B35', f"Expected #FF6B35, got {colors['accent_orange']}"
        
        print("✅ Color values are correct for dark theme")
        return True
    except Exception as e:
        print(f"❌ Color value test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing UI Color Changes")
    print("=" * 50)
    
    tests = [
        test_file_syntax,
        test_color_imports,
        test_color_values
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! UI changes are ready.")
        return True
    else:
        print("⚠️ Some tests failed. Please review the issues above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
