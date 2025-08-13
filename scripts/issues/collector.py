"""GitHub issue collector module."""

import os
import time
from typing import List, Dict, Optional
from pathlib import Path

from ..github_client.client import GitHubClient
from ..models.github_models import IssueData


class IssueCollector:
    """Collects GitHub issues for repositories."""
    
    def __init__(self, token: Optional[str] = None):
        """Initialize collector with optional GitHub token."""
        self.client = GitHubClient(token)
    
    def collect_repository_issues(self, owner: str, repo: str, max_issues: int = 500) -> List[IssueData]:
        """Collect issues for a single repository."""
        print(f"Collecting issues for {owner}/{repo}...")
        issues = self.client.get_issues(owner, repo, max_issues)
        print(f"  Found {len(issues)} issues")
        return issues
    
    def collect_multiple_repositories(self, repo_paths: List[str], max_issues_per_repo: int = 500) -> Dict[str, List[IssueData]]:
        """
        Collect issues for multiple repositories.
        
        Args:
            repo_paths: List of repository paths in 'owner/repo' format
            max_issues_per_repo: Maximum issues to collect per repository
        
        Returns:
            Dictionary mapping repo_path to list of issues
        """
        all_issues = {}
        
        for i, repo_path in enumerate(repo_paths, 1):
            print(f"[{i}/{len(repo_paths)}] Processing {repo_path}")
            
            try:
                owner, repo = repo_path.split('/')
                issues = self.collect_repository_issues(owner, repo, max_issues_per_repo)
                all_issues[repo_path] = issues
                
                # Brief pause to be respectful to API
                time.sleep(0.5)
                
            except ValueError:
                print(f"  Error: Invalid repository path format: {repo_path}")
                all_issues[repo_path] = []
            except Exception as e:
                print(f"  Error collecting issues for {repo_path}: {str(e)}")
                all_issues[repo_path] = []
        
        return all_issues