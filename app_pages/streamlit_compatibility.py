"""
Streamlit Compatibility Module

This module provides compatibility functions for different versions of Streamlit.
It ensures that the application works with both older and newer versions of Streamlit
by providing fallback implementations for features that may not be available.
"""

import streamlit as st


def get_metric(label, value, help=None):
    """
    Get the appropriate metric function based on Streamlit version
    
    Args:
        label (str): The label for the metric
        value (str): The value to display
        help (str, optional): Help text to show on hover
    """
    if hasattr(st, 'metric'):
        if help:
            st.metric(label, value, help=help)
        else:
            st.metric(label, value)
    else:
        # Fallback for older versions - use markdown
        if help:
            st.markdown(f"**{label}:** {value}")
            if hasattr(st, 'caption'):
                st.caption(help)
            else:
                st.markdown(f"*{help}*")
        else:
            st.markdown(f"**{label}:** {value}")


def get_columns(num_cols):
    """
    Get the appropriate columns function based on Streamlit version
    
    Args:
        num_cols (int): Number of columns to create
        
    Returns:
        List of column objects
    """
    if hasattr(st, 'columns'):
        return st.columns(num_cols)
    elif hasattr(st, 'beta_columns'):
        return st.beta_columns(num_cols)
    else:
        # Fallback for very old versions - return list of containers
        containers = []
        for i in range(num_cols):
            st.markdown(f"**Column {i+1}:**")
            containers.append(st.container())
        return containers


def get_expander(label, expanded=False):
    """
    Get the appropriate expander function based on Streamlit version
    
    Args:
        label (str): The label for the expander
        expanded (bool): Whether the expander should be expanded by default
        
    Returns:
        Expander object or container
    """
    if hasattr(st, 'expander'):
        return st.expander(label, expanded=expanded)
    elif hasattr(st, 'beta_expander'):
        return st.beta_expander(label, expanded=expanded)
    else:
        # Fallback for very old versions - use container with header
        st.markdown(f"### {label}")
        return st.container()


def get_button(label, key=None, help=None, on_click=None, args=None, kwargs=None, disabled=False):
    """
    Get the appropriate button function based on Streamlit version
    
    Args:
        label (str): The label for the button
        key (str, optional): Unique key for the button
        help (str, optional): Help text to show on hover
        on_click (callable, optional): Callback function
        args (tuple, optional): Arguments for callback
        kwargs (dict, optional): Keyword arguments for callback
        disabled (bool): Whether the button should be disabled
        
    Returns:
        bool: True if button was clicked
    """
    # Build button arguments, excluding unsupported parameters for older versions
    button_args = {'label': label}
    
    if key is not None:
        button_args['key'] = key
    if help is not None and hasattr(st, 'help'):  # Check if help is supported
        button_args['help'] = help
    if on_click is not None:
        button_args['on_click'] = on_click
    if args is not None:
        button_args['args'] = args
    if kwargs is not None:
        button_args['kwargs'] = kwargs
    if disabled:
        button_args['disabled'] = disabled
    
    # Remove unsupported parameters for older Streamlit versions
    # Don't include 'type' or 'use_container_width' as they cause errors
    
    return st.button(**button_args)


def get_selectbox(label, options, index=0, format_func=str, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False):
    """
    Get the appropriate selectbox function based on Streamlit version
    
    Args:
        label (str): The label for the selectbox
        options (list): List of options
        index (int): Default selected index
        format_func (callable): Function to format options
        key (str, optional): Unique key
        help (str, optional): Help text
        on_change (callable, optional): Callback function
        args (tuple, optional): Arguments for callback
        kwargs (dict, optional): Keyword arguments for callback
        disabled (bool): Whether the selectbox should be disabled
        
    Returns:
        Selected option
    """
    selectbox_args = {
        'label': label,
        'options': options,
        'index': index,
        'format_func': format_func
    }
    
    if key is not None:
        selectbox_args['key'] = key
    if help is not None and hasattr(st, 'help'):
        selectbox_args['help'] = help
    if on_change is not None:
        selectbox_args['on_change'] = on_change
    if args is not None:
        selectbox_args['args'] = args
    if kwargs is not None:
        selectbox_args['kwargs'] = kwargs
    if disabled:
        selectbox_args['disabled'] = disabled
    
    return st.selectbox(**selectbox_args)


def get_radio(label, options, index=0, format_func=str, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, horizontal=False):
    """
    Get the appropriate radio function based on Streamlit version
    
    Args:
        label (str): The label for the radio buttons
        options (list): List of options
        index (int): Default selected index
        format_func (callable): Function to format options
        key (str, optional): Unique key
        help (str, optional): Help text
        on_change (callable, optional): Callback function
        args (tuple, optional): Arguments for callback
        kwargs (dict, optional): Keyword arguments for callback
        disabled (bool): Whether the radio should be disabled
        horizontal (bool): Whether to display horizontally
        
    Returns:
        Selected option
    """
    radio_args = {
        'label': label,
        'options': options,
        'index': index,
        'format_func': format_func
    }
    
    if key is not None:
        radio_args['key'] = key
    if help is not None and hasattr(st, 'help'):
        radio_args['help'] = help
    if on_change is not None:
        radio_args['on_change'] = on_change
    if args is not None:
        radio_args['args'] = args
    if kwargs is not None:
        radio_args['kwargs'] = kwargs
    if disabled:
        radio_args['disabled'] = disabled
    
    # Only add horizontal if supported (newer Streamlit versions)
    if horizontal and hasattr(st.radio, '__code__') and 'horizontal' in st.radio.__code__.co_varnames:
        radio_args['horizontal'] = horizontal
    
    return st.radio(**radio_args)


# Version detection utilities
def get_streamlit_version():
    """Get the current Streamlit version"""
    return getattr(st, '__version__', 'Unknown')


def has_feature(feature_name):
    """Check if a Streamlit feature is available"""
    return hasattr(st, feature_name)


def get_dataframe(data, width=None, height=None):
    """
    Get the appropriate dataframe function based on Streamlit version

    Args:
        data: DataFrame or data to display
        width: Width parameter (ignored in older versions)
        height: Height parameter (ignored in older versions)

    Returns:
        Displayed dataframe
    """
    # Check if use_container_width is supported
    try:
        # Try with use_container_width first
        if width == 'container' and hasattr(st.dataframe, '__code__'):
            # Check if use_container_width parameter exists
            import inspect
            sig = inspect.signature(st.dataframe)
            if 'use_container_width' in sig.parameters:
                return st.dataframe(data, use_container_width=True)
    except:
        pass

    # Fallback to basic dataframe without width parameter
    dataframe_args = {'data': data}
    if height is not None:
        dataframe_args['height'] = height

    return st.dataframe(**dataframe_args)


def get_compatibility_info():
    """Get information about Streamlit compatibility"""
    return {
        'version': get_streamlit_version(),
        'has_metric': has_feature('metric'),
        'has_caption': has_feature('caption'),
        'has_columns': has_feature('columns'),
        'has_beta_columns': has_feature('beta_columns'),
        'has_expander': has_feature('expander'),
        'has_beta_expander': has_feature('beta_expander'),
    }
