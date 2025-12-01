"""
Time format conversion utilities
"""

def seconds_to_mmss_ms(seconds):
    """
    Convert seconds (float) to MM:SS:mmm format.
    
    Args:
        seconds (float): Time in seconds (e.g., 54.179125)
    
    Returns:
        str: Time in MM:SS:mmm format (e.g., "00:54:179")
    
    Examples:
        >>> seconds_to_mmss_ms(54.179125)
        '00:54:179'
        >>> seconds_to_mmss_ms(125.5)
        '02:05:500'
        >>> seconds_to_mmss_ms(3661.123)
        '61:01:123'
    """
    # Extract minutes
    minutes = int(seconds // 60)
    
    # Extract remaining seconds
    remaining_seconds = seconds % 60
    
    # Extract whole seconds and milliseconds
    secs = int(remaining_seconds)
    milliseconds = int((remaining_seconds - secs) * 1000)
    
    # Format as MM:SS:mmm
    return f"{minutes:02d}:{secs:02d}:{milliseconds:03d}"


# Alternative version that handles hours as well
def seconds_to_hhmmss_ms(seconds):
    """
    Convert seconds (float) to HH:MM:SS:mmm format.
    
    Args:
        seconds (float): Time in seconds
    
    Returns:
        str: Time in HH:MM:SS:mmm format
    
    Examples:
        >>> seconds_to_hhmmss_ms(54.179125)
        '00:00:54:179'
        >>> seconds_to_hhmmss_ms(3661.123)
        '01:01:01:123'
    """
    # Extract hours
    hours = int(seconds // 3600)
    remaining = seconds % 3600
    
    # Extract minutes
    minutes = int(remaining // 60)
    
    # Extract remaining seconds
    remaining_seconds = remaining % 60
    
    # Extract whole seconds and milliseconds
    secs = int(remaining_seconds)
    milliseconds = int((remaining_seconds - secs) * 1000)
    
    # Format as HH:MM:SS:mmm
    return f"{hours:02d}:{minutes:02d}:{secs:02d}:{milliseconds:03d}"


if __name__ == "__main__":
    # Test examples
    test_times = [54.179125, 125.5, 3661.123, 0.001, 59.999]
    
    print("Time Conversion Examples:")
    print("=" * 50)
    print(f"{'Seconds':<15} {'MM:SS:mmm':<15} {'HH:MM:SS:mmm'}")
    print("=" * 50)
    
    for time_val in test_times:
        mmss = seconds_to_mmss_ms(time_val)
        hhmmss = seconds_to_hhmmss_ms(time_val)
        print(f"{time_val:<15.6f} {mmss:<15} {hhmmss}")
