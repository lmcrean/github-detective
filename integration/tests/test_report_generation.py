"""Integration tests for markdown report generation."""

import pytest
import os
import pandas as pd
import tempfile
import json
from pathlib import Path
import sys

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from scripts.generate_reports import ReportGenerator


class TestReportGeneration:
    """Test markdown report generation functionality."""
    
    @pytest.fixture
    def sample_data(self):
        """Create sample CSV data for testing."""
        return pd.DataFrame([
            {
                'Name': 'test/ai-repo', 
                'Field': 'AI/ML',
                'Stars': 15000,
                'Forks': 2500,
                'Contributors': 150,
                'Open Issues': 45,
                'Open Pull Requests': 12,
                'Date Created': '2020-01-15',
                'Last Active': '2024-01-15'
            },
            {
                'Name': 'test/typescript-repo',
                'Field': 'TypeScript', 
                'Stars': 8000,
                'Forks': 1200,
                'Contributors': 80,
                'Open Issues': 25,
                'Open Pull Requests': 8,
                'Date Created': '2021-03-20',
                'Last Active': '2024-01-10'
            },
            {
                'Name': 'test/csharp-repo',
                'Field': 'C# ASP.NET',
                'Stars': 12000, 
                'Forks': 1800,
                'Contributors': 95,
                'Open Issues': 30,
                'Open Pull Requests': 15,
                'Date Created': '2019-08-12',
                'Last Active': '2024-01-12'
            }
        ])
    
    @pytest.fixture
    def sample_metadata(self):
        """Create sample metadata for testing."""
        return {
            'last_updated': '2024-01-15 12:00:00 UTC',
            'collection_time_seconds': 45.2,
            'total_repositories': 3
        }
    
    def test_overview_report_content(self, sample_data, sample_metadata, tmp_path):
        """Test that overview report contains expected content."""
        # Create temporary files
        csv_path = tmp_path / 'test_data.csv'
        metadata_path = tmp_path / 'github_stats_metadata.json'
        views_path = tmp_path / 'views'
        views_path.mkdir()
        
        sample_data.to_csv(csv_path, index=False)
        with open(metadata_path, 'w') as f:
            json.dump(sample_metadata, f)
        
        # Generate report
        generator = ReportGenerator(str(csv_path))
        
        # Override views path for testing
        original_dir = os.getcwd()
        os.chdir(tmp_path)
        
        try:
            generator.generate_overview_report()
            
            # Check that file was created
            report_path = views_path / 'all.md'
            assert report_path.exists()
            
            # Read and verify content
            content = report_path.read_text(encoding='utf-8')
            
            # Check header and metadata
            assert '# Enterprise Codebases Research - Overview' in content
            assert '2024-01-15 12:00:00 UTC' in content
            
            # Check summary statistics
            assert '**Total Repositories**: 3' in content
            assert '**Total Stars**: 35,000' in content  # 15000 + 8000 + 12000
            assert '**Technology Categories**: 3' in content
            assert '**Collection Time**: 45.2 seconds' in content
            
            # Check category breakdown
            assert '**AI/ML**: 1 repositories (15,000 total stars)' in content
            assert '**TypeScript**: 1 repositories (8,000 total stars)' in content
            assert '**C# ASP.NET**: 1 repositories (12,000 total stars)' in content
            
            # Check table headers
            assert '| Repository | Category | Stars | Forks | Contributors | Open PRs |' in content
            
            # Check top repo (should be AI repo with highest stars)
            assert 'test/ai-repo' in content
            assert '15k' in content  # Formatted stars
            
            # Check links format
            assert 'target="_blank"' in content
            assert 'https://github.com/test/ai-repo' in content
            
        finally:
            os.chdir(original_dir)
    
    def test_category_report_content(self, sample_data, sample_metadata, tmp_path):
        """Test that category reports contain expected content."""
        # Create temporary files
        csv_path = tmp_path / 'test_data.csv'
        metadata_path = tmp_path / 'github_stats_metadata.json'
        views_path = tmp_path / 'views'
        views_path.mkdir()
        
        sample_data.to_csv(csv_path, index=False)
        with open(metadata_path, 'w') as f:
            json.dump(sample_metadata, f)
        
        # Generate report
        generator = ReportGenerator(str(csv_path))
        
        # Override views path for testing
        original_dir = os.getcwd()
        os.chdir(tmp_path)
        
        try:
            generator._generate_category_report('AI/ML', 'ai_ml.md')
            
            # Check that file was created
            report_path = views_path / 'ai_ml.md'
            assert report_path.exists()
            
            # Read and verify content
            content = report_path.read_text(encoding='utf-8')
            
            # Check header
            assert '# AI/ML Repositories' in content
            assert '2024-01-15 12:00:00 UTC' in content
            
            # Check overview statistics
            assert '**Total Repositories**: 1' in content
            assert '**Total Stars**: 15,000' in content
            assert '**Average Stars**: 15,000' in content
            
            # Check table structure
            assert '| Repository | Stars | Forks | Contributors | Open Issues | Open PRs | Created | Last Active |' in content
            
            # Check repository data
            assert 'test/ai-repo' in content
            assert '15k' in content  # Formatted number
            assert '2.5k' in content  # Formatted forks
            assert '150' in content  # Contributors
            assert '2020-01-15' in content  # Created date
            
            # Check insights section
            assert '## Key Insights' in content
            assert '### Most Popular' in content
            assert '### Most Active Development' in content
            
            # Check navigation
            assert '[← Back to Overview](all.md)' in content
            
        finally:
            os.chdir(original_dir)
    
    def test_report_formatting_consistency(self, sample_data, sample_metadata, tmp_path):
        """Test that number formatting is consistent across reports."""
        # Create temporary files
        csv_path = tmp_path / 'test_data.csv'
        metadata_path = tmp_path / 'github_stats_metadata.json'
        views_path = tmp_path / 'views'
        views_path.mkdir()
        
        sample_data.to_csv(csv_path, index=False)
        with open(metadata_path, 'w') as f:
            json.dump(sample_metadata, f)
        
        generator = ReportGenerator(str(csv_path))
        
        original_dir = os.getcwd()
        os.chdir(tmp_path)
        
        try:
            generator.generate_all_reports()
            
            # Read all generated files
            all_content = (views_path / 'all.md').read_text(encoding='utf-8')
            ai_content = (views_path / 'ai_ml.md').read_text(encoding='utf-8')
            
            # Check consistent formatting of same numbers
            # AI repo has 15000 stars -> should be "15k" in both files
            assert '15k' in all_content
            assert '15k' in ai_content
            
            # Check that forks (2500) are formatted as "2.5k"
            assert '2.5k' in all_content or '2.5k' in ai_content
            
        finally:
            os.chdir(original_dir)
    
    def test_empty_category_handling(self, tmp_path):
        """Test handling of empty categories."""
        # Create empty dataset for a category
        empty_data = pd.DataFrame(columns=['Name', 'Field', 'Stars', 'Forks', 'Contributors', 'Open Issues', 'Open Pull Requests', 'Date Created', 'Last Active'])
        
        csv_path = tmp_path / 'empty_data.csv'
        metadata_path = tmp_path / 'github_stats_metadata.json'
        views_path = tmp_path / 'views'
        views_path.mkdir()
        
        empty_data.to_csv(csv_path, index=False)
        with open(metadata_path, 'w') as f:
            json.dump({'last_updated': '2024-01-15', 'collection_time_seconds': 0}, f)
        
        generator = ReportGenerator(str(csv_path))
        
        original_dir = os.getcwd()
        os.chdir(tmp_path)
        
        try:
            # This should not crash and should handle empty data gracefully
            generator._generate_category_report('NonExistent', 'test.md')
            
            # File should not be created for empty categories
            assert not (views_path / 'test.md').exists()
            
        finally:
            os.chdir(original_dir)


class TestReportValidation:
    """Test validation of generated reports against live data."""
    
    @pytest.mark.skipif(not Path('data/raw/github_repository_stats.csv').exists(), 
                       reason="No live data available")
    def test_live_data_report_generation(self):
        """Test report generation with actual collected data."""
        # Only run if we have real data
        generator = ReportGenerator()
        
        # Test that we can generate reports without errors
        generator.generate_all_reports()
        
        # Verify files were created
        assert Path('views/all.md').exists()
        assert Path('views/ai_ml.md').exists()
        assert Path('views/typescript.md').exists()
        assert Path('views/csharp.md').exists()
        
        # Basic content validation
        all_content = Path('views/all.md').read_text(encoding='utf-8')
        assert '# Enterprise Codebases Research - Overview' in all_content
        assert 'Total Repositories' in all_content
        assert 'Total Stars' in all_content


if __name__ == '__main__':
    pytest.main([__file__, '-v'])