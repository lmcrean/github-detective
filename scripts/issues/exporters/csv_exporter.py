"""CSV exporter for GitHub issues."""

import os
import csv
from pathlib import Path
from datetime import datetime
from typing import List, Dict
from ...models.github_models import IssueData


class CSVExporter:
    """Exports GitHub issues to CSV format."""
    
    def __init__(self, output_dir: str = 'data/issues'):
        """Initialize CSV exporter with output directory."""
        self.output_dir = output_dir
        Path(self.output_dir).mkdir(parents=True, exist_ok=True)
    
    def export_repository_issues(self, owner: str, repo: str, issues: List[IssueData]) -> str:
        """
        Export issues for a single repository to CSV.
        
        Args:
            owner: Repository owner
            repo: Repository name
            issues: List of issue data
        
        Returns:
            Path to exported CSV file
        """
        filename = f"{owner}_{repo}.csv"
        filepath = os.path.join(self.output_dir, filename)
        repo_path = f"{owner}/{repo}"
        
        with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
            # Write metadata header as comments
            csvfile.write(f"# Issues Total: {len(issues)}\n")
            csvfile.write(f"# Repository: https://github.com/{repo_path}\n")
            csvfile.write(f"# Generated: {datetime.now().strftime('%Y-%m-%d')}\n")
            csvfile.write("#\n")
            
            writer = csv.writer(csvfile)
            
            # Write CSV header
            writer.writerow(['issue_title', 'comments_count', 'labels', 'opened_date', 'hyperlink'])
            
            # Write issue data (sorted by most recently updated first)
            issues_sorted = sorted(issues, key=lambda x: x.updated_at, reverse=True)
            for issue in issues_sorted:
                writer.writerow(issue.to_csv_row(repo_path))
        
        print(f"Issues exported to: {filepath}")
        return filepath
    
    def export_multiple_repositories(self, repo_issues: Dict[str, List[IssueData]]) -> List[str]:
        """
        Export issues for multiple repositories to separate CSV files.
        
        Args:
            repo_issues: Dictionary mapping repo_path to list of issues
        
        Returns:
            List of paths to exported CSV files
        """
        exported_files = []
        
        for repo_path, issues in repo_issues.items():
            try:
                owner, repo = repo_path.split('/')
                filepath = self.export_repository_issues(owner, repo, issues)
                exported_files.append(filepath)
            except ValueError:
                print(f"Error: Invalid repository path format: {repo_path}")
                continue
        
        return exported_files
    
    def export_combined_csv(self, repo_issues: Dict[str, List[IssueData]], filename: str = 'all_issues.csv') -> str:
        """
        Export all issues to a single combined CSV file.
        
        Args:
            repo_issues: Dictionary mapping repo_path to list of issues
            filename: Output filename
        
        Returns:
            Path to combined CSV file
        """
        filepath = os.path.join(self.output_dir, filename)
        total_issues = sum(len(issues) for issues in repo_issues.values())
        
        with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
            # Write metadata header
            csvfile.write(f"# Combined Issues: {total_issues}\n")
            csvfile.write(f"# Repositories: {len(repo_issues)}\n")
            csvfile.write(f"# Generated: {datetime.now().strftime('%Y-%m-%d')}\n")
            csvfile.write("#\n")
            
            writer = csv.writer(csvfile)
            
            # Write CSV header
            writer.writerow(['repository', 'issue_title', 'comments_count', 'labels', 'opened_date', 'hyperlink'])
            
            # Write all issues
            for repo_path, issues in repo_issues.items():
                issues_sorted = sorted(issues, key=lambda x: x.updated_at, reverse=True)
                for issue in issues_sorted:
                    row = issue.to_csv_row(repo_path)
                    # Add repository column at the beginning
                    writer.writerow([repo_path] + row)
        
        print(f"Combined issues exported to: {filepath}")
        return filepath