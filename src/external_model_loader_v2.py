"""
External Model Loader V2 for BulldozerPriceGenius
Simplified version using gdown library to handle Google Drive large files
"""

import os
import pickle
import streamlit as st
from typing import Optional, Tuple, Any
import time
import tempfile

# Import gdown at module level to ensure it's available
try:
    import gdown
    GDOWN_AVAILABLE = True
except ImportError:
    GDOWN_AVAILABLE = False
    gdown = None


class ExternalModelLoaderV2:
    """
    Simplified external model loader using gdown library.
    Specifically designed to handle Google Drive large file downloads.
    """

    def __init__(self):
        # Google Drive file ID for the 561MB RandomForest model
        self.model_file_id = self._get_model_file_id()

        # Preprocessing components (small file, can be local)
        self.preprocessing_path = "src/models/preprocessing_components.pkl"

    def _get_cache_decorator(self):
        """Get the appropriate caching decorator based on Streamlit version"""
        if hasattr(st, 'cache_resource'):
            return st.cache_resource
        elif hasattr(st, 'cache'):
            return st.cache(allow_output_mutation=True)
        else:
            # No caching available
            def no_cache(func):
                return func
            return no_cache
    
    def _get_model_file_id(self) -> str:
        """Get the Google Drive file ID from environment variables or default."""
        # Try to get from Streamlit secrets first (for Streamlit Cloud)
        try:
            if hasattr(st, 'secrets') and 'GOOGLE_DRIVE_MODEL_ID' in st.secrets:
                return st.secrets['GOOGLE_DRIVE_MODEL_ID']
        except Exception:
            pass
        
        # Try environment variable (for Heroku)
        file_id = os.getenv('GOOGLE_DRIVE_MODEL_ID')
        if file_id:
            return file_id
        
        # Default file ID for the BulldozerPriceGenius model
        return "1mSIR9TnJvP4zpVHlrsMGm11WS-DWyyTp"
    
    def load_model_from_google_drive(_self) -> Tuple[Optional[Any], Optional[dict], Optional[str]]:
        """
        Download and cache the ML model from Google Drive using gdown library.
        
        Returns:
            Tuple of (model, preprocessing_data, error_message)
        """
        try:
            # File ID is now configured by default, no need to check for placeholder
            
            # Show progress to user
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            status_text.text("🔄 Initializing model download from Google Drive...")
            progress_bar.progress(10)
            
            start_time = time.time()
            
            # Try gdown library (best for large Google Drive files)
            if GDOWN_AVAILABLE:
                try:
                    status_text.text("🌐 Connecting to Google Drive...")
                    progress_bar.progress(20)

                    # Create temporary file for download
                    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.pkl')
                    temp_file.close()

                    # Construct download URL
                    download_url = f"https://drive.google.com/uc?id={_self.model_file_id}"

                    status_text.text("📥 Downloading model file (561MB)...")
                    progress_bar.progress(30)

                    # Download with gdown (handles Google Drive confirmation pages automatically)
                    success = gdown.download(
                        download_url,
                        temp_file.name,
                        quiet=True,  # Suppress gdown output
                        fuzzy=True   # Enable fuzzy matching for better compatibility
                    )

                    progress_bar.progress(70)

                    # Check if download was successful
                    if success and os.path.exists(temp_file.name):
                        file_size = os.path.getsize(temp_file.name)

                        if file_size > 1024 * 1024:  # At least 1MB
                            status_text.text("🔧 Loading model into memory...")
                            progress_bar.progress(80)

                            # Load the model
                            with open(temp_file.name, 'rb') as f:
                                model = pickle.load(f)

                            # Clean up temp file
                            os.unlink(temp_file.name)

                            # Verify model is valid
                            if hasattr(model, 'predict'):
                                progress_bar.progress(90)
                                status_text.text("📊 Loading preprocessing components...")

                                # Load preprocessing components (local file)
                                preprocessing_data = None
                                try:
                                    if os.path.exists(_self.preprocessing_path):
                                        with open(_self.preprocessing_path, 'rb') as f:
                                            preprocessing_data = pickle.load(f)
                                except Exception as e:
                                    st.warning(f"Could not load preprocessing components: {e}")

                                progress_bar.progress(100)
                                download_time = time.time() - start_time
                                status_text.text(f"✅ Model loaded successfully in {download_time:.1f} seconds!")

                                # Clear progress indicators after a short delay
                                time.sleep(2)
                                progress_bar.empty()
                                status_text.empty()

                                return model, preprocessing_data, None
                            else:
                                # Clean up and report error
                                if os.path.exists(temp_file.name):
                                    os.unlink(temp_file.name)
                                raise Exception("Downloaded file is not a valid ML model")
                        else:
                            # File too small, likely an error page
                            if os.path.exists(temp_file.name):
                                os.unlink(temp_file.name)
                            raise Exception(f"Downloaded file too small ({file_size} bytes), likely an error page")
                    else:
                        # Download failed
                        if os.path.exists(temp_file.name):
                            os.unlink(temp_file.name)
                        raise Exception("gdown download failed or returned no file")

                except Exception as e:
                    error_msg = (
                        "🚫 **Google Drive Download Failed**\n\n"
                        f"Unable to download the model file from Google Drive.\n\n"
                        f"**Error details:** {str(e)}\n\n"
                        "**Possible causes:**\n"
                        "• Google Drive file sharing permissions\n"
                        "• Network connectivity issues\n"
                        "• File ID incorrect or file moved/deleted\n"
                        "• Google Drive temporary restrictions\n\n"
                        "**Fallback:** Using statistical prediction instead."
                    )
                    return None, None, error_msg
                    
            else:
                # gdown is not available - add debugging info
                try:
                    import gdown as debug_gdown
                    debug_info = f"gdown version: {debug_gdown.__version__}"
                except ImportError as debug_e:
                    debug_info = f"gdown import error: {debug_e}"

                error_msg = (
                    "📦 **Missing Dependency (Debug Info)**\n\n"
                    f"GDOWN_AVAILABLE flag: {GDOWN_AVAILABLE}\n"
                    f"Debug import test: {debug_info}\n\n"
                    "The 'gdown' library is required for downloading large files from Google Drive. "
                    "Please install it with: pip install gdown\n\n"
                    "**Fallback:** Using statistical prediction instead."
                )
                return None, None, error_msg
            
        except Exception as e:
            error_msg = (
                f"❌ **Unexpected Error**\n\n"
                f"An unexpected error occurred while loading the model: {str(e)}\n\n"
                f"Please try refreshing the page or contact support if the issue persists."
            )
            return None, None, error_msg
        
        finally:
            # Clean up progress indicators if they still exist
            try:
                progress_bar.empty()
                status_text.empty()
            except:
                pass
    
    def get_model_info(self) -> dict:
        """Get information about the external model configuration."""
        return {
            'model_source': 'Google Drive (gdown)',
            'model_file_id': self.model_file_id,
            'download_method': 'gdown library',
            'preprocessing_path': self.preprocessing_path,
            'cache_enabled': True,
            'expected_size': '561MB'
        }
    
    def clear_model_cache(self):
        """Clear the cached model to force re-download."""
        try:
            # Clear the specific method cache
            self.load_model_from_google_drive.clear()

            # Also clear all Streamlit caches
            if hasattr(st, 'cache_resource'):
                st.cache_resource.clear()
            if hasattr(st, 'cache_data'):
                st.cache_data.clear()

            st.success("All caches cleared. The model will be re-downloaded on next use.")
        except Exception as e:
            st.error(f"Error clearing cache: {e}")


# Apply caching decorator dynamically based on Streamlit version
def _apply_cache_decorator():
    """Apply the appropriate caching decorator to the load method"""
    loader_instance = ExternalModelLoaderV2()
    cache_decorator = loader_instance._get_cache_decorator()
    loader_instance.load_model_from_google_drive = cache_decorator(loader_instance.load_model_from_google_drive)
    return loader_instance

# Global instance for easy access
external_model_loader_v2 = _apply_cache_decorator()
