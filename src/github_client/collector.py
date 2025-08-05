"""GitHub repository data collector."""

import os
import time
import pandas as pd
import json
from typing import Dict, List, Optional
from dotenv import load_dotenv

from .client import GitHubClient
from .models import RepositoryStats, CollectionMetadata
from .markdown_generator import MarkdownGenerator


class RepositoryCollector:
    """Collects GitHub repository statistics."""
    
    def __init__(self, token: Optional[str] = None):
        """Initialize collector with optional GitHub token."""
        self.client = GitHubClient(token)
        self.results: List[RepositoryStats] = []
    
    def collect_repositories(self, repositories_config: Dict[str, List[str]]) -> List[RepositoryStats]:
        """Collect statistics for all repositories in config."""
        self.results = []
        total_repos = sum(len(repos) for repos in repositories_config.values())
        current_repo = 0
        
        for field, repo_list in repositories_config.items():
            print(f"\nProcessing {field} repositories...")
            
            for repo_path in repo_list:
                current_repo += 1
                owner, repo = repo_path.split('/')
                
                print(f"[{current_repo}/{total_repos}] Fetching {repo_path}... ", end="")
                
                stats = self.client.get_repo_stats(owner, repo)
                if stats:
                    stats.field = field  # Set the category
                    self.results.append(stats)
                    contributors_text = str(stats.contributors) if stats.contributors >= 0 else "N/A"
                    prs_text = str(stats.open_prs) if stats.open_prs >= 0 else "N/A"
                    languages_text = stats.languages[:50] + "..." if len(stats.languages) > 50 else stats.languages
                    languages_text = languages_text if languages_text else "N/A"
                    print(f"Success: {stats.stars} stars, {contributors_text} contributors, {prs_text} PRs, {languages_text}")
                else:
                    print("Failed")
                
                time.sleep(0.1)  # Rate limiting
        
        return self.results
    
    def save_to_csv(self, filepath: str) -> None:
        """Save collected data to CSV file."""
        if not self.results:
            print("No data to save")
            return
        
        # Convert to DataFrame
        data = [repo.to_dict() for repo in self.results]
        df = pd.DataFrame(data)
        
        # Save to CSV
        df.to_csv(filepath, index=False)
        print(f"Data saved to {filepath}")
    
    def save_metadata(self, filepath: str, collection_time: float) -> None:
        """Save collection metadata to JSON file."""
        if not self.results:
            return
        
        total_stars = sum(repo.stars for repo in self.results)
        metadata = CollectionMetadata.create(
            repo_count=len(self.results),
            total_stars=total_stars,
            collection_time=collection_time
        )
        
        with open(filepath, 'w') as f:
            json.dump(metadata.__dict__, f, indent=2)
        
        print(f"Metadata saved to {filepath}")


def main():
    """Main collection script."""
    # Load environment variables
    load_dotenv()
    github_token = os.getenv('API_GITHUB_TOKEN')  # Get token from environment
    
    # Load repository configuration
    import yaml
    with open('src/config/repositories.yml', 'r') as f:
        repositories_config = yaml.safe_load(f)['repositories']
    
    print("Starting data collection...")
    print(f"Authentication: {'Enabled' if github_token else 'Disabled (60 requests/hour limit)'}")
    print("="*50)
    
    # Collect data
    collector = RepositoryCollector(github_token)
    start_time = time.time()
    results = collector.collect_repositories(repositories_config)
    end_time = time.time()
    
    print("\n" + "="*50)
    print(f"Data collection completed!")
    print(f"Successfully collected data for {len(results)} repositories")
    print(f"Total time: {end_time - start_time:.2f} seconds")
    
    # Save results
    csv_path = 'data/output/github_repository_stats.csv'
    collector.save_to_csv(csv_path)
    collector.save_metadata('data/output/github_stats_metadata.json', end_time - start_time)
    
    # Generate markdown documentation
    print("\nGenerating markdown documentation...")
    markdown_gen = MarkdownGenerator(csv_path)
    markdown_gen.generate_markdown_files()
    print("Markdown documentation generated in docs/ directory")


if __name__ == '__main__':
    main()