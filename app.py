import streamlit as st
import sys
import traceback
import os

# Add error handling for Heroku deployment
try:
    from app_pages.multipage import MultiPage
except ImportError as e:
    st.error(f"❌ Import Error: {e}")
    st.error("Please check that all dependencies are installed correctly.")
    st.error("This may be a Heroku deployment issue.")
    st.stop()

# Load pages scripts with error handling
try:
    from app_pages.one_case_study import case_study_body  # Case Study Page
    from app_pages.two_hypothesis_and_validation import hypothesis_and_validation_body  # Hypothesis & Validation Page
    from app_pages.three_project_framework import project_framework_body  # Project Framework Page
    from app_pages.four_interactive_prediction import interactive_prediction_body  # Interactive Prediction Page
    from app_pages.five_documentation import documentation_body  # Documentation Page
    from app_pages.six_ml_pipeline import ml_pipeline_body  # ML Pipeline Page
except ImportError as e:
    st.error(f"❌ Page Import Error: {e}")
    st.error("Failed to load application pages.")
    st.error("This may indicate missing dependencies or file path issues.")
    st.stop()

# Main application with error handling
try:
    # Create an instance of the app
    app = MultiPage(app_name="BulldozerPriceGenius(BPG)")  # App name displayed in the UI

    # Add app pages
    app.add_page("one_case_study", case_study_body)  # Add Case Study page
    app.add_page("two_hypothesis_and_validation", hypothesis_and_validation_body)  # Add Hypothesis & Validation page
    app.add_page("three_project_framework", project_framework_body)  # Add Project Framework page
    app.add_page("four_interactive_prediction", interactive_prediction_body)  # Add Interactive Prediction page
    app.add_page("five_documentation", documentation_body)  # Add Documentation page
    app.add_page("six_ml_pipeline", ml_pipeline_body)  # Add ML Pipeline page

    # Run the app
    app.run()  # Start the Streamlit app

except Exception as e:
    st.error(f"❌ Application Error: {e}")
    st.error("**Full Error Details:**")
    st.code(traceback.format_exc())

    # Show environment info for debugging (guarded in production)
    is_production = os.getenv('STREAMLIT_ENV', '').lower() == 'production'
    if not is_production:
        st.error("**Environment Information:**")
        st.write(f"Python version: {sys.version}")
        st.write(f"Current working directory: {os.getcwd()}")
        st.write(f"Python path: {sys.path}")

        # Show available files for debugging
        st.error("**Available Files:**")
        try:
            import os
            files = []
            for root, dirs, filenames in os.walk('.'):
                for filename in filenames:
                    files.append(os.path.join(root, filename))
            st.write(files[:20])  # Show first 20 files
        except Exception as file_error:
            st.write(f"Could not list files: {file_error}")
    else:
        with st.expander("🔧 Developer Diagnostics", expanded=False):
            try:
                st.write(f"Python version: {sys.version}")
                st.write(f"Current working directory: {os.getcwd()}")
                st.write(f"Python path: {sys.path}")
                import os
                files = []
                for root, dirs, filenames in os.walk('.'):
                    for filename in filenames:
                        files.append(os.path.join(root, filename))
                st.write(files[:20])
            except Exception as file_error:
                st.write(f"Could not list files: {file_error}")
