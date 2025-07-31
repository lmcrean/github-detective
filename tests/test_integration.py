"""Integration tests for GitHub API functionality."""

import pytest
import os
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from github_client.client import GitHubClient
from github_client.collector import RepositoryCollector
from github_client.utils import format_number, format_repo_stats_for_display


class TestGitHubClient:
    """Test GitHub API client functionality."""
    
    def test_format_number(self):
        """Test number formatting utility."""
        assert format_number(999) == "999"
        assert format_number(1234) == "1.2k"
        assert format_number(12345) == "12k"
        assert format_number(1234567) == "1.2M"
        assert format_number(12345678) == "12M"
        assert format_number(1234567890) == "1.2B"
    
    def test_client_initialization(self):
        """Test client can be initialized."""
        client = GitHubClient()
        assert client.base_url == 'https://api.github.com'
        assert client.headers == {}
        
        client_with_token = GitHubClient("test_token")
        assert client_with_token.headers == {'Authorization': 'token test_token'}
    
    @pytest.mark.skipif(not os.environ.get('API_GITHUB_TOKEN'), reason="No GitHub token available")
    def test_real_api_call(self):
        """Test actual API call with real token (if available)."""
        token = os.environ.get('API_GITHUB_TOKEN')
        client = GitHubClient(token)
        
        # Test with a small, stable repository
        stats = client.get_repo_stats('octocat', 'Hello-World')
        
        if stats:  # Only test if repo exists and is accessible
            assert stats.repo_path == 'octocat/Hello-World'
            assert isinstance(stats.stars, int)
            assert isinstance(stats.forks, int)
            assert stats.field == ''  # Should be empty initially


class TestRepositoryCollector:
    """Test repository collector functionality."""
    
    def test_collector_initialization(self):
        """Test collector can be initialized."""
        collector = RepositoryCollector()
        assert isinstance(collector.client, GitHubClient)
        assert collector.results == []
    
    def test_format_repo_stats_for_display(self):
        """Test stats formatting for display."""
        test_stats = [
            {
                'Name': 'test/repo',
                'Stars': 12345,
                'Forks': 678,
                'Contributors': 42,
                'Open Pull Requests': 5
            }
        ]
        
        formatted = format_repo_stats_for_display(test_stats)
        
        assert len(formatted) == 1
        assert formatted[0]['Stars'] == '12k'
        assert formatted[0]['Forks'] == '678'
        assert formatted[0]['Contributors'] == '42'


class TestConfigurationLoading:
    """Test configuration file loading."""
    
    def test_yaml_config_exists(self):
        """Test that repositories.yml exists and is readable."""  
        config_path = Path(__file__).parent.parent / 'src' / 'config' / 'repositories.yml'
        assert config_path.exists(), "repositories.yml should exist"
        
        import yaml
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
        
        assert 'repositories' in config
        assert isinstance(config['repositories'], dict)
        assert len(config['repositories']) > 0


class TestDataPersistence:
    """Test data saving and loading."""
    
    def test_data_directory_structure(self):
        """Test that required directories exist."""
        github_repo_root = Path(__file__).parent.parent
        assert (github_repo_root / 'data' / 'output').exists()
        assert (github_repo_root / 'src').exists()
        assert (github_repo_root / 'scripts').exists()
        assert (github_repo_root / 'tests').exists()


if __name__ == '__main__':
    pytest.main([__file__, '-v'])