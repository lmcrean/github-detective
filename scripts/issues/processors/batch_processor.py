"""Batch processor for handling multiple repository issue collection."""

import os
import yaml
from typing import List, Dict
from pathlib import Path
from dotenv import load_dotenv

from ..collector import IssueCollector
from ..analyzer import IssueAnalyzer
from ..exporters.csv_exporter import CSVExporter
from ..exporters.markdown_exporter import MarkdownExporter


class BatchProcessor:
    """Process issues for multiple repositories in batch."""
    
    def __init__(self, token: str = None):
        """Initialize batch processor."""
        load_dotenv()
        self.token = token or os.getenv('GITHUB_TOKEN') or os.getenv('API_GITHUB_TOKEN')
        
        self.collector = IssueCollector(self.token)
        self.analyzer = IssueAnalyzer()
        self.csv_exporter = CSVExporter()
        self.markdown_exporter = MarkdownExporter()
    
    def load_repositories_from_config(self, config_file: str = 'scripts/config/issue_collection_repos.yml') -> List[str]:
        """Load repository list from YAML configuration."""
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f)
        return config['repositories']
    
    def load_repositories_from_notes(self, filepath: str = ".notes/batch1.md") -> List[str]:
        """Read repository URLs from notes file and extract owner/repo."""
        repositories = []
        
        if not os.path.exists(filepath):
            print(f"Notes file not found: {filepath}")
            return repositories
        
        with open(filepath, 'r') as f:
            content = f.read()
        
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith('https://github.com/'):
                repo_path = line.replace('https://github.com/', '').strip('/')
                if '/' in repo_path:
                    repositories.append(repo_path)
        
        return repositories
    
    def process_repositories(self, repo_paths: List[str], max_issues_per_repo: int = 500, 
                           export_csv: bool = True, export_markdown: bool = True, 
                           export_combined: bool = True) -> Dict:
        """
        Process multiple repositories for issue collection and analysis.
        
        Args:
            repo_paths: List of repository paths in 'owner/repo' format
            max_issues_per_repo: Maximum issues to collect per repository
            export_csv: Whether to export individual CSV files
            export_markdown: Whether to export individual markdown files
            export_combined: Whether to export combined reports
        
        Returns:
            Dictionary with processing results
        """
        print("GitHub Issue Batch Processor")
        print("=" * 50)
        print(f"Authentication: {'Enabled' if self.token else 'Disabled (60 requests/hour limit)'}")
        print(f"Repositories to process: {len(repo_paths)}")
        print(f"Max issues per repo: {max_issues_per_repo}")
        print()
        
        # Collect issues
        print("Collecting issues...")
        repo_issues = self.collector.collect_multiple_repositories(repo_paths, max_issues_per_repo)
        
        # Analyze issues
        print("\nAnalyzing issues...")
        repo_analyses = self.analyzer.analyze_multiple_repositories(repo_issues)
        summary_analysis = self.analyzer.get_summary_statistics(repo_issues)
        
        # Export results
        exported_files = []
        
        if export_csv:
            print("\nExporting to CSV...")
            csv_files = self.csv_exporter.export_multiple_repositories(repo_issues)
            exported_files.extend(csv_files)
            
            if export_combined:
                combined_csv = self.csv_exporter.export_combined_csv(repo_issues)
                exported_files.append(combined_csv)
        
        if export_markdown:
            print("\nExporting to Markdown...")
            md_files = self.markdown_exporter.export_multiple_repositories(repo_issues, repo_analyses)
            exported_files.extend(md_files)
            
            if export_combined:
                summary_md = self.markdown_exporter.export_summary_report(repo_issues, summary_analysis)
                exported_files.append(summary_md)
        
        # Print summary
        print("\n" + "=" * 50)
        print("Processing Complete!")
        print(f"Total repositories processed: {len(repo_issues)}")
        print(f"Total issues collected: {summary_analysis['total_issues']}")
        print(f"Files exported: {len(exported_files)}")
        print("=" * 50)
        
        return {
            'repo_issues': repo_issues,
            'repo_analyses': repo_analyses,
            'summary_analysis': summary_analysis,
            'exported_files': exported_files
        }