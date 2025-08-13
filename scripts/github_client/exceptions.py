"""Custom exceptions for GitHub API client."""


class GitHubAPIError(Exception):
    """Base exception for GitHub API errors."""
    
    def __init__(self, message: str, status_code: int = None):
        super().__init__(message)
        self.status_code = status_code


class RateLimitError(GitHubAPIError):
    """Raised when GitHub API rate limit is exceeded."""
    
    def __init__(self, reset_time: int = None):
        super().__init__("GitHub API rate limit exceeded", 429)
        self.reset_time = reset_time


class AuthenticationError(GitHubAPIError):
    """Raised when authentication fails."""
    
    def __init__(self, message: str = "Authentication failed"):
        super().__init__(message, 401)


class RepositoryNotFoundError(GitHubAPIError):
    """Raised when repository is not found."""
    
    def __init__(self, repo_path: str):
        super().__init__(f"Repository not found: {repo_path}", 404)
        self.repo_path = repo_path


class AccessDeniedError(GitHubAPIError):
    """Raised when access to resource is denied."""
    
    def __init__(self, repo_path: str):
        super().__init__(f"Access denied to repository: {repo_path}", 403)
        self.repo_path = repo_path