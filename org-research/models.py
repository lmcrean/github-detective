"""Data models for organization repository collection."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class OrganizationRepository:
    """Repository data model for organization-wide collection."""
    org_name: str
    repo_name: str
    open_issue_count: int
    stars_count: int
    forks_count: int
    last_pushed_date: str
    pull_requests_open_count: int
    about_description: Optional[str] = None
    
    def to_dict(self):
        """Convert to dictionary for CSV export."""
        return {
            'org_name': self.org_name,
            'repo_name': self.repo_name,
            'open_issue_count': self.open_issue_count,
            'stars_count': self.stars_count,
            'forks_count': self.forks_count,
            'last_pushed_date': self.last_pushed_date,
            'pull_requests_open_count': self.pull_requests_open_count,
            'about_description': self.about_description or ''
        }
    
    @classmethod
    def from_api_response(cls, org_name: str, repo_data: dict, pr_count: int) -> 'OrganizationRepository':
        """Create instance from GitHub API response."""
        return cls(
            org_name=org_name,
            repo_name=repo_data['name'],
            open_issue_count=repo_data.get('open_issues_count', 0),
            stars_count=repo_data.get('stargazers_count', 0),
            forks_count=repo_data.get('forks_count', 0),
            last_pushed_date=repo_data.get('pushed_at', '')[:10] if repo_data.get('pushed_at') else '',
            pull_requests_open_count=pr_count,
            about_description=repo_data.get('description', '')
        )