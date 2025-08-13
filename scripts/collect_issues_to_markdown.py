"""Collect GitHub issues from CSV and save as individual markdown files."""

import os
import csv
import re
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional, Tuple
from urllib.parse import urlparse

# Add parent directory to path for imports
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.github_client.client import GitHubClient
from scripts.merged_prs_30d.fetch_merged_prs import MergedPRsFetcher

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


class IssueToMarkdownCollector:
    """Collect GitHub issues and save them as markdown files."""
    
    def __init__(self):
        """Initialize the collector with GitHub clients."""
        token = os.getenv('API_GITHUB_TOKEN') or os.getenv('GITHUB_TOKEN')
        self.github_client = GitHubClient(token)
        self.pr_fetcher = MergedPRsFetcher(token)
        self.pr_rate_cache = {}  # Cache for PR rates to avoid duplicate API calls
        
    def parse_github_url(self, url: str) -> Optional[Tuple[str, str, int]]:
        """Parse GitHub issue URL to extract owner, repo, and issue number."""
        try:
            # Pattern: https://github.com/owner/repo/issues/number
            match = re.search(r'github\.com/([^/]+)/([^/]+)/issues/(\d+)', url)
            if match:
                return match.group(1), match.group(2), int(match.group(3))
            return None
        except Exception as e:
            print(f"Error parsing URL {url}: {e}")
            return None
    
    def sanitize_filename(self, text: str, max_length: int = 15) -> str:
        """Sanitize text for use in filename."""
        # Remove special characters, keeping only alphanumeric, space, and hyphen
        text = re.sub(r'[^a-zA-Z0-9\s\-]', '', text)
        # Replace spaces with hyphens
        text = re.sub(r'\s+', '-', text)
        # Remove consecutive hyphens
        text = re.sub(r'-+', '-', text)
        # Trim to max length, ensuring we don't cut in the middle of a word
        if len(text) > max_length:
            text = text[:max_length]
            # Remove trailing hyphen if present
            text = text.rstrip('-')
        # Convert to lowercase
        return text.lower()
    
    def get_30d_pr_rate(self, owner: str, repo: str) -> int:
        """Get 30-day PR merge rate for a repository (cached)."""
        cache_key = f"{owner}/{repo}"
        if cache_key in self.pr_rate_cache:
            return self.pr_rate_cache[cache_key]
        
        print(f"  Fetching 30-day PR merge rate for {owner}/{repo}...")
        rate = self.pr_fetcher.get_merged_prs_count(owner, repo, days=30)
        self.pr_rate_cache[cache_key] = rate
        return rate
    
    def format_datetime(self, datetime_str: str) -> Tuple[str, str, str]:
        """Parse ISO datetime string and return date, date part, and time."""
        try:
            dt = datetime.fromisoformat(datetime_str.replace('Z', '+00:00'))
            date = dt.strftime('%Y-%m-%d')
            time = dt.strftime('%H:%M:%S')
            return date, date, time
        except Exception as e:
            print(f"Error parsing datetime {datetime_str}: {e}")
            return datetime_str[:10] if len(datetime_str) >= 10 else datetime_str, "", ""
    
    def create_markdown_content(self, issue_data: Dict, comments: list, pr_rate: int, url: str) -> str:
        """Create markdown content for an issue."""
        # Extract issue details
        title = issue_data.get('title', 'No title')
        labels = ', '.join([label['name'] for label in issue_data.get('labels', [])])
        comment_count = issue_data.get('comments', 0)
        status = issue_data.get('state', 'unknown')
        created_date, _, _ = self.format_datetime(issue_data.get('created_at', ''))
        body = issue_data.get('body', '') or ''
        
        # Build markdown content
        content = []
        content.append(f"issue title: {title}")
        content.append(f"labels: {labels if labels else 'none'}")
        content.append(f"comment count: {comment_count}")
        content.append(f"hyperlink: {url}")
        content.append(f"status: {status}")
        content.append(f"date opened: {created_date}")
        content.append(f"repo 30d_merge_rate: {pr_rate if pr_rate >= 0 else 'unknown'}")
        content.append("")
        content.append("====")
        content.append("")
        content.append("description:")
        content.append(body)
        content.append("")
        content.append("===")
        content.append("")
        
        # Add comments
        for i, comment in enumerate(comments, 1):
            author = comment.get('user', {}).get('login', 'unknown')
            created_at = comment.get('created_at', '')
            date, _, time = self.format_datetime(created_at)
            comment_body = comment.get('body', '')
            
            content.append(f"comment #{i} by {author}, {date}, {time}")
            content.append(comment_body)
            content.append("")
        
        return '\n'.join(content)
    
    def generate_filename(self, owner: str, repo: str, title: str, date_str: str, 
                         output_dir: Path) -> Path:
        """Generate unique filename for the issue."""
        # Parse date to get components
        try:
            dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            year = dt.strftime('%y')  # 2-digit year
            month = dt.strftime('%m')  # 2-digit month
            day = dt.strftime('%d')    # 2-digit day
        except Exception:
            # Fallback if date parsing fails
            year, month, day = '00', '00', '00'
        
        # Create directory structure
        dir_path = output_dir / year / month
        dir_path.mkdir(parents=True, exist_ok=True)
        
        # Generate filename components
        org_prefix = owner[:3].lower()
        repo_prefix = repo[:10].lower()
        title_part = self.sanitize_filename(title, 15)
        
        # Build base filename
        base_filename = f"{day}_{org_prefix}_{repo_prefix}_{title_part}.md"
        file_path = dir_path / base_filename
        
        # Handle duplicates by appending number
        counter = 2
        while file_path.exists():
            alt_filename = f"{day}_{org_prefix}_{repo_prefix}_{title_part}_{counter}.md"
            file_path = dir_path / alt_filename
            counter += 1
        
        return file_path
    
    def process_csv(self, csv_path: str, output_dir: str = "data/issues"):
        """Process CSV file and collect all issues."""
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Read CSV file
        with open(csv_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)
            total_issues = len(rows)
            
            print(f"Found {total_issues} issues to process")
            
            success_count = 0
            error_count = 0
            
            for idx, row in enumerate(rows, 1):
                url = row.get('hyperlink', '')
                print(f"\nProcessing issue {idx}/{total_issues}: {url}")
                
                # Parse URL
                parsed = self.parse_github_url(url)
                if not parsed:
                    print(f"  Error: Could not parse URL")
                    error_count += 1
                    continue
                
                owner, repo, issue_number = parsed
                
                try:
                    # Fetch issue details
                    print(f"  Fetching issue details for {owner}/{repo}#{issue_number}")
                    issue_data = self.github_client.get_issue_details(owner, repo, issue_number)
                    
                    if not issue_data:
                        print(f"  Error: Could not fetch issue details")
                        error_count += 1
                        continue
                    
                    # Fetch comments
                    print(f"  Fetching comments...")
                    comments = self.github_client.get_issue_comments(owner, repo, issue_number)
                    print(f"  Found {len(comments)} comments")
                    
                    # Get PR rate (cached)
                    pr_rate = self.get_30d_pr_rate(owner, repo)
                    
                    # Generate markdown content
                    markdown_content = self.create_markdown_content(
                        issue_data, comments, pr_rate, url
                    )
                    
                    # Generate filename and save
                    file_path = self.generate_filename(
                        owner, repo, 
                        issue_data.get('title', 'untitled'),
                        issue_data.get('created_at', ''),
                        output_path
                    )
                    
                    # Write markdown file
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(markdown_content)
                    
                    print(f"  Saved to: {file_path}")
                    success_count += 1
                    
                    # Small delay to respect API rate limits
                    time.sleep(0.5)
                    
                except Exception as e:
                    print(f"  Error processing issue: {e}")
                    error_count += 1
                    continue
            
            # Print summary
            print(f"\n{'='*60}")
            print(f"Processing complete!")
            print(f"  Successfully processed: {success_count}/{total_issues} issues")
            print(f"  Errors: {error_count}")
            print(f"  Output directory: {output_path}")


def main():
    """Main entry point."""
    csv_path = "data/repos/shopify_stripe_filter3.csv"
    
    # Check if CSV exists
    if not os.path.exists(csv_path):
        print(f"Error: CSV file not found at {csv_path}")
        return
    
    # Create collector and process
    collector = IssueToMarkdownCollector()
    collector.process_csv(csv_path)


if __name__ == "__main__":
    main()