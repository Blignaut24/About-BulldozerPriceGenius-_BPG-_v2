"""
Utility functions for formatting price displays in the bulldozer price prediction app.
Provides consistent formatting for price ranges and individual prices to avoid truncation
in Streamlit metric components.
"""


def format_price_short(price):
    """
    Format a price value for compact display in Streamlit metrics.
    
    Args:
        price (float): The price value to format
        
    Returns:
        str: Formatted price string (e.g., "$138K", "$1.2M")
    """
    if price >= 1000000:
        return f"${price/1000000:.1f}M"
    elif price >= 1000:
        return f"${price/1000:.0f}K"
    else:
        return f"${price:,.0f}"


def format_price_full(price):
    """
    Format a price value for full display with commas.
    
    Args:
        price (float): The price value to format
        
    Returns:
        str: Formatted price string (e.g., "$138,679")
    """
    return f"${price:,.0f}"


def format_price_range(lower, upper, show_full_in_help=True):
    """
    Format a price range for display in Streamlit metrics.
    
    Args:
        lower (float): Lower bound of the price range
        upper (float): Upper bound of the price range
        show_full_in_help (bool): Whether to include full range in help text
        
    Returns:
        tuple: (short_display, help_text) for use in st.metric
    """
    short_range = f"{format_price_short(lower)} - {format_price_short(upper)}"
    
    if show_full_in_help:
        full_range = f"{format_price_full(lower)} - {format_price_full(upper)}"
        help_text = f"Full range: {full_range}"
    else:
        help_text = None
    
    return short_range, help_text


def format_price_range_with_confidence(lower, upper, confidence_pct=15):
    """
    Format a price range with confidence interval information.
    
    Args:
        lower (float): Lower bound of the price range
        upper (float): Upper bound of the price range
        confidence_pct (int): Confidence percentage (e.g., 15 for ±15%)
        
    Returns:
        tuple: (short_display, help_text) for use in st.metric
    """
    short_range = f"{format_price_short(lower)} - {format_price_short(upper)}"
    full_range = f"{format_price_full(lower)} - {format_price_full(upper)}"
    help_text = f"Estimated price range: {full_range} (±{confidence_pct}%)"
    
    return short_range, help_text
