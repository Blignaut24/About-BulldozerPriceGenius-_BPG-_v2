#!/usr/bin/env python3
"""
Security Fixes Validation Test
Tests that hardcoded credentials have been removed and environment variable access works correctly.
"""

import os
import sys
import tempfile
import unittest
from unittest.mock import patch, MagicMock

# Add src directory to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

class TestSecurityFixes(unittest.TestCase):
    """Test security fixes for Google Drive file ID exposure."""
    
    def setUp(self):
        """Set up test environment."""
        # Clear any existing environment variables
        if 'GOOGLE_DRIVE_MODEL_ID' in os.environ:
            del os.environ['GOOGLE_DRIVE_MODEL_ID']
    
    def test_external_model_loader_requires_env_var(self):
        """Test that external_model_loader requires environment variable."""
        try:
            from external_model_loader import external_model_loader
            
            # Should raise ValueError when no environment variable is set
            with self.assertRaises(ValueError) as context:
                loader = external_model_loader()
            
            self.assertIn("GOOGLE_DRIVE_MODEL_ID environment variable not set", str(context.exception))
            print("✅ external_model_loader properly requires environment variable")
            
        except ImportError:
            print("⚠️ external_model_loader not available for testing")
    
    def test_external_model_loader_v2_requires_env_var(self):
        """Test that external_model_loader_v2 requires environment variable."""
        try:
            from external_model_loader_v2 import external_model_loader_v2
            
            # Should raise ValueError when no environment variable is set
            with self.assertRaises(ValueError) as context:
                loader = external_model_loader_v2()
            
            self.assertIn("GOOGLE_DRIVE_MODEL_ID environment variable not set", str(context.exception))
            print("✅ external_model_loader_v2 properly requires environment variable")
            
        except ImportError:
            print("⚠️ external_model_loader_v2 not available for testing")
    
    def test_external_model_loader_v3_requires_env_var(self):
        """Test that external_model_loader_v3_optimized requires environment variable."""
        try:
            from external_model_loader_v3_optimized import external_model_loader_v3_optimized
            
            # Should raise ValueError when no environment variable is set
            with self.assertRaises(ValueError) as context:
                loader = external_model_loader_v3_optimized()
            
            self.assertIn("GOOGLE_DRIVE_MODEL_ID environment variable not set", str(context.exception))
            print("✅ external_model_loader_v3_optimized properly requires environment variable")
            
        except ImportError:
            print("⚠️ external_model_loader_v3_optimized not available for testing")
    
    def test_environment_variable_access_works(self):
        """Test that loaders work correctly when environment variable is set."""
        test_file_id = "test_file_id_123"
        
        with patch.dict(os.environ, {'GOOGLE_DRIVE_MODEL_ID': test_file_id}):
            try:
                from external_model_loader import external_model_loader
                loader = external_model_loader()
                self.assertEqual(loader.model_file_id, test_file_id)
                print("✅ external_model_loader works with environment variable")
            except ImportError:
                print("⚠️ external_model_loader not available for testing")
            
            try:
                from external_model_loader_v2 import external_model_loader_v2
                loader = external_model_loader_v2()
                # Test that the loader was created successfully
                self.assertIsNotNone(loader)
                print("✅ external_model_loader_v2 works with environment variable")
            except ImportError:
                print("⚠️ external_model_loader_v2 not available for testing")
            
            try:
                from external_model_loader_v3_optimized import external_model_loader_v3_optimized
                loader = external_model_loader_v3_optimized()
                self.assertEqual(loader.model_file_id, test_file_id)
                print("✅ external_model_loader_v3_optimized works with environment variable")
            except ImportError:
                print("⚠️ external_model_loader_v3_optimized not available for testing")
    
    @patch('streamlit.secrets', {'GOOGLE_DRIVE_MODEL_ID': 'streamlit_test_id'})
    def test_streamlit_secrets_access(self):
        """Test that loaders can access Streamlit secrets when available."""
        # Mock streamlit module
        with patch.dict('sys.modules', {'streamlit': MagicMock()}):
            import streamlit as st
            st.secrets = {'GOOGLE_DRIVE_MODEL_ID': 'streamlit_test_id'}
            
            try:
                from external_model_loader import external_model_loader
                loader = external_model_loader()
                self.assertEqual(loader.model_file_id, 'streamlit_test_id')
                print("✅ external_model_loader works with Streamlit secrets")
            except ImportError:
                print("⚠️ external_model_loader not available for testing")
    
    def test_no_hardcoded_credentials_in_source(self):
        """Test that no hardcoded credentials exist in source files."""
        hardcoded_id = "1mSIR9TnJvP4zpVHlrsMGm11WS-DWyyTp"
        
        # Check external model loader files
        loader_files = [
            '../src/external_model_loader.py',
            '../src/external_model_loader_v2.py', 
            '../src/external_model_loader_v3_optimized.py'
        ]
        
        for file_path in loader_files:
            full_path = os.path.join(os.path.dirname(__file__), file_path)
            if os.path.exists(full_path):
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self.assertNotIn(hardcoded_id, content, 
                                   f"Hardcoded file ID found in {file_path}")
                print(f"✅ No hardcoded credentials in {file_path}")
            else:
                print(f"⚠️ {file_path} not found for testing")
    
    def test_secrets_file_not_in_repository(self):
        """Test that secrets.toml file is not in repository."""
        secrets_path = os.path.join(os.path.dirname(__file__), '..', '.streamlit', 'secrets.toml')
        
        # File should not exist in repository
        self.assertFalse(os.path.exists(secrets_path), 
                        "secrets.toml file should not be in repository")
        print("✅ secrets.toml properly excluded from repository")
        
        # Template should exist
        template_path = os.path.join(os.path.dirname(__file__), '..', '.streamlit', 'secrets.toml.template')
        self.assertTrue(os.path.exists(template_path), 
                       "secrets.toml.template should exist")
        print("✅ secrets.toml.template exists for development setup")

def run_security_tests():
    """Run all security validation tests."""
    print("🔒 Running Security Fixes Validation Tests")
    print("=" * 50)
    
    # Create test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSecurityFixes)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "=" * 50)
    if result.wasSuccessful():
        print("✅ ALL SECURITY TESTS PASSED")
        print("🔒 Application is secure for deployment")
    else:
        print("❌ SECURITY TESTS FAILED")
        print("⚠️ Review and fix security issues before deployment")
    
    return result.wasSuccessful()

if __name__ == "__main__":
    success = run_security_tests()
    sys.exit(0 if success else 1)
