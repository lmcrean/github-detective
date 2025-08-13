"""Rate limiting functionality for GitHub API client."""

import time
import requests
from typing import Optional, Dict, Any
from .exceptions import RateLimitError


class RateLimiter:
    """Handles GitHub API rate limiting."""
    
    def __init__(self, delay: float = 0.5):
        """
        Initialize rate limiter.
        
        Args:
            delay: Base delay between requests in seconds
        """
        self.delay = delay
        self.last_request_time = 0
    
    def wait_if_needed(self) -> None:
        """Wait if needed to respect rate limits."""
        current_time = time.time()
        time_since_last = current_time - self.last_request_time
        
        if time_since_last < self.delay:
            sleep_time = self.delay - time_since_last
            time.sleep(sleep_time)
        
        self.last_request_time = time.time()
    
    def handle_rate_limit_response(self, response: requests.Response) -> None:
        """
        Handle rate limit response from GitHub API.
        
        Args:
            response: HTTP response from GitHub API
        
        Raises:
            RateLimitError: If rate limit is exceeded
        """
        if response.status_code == 429:
            reset_time = int(response.headers.get('X-RateLimit-Reset', 0))
            current_time = int(time.time())
            
            if reset_time > current_time:
                wait_time = reset_time - current_time + 1
                print(f"Rate limit exceeded. Waiting {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                # Fallback: wait 60 seconds if reset time is unclear
                print("Rate limit exceeded. Waiting 60 seconds...")
                time.sleep(60)
    
    def get_rate_limit_info(self, headers: Dict[str, str]) -> Dict[str, Any]:
        """
        Extract rate limit information from response headers.
        
        Args:
            headers: HTTP response headers
        
        Returns:
            Dictionary with rate limit information
        """
        return {
            'limit': int(headers.get('X-RateLimit-Limit', 0)),
            'remaining': int(headers.get('X-RateLimit-Remaining', 0)),
            'reset': int(headers.get('X-RateLimit-Reset', 0)),
            'used': int(headers.get('X-RateLimit-Used', 0))
        }
    
    def check_rate_limit_status(self, response: requests.Response) -> Dict[str, Any]:
        """
        Check current rate limit status from response.
        
        Args:
            response: HTTP response from GitHub API
        
        Returns:
            Dictionary with rate limit status
        """
        rate_limit_info = self.get_rate_limit_info(response.headers)
        
        # Calculate time until reset
        current_time = int(time.time())
        reset_time = rate_limit_info['reset']
        time_until_reset = max(0, reset_time - current_time)
        
        rate_limit_info['time_until_reset'] = time_until_reset
        rate_limit_info['rate_limited'] = response.status_code == 429
        
        return rate_limit_info