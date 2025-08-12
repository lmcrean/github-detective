"""GitHub issue collector module."""

import os
import time
from typing import List, Dict, Optional
from pathlib import Path

from .client import GitHubClient
from .models import IssueData


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
    
    def save_issues_to_markdown(self, owner: str, repo: str, issues: List[IssueData], output_dir: str = ".notes/issues") -> str:
        """Save issues to a markdown file."""
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        filename = f"{owner.lower()}-{repo.lower()}-issues.md"
        filepath = os.path.join(output_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# Issues for {owner}/{repo}\n\n")
            f.write(f"**Total Issues**: {len(issues)}\n")
            f.write(f"**Repository**: https://github.com/{owner}/{repo}\n\n")
            
            if not issues:
                f.write("No issues found.\n")
            else:
                open_issues = [i for i in issues if i.state == 'open']
                closed_issues = [i for i in issues if i.state == 'closed']
                
                f.write(f"**Open Issues**: {len(open_issues)}\n")
                f.write(f"**Closed Issues**: {len(closed_issues)}\n\n")
                f.write("---\n\n")
                f.write("## Issues List (Most Recently Updated First)\n\n")
                
                for issue in issues:
                    f.write(issue.to_markdown_entry())
                    f.write("\n\n")
        
        print(f"  Saved to {filepath}")
        return filepath
    
    def collect_from_list(self, repositories: List[str], max_issues_per_repo: int = 500) -> Dict[str, List[IssueData]]:
        """Collect issues from a list of repository paths."""
        results = {}
        
        for repo_path in repositories:
            parts = repo_path.strip().split('/')
            if len(parts) == 2:
                owner, repo = parts
                issues = self.collect_repository_issues(owner, repo, max_issues_per_repo)
                results[repo_path] = issues
                time.sleep(1)
            else:
                print(f"Skipping invalid repository path: {repo_path}")
        
        return results
    
    def save_all_issues(self, results: Dict[str, List[IssueData]], output_dir: str = ".notes/issues") -> List[str]:
        """Save all collected issues to markdown files."""
        saved_files = []
        
        for repo_path, issues in results.items():
            owner, repo = repo_path.split('/')
            filepath = self.save_issues_to_markdown(owner, repo, issues, output_dir)
            saved_files.append(filepath)
        
        return saved_files