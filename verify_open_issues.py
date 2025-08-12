import pandas as pd
import requests
import re
import time
import os
from typing import Dict, Any, Optional

class IssueStatusChecker:
    def __init__(self, token: Optional[str] = None):
        """Initialize with GitHub token for API access."""
        self.token = token
        self.headers = {'Authorization': f'token {token}'} if token else {}
        self.base_url = 'https://api.github.com'
        self.checked_count = 0
        self.open_count = 0
        self.closed_count = 0
        self.error_count = 0
    
    def extract_issue_info(self, hyperlink: str) -> Dict[str, str]:
        """Extract owner, repo, and issue number from GitHub URL."""
        # Pattern: https://github.com/owner/repo/issues/number
        pattern = r'https://github\.com/([^/]+)/([^/]+)/issues/(\d+)'
        match = re.match(pattern, hyperlink)
        
        if match:
            return {
                'owner': match.group(1),
                'repo': match.group(2),
                'issue_number': match.group(3)
            }
        else:
            return {}
    
    def check_issue_status(self, owner: str, repo: str, issue_number: str) -> Optional[str]:
        """Check if GitHub issue is open or closed."""
        url = f'{self.base_url}/repos/{owner}/{repo}/issues/{issue_number}'
        
        try:
            response = requests.get(url, headers=self.headers)
            
            if response.status_code == 200:
                data = response.json()
                return data.get('state', 'unknown')
            elif response.status_code == 404:
                print(f"  Issue #{issue_number} not found (404) - may have been deleted")
                return 'not_found'
            elif response.status_code == 403:
                print(f"  Rate limit or access denied for {owner}/{repo}#{issue_number}")
                return 'access_denied'
            else:
                print(f"  API error {response.status_code} for {owner}/{repo}#{issue_number}")
                return 'error'
                
        except Exception as e:
            print(f"  Exception checking {owner}/{repo}#{issue_number}: {str(e)}")
            return 'error'
    
    def process_csv_file(self, input_file: str, output_file: str):
        """Process CSV file to verify issue statuses and filter open issues."""
        print(f"Loading CSV file: {input_file}")
        df = pd.read_csv(input_file)
        
        print(f"Found {len(df)} issues to verify")
        
        # Track results
        open_issues = []
        
        for index, row in df.iterrows():
            self.checked_count += 1
            hyperlink = row['hyperlink']
            
            # Extract issue info from URL
            issue_info = self.extract_issue_info(hyperlink)
            
            if not issue_info:
                print(f"  [{self.checked_count}/{len(df)}] Could not parse URL: {hyperlink}")
                self.error_count += 1
                continue
            
            owner = issue_info['owner']
            repo = issue_info['repo']
            issue_number = issue_info['issue_number']
            
            print(f"  [{self.checked_count}/{len(df)}] Checking {owner}/{repo}#{issue_number}...")
            
            # Check issue status
            status = self.check_issue_status(owner, repo, issue_number)
            
            if status == 'open':
                self.open_count += 1
                open_issues.append(row)
                print(f"    [OPEN] - keeping issue")
            elif status == 'closed':
                self.closed_count += 1
                print(f"    [CLOSED] - removing issue")
            else:
                self.error_count += 1
                print(f"    [ERROR: {status}] - removing issue")
            
            # Rate limiting - be gentle with GitHub API
            if self.checked_count % 10 == 0:
                print(f"  Progress: {self.checked_count}/{len(df)} checked, {self.open_count} open, {self.closed_count} closed")
                time.sleep(1)  # Brief pause every 10 requests
        
        # Create filtered dataframe with only open issues
        if open_issues:
            filtered_df = pd.DataFrame(open_issues)
            filtered_df.to_csv(output_file, index=False)
            print(f"\nSaved {len(filtered_df)} open issues to: {output_file}")
        else:
            print(f"\nNo open issues found! Creating empty CSV at: {output_file}")
            # Create empty CSV with same headers
            empty_df = pd.DataFrame(columns=df.columns)
            empty_df.to_csv(output_file, index=False)
        
        # Print summary
        self.print_summary(len(df))
    
    def print_summary(self, total_issues: int):
        """Print processing summary."""
        print(f"\n{'='*50}")
        print(f"ISSUE VERIFICATION SUMMARY")
        print(f"{'='*50}")
        print(f"Total issues checked: {self.checked_count}")
        print(f"Open issues found:    {self.open_count}")
        print(f"Closed issues found:  {self.closed_count}")
        print(f"Errors/Not found:     {self.error_count}")
        print(f"Open issue rate:      {(self.open_count/self.checked_count*100):.1f}%")
        print(f"Closed issue rate:    {(self.closed_count/self.checked_count*100):.1f}%")
        print(f"{'='*50}")

def main():
    # Load .env file
    from dotenv import load_dotenv
    load_dotenv()
    
    # Get GitHub token from environment
    token = os.getenv('API_GITHUB_TOKEN')
    if not token:
        print("Warning: No GitHub token found. Using unauthenticated requests (60/hour limit)")
    else:
        print("Using authenticated GitHub API requests (5000/hour limit)")
    
    # File paths
    input_file = "C:\\Projects\\github-library\\data\\repos\\shopify_stripe_filter2.csv"
    output_file = "C:\\Projects\\github-library\\data\\repos\\shopify_stripe_filter3.csv"
    
    # Create checker and process file
    checker = IssueStatusChecker(token)
    checker.process_csv_file(input_file, output_file)

if __name__ == "__main__":
    main()