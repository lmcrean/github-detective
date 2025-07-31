"""Data models for GitHub repository statistics."""

from dataclasses import dataclass
from typing import Dict, List, Optional
from datetime import datetime


@dataclass
class RepositoryStats:
    """Repository statistics from GitHub API."""
    repo_path: str
    field: str
    stars: int
    forks: int
    contributors: int
    open_issues: int
    open_prs: int
    created_at: str
    pushed_at: str
    languages: str = ""  # Top 5 languages as formatted string

    def to_dict(self) -> Dict:
        """Convert to dictionary format."""
        return {
            'Name': self.repo_path,
            'Field': self.field,
            'Stars': self.stars,
            'Forks': self.forks,
            'Contributors': self.contributors,
            'Open Issues': self.open_issues,
            'Open Pull Requests': self.open_prs,
            'Date Created': self.created_at,
            'Last Active': self.pushed_at,
            'Top Languages': self.languages
        }


@dataclass
class CollectionMetadata:
    """Metadata about data collection run."""
    last_updated: str
    total_repositories: int
    total_stars: int
    collection_time_seconds: float
    
    @classmethod
    def create(cls, repo_count: int, total_stars: int, collection_time: float) -> 'CollectionMetadata':
        """Create metadata with current timestamp."""
        return cls(
            last_updated=datetime.now().isoformat(),
            total_repositories=repo_count,
            total_stars=total_stars,
            collection_time_seconds=round(collection_time, 2)
        )