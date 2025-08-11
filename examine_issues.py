#!/usr/bin/env python3
"""Script to examine specific GitHub issues for viability assessment."""

import requests
import os
import json
from typing import Dict, Any

def get_issue_details(owner: str, repo: str, issue_number: int) -> Dict[str, Any]:
    """Fetch detailed information about a specific issue."""
    
    # Use GitHub token if available
    token = os.getenv('GITHUB_TOKEN')
    headers = {'Authorization': f'token {token}'} if token else {}
    
    # Fetch issue details
    issue_url = f'https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}'
    
    try:
        response = requests.get(issue_url, headers=headers)
        response.raise_for_status()
        issue_data = response.json()
        
        # Also fetch comments
        comments_url = issue_data['comments_url']
        comments_response = requests.get(comments_url, headers=headers)
        comments_response.raise_for_status()
        comments_data = comments_response.json()
        
        return {
            'issue': issue_data,
            'comments': comments_data
        }
    
    except requests.RequestException as e:
        print(f"Error fetching issue {owner}/{repo}#{issue_number}: {e}")
        return {}

def analyze_issue(owner: str, repo: str, issue_number: int, title: str):
    """Analyze a specific issue for viability."""
    
    print(f"\n{'='*80}")
    print(f"ANALYZING: {owner}/{repo} #{issue_number}")
    print(f"TITLE: {title}")
    print(f"{'='*80}")
    
    data = get_issue_details(owner, repo, issue_number)
    
    if not data:
        print("❌ Could not fetch issue data")
        return
    
    issue = data['issue']
    comments = data['comments']
    
    # Basic issue info
    print(f"\n[ISSUE OVERVIEW]")
    print(f"  State: {issue['state']}")
    print(f"  Created: {issue['created_at'][:10]}")
    print(f"  Updated: {issue['updated_at'][:10]}")
    print(f"  Comments: {issue['comments']}")
    print(f"  Labels: {[label['name'] for label in issue.get('labels', [])]}")
    print(f"  Assignee: {issue['assignee']['login'] if issue['assignee'] else 'None'}")
    
    # Issue body
    print(f"\n[ISSUE DESCRIPTION]")
    print(f"  {issue['body'][:500]}{'...' if len(issue['body']) > 500 else ''}")
    
    # Recent comments analysis
    if comments:
        print(f"\n[RECENT COMMENTS] ({len(comments)} total):")
        for comment in comments[-3:]:  # Show last 3 comments
            author = comment['user']['login']
            date = comment['created_at'][:10]
            body = comment['body'][:200].replace('\n', ' ')
            print(f"  * {author} ({date}): {body}{'...' if len(comment['body']) > 200 else ''}")
    else:
        print(f"\n[NO COMMENTS]")
    
    # Check if issue is still open and recent
    is_open = issue['state'] == 'open'
    print(f"\n[VIABILITY INDICATORS]")
    print(f"  + Issue is open: {is_open}")
    print(f"  + Has recent activity: {issue['updated_at'][:4] == '2025'}")
    print(f"  + Has engagement: {issue['comments'] > 0}")

def main():
    """Analyze the 3 nominated issues."""
    
    issues = [
        ("stripe", "stripe-go", 2092, "Missing .Metadata field for BankAccountCreateParams"),
        ("stripe", "stripe-go", 2093, "Unable to create BankAccount"),  
        ("mastercard", "flow", 999, "Fix mermaid compatibility")
    ]
    
    for owner, repo, issue_num, title in issues:
        analyze_issue(owner, repo, issue_num, title)

if __name__ == "__main__":
    main()