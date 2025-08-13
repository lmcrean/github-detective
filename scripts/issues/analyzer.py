"""Issue analysis functionality."""

from typing import List, Dict, Any
from collections import Counter
from ..models.github_models import IssueData


class IssueAnalyzer:
    """Analyzes GitHub issues for insights and metrics."""
    
    def __init__(self):
        """Initialize analyzer."""
        pass
    
    def analyze_issues(self, issues: List[IssueData]) -> Dict[str, Any]:
        """
        Analyze a collection of issues and return metrics.
        
        Args:
            issues: List of issue data
        
        Returns:
            Dictionary with analysis metrics
        """
        if not issues:
            return self._empty_analysis()
        
        # Basic counts
        total_issues = len(issues)
        open_issues = [i for i in issues if i.state == 'open']
        closed_issues = [i for i in issues if i.state == 'closed']
        
        # Label analysis
        all_labels = []
        for issue in issues:
            all_labels.extend(issue.labels)
        label_counts = Counter(all_labels)
        
        # Comment analysis
        comment_counts = [i.comments for i in issues]
        avg_comments = sum(comment_counts) / len(comment_counts) if comment_counts else 0
        
        # Recent activity (issues updated in last 30 days)
        from datetime import datetime, timedelta
        cutoff_date = datetime.now() - timedelta(days=30)
        recent_issues = []
        for issue in issues:
            try:
                updated_dt = datetime.fromisoformat(issue.updated_at.replace('Z', '+00:00'))
                if updated_dt.replace(tzinfo=None) > cutoff_date:
                    recent_issues.append(issue)
            except:
                continue
        
        return {
            'total_issues': total_issues,
            'open_issues': len(open_issues),
            'closed_issues': len(closed_issues),
            'open_percentage': (len(open_issues) / total_issues * 100) if total_issues > 0 else 0,
            'most_common_labels': label_counts.most_common(10),
            'average_comments': round(avg_comments, 1),
            'recent_activity_count': len(recent_issues),
            'recent_activity_percentage': (len(recent_issues) / total_issues * 100) if total_issues > 0 else 0,
            'issues_by_author': self._analyze_authors(issues),
            'comment_distribution': self._analyze_comment_distribution(comment_counts)
        }
    
    def analyze_multiple_repositories(self, repo_issues: Dict[str, List[IssueData]]) -> Dict[str, Dict[str, Any]]:
        """
        Analyze issues for multiple repositories.
        
        Args:
            repo_issues: Dictionary mapping repo_path to list of issues
        
        Returns:
            Dictionary mapping repo_path to analysis results
        """
        analyses = {}
        
        for repo_path, issues in repo_issues.items():
            analyses[repo_path] = self.analyze_issues(issues)
        
        return analyses
    
    def get_summary_statistics(self, repo_issues: Dict[str, List[IssueData]]) -> Dict[str, Any]:
        """
        Get summary statistics across all repositories.
        
        Args:
            repo_issues: Dictionary mapping repo_path to list of issues
        
        Returns:
            Summary statistics dictionary
        """
        all_issues = []
        for issues in repo_issues.values():
            all_issues.extend(issues)
        
        total_repos = len(repo_issues)
        repos_with_issues = len([repo for repo, issues in repo_issues.items() if issues])
        
        analysis = self.analyze_issues(all_issues)
        analysis.update({
            'total_repositories': total_repos,
            'repositories_with_issues': repos_with_issues,
            'average_issues_per_repo': len(all_issues) / repos_with_issues if repos_with_issues > 0 else 0
        })
        
        return analysis
    
    def _empty_analysis(self) -> Dict[str, Any]:
        """Return empty analysis structure."""
        return {
            'total_issues': 0,
            'open_issues': 0,
            'closed_issues': 0,
            'open_percentage': 0,
            'most_common_labels': [],
            'average_comments': 0,
            'recent_activity_count': 0,
            'recent_activity_percentage': 0,
            'issues_by_author': {},
            'comment_distribution': {}
        }
    
    def _analyze_authors(self, issues: List[IssueData]) -> Dict[str, int]:
        """Analyze issue authors."""
        authors = [i.author for i in issues if i.author]
        return dict(Counter(authors).most_common(10))
    
    def _analyze_comment_distribution(self, comment_counts: List[int]) -> Dict[str, int]:
        """Analyze distribution of comment counts."""
        if not comment_counts:
            return {}
        
        return {
            'no_comments': len([c for c in comment_counts if c == 0]),
            'few_comments_1_5': len([c for c in comment_counts if 1 <= c <= 5]),
            'moderate_comments_6_15': len([c for c in comment_counts if 6 <= c <= 15]),
            'many_comments_16_plus': len([c for c in comment_counts if c >= 16]),
            'max_comments': max(comment_counts),
            'min_comments': min(comment_counts)
        }