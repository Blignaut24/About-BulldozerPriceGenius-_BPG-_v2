"""
External Model Loader for BulldozerPriceGenius
Handles downloading and caching of large ML models from Google Drive
"""

import os
import pickle
import requests
import streamlit as st
from io import BytesIO
from typing import Optional, Tuple, Any
import time


class ExternalModelLoader:
    """
    Handles loading large ML models from external storage (Google Drive)
    to overcome Heroku's 500MB slug size limit.
    """
    
    def __init__(self):
        # Google Drive file ID for the 561MB RandomForest model
        # Replace this with your actual Google Drive file ID
        self.model_file_id = self._get_model_file_id()
        self.model_download_url = f"https://drive.google.com/uc?export=download&id={self.model_file_id}"
        
        # Preprocessing components (small file, can be local)
        self.preprocessing_path = "src/models/preprocessing_components.pkl"
    
    def _get_model_file_id(self) -> str:
        """
        Get the Google Drive file ID from environment variables or default.
        In production, set GOOGLE_DRIVE_MODEL_ID environment variable.
        """
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
        
        # Production file ID for BulldozerPriceGenius model (561MB RandomForest)
        # This is the public Google Drive file ID for the trained model
        return "1mSIR9TnJvP4zpVHlrsMGm11WS-DWyyTp"
    
    @st.cache_resource(max_entries=1, show_spinner="🔄 Loading ML Model...")
    def load_model_from_google_drive(_self) -> Tuple[Optional[Any], Optional[dict], Optional[str]]:
        """
        Download and cache the ML model from Google Drive.
        
        Returns:
            Tuple of (model, preprocessing_data, error_message)
        """
        try:
            # Check if file ID is configured
            if _self.model_file_id == "YOUR_GOOGLE_DRIVE_FILE_ID_HERE":
                error_msg = (
                    "🔧 **Model Configuration Required**\n\n"
                    "The Google Drive model file ID is not configured. "
                    "Please set the GOOGLE_DRIVE_MODEL_ID environment variable or "
                    "add it to your Streamlit secrets."
                )
                return None, None, error_msg
            
            # Show progress to user
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            status_text.text("🔄 Downloading ML model from Google Drive...")
            progress_bar.progress(10)
            
            # Download model with timeout and progress tracking
            start_time = time.time()
            
            # Use session with timeout
            session = requests.Session()
            session.headers.update({
                'User-Agent': 'BulldozerPriceGenius/1.0'
            })
            
            progress_bar.progress(20)
            status_text.text("🌐 Connecting to Google Drive...")
            
            # Download with streaming to handle large file
            # Handle Google Drive's download confirmation for large files
            download_url = _self.model_download_url
            first_chunk = b''

            # Try multiple Google Drive download strategies for large files
            for attempt in range(4):
                try:
                    if attempt == 0:
                        # Standard download URL
                        download_url = f"https://drive.google.com/uc?export=download&id={_self.model_file_id}"
                        status_text.text("🔄 Attempting standard Google Drive download...")
                    elif attempt == 1:
                        # Try with confirmation parameter to bypass virus scan
                        download_url = f"https://drive.google.com/uc?export=download&id={_self.model_file_id}&confirm=t"
                        status_text.text("🔄 Bypassing Google Drive virus scan...")
                    elif attempt == 2:
                        # Try to extract download link from HTML response
                        status_text.text("🔄 Parsing Google Drive confirmation page...")
                        download_url = _self._get_direct_download_link_from_html(session, _self.model_file_id)
                        if not download_url:
                            continue
                    elif attempt == 3:
                        # Last resort: try docs.google.com
                        download_url = f"https://docs.google.com/uc?export=download&id={_self.model_file_id}"
                        status_text.text("🔄 Trying alternative Google Drive endpoint...")

                    response = session.get(
                        download_url,
                        stream=True,
                        timeout=(30, 300),  # 30s connect, 300s read timeout
                        allow_redirects=True
                    )
                    response.raise_for_status()

                    # Check if we're getting the actual file or HTML
                    content_type = response.headers.get('content-type', '').lower()

                    # Read first chunk to check content
                    first_chunk = next(response.iter_content(chunk_size=1024), b'')

                    # Check if this looks like a pickle file
                    if (first_chunk.startswith(b'\x80') or
                        'application/octet-stream' in content_type or
                        'application/x-pickle' in content_type or
                        (len(first_chunk) > 0 and not first_chunk.startswith(b'<'))):
                        # This looks like a binary file (pickle), proceed with download
                        status_text.text("✅ Found valid model file, downloading...")
                        break
                    elif ('text/html' in content_type or
                          first_chunk.startswith(b'<!DOCTYPE') or
                          first_chunk.startswith(b'<html')):
                        # This is HTML, try next method
                        response.close()
                        if attempt == 3:
                            # Last attempt failed, provide detailed error
                            # Last attempt with standard methods failed, try large file handler
                            status_text.text("🔄 Trying specialized large file download...")
                            model_data, error_msg = _self._download_large_google_drive_file(
                                session, _self.model_file_id, status_text, progress_bar
                            )

                            if model_data is not None:
                                # Success with large file handler
                                progress_bar.progress(80)
                                status_text.text("🔧 Loading model into memory...")

                                # Load the model from bytes
                                model = pickle.load(model_data)

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
                                # All methods failed
                                error_msg = (
                                    "🚫 **Google Drive Download Issue**\n\n"
                                    "Google Drive is serving a confirmation page instead of the model file. "
                                    "This happens with large files (>25MB) that require virus scan bypass.\n\n"
                                    f"**Technical details:** {error_msg}\n\n"
                                    "**Possible solutions:**\n"
                                    "1. The file may be temporarily unavailable\n"
                                    "2. Google Drive may have changed its download mechanism\n"
                                    "3. The file sharing permissions may need adjustment\n\n"
                                    "**Fallback:** Using statistical prediction instead."
                                )
                                return None, None, error_msg
                        continue
                    else:
                        # Unknown content type, but if it's not HTML, try to proceed
                        if not first_chunk.startswith(b'<'):
                            status_text.text("⚠️ Unknown file type, attempting download...")
                            break
                        else:
                            response.close()
                            continue

                except Exception as e:
                    response.close() if 'response' in locals() else None
                    if attempt == 3:
                        raise e
                    continue
            
            progress_bar.progress(40)
            status_text.text("📥 Downloading model file (561MB)...")

            # Read the content
            model_data = BytesIO()
            total_size = int(response.headers.get('content-length', 0))
            downloaded = 0

            # Write the first chunk we already read
            if first_chunk:
                model_data.write(first_chunk)
                downloaded += len(first_chunk)

            # Continue reading the rest
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    model_data.write(chunk)
                    downloaded += len(chunk)

                    # Update progress
                    if total_size > 0:
                        progress = 40 + int((downloaded / total_size) * 40)
                        progress_bar.progress(min(progress, 80))
            
            progress_bar.progress(80)
            status_text.text("🔧 Loading model into memory...")
            
            # Load the model from bytes
            model_data.seek(0)
            model = pickle.load(model_data)
            
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
            
        except requests.exceptions.Timeout:
            error_msg = (
                "⏱️ **Download Timeout**\n\n"
                "The model download took too long. This might be due to a slow "
                "internet connection. Please try again."
            )
            return None, None, error_msg
            
        except requests.exceptions.ConnectionError:
            error_msg = (
                "🌐 **Connection Error**\n\n"
                "Could not connect to Google Drive. Please check your internet "
                "connection and try again."
            )
            return None, None, error_msg
            
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                error_msg = (
                    "📁 **Model File Not Found**\n\n"
                    "The model file could not be found on Google Drive. "
                    "Please check the file ID configuration."
                )
            else:
                error_msg = (
                    f"🚫 **Download Error**\n\n"
                    f"HTTP {e.response.status_code}: Could not download the model file."
                )
            return None, None, error_msg
            
        except pickle.UnpicklingError:
            error_msg = (
                "🔧 **Model Loading Error**\n\n"
                "The downloaded file could not be loaded as a machine learning model. "
                "The file might be corrupted or in an incompatible format."
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
            'model_source': 'Google Drive',
            'model_file_id': self.model_file_id,
            'download_url': self.model_download_url,
            'preprocessing_path': self.preprocessing_path,
            'cache_enabled': True,
            'expected_size': '561MB'
        }
    
    def _get_direct_download_link_from_html(self, session, file_id):
        """
        Parse Google Drive HTML response to extract direct download link.
        This handles the virus scan warning page for large files.
        """
        try:
            # Get the initial page that might contain the download link
            html_url = f"https://drive.google.com/file/d/{file_id}/view"
            response = session.get(html_url, timeout=30)

            if response.status_code != 200:
                return None

            html_content = response.text

            # Look for common patterns in Google Drive download pages
            import re

            # Pattern 1: Look for download URL in JavaScript
            download_patterns = [
                r'"downloadUrl":"([^"]+)"',
                r'href="([^"]*uc\?export=download[^"]*)"',
                r'"url":"([^"]*uc\?export=download[^"]*)"',
                r'action="([^"]*uc\?export=download[^"]*)"'
            ]

            for pattern in download_patterns:
                matches = re.findall(pattern, html_content)
                if matches:
                    download_url = matches[0].replace('\\u003d', '=').replace('\\u0026', '&')
                    if 'export=download' in download_url:
                        return download_url

            # Pattern 2: Try to construct URL with confirmation token
            confirm_patterns = [
                r'name="confirm" value="([^"]+)"',
                r'"confirm":"([^"]+)"',
                r'confirm=([^&\s"]+)'
            ]

            for pattern in confirm_patterns:
                matches = re.findall(pattern, html_content)
                if matches:
                    confirm_token = matches[0]
                    return f"https://drive.google.com/uc?export=download&id={file_id}&confirm={confirm_token}"

            return None

        except Exception:
            return None

    def _download_large_google_drive_file(self, session, file_id, status_text, progress_bar):
        """
        Alternative method to download large files from Google Drive.
        Uses a session-based approach to handle confirmation pages.
        """
        try:
            # Step 1: Get the initial download page
            initial_url = f"https://drive.google.com/uc?export=download&id={file_id}"
            response = session.get(initial_url, stream=False, timeout=30)

            if response.status_code != 200:
                return None, "Failed to access Google Drive download page"

            # Step 2: Check if we got a direct download or confirmation page
            content_type = response.headers.get('content-type', '').lower()

            if 'text/html' in content_type:
                # We got a confirmation page, need to extract the real download URL
                status_text.text("🔄 Handling Google Drive confirmation page...")

                # Look for the download form in the HTML
                import re
                html_content = response.text

                # Try to find the download form action URL
                form_match = re.search(r'<form[^>]*action="([^"]*)"[^>]*method="post"', html_content)
                if form_match:
                    download_url = form_match.group(1).replace('&amp;', '&')

                    # Extract form data
                    form_data = {}

                    # Look for hidden input fields
                    input_matches = re.findall(r'<input[^>]*name="([^"]*)"[^>]*value="([^"]*)"', html_content)
                    for name, value in input_matches:
                        form_data[name] = value

                    # Add confirm parameter
                    form_data['confirm'] = 't'

                    # Submit the form to get the actual file
                    status_text.text("🔄 Submitting download confirmation...")
                    response = session.post(download_url, data=form_data, stream=True, timeout=(30, 300))

                    if response.status_code != 200:
                        return None, f"Download confirmation failed: HTTP {response.status_code}"
                else:
                    # Try alternative confirmation approach
                    confirm_url = f"https://drive.google.com/uc?export=download&id={file_id}&confirm=t"
                    response = session.get(confirm_url, stream=True, timeout=(30, 300))

                    if response.status_code != 200:
                        return None, f"Alternative confirmation failed: HTTP {response.status_code}"

            # Step 3: Verify we're getting binary content
            first_chunk = next(response.iter_content(chunk_size=1024), b'')
            if first_chunk.startswith(b'<') or 'text/html' in response.headers.get('content-type', ''):
                return None, "Still receiving HTML after confirmation attempts"

            # Step 4: Download the file
            status_text.text("📥 Downloading model file (561MB)...")
            model_data = BytesIO()
            total_size = int(response.headers.get('content-length', 0))
            downloaded = 0

            # Write the first chunk
            if first_chunk:
                model_data.write(first_chunk)
                downloaded += len(first_chunk)

            # Continue downloading
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    model_data.write(chunk)
                    downloaded += len(chunk)

                    # Update progress
                    if total_size > 0:
                        progress = 40 + int((downloaded / total_size) * 40)
                        progress_bar.progress(min(progress, 80))

            model_data.seek(0)
            return model_data, None

        except Exception as e:
            return None, f"Large file download failed: {str(e)}"

    def clear_model_cache(self):
        """Clear the cached model to force re-download."""
        try:
            self.load_model_from_google_drive.clear()
            st.success("Model cache cleared. The model will be re-downloaded on next use.")
        except Exception as e:
            st.error(f"Error clearing cache: {e}")


# Global instance for easy access
external_model_loader = ExternalModelLoader()
