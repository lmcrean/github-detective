#!/usr/bin/env python3
"""Examine the top 3 candidate issues in detail."""

import requests
import os

def examine_issue_detail(owner: str, repo: str, issue_number: int, title: str):
    """Get detailed analysis of an issue."""
    
    token = os.getenv('GITHUB_TOKEN')
    headers = {'Authorization': f'token {token}'} if token else {}
    
    print(f"\n{'='*100}")
    print(f"DEEP DIVE: {owner}/{repo} #{issue_number}")
    print(f"TITLE: {title}")
    print(f"{'='*100}")
    
    # Get issue details
    issue_url = f'https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}'
    
    try:
        response = requests.get(issue_url, headers=headers)
        response.raise_for_status()
        issue = response.json()
        
        # Get comments
        comments_url = issue['comments_url']
        comments_response = requests.get(comments_url, headers=headers)
        comments_response.raise_for_status()
        comments = comments_response.json()
        
        # Basic info
        print(f"\n[ISSUE STATUS]")
        print(f"State: {issue['state']}")
        print(f"Created: {issue['created_at'][:10]}")
        print(f"Updated: {issue['updated_at'][:10]}")
        print(f"Comments: {issue['comments']}")
        print(f"Labels: {[label['name'] for label in issue.get('labels', [])]}")
        print(f"Assignee: {issue['assignee']['login'] if issue['assignee'] else 'None'}")
        print(f"Author: {issue['user']['login']}")
        
        # Full description
        print(f"\n[FULL DESCRIPTION]")
        print(issue['body'] if issue['body'] else "(No description)")
        
        # All comments with full text
        if comments:
            print(f"\n[ALL COMMENTS] ({len(comments)} total)")
            for i, comment in enumerate(comments):
                author = comment['user']['login']
                date = comment['created_at'][:10]
                body = comment['body']
                print(f"\n--- Comment {i+1} by {author} on {date} ---")
                print(body)
        else:
            print(f"\n[NO COMMENTS]")
        
        # Get recent repository commits to assess activity
        commits_url = f'https://api.github.com/repos/{owner}/{repo}/commits'
        commits_response = requests.get(commits_url + '?per_page=10', headers=headers)
        if commits_response.status_code == 200:
            commits = commits_response.json()
            print(f"\n[RECENT REPO ACTIVITY]")
            for commit in commits[:5]:
                date = commit['commit']['committer']['date'][:10]
                message = commit['commit']['message'][:80].replace('\n', ' ')
                print(f"  {date}: {message}")
        
        print(f"\n[VIABILITY ASSESSMENT]")
        
        # Check maintainer engagement
        maintainer_commented = any(comment['author_association'] in ['MEMBER', 'OWNER', 'COLLABORATOR'] 
                                 for comment in comments)
        print(f"✓ Maintainer engagement: {'YES' if maintainer_commented else 'NO'}")
        
        # Check if it's a recent issue  
        recent = issue['updated_at'][:4] == '2025'
        print(f"✓ Recent activity: {'YES' if recent else 'NO'}")
        
        # Check if there's community interest
        has_engagement = issue['comments'] > 0
        print(f"✓ Community engagement: {'YES' if has_engagement else 'NO'}")
        
        # Check labels for complexity indicators
        complexity_labels = ['good first issue', 'help wanted', 'bug', 'enhancement']
        has_helpful_labels = any(label['name'].lower() in complexity_labels 
                               for label in issue.get('labels', []))
        print(f"✓ Helpful labels: {'YES' if has_helpful_labels else 'NO'}")
        
        # Overall viability score
        score = sum([maintainer_commented, recent, has_engagement, has_helpful_labels])
        print(f"\n★ VIABILITY SCORE: {score}/4")
        
        if score >= 3:
            print("✅ HIGH VIABILITY")
        elif score >= 2:
            print("⚠️  MEDIUM VIABILITY")
        else:
            print("❌ LOW VIABILITY")
    
    except Exception as e:
        print(f"❌ ERROR: Could not fetch issue details: {e}")

def main():
    """Examine top 3 candidates."""
    
    # Top candidates based on verification results
    candidates = [
        ("NVIDIA", "cccl", 5327, "[BUG]: Potentially uninitialized/oob reads in DeviceMergeSort, DeviceReduceByKey, and DeviceScanByKey"),
        ("stripe", "react-stripe-js", 603, "[BUG]: The on method of useCheckout() function is omitted"),
        ("NVIDIA", "nvidia-container-toolkit", 1239, "Wrong CDI spec creates error \"Unresolvable CDI device\"")
    ]
    
    for owner, repo, issue_num, title in candidates:
        examine_issue_detail(owner, repo, issue_num, title)

if __name__ == "__main__":
    main()