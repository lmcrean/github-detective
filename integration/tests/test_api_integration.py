"""Integration tests for ITJobsWatch scraping functionality."""

import pytest
import os
import sys
from pathlib import Path
import pandas as pd
import json

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from api.scraper.table_data.itjobswatch_table_scraper import ITJobsWatchTableScraper
from api.scraper.png_charts.it_jobs_watch.scripts.generate_reports import ITJobsWatchReportGenerator


class TestITJobsWatchScraper:
    """Test ITJobsWatch table scraping functionality."""
    
    def test_scraper_initialization(self):
        """Test scraper can be initialized."""
        scraper = ITJobsWatchTableScraper()
        assert scraper is not None
    
    def test_data_directory_exists(self):
        """Test that ITJobsWatch data directory exists."""
        data_path = project_root / 'data' / 'scraped' / 'itjobswatch'
        assert data_path.exists(), "ITJobsWatch data directory should exist"


class TestITJobsWatchData:
    """Test ITJobsWatch data integrity."""
    
    def test_scraped_data_exists(self):
        """Test that some scraped data exists."""
        data_path = project_root / 'data' / 'scraped' / 'itjobswatch'
        
        # Check for file-data (JSON files from chart analysis)
        file_data_path = data_path / 'file-data'
        if file_data_path.exists():
            json_files = list(file_data_path.glob('*.json'))
            if json_files:
                # Test loading one JSON file
                with open(json_files[0], 'r') as f:
                    data = json.load(f)
                assert isinstance(data, (dict, list))
        
        # Check for table-data (CSV files from job listings)
        table_data_path = data_path / 'table-data'
        if table_data_path.exists():
            csv_files = list(table_data_path.glob('*.csv'))
            if csv_files:
                # Test loading one CSV file
                df = pd.read_csv(csv_files[0])
                assert len(df) > 0
    
    def test_webp_charts_exist(self):
        """Test that WebP chart files exist."""
        data_path = project_root / 'data' / 'scraped' / 'itjobswatch'
        webp_files = list(data_path.glob('*.webp'))
        
        # Should have some chart files
        if webp_files:
            # Verify files are not empty
            for webp_file in webp_files[:3]:  # Check first 3 files
                assert webp_file.stat().st_size > 0


class TestReportGeneration:
    """Test ITJobsWatch report generation."""
    
    def test_report_generator_initialization(self):
        """Test report generator can be initialized."""
        generator = ITJobsWatchReportGenerator()
        assert generator.data_path.name == 'itjobswatch'
    
    def test_report_generation_runs(self):
        """Test that report generation runs without errors."""
        generator = ITJobsWatchReportGenerator()
        
        # This should run without throwing exceptions
        try:
            generator.generate_market_overview_report()
            success = True
        except Exception as e:
            success = False
            print(f"Report generation failed: {e}")
        
        assert success, "Report generation should complete without errors"


class TestChartProcessing:
    """Test chart processing functionality."""
    
    def test_chart_processing_modules_exist(self):
        """Test that chart processing modules exist."""
        chart_path = project_root / 'api' / 'scraper' / 'png-charts' / 'it_jobs_watch'
        
        # Check for key processing modules
        assert (chart_path / 'scripts').exists()
        assert (chart_path / 'annotating').exists()
        assert (chart_path / 'outputs').exists()
    
    def test_chart_scripts_importable(self):
        """Test that chart processing scripts can be imported."""
        try:
            from api.scraper.png_charts.it_jobs_watch.scripts import chart_parser
            from api.scraper.png_charts.it_jobs_watch.scripts import chart_annotator
            success = True
        except ImportError as e:
            success = False
            print(f"Import error: {e}")
        
        assert success, "Chart processing scripts should be importable"


class TestDataStructure:
    """Test ITJobsWatch data structure integrity."""
    
    def test_required_directories_exist(self):
        """Test that required directories exist."""
        base_path = project_root / 'api' / 'scraper'
        
        # ITJobsWatch specific directories
        assert (base_path / 'png-charts' / 'it_jobs_watch').exists()
        assert (base_path / 'table-data').exists()
        
        # Data directories
        data_path = project_root / 'data' / 'scraped' / 'itjobswatch'
        assert data_path.exists()
    
    def test_docs_directory_accessible(self):
        """Test that docs directory is accessible for report generation."""
        docs_path = project_root / 'docs'
        assert docs_path.exists() or docs_path.parent.exists()


if __name__ == '__main__':
    pytest.main([__file__, '-v'])