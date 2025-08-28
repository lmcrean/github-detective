import pandas as pd
from datetime import datetime, timedelta
import requests
import os
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_commit_and_merge_stats(org, repo, token=None, days=30):
    """Get commit and merge count for the last N days using GitHub API."""
    try:
        # Prepare headers
        headers = {'Accept': 'application/vnd.github.v3+json'}
        if token:
            headers['Authorization'] = f'token {token}'
        
        # Calculate since date
        since_date = (datetime.now() - timedelta(days=days)).isoformat()
        
        # Get commits from last 30 days
        commits_url = f"https://api.github.com/repos/{org}/{repo}/commits"
        params = {
            'since': since_date,
            'per_page': 100
        }
        
        all_commits = []
        page = 1
        
        while True:
            params['page'] = page
            response = requests.get(commits_url, headers=headers, params=params)
            
            if response.status_code == 404:
                print(f"  Repository {org}/{repo} not found (404)")
                return 0, 0
            elif response.status_code == 403:
                print(f"  Access denied to {org}/{repo} (403)")
                return 0, 0
            elif response.status_code != 200:
                print(f"  API error for {org}/{repo}: {response.status_code}")
                return 0, 0
            
            commits = response.json()
            
            if not commits:
                break
                
            all_commits.extend(commits)
            
            # Check if there are more pages
            if len(commits) < 100:
                break
            
            page += 1
            
            # Rate limiting protection
            time.sleep(0.1)
        
        total_commits = len(all_commits)
        
        # Count merge commits (commits with more than one parent)
        merges = sum(1 for commit in all_commits 
                    if 'parents' in commit and len(commit.get('parents', [])) > 1)
        
        return total_commits, merges
        
    except requests.exceptions.RequestException as e:
        print(f"  Network error for {org}/{repo}: {e}")
        return 0, 0
    except Exception as e:
        print(f"  Error fetching data for {org}/{repo}: {e}")
        return 0, 0

def main():
    # Get GitHub token from environment
    github_token = os.getenv('API_GITHUB_TOKEN') or os.getenv('GITHUB_TOKEN')
    
    if not github_token:
        print("Warning: No GitHub token found. API rate limits will be restricted.")
        print("Set API_GITHUB_TOKEN or GITHUB_TOKEN in .env file for better rate limits.")
    
    # Input and output file paths
    input_file = r"C:\Projects\github-library\data\repos\batch_Aug28\ftse100_active_repos_last30d.csv"
    output_file = r"C:\Projects\github-library\data\repos\batch_Aug28\ftse100_active_repos_with_metrics.csv"
    
    # Read the input CSV
    print(f"Reading input file: {input_file}")
    df = pd.read_csv(input_file)
    
    # Add new columns
    commits_30d = []
    merges_30d = []
    health_scores = []
    
    total_repos = len(df)
    print(f"\nProcessing {total_repos} repositories...")
    print("=" * 60)
    
    for idx, row in df.iterrows():
        org = row['org']
        repo = row['repo']
        
        print(f"\n[{idx+1}/{total_repos}] Processing {org}/{repo}...")
        
        # Get commit and merge stats
        commits, merges = get_commit_and_merge_stats(org, repo, github_token, days=30)
        
        commits_30d.append(commits)
        merges_30d.append(merges)
        
        # Calculate health score (average of commits and merges in last 30 days)
        health_score = (commits + merges) / 2
        health_scores.append(health_score)
        
        # Print progress
        print(f"  OK Commits: {commits}, Merges: {merges}, Health Score: {health_score:.2f}")
        
        # Rate limiting - be respectful to GitHub API
        time.sleep(0.5)
    
    # Add new columns to dataframe
    df['commits_last_30d'] = commits_30d
    df['merges_last_30d'] = merges_30d
    df['repo_health_score'] = health_scores
    
    # Save to new CSV file
    df.to_csv(output_file, index=False)
    
    print("\n" + "=" * 60)
    print(f"OK Data saved to: {output_file}")
    print(f"OK Total repositories processed: {total_repos}")
    
    # Print summary statistics
    print(f"\nSummary Statistics:")
    print(f"  - Average commits (30d): {df['commits_last_30d'].mean():.2f}")
    print(f"  - Average merges (30d): {df['merges_last_30d'].mean():.2f}")
    print(f"  - Average health score: {df['repo_health_score'].mean():.2f}")
    
    # Find and display top repositories
    top_5 = df.nlargest(5, 'repo_health_score')[['org', 'repo', 'commits_last_30d', 'merges_last_30d', 'repo_health_score']]
    
    if top_5['repo_health_score'].sum() > 0:
        print(f"\nTop 5 Most Active Repositories:")
        for _, row in top_5.iterrows():
            print(f"  - {row['org']}/{row['repo']}: {row['commits_last_30d']} commits, {row['merges_last_30d']} merges (score: {row['repo_health_score']:.2f})")
    else:
        print("\nWarning: No activity found in the last 30 days for any repository")

if __name__ == "__main__":
    main()