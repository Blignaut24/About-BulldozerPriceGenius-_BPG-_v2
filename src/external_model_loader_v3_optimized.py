"""
External Model Loader V3 - Performance Optimized for Heroku
Optimized version with enhanced caching, timeout handling, and Heroku-specific improvements
"""

import os
import pickle
import streamlit as st
from typing import Optional, Tuple, Any
import time
import tempfile
import threading
from concurrent.futures import ThreadPoolExecutor, TimeoutError as FutureTimeoutError

# Import gdown at module level to ensure it's available
try:
    import gdown
    GDOWN_AVAILABLE = True
except ImportError:
    GDOWN_AVAILABLE = False
    gdown = None


class ExternalModelLoaderV3Optimized:
    """
    Performance-optimized external model loader for Heroku deployment.
    Features:
    - Enhanced caching with memory persistence
    - Timeout handling for network operations
    - Parallel loading of model and preprocessing components
    - Heroku-specific optimizations
    """
    
    def __init__(self):
        # Google Drive file ID for the 561MB RandomForest model
        self.model_file_id = self._get_model_file_id()
        
        # Preprocessing components (small file, can be local)
        self.preprocessing_path = "src/models/preprocessing_components.pkl"
        
        # Performance settings
        self.download_timeout = 300  # 5 minutes timeout for download
        self.load_timeout = 120      # 2 minutes timeout for model loading
        
        # Cache settings
        self._model_cache = None
        self._preprocessing_cache = None
        self._cache_timestamp = None
        self._cache_ttl = 3600  # 1 hour cache TTL
    
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
    
    def _is_cache_valid(self) -> bool:
        """Check if the current cache is still valid."""
        if self._model_cache is None or self._cache_timestamp is None:
            return False
        
        cache_age = time.time() - self._cache_timestamp
        return cache_age < self._cache_ttl
    
    def _load_preprocessing_components(self) -> Optional[dict]:
        """Load preprocessing components with caching."""
        if self._preprocessing_cache is not None:
            return self._preprocessing_cache
        
        try:
            if os.path.exists(self.preprocessing_path):
                with open(self.preprocessing_path, 'rb') as f:
                    preprocessing_data = pickle.load(f)
                self._preprocessing_cache = preprocessing_data
                return preprocessing_data
        except Exception as e:
            st.warning(f"Could not load preprocessing components: {e}")
        
        return None
    
    def _download_with_timeout(self, download_url: str, temp_file_path: str) -> bool:
        """Download model with timeout handling."""
        def download_task():
            return gdown.download(
                download_url,
                temp_file_path,
                quiet=True,
                fuzzy=True
            )
        
        with ThreadPoolExecutor(max_workers=1) as executor:
            future = executor.submit(download_task)
            try:
                result = future.result(timeout=self.download_timeout)
                return result is not None
            except FutureTimeoutError:
                st.error(f"⏰ Download timeout after {self.download_timeout} seconds")
                return False
            except Exception as e:
                st.error(f"❌ Download error: {e}")
                return False
    
    def _load_model_with_timeout(self, temp_file_path: str) -> Optional[Any]:
        """Load model from file with timeout handling."""
        def load_task():
            with open(temp_file_path, 'rb') as f:
                return pickle.load(f)
        
        with ThreadPoolExecutor(max_workers=1) as executor:
            future = executor.submit(load_task)
            try:
                model = future.result(timeout=self.load_timeout)
                return model
            except FutureTimeoutError:
                st.error(f"⏰ Model loading timeout after {self.load_timeout} seconds")
                return None
            except Exception as e:
                st.error(f"❌ Model loading error: {e}")
                return None
    
    @st.cache_resource
    def load_model_from_google_drive(_self) -> Tuple[Optional[Any], Optional[dict], Optional[str]]:
        """
        Download and cache the ML model from Google Drive with performance optimizations.
        
        Returns:
            Tuple of (model, preprocessing_data, error_message)
        """
        # Check if we have a valid cache
        if _self._is_cache_valid():
            st.info("⚡ Using cached model (fast load)")
            preprocessing_data = _self._load_preprocessing_components()
            return _self._model_cache, preprocessing_data, None
        
        try:
            # Show progress to user with performance info
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            status_text.text("🔄 Initializing optimized model download...")
            progress_bar.progress(5)
            
            start_time = time.time()
            
            # Try gdown library (best for large Google Drive files)
            if GDOWN_AVAILABLE:
                try:
                    status_text.text("🌐 Connecting to Google Drive (optimized)...")
                    progress_bar.progress(10)

                    # Create temporary file for download
                    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.pkl')
                    temp_file.close()

                    # Construct download URL
                    download_url = f"https://drive.google.com/uc?id={_self.model_file_id}"

                    status_text.text("📥 Downloading model file (561MB) with timeout protection...")
                    progress_bar.progress(15)

                    # Download with timeout handling
                    download_start = time.time()
                    success = _self._download_with_timeout(download_url, temp_file.name)
                    download_time = time.time() - download_start

                    if not success:
                        if os.path.exists(temp_file.name):
                            os.unlink(temp_file.name)
                        raise Exception("Download failed or timed out")

                    progress_bar.progress(60)
                    status_text.text(f"✅ Download completed in {download_time:.1f}s, loading model...")

                    # Check if download was successful
                    if os.path.exists(temp_file.name):
                        file_size = os.path.getsize(temp_file.name)

                        if file_size > 1024 * 1024:  # At least 1MB
                            progress_bar.progress(70)

                            # Load the model with timeout protection
                            load_start = time.time()
                            model = _self._load_model_with_timeout(temp_file.name)
                            load_time = time.time() - load_start

                            # Clean up temp file
                            os.unlink(temp_file.name)

                            if model is None:
                                raise Exception("Model loading failed or timed out")

                            # Verify model is valid
                            if hasattr(model, 'predict'):
                                progress_bar.progress(85)
                                status_text.text("📊 Loading preprocessing components...")

                                # Load preprocessing components in parallel
                                preprocessing_data = _self._load_preprocessing_components()

                                # Cache the model and timestamp
                                _self._model_cache = model
                                _self._cache_timestamp = time.time()

                                progress_bar.progress(100)
                                total_time = time.time() - start_time
                                status_text.text(f"✅ Model loaded successfully in {total_time:.1f}s (download: {download_time:.1f}s, load: {load_time:.1f}s)")

                                # Clear progress indicators after a short delay
                                time.sleep(2)
                                progress_bar.empty()
                                status_text.empty()

                                return model, preprocessing_data, None
                            else:
                                raise Exception("Downloaded file is not a valid ML model")
                        else:
                            # File too small, likely an error page
                            if os.path.exists(temp_file.name):
                                os.unlink(temp_file.name)
                            raise Exception(f"Downloaded file too small ({file_size} bytes), likely an error page")
                    else:
                        raise Exception("Download failed - no file created")

                except Exception as e:
                    error_msg = (
                        "🚫 **Optimized Google Drive Download Failed**\n\n"
                        f"Unable to download the model file from Google Drive.\n\n"
                        f"**Error details:** {str(e)}\n\n"
                        "**Performance Notes:**\n"
                        f"• Download timeout: {_self.download_timeout}s\n"
                        f"• Load timeout: {_self.load_timeout}s\n"
                        "• Using optimized download with timeout protection\n\n"
                        "**Possible causes:**\n"
                        "• Network connectivity issues (common on Heroku)\n"
                        "• Google Drive temporary restrictions\n"
                        "• Heroku dyno resource limitations\n"
                        "• File sharing permissions\n\n"
                        "**Fallback:** Using statistical prediction instead."
                    )
                    return None, None, error_msg
                    
            else:
                # gdown not available
                error_msg = (
                    "📦 **Missing Dependency (Optimized Version)**\n\n"
                    "The 'gdown' library is required for downloading large files from Google Drive. "
                    "Please install it with: pip install gdown\n\n"
                    "**Fallback:** Using statistical prediction instead."
                )
                return None, None, error_msg
            
        except Exception as e:
            error_msg = f"🚫 **Unexpected Error in Optimized Loader:** {str(e)}"
            return None, None, error_msg
    
    def get_model_info(self) -> dict:
        """Get information about the external model configuration."""
        cache_status = "Valid" if self._is_cache_valid() else "Invalid/Empty"
        cache_age = (time.time() - self._cache_timestamp) if self._cache_timestamp else 0
        
        return {
            'model_source': 'Google Drive (gdown) - Optimized',
            'model_file_id': self.model_file_id,
            'download_method': 'gdown library with timeout protection',
            'preprocessing_path': self.preprocessing_path,
            'cache_enabled': True,
            'cache_status': cache_status,
            'cache_age_seconds': int(cache_age),
            'cache_ttl_seconds': self._cache_ttl,
            'download_timeout': self.download_timeout,
            'load_timeout': self.load_timeout,
            'expected_size': '561MB'
        }
    
    def clear_model_cache(self):
        """Clear the cached model to force re-download."""
        try:
            # Clear internal cache
            self._model_cache = None
            self._preprocessing_cache = None
            self._cache_timestamp = None
            
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


# Global instance for easy access
external_model_loader_v3_optimized = ExternalModelLoaderV3Optimized()
