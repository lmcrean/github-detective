"""Markdown utility functions for generating documentation."""

import os
from typing import Dict, List, Any
from datetime import datetime
import pandas as pd


class MarkdownUtils:
    """Utility class for markdown operations."""
    
    @staticmethod
    def format_number(num: int) -> str:
        """Format large numbers with k/M suffixes for readability.
        
        Examples:
            1234 -> "1.2k"
            12345 -> "12.3k"
            1234567 -> "1.2M"
        """
        if num < 1000:
            return str(num)
        elif num < 1000000:
            if num < 10000:
                return f"{num/1000:.1f}k"
            else:
                return f"{num/1000:.0f}k"
        elif num < 1000000000:
            if num < 10000000:
                return f"{num/1000000:.1f}M"
            else:
                return f"{num/1000000:.0f}M"
        else:
            return f"{num/1000000000:.1f}B"
    
    @staticmethod
    def create_table_header(headers: List[str]) -> str:
        """Create markdown table header."""
        header_row = "| " + " | ".join(headers) + " |"
        separator_row = "|" + "|".join(["---" for _ in headers]) + "|"
        return f"{header_row}\n{separator_row}"
    
    @staticmethod
    def create_table_row(values: List[str]) -> str:
        """Create markdown table row."""
        return "| " + " | ".join(str(v) for v in values) + " |"
    
    @staticmethod
    def generate_repo_table(repositories: List[Dict[str, Any]], title: str = "Repository Statistics") -> str:
        """
        Generate markdown table for repository statistics.
        
        Args:
            repositories: List of repository data dictionaries
            title: Table title
        
        Returns:
            Markdown formatted table
        """
        if not repositories:
            return f"## {title}\n\nNo repositories found.\n"
        
        lines = [
            f"## {title}",
            "",
            MarkdownUtils.create_table_header([
                "Rank", "Repository", "Stars", "Forks", "Contributors", 
                "Open Issues", "Open PRs", "Last Active", "Top Languages"
            ])
        ]
        
        for rank, repo in enumerate(repositories, 1):
            repo_name = repo.get('Name', repo.get('repo_path', 'Unknown'))
            repo_link = f"[{repo_name}](https://github.com/{repo_name})"
            
            # Handle numeric formatting and N/A values
            stars = MarkdownUtils.format_number(repo.get('Stars', 0))
            forks = MarkdownUtils.format_number(repo.get('Forks', 0))
            contributors = "N/A" if repo.get('Contributors', 0) == -1 else str(repo.get('Contributors', 0))
            open_issues = MarkdownUtils.format_number(repo.get('Open Issues', 0))
            open_prs = "N/A" if repo.get('Open Pull Requests', 0) == -1 else str(repo.get('Open Pull Requests', 0))
            
            # Format date and languages
            last_active = str(repo.get('Last Active', 'N/A')).split('T')[0]
            languages = str(repo.get('Top Languages', 'N/A'))
            if len(languages) > 50:
                languages = languages[:47] + "..."
            
            row = MarkdownUtils.create_table_row([
                str(rank), repo_link, stars, forks, contributors,
                open_issues, open_prs, last_active, languages
            ])
            lines.append(row)
        
        return '\n'.join(lines)
    
    @staticmethod
    def generate_summary_section(repositories: List[Dict[str, Any]], title: str) -> str:
        """Generate summary section with statistics."""
        if not repositories:
            return f"# {title}\n\nNo data available.\n"
        
        total_repos = len(repositories)
        total_stars = sum(repo.get('Stars', 0) for repo in repositories)
        total_forks = sum(repo.get('Forks', 0) for repo in repositories)
        
        lines = [
            f"# {title}",
            "",
            f"**Total Repositories:** {total_repos:,}",
            f"**Total Stars:** {MarkdownUtils.format_number(total_stars)}",
            f"**Total Forks:** {MarkdownUtils.format_number(total_forks)}",
            "",
            f"*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*",
            ""
        ]
        
        return '\n'.join(lines)
    
    @staticmethod
    def generate_filename(field: str) -> str:
        """Convert field name to kebab-case filename."""
        if field == "AI/ML":
            return "ai-ml.md"
        elif field == "C# ASP.NET":
            return "csharp-aspdotnet.md"
        
        # General case: lowercase and replace spaces/underscores with hyphens
        return field.lower().replace(' ', '-').replace('_', '-') + '.md'
    
    @staticmethod
    def write_markdown_file(content: str, file_path: str) -> None:
        """Write markdown content to file."""
        # Create output directory if needed
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)