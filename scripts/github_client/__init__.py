"""GitHub API package for repository statistics collection."""

from .client import GitHubClient
from .collector import RepositoryCollector
from .auth import GitHubAuth
from .rate_limiter import RateLimiter
from .exceptions import GitHubAPIError, RateLimitError, RepositoryNotFoundError, AccessDeniedError
from ..models.github_models import RepositoryStats, CollectionMetadata, IssueData
from ..utils.markdown_utils import MarkdownUtils

# For backward compatibility
format_number = MarkdownUtils.format_number

def format_repo_stats_for_display(stats_list) -> list:
    """Format repository stats with readable numbers (backward compatibility)."""
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

__all__ = [
    'GitHubClient', 'RepositoryCollector', 'GitHubAuth', 'RateLimiter',
    'GitHubAPIError', 'RateLimitError', 'RepositoryNotFoundError', 'AccessDeniedError',
    'RepositoryStats', 'CollectionMetadata', 'IssueData',
    'format_number', 'format_repo_stats_for_display'
]