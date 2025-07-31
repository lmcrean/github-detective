"""Utility functions for formatting and data processing."""

def format_number(num: int) -> str:
    """Format large numbers with k/M suffixes for readability.
    
    Examples:
        1234 -> "1.2k"
        12345 -> "12.3k"
        1234567 -> "1.2M"
    """
    if num < 1000:
        return str(num)
    elif num < 1000000:
        if num < 10000:
            return f"{num/1000:.1f}k"
        else:
            return f"{num/1000:.0f}k"
    elif num < 1000000000:
        if num < 10000000:
            return f"{num/1000000:.1f}M"
        else:
            return f"{num/1000000:.0f}M"
    else:
        return f"{num/1000000000:.1f}B"


def format_repo_stats_for_display(stats_list) -> list:
    """Format repository stats with readable numbers."""
    formatted = []
    for stats in stats_list:
        formatted_stats = stats.copy() if isinstance(stats, dict) else stats.to_dict()
        
        # Format numeric fields
        if 'Stars' in formatted_stats:
            formatted_stats['Stars'] = format_number(formatted_stats['Stars'])
        if 'Forks' in formatted_stats:
            formatted_stats['Forks'] = format_number(formatted_stats['Forks'])
        if 'Contributors' in formatted_stats and formatted_stats['Contributors'] > 0:
            formatted_stats['Contributors'] = format_number(formatted_stats['Contributors'])
        elif 'Contributors' in formatted_stats and formatted_stats['Contributors'] == -1:
            formatted_stats['Contributors'] = "N/A"
        
        if 'Open Pull Requests' in formatted_stats and formatted_stats['Open Pull Requests'] == -1:
            formatted_stats['Open Pull Requests'] = "N/A"
            
        formatted.append(formatted_stats)
    
    return formatted