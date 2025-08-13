"""Repository analysis functionality."""

from typing import List, Dict, Any
from collections import Counter
from ..models.github_models import RepositoryStats


class RepositoryAnalyzer:
    """Analyzes GitHub repositories for insights and metrics."""
    
    def __init__(self):
        """Initialize analyzer."""
        pass
    
    def analyze_repositories(self, repositories: List[RepositoryStats]) -> Dict[str, Any]:
        """
        Analyze a collection of repositories and return metrics.
        
        Args:
            repositories: List of repository statistics
        
        Returns:
            Dictionary with analysis metrics
        """
        if not repositories:
            return self._empty_analysis()
        
        # Basic counts
        total_repos = len(repositories)
        
        # Aggregate metrics
        total_stars = sum(repo.stars for repo in repositories)
        total_forks = sum(repo.forks for repo in repositories)
        total_issues = sum(repo.open_issues for repo in repositories)
        
        # Language analysis
        all_languages = []
        for repo in repositories:
            if repo.languages:
                # Extract languages from the formatted string
                lang_parts = repo.languages.split(', ')
                for part in lang_parts:
                    if '(' in part:
                        lang_name = part.split(' (')[0]
                        all_languages.append(lang_name)
        
        language_counts = Counter(all_languages)
        
        # Field/category analysis
        field_counts = Counter(repo.field for repo in repositories)
        
        # Size categorization by stars
        size_categories = {
            'large': len([r for r in repositories if r.stars >= 10000]),
            'medium': len([r for r in repositories if 1000 <= r.stars < 10000]),
            'small': len([r for r in repositories if 100 <= r.stars < 1000]),
            'tiny': len([r for r in repositories if r.stars < 100])
        }
        
        # Activity analysis (repositories with PRs)
        repos_with_prs = [r for r in repositories if r.open_prs > 0]
        avg_prs = sum(r.open_prs for r in repos_with_prs) / len(repos_with_prs) if repos_with_prs else 0
        
        # Contributor analysis
        repos_with_contributors = [r for r in repositories if r.contributors > 0]
        avg_contributors = sum(r.contributors for r in repos_with_contributors) / len(repos_with_contributors) if repos_with_contributors else 0
        
        return {
            'total_repositories': total_repos,
            'total_stars': total_stars,
            'total_forks': total_forks,
            'total_open_issues': total_issues,
            'average_stars': total_stars / total_repos if total_repos > 0 else 0,
            'average_forks': total_forks / total_repos if total_repos > 0 else 0,
            'average_open_issues': total_issues / total_repos if total_repos > 0 else 0,
            'average_prs': round(avg_prs, 1),
            'average_contributors': round(avg_contributors, 1),
            'most_common_languages': language_counts.most_common(10),
            'field_distribution': dict(field_counts),
            'size_distribution': size_categories,
            'repos_with_prs': len(repos_with_prs),
            'repos_with_contributors': len(repos_with_contributors)
        }
    
    def analyze_by_field(self, repositories: List[RepositoryStats]) -> Dict[str, Dict[str, Any]]:
        """
        Analyze repositories grouped by field/category.
        
        Args:
            repositories: List of repository statistics
        
        Returns:
            Dictionary mapping field to analysis results
        """
        field_analyses = {}
        
        # Group repositories by field
        repos_by_field = {}
        for repo in repositories:
            field = repo.field or 'Unknown'
            if field not in repos_by_field:
                repos_by_field[field] = []
            repos_by_field[field].append(repo)
        
        # Analyze each field
        for field, field_repos in repos_by_field.items():
            field_analyses[field] = self.analyze_repositories(field_repos)
        
        return field_analyses
    
    def get_top_repositories(self, repositories: List[RepositoryStats], 
                           sort_by: str = 'stars', limit: int = 10) -> List[RepositoryStats]:
        """
        Get top repositories sorted by specified metric.
        
        Args:
            repositories: List of repository statistics
            sort_by: Metric to sort by ('stars', 'forks', 'open_issues', 'contributors', 'open_prs')
            limit: Maximum number of repositories to return
        
        Returns:
            List of top repositories
        """
        if not repositories:
            return []
        
        sort_key_map = {
            'stars': lambda r: r.stars,
            'forks': lambda r: r.forks,
            'open_issues': lambda r: r.open_issues,
            'contributors': lambda r: r.contributors if r.contributors > 0 else 0,
            'open_prs': lambda r: r.open_prs if r.open_prs > 0 else 0
        }
        
        if sort_by not in sort_key_map:
            sort_by = 'stars'
        
        sorted_repos = sorted(repositories, key=sort_key_map[sort_by], reverse=True)
        return sorted_repos[:limit]
    
    def identify_trending_repositories(self, repositories: List[RepositoryStats]) -> List[RepositoryStats]:
        """
        Identify potentially trending repositories based on various factors.
        
        Args:
            repositories: List of repository statistics
        
        Returns:
            List of trending repositories
        """
        if not repositories:
            return []
        
        trending_candidates = []
        
        for repo in repositories:
            # Calculate a "trending score" based on multiple factors
            score = 0
            
            # Stars per contributor ratio (indicates efficiency/quality)
            if repo.contributors > 0:
                stars_per_contributor = repo.stars / repo.contributors
                score += min(stars_per_contributor / 100, 5)  # Cap at 5 points
            
            # High PR activity indicates active development
            if repo.open_prs > 0:
                score += min(repo.open_prs / 10, 3)  # Cap at 3 points
            
            # Balance between stars and issues (good maintenance)
            if repo.stars > 0 and repo.open_issues >= 0:
                issue_ratio = repo.open_issues / repo.stars
                if issue_ratio < 0.1:  # Low issue ratio is good
                    score += 2
            
            # Add score to repo for sorting
            repo.trending_score = score
            
            if score > 3:  # Minimum threshold for trending
                trending_candidates.append(repo)
        
        # Sort by trending score and return top candidates
        trending_candidates.sort(key=lambda r: r.trending_score, reverse=True)
        return trending_candidates[:20]  # Top 20 trending
    
    def _empty_analysis(self) -> Dict[str, Any]:
        """Return empty analysis structure."""
        return {
            'total_repositories': 0,
            'total_stars': 0,
            'total_forks': 0,
            'total_open_issues': 0,
            'average_stars': 0,
            'average_forks': 0,
            'average_open_issues': 0,
            'average_prs': 0,
            'average_contributors': 0,
            'most_common_languages': [],
            'field_distribution': {},
            'size_distribution': {'large': 0, 'medium': 0, 'small': 0, 'tiny': 0},
            'repos_with_prs': 0,
            'repos_with_contributors': 0
        }