"""GitHub-specific data models."""

from dataclasses import dataclass
from typing import Dict, List, Optional
from datetime import datetime
from .base import BaseModel


@dataclass
class RepositoryStats(BaseModel):
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
class CollectionMetadata(BaseModel):
    """Metadata about data collection run."""
    last_updated: str
    total_repositories: int
    total_stars: int
    collection_time_seconds: float
    
    def to_dict(self) -> Dict:
        """Convert to dictionary format."""
        return {
            'last_updated': self.last_updated,
            'total_repositories': self.total_repositories,
            'total_stars': self.total_stars,
            'collection_time_seconds': self.collection_time_seconds
        }
    
    @classmethod
    def create(cls, repo_count: int, total_stars: int, collection_time: float) -> 'CollectionMetadata':
        """Create metadata with current timestamp."""
        return cls(
            last_updated=datetime.now().isoformat(),
            total_repositories=repo_count,
            total_stars=total_stars,
            collection_time_seconds=round(collection_time, 2)
        )


@dataclass
class IssueData(BaseModel):
    """GitHub issue data model."""
    number: int
    title: str
    state: str
    labels: List[str]
    comments: int
    created_at: str
    updated_at: str
    body: Optional[str] = None
    author: Optional[str] = None
    
    def to_dict(self) -> Dict:
        """Convert to dictionary format."""
        return {
            'number': self.number,
            'title': self.title,
            'state': self.state,
            'labels': self.labels,
            'comments': self.comments,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'body': self.body,
            'author': self.author
        }
    
    def to_markdown_entry(self) -> str:
        """Convert issue to markdown list entry."""
        labels_str = ", ".join(self.labels) if self.labels else "No labels"
        body_preview = ""
        if self.body:
            preview = self.body[:200].replace('\n', ' ').strip()
            if len(self.body) > 200:
                preview += "..."
            body_preview = f"\n  > {preview}"
        
        return (
            f"- **#{self.number}: {self.title}**\n"
            f"  - Labels: {labels_str}\n"
            f"  - Comments: {self.comments}\n"
            f"  - Last updated: {self.updated_at[:10]}"
            f"{body_preview}"
        )
    
    def to_csv_row(self, repo_path: str) -> List[str]:
        """Convert issue to CSV row format.
        
        Returns: [title, comments_count, labels, opened_date, hyperlink]
        """
        # Handle CSV escaping for title
        title_escaped = self.title.replace('"', '""') if '"' in self.title else self.title
        
        # Format labels as comma-separated string within quotes if multiple
        labels_str = ", ".join(self.labels) if self.labels else ""
        
        # Extract date (YYYY-MM-DD format)
        opened_date = self.created_at[:10] if self.created_at else ""
        
        # Create GitHub issue URL
        hyperlink = f"https://github.com/{repo_path}/issues/{self.number}"
        
        return [
            title_escaped,
            str(self.comments),
            labels_str,
            opened_date,
            hyperlink
        ]