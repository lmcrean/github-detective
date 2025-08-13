"""Markdown exporter for GitHub issues."""

import os
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any
from ...models.github_models import IssueData
from ...utils.markdown_utils import MarkdownUtils


class MarkdownExporter:
    """Exports GitHub issues to Markdown format."""
    
    def __init__(self, output_dir: str = '.notes/issues'):
        """Initialize markdown exporter with output directory."""
        self.output_dir = output_dir
        Path(self.output_dir).mkdir(parents=True, exist_ok=True)
    
    def export_repository_issues(self, owner: str, repo: str, issues: List[IssueData], analysis: Dict[str, Any] = None) -> str:
        """
        Export issues for a single repository to Markdown.
        
        Args:
            owner: Repository owner
            repo: Repository name
            issues: List of issue data
            analysis: Optional analysis data to include
        
        Returns:
            Path to exported Markdown file
        """
        filename = f"{owner.lower()}-{repo.lower()}-issues.md"
        filepath = os.path.join(self.output_dir, filename)
        repo_path = f"{owner}/{repo}"
        
        content_lines = [
            f"# Issues for {owner}/{repo}",
            "",
            f"**Total Issues**: {len(issues)}",
            f"**Repository**: https://github.com/{repo_path}",
            f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            ""
        ]
        
        if not issues:
            content_lines.append("No issues found.")
        else:
            # Add analysis if provided
            if analysis:
                content_lines.extend(self._format_analysis(analysis))
            
            # Add issue breakdown
            open_issues = [i for i in issues if i.state == 'open']
            closed_issues = [i for i in issues if i.state == 'closed']
            
            content_lines.extend([
                f"**Open Issues**: {len(open_issues)}",
                f"**Closed Issues**: {len(closed_issues)}",
                "",
                "---",
                "",
                "## Issues List (Most Recently Updated First)",
                ""
            ])
            
            # Sort issues by update time
            issues_sorted = sorted(issues, key=lambda x: x.updated_at, reverse=True)
            for issue in issues_sorted:
                content_lines.extend([
                    issue.to_markdown_entry(),
                    ""
                ])
        
        content = '\n'.join(content_lines)
        MarkdownUtils.write_markdown_file(content, filepath)
        
        print(f"Issues exported to: {filepath}")
        return filepath
    
    def export_multiple_repositories(self, repo_issues: Dict[str, List[IssueData]], repo_analyses: Dict[str, Dict[str, Any]] = None) -> List[str]:
        """
        Export issues for multiple repositories to separate Markdown files.
        
        Args:
            repo_issues: Dictionary mapping repo_path to list of issues
            repo_analyses: Optional analyses for each repository
        
        Returns:
            List of paths to exported Markdown files
        """
        exported_files = []
        
        for repo_path, issues in repo_issues.items():
            try:
                owner, repo = repo_path.split('/')
                analysis = repo_analyses.get(repo_path) if repo_analyses else None
                filepath = self.export_repository_issues(owner, repo, issues, analysis)
                exported_files.append(filepath)
            except ValueError:
                print(f"Error: Invalid repository path format: {repo_path}")
                continue
        
        return exported_files
    
    def export_summary_report(self, repo_issues: Dict[str, List[IssueData]], summary_analysis: Dict[str, Any], filename: str = 'issues-summary.md') -> str:
        """
        Export a summary report of all issues.
        
        Args:
            repo_issues: Dictionary mapping repo_path to list of issues
            summary_analysis: Summary analysis data
            filename: Output filename
        
        Returns:
            Path to summary report file
        """
        filepath = os.path.join(self.output_dir, filename)
        
        content_lines = [
            "# GitHub Issues Summary Report",
            "",
            f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
            "## Overview",
            ""
        ]
        
        # Add summary statistics
        content_lines.extend(self._format_analysis(summary_analysis))
        
        # Add repository breakdown
        content_lines.extend([
            "",
            "## Repository Breakdown",
            ""
        ])
        
        # Sort repositories by issue count
        repo_list = [(repo_path, len(issues)) for repo_path, issues in repo_issues.items()]
        repo_list.sort(key=lambda x: x[1], reverse=True)
        
        content_lines.append("| Repository | Total Issues | Open | Closed |")
        content_lines.append("|-----------|--------------|------|--------|")
        
        for repo_path, total_issues in repo_list:
            issues = repo_issues[repo_path]
            open_count = len([i for i in issues if i.state == 'open'])
            closed_count = len([i for i in issues if i.state == 'closed'])
            repo_link = f"[{repo_path}](https://github.com/{repo_path})"
            
            content_lines.append(f"| {repo_link} | {total_issues} | {open_count} | {closed_count} |")
        
        content = '\n'.join(content_lines)
        MarkdownUtils.write_markdown_file(content, filepath)
        
        print(f"Summary report exported to: {filepath}")
        return filepath
    
    def _format_analysis(self, analysis: Dict[str, Any]) -> List[str]:
        """Format analysis data for markdown output."""
        lines = []
        
        if 'total_issues' in analysis:
            lines.extend([
                "## Statistics",
                "",
                f"- **Total Issues**: {analysis['total_issues']}",
                f"- **Open Issues**: {analysis['open_issues']} ({analysis['open_percentage']:.1f}%)",
                f"- **Closed Issues**: {analysis['closed_issues']}",
                f"- **Average Comments per Issue**: {analysis['average_comments']}",
                f"- **Recent Activity** (last 30 days): {analysis['recent_activity_count']} issues ({analysis['recent_activity_percentage']:.1f}%)",
                ""
            ])
        
        if 'most_common_labels' in analysis and analysis['most_common_labels']:
            lines.extend([
                "### Most Common Labels",
                ""
            ])
            for label, count in analysis['most_common_labels'][:5]:
                lines.append(f"- **{label}**: {count} issues")
            lines.append("")
        
        if 'issues_by_author' in analysis and analysis['issues_by_author']:
            lines.extend([
                "### Top Issue Authors",
                ""
            ])
            for author, count in list(analysis['issues_by_author'].items())[:5]:
                lines.append(f"- **{author}**: {count} issues")
            lines.append("")
        
        return lines