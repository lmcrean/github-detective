"""Authentication handling for GitHub API client."""

import os
from typing import Optional, Dict
from .exceptions import AuthenticationError


class GitHubAuth:
    """Handles GitHub API authentication."""
    
    def __init__(self, token: Optional[str] = None):
        """
        Initialize authentication handler.
        
        Args:
            token: GitHub API token (if None, will try to get from environment)
        """
        self.token = token or self._get_token_from_env()
        self.headers = self._build_headers()
    
    def _get_token_from_env(self) -> Optional[str]:
        """Get GitHub token from environment variables."""
        # Try common environment variable names
        env_vars = ['API_GITHUB_TOKEN', 'GITHUB_TOKEN', 'GH_TOKEN']
        
        for var in env_vars:
            token = os.getenv(var)
            if token:
                return token
        
        return None
    
    def _build_headers(self) -> Dict[str, str]:
        """Build HTTP headers for GitHub API requests."""
        headers = {
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'GitHub-Library-Tool/1.0'
        }
        
        if self.token:
            headers['Authorization'] = f'token {self.token}'
        
        return headers
    
    def is_authenticated(self) -> bool:
        """Check if client has authentication token."""
        return self.token is not None
    
    def get_headers(self) -> Dict[str, str]:
        """Get headers for API requests."""
        return self.headers.copy()
    
    def validate_token(self) -> bool:
        """
        Validate the GitHub token by making a test API call.
        
        Returns:
            True if token is valid, False otherwise
        """
        if not self.token:
            return False
        
        try:
            import requests
            response = requests.get(
                'https://api.github.com/user',
                headers=self.headers,
                timeout=10
            )
            return response.status_code == 200
        except Exception:
            return False
    
    def get_rate_limits(self) -> Dict[str, int]:
        """
        Get current rate limits for the authenticated user.
        
        Returns:
            Dictionary with rate limit information
        """
        if not self.token:
            return {
                'core': {'limit': 60, 'remaining': 60},
                'search': {'limit': 10, 'remaining': 10}
            }
        
        try:
            import requests
            response = requests.get(
                'https://api.github.com/rate_limit',
                headers=self.headers,
                timeout=10
            )
            
            if response.status_code == 200:
                return response.json()['rate']
            else:
                # Return default limits for authenticated users
                return {
                    'core': {'limit': 5000, 'remaining': 5000},
                    'search': {'limit': 30, 'remaining': 30}
                }
        except Exception:
            # Return default limits if check fails
            return {
                'core': {'limit': 5000, 'remaining': 5000},
                'search': {'limit': 30, 'remaining': 30}
            }