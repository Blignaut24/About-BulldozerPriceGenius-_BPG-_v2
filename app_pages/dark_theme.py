"""
Dark Theme Implementation for BulldozerPriceGenius Streamlit Application
Provides comprehensive dark mode styling across all pages and components
"""

import streamlit as st

def apply_dark_theme():
    """
    Apply comprehensive dark theme styling to the Streamlit application
    This function should be called at the beginning of each page
    """
    st.markdown("""
    <style>
    /* ===== GLOBAL DARK THEME STYLES ===== */
    
    /* Main App Background */
    .stApp {
        background-color: #1e1e1e !important;
        color: #ffffff !important;
    }
    
    /* Sidebar Styling */
    .css-1d391kg {
        background-color: #2d2d2d !important;
    }
    
    .css-1lcbmhc {
        background-color: #2d2d2d !important;
    }
    
    /* Main Content Area */
    .main .block-container {
        background-color: #1e1e1e !important;
        color: #ffffff !important;
    }
    
    /* Headers and Text */
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
    }
    
    p, div, span, label {
        color: #e0e0e0 !important;
    }
    
    /* Input Fields */
    .stTextInput > div > div > input {
        background-color: #3d3d3d !important;
        color: #ffffff !important;
        border: 1px solid #555555 !important;
    }
    
    .stNumberInput > div > div > input {
        background-color: #3d3d3d !important;
        color: #ffffff !important;
        border: 1px solid #555555 !important;
    }
    
    .stSelectbox > div > div > div {
        background-color: #3d3d3d !important;
        color: #ffffff !important;
        border: 1px solid #555555 !important;
    }
    
    /* Dropdown Options */
    .stSelectbox [data-baseweb="select"] {
        background-color: #3d3d3d !important;
    }
    
    /* Radio Buttons */
    .stRadio > div {
        background-color: #2d2d2d !important;
        border-radius: 8px !important;
        padding: 10px !important;
    }
    
    .stRadio label {
        color: #ffffff !important;
    }
    
    /* Checkboxes */
    .stCheckbox label {
        color: #ffffff !important;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background-color: #2d2d2d !important;
        color: #ffffff !important;
        border: 1px solid #555555 !important;
    }
    
    .streamlit-expanderContent {
        background-color: #2d2d2d !important;
        border: 1px solid #555555 !important;
    }
    
    /* Metrics */
    .metric-container {
        background-color: #2d2d2d !important;
        border: 1px solid #555555 !important;
        border-radius: 8px !important;
        padding: 15px !important;
    }
    
    [data-testid="metric-container"] {
        background-color: #2d2d2d !important;
        border: 1px solid #555555 !important;
        border-radius: 8px !important;
        padding: 15px !important;
    }
    
    /* DataFrames */
    .stDataFrame {
        background-color: #2d2d2d !important;
    }
    
    .stDataFrame table {
        background-color: #2d2d2d !important;
        color: #ffffff !important;
    }
    
    .stDataFrame th {
        background-color: #3d3d3d !important;
        color: #ffffff !important;
        border: 1px solid #555555 !important;
    }
    
    .stDataFrame td {
        background-color: #2d2d2d !important;
        color: #ffffff !important;
        border: 1px solid #555555 !important;
    }
    
    /* Plotly Charts */
    .js-plotly-plot {
        background-color: #1e1e1e !important;
    }
    
    /* Success/Info/Warning/Error Messages */
    .stSuccess {
        background-color: #1b4332 !important;
        color: #d1e7dd !important;
        border: 1px solid #2d5a3d !important;
    }
    
    .stInfo {
        background-color: #0c4a6e !important;
        color: #cce7ff !important;
        border: 1px solid #1e5a8a !important;
    }
    
    .stWarning {
        background-color: #7c2d12 !important;
        color: #fed7aa !important;
        border: 1px solid #9a3412 !important;
    }
    
    .stError {
        background-color: #7f1d1d !important;
        color: #fecaca !important;
        border: 1px solid #991b1b !important;
    }
    
    /* Progress Bars */
    .stProgress > div > div > div {
        background-color: #FF6B35 !important;
    }
    
    .stProgress > div > div {
        background-color: #3d3d3d !important;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #2d2d2d !important;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #3d3d3d !important;
        color: #ffffff !important;
        border: 1px solid #555555 !important;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #FF6B35 !important;
        color: #ffffff !important;
    }
    
    /* Columns and Containers */
    .element-container {
        background-color: transparent !important;
    }
    
    /* Custom Dark Theme for Form Sections */
    .dark-section-required {
        background: linear-gradient(90deg, #3d2914 0%, #4a3319 100%) !important;
        border-left: 5px solid #ffc107 !important;
        color: #fff3cd !important;
    }
    
    .dark-section-technical {
        background: linear-gradient(90deg, #1a2332 0%, #1e2a3a 100%) !important;
        border-left: 5px solid #17a2b8 !important;
        color: #d1ecf1 !important;
    }
    
    .dark-section-optional {
        background: linear-gradient(90deg, #2d1b1b 0%, #3a2222 100%) !important;
        border-left: 5px solid #dc3545 !important;
        color: #f8d7da !important;
    }
    
    .dark-section-validation {
        background: linear-gradient(90deg, #2a2a2a 0%, #333333 100%) !important;
        border-left: 5px solid #6c757d !important;
        color: #e2e3e5 !important;
    }
    
    /* Dark Theme for Progress Indicators */
    .dark-progress-container {
        background: #2d2d2d !important;
        border: 1px solid #555555 !important;
        border-radius: 5px !important;
        color: #ffffff !important;
    }
    
    .dark-progress-bar {
        background: #28a745 !important;
        height: 8px !important;
        border-radius: 4px !important;
    }
    
    .dark-progress-bg {
        background: #3d3d3d !important;
        height: 8px !important;
        border-radius: 4px !important;
    }
    
    /* Dark Theme for Prediction Results */
    .dark-prediction-result {
        background: linear-gradient(90deg, #1a2f1a 0%, #1e3a1e 100%) !important;
        border-left: 5px solid #28a745 !important;
        color: #d4edda !important;
        border-radius: 10px !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3) !important;
    }
    
    .dark-prediction-header {
        color: #28a745 !important;
    }
    
    .dark-prediction-text {
        color: #ffffff !important;
    }
    
    /* Dark Theme for Method Selection */
    .dark-method-selection {
        background: #2d2d2d !important;
        border: 1px solid #555555 !important;
        border-radius: 8px !important;
        padding: 15px !important;
    }
    
    /* Dark Theme for Test Scenario Buttons */
    .dark-test-button {
        background-color: #3d3d3d !important;
        color: #ffffff !important;
        border: 1px solid #555555 !important;
        border-radius: 8px !important;
        padding: 10px !important;
        transition: all 0.3s ease !important;
    }
    
    .dark-test-button:hover {
        background-color: #4d4d4d !important;
        border-color: #FF6B35 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 12px rgba(255, 107, 53, 0.3) !important;
    }
    
    </style>
    """, unsafe_allow_html=True)

def get_dark_theme_colors():
    """
    Return color palette for dark theme
    """
    return {
        'primary_bg': '#1e1e1e',
        'secondary_bg': '#2d2d2d',
        'tertiary_bg': '#3d3d3d',
        'text_primary': '#ffffff',
        'text_secondary': '#e0e0e0',
        'text_muted': '#b0b0b0',
        'accent_orange': '#FF6B35',
        'accent_blue': '#17a2b8',
        'accent_green': '#28a745',
        'accent_red': '#dc3545',
        'accent_yellow': '#ffc107',
        'border_color': '#555555',
        'success_bg': '#1b4332',
        'success_text': '#d1e7dd',
        'info_bg': '#0c4a6e',
        'info_text': '#cce7ff',
        'warning_bg': '#7c2d12',
        'warning_text': '#fed7aa',
        'error_bg': '#7f1d1d',
        'error_text': '#fecaca'
    }

def create_dark_section_html(title, content, section_type="default"):
    """
    Create a dark-themed section with proper styling
    
    Args:
        title (str): Section title
        content (str): Section content
        section_type (str): Type of section (required, technical, optional, validation)
    """
    colors = get_dark_theme_colors()
    
    section_classes = {
        'required': 'dark-section-required',
        'technical': 'dark-section-technical', 
        'optional': 'dark-section-optional',
        'validation': 'dark-section-validation'
    }
    
    section_class = section_classes.get(section_type, 'dark-section-validation')
    
    return f"""
    <div class="{section_class}" style="padding: 15px; border-radius: 8px; margin: 10px 0;">
        <h3 style="margin: 0 0 10px 0;">{title}</h3>
        <p style="margin: 0;">{content}</p>
    </div>
    """

def create_dark_progress_bar(completed, total, label="Progress"):
    """
    Create a dark-themed progress bar
    
    Args:
        completed (int): Number of completed items
        total (int): Total number of items
        label (str): Progress bar label
    """
    percentage = (completed / total) * 100 if total > 0 else 0
    
    return f"""
    <div class="dark-progress-container" style="padding: 10px; margin: 10px 0;">
        <strong>{label}: {completed}/{total} ({percentage:.0f}%)</strong>
        <div class="dark-progress-bg" style="margin: 5px 0;">
            <div class="dark-progress-bar" style="width: {percentage}%;"></div>
        </div>
    </div>
    """
