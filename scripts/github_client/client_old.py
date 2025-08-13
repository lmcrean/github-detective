"""GitHub API client for repository statistics."""

import requests
import time
import re
from typing import Optional, Dict, Any, List
from .models import RepositoryStats, IssueData


class GitHubClient:
    """GitHub API client with rate limiting and error handling."""
    
    def __init__(self, token: Optional[str] = None):
        """Initialize client with optional authentication token."""
        self.token = token
        self.headers = {'Authorization': f'token {token}'} if token else {}
        self.base_url = 'https://api.github.com'
    
    def get_repo_stats(self, owner: str, repo: str) -> Optional[RepositoryStats]:
        """Fetch complete repository statistics."""
        repo_url = f'{self.base_url}/repos/{owner}/{repo}'
        
        try:
            response = requests.get(repo_url, headers=self.headers)
            
            if response.status_code == 404:
                print(f"Warning: Repository {owner}/{repo} not found (404)")
                return None
            elif response.status_code == 403:
                print(f"Warning: Access denied to {owner}/{repo} (403 - private repo?)")
                return None
            elif response.status_code == 429:
                print(f"Warning: Rate limit exceeded. Waiting 60 seconds...")
                time.sleep(60)
                return self.get_repo_stats(owner, repo)
            
            response.raise_for_status()
            repo_data = response.json()
            
            # Get additional metrics
            contributors_count = self._get_contributors_count(owner, repo)
            open_prs_count = self._get_open_prs_count(owner, repo)
            languages_formatted = self._get_repo_languages(owner, repo)
            
            return RepositoryStats(
                repo_path=f'{owner}/{repo}',
                field='',  # Will be set by caller
                stars=repo_data['stargazers_count'],
                forks=repo_data['forks_count'],
                contributors=contributors_count,
                open_issues=repo_data['open_issues_count'],
                open_prs=open_prs_count,
                created_at=repo_data['created_at'][:10],
                pushed_at=repo_data['pushed_at'][:10] if repo_data['pushed_at'] else repo_data['created_at'][:10],
                languages=languages_formatted
            )
            
        except Exception as e:
            print(f"Error fetching {owner}/{repo}: {str(e)}")
            return None
    
    def _get_contributors_count(self, owner: str, repo: str) -> int:
        """Get accurate contributors count with pagination support."""
        try:
            contributors_url = f'{self.base_url}/repos/{owner}/{repo}/contributors?per_page=100&anon=true'
            response = requests.get(contributors_url, headers=self.headers)
            
            if response.status_code == 200:
                contributors = response.json()
                total_count = len(contributors)
                
                # Check for pagination
                if 'Link' in response.headers:
                    link_header = response.headers['Link']
                    last_page_match = re.search(r'page=(\d+)>; rel="last"', link_header)
                    if last_page_match:
                        last_page = int(last_page_match.group(1))
                        last_page_url = f'{contributors_url}&page={last_page}'
                        last_response = requests.get(last_page_url, headers=self.headers)
                        if last_response.status_code == 200:
                            last_page_contributors = len(last_response.json())
                            total_count = (last_page - 1) * 100 + last_page_contributors
                
                return total_count
            else:
                return -1
        except Exception as e:
            print(f"Error counting contributors for {owner}/{repo}: {str(e)}")
            return -1
    
    def _get_open_prs_count(self, owner: str, repo: str) -> int:
        """Get open pull requests count using search API for accuracy."""
        try:
            # Use search API for direct total count
            search_url = f'{self.base_url}/search/issues?q=is:pr+is:open+repo:{owner}/{repo}'
            response = requests.get(search_url, headers=self.headers)
            
            if response.status_code == 200:
                data = response.json()
                return data.get('total_count', 0)
            
            # Fallback to pulls endpoint with pagination
            prs_url = f'{self.base_url}/repos/{owner}/{repo}/pulls?state=open&per_page=100'
            response = requests.get(prs_url, headers=self.headers)
            
            if response.status_code == 200:
                prs = response.json()
                total_count = len(prs)
                
                # Check for pagination
                if 'Link' in response.headers:
                    link_header = response.headers['Link']
                    last_page_match = re.search(r'page=(\d+)>; rel="last"', link_header)
                    if last_page_match:
                        last_page = int(last_page_match.group(1))
                        last_page_url = f'{prs_url}&page={last_page}'
                        last_response = requests.get(last_page_url, headers=self.headers)
                        if last_response.status_code == 200:
                            last_page_prs = len(last_response.json())
                            total_count = (last_page - 1) * 100 + last_page_prs
                
                return total_count
            else:
                return -1
        except Exception as e:
            print(f"Error counting PRs for {owner}/{repo}: {str(e)}")
            return -1
    
    def _get_repo_languages(self, owner: str, repo: str) -> str:
        """Get top 5 programming languages used in repository with percentages."""
        try:
            languages_url = f'{self.base_url}/repos/{owner}/{repo}/languages'
            response = requests.get(languages_url, headers=self.headers)
            
            if response.status_code == 200:
                languages_data = response.json()
                
                if not languages_data:
                    return ""
                
                # Calculate total bytes and percentages
                total_bytes = sum(languages_data.values())
                if total_bytes == 0:
                    return ""
                
                # Sort by bytes (descending) and take top 5
                sorted_languages = sorted(languages_data.items(), key=lambda x: x[1], reverse=True)[:5]
                
                # Format as "Language (percentage%)"
                formatted_langs = []
                for lang, bytes_count in sorted_languages:
                    percentage = (bytes_count / total_bytes) * 100
                    # Format with 1 decimal place to match GitHub's display
                    formatted_langs.append(f"{lang} ({percentage:.1f}%)")
                    
                    # Only include top 5 languages
                    if len(formatted_langs) >= 5:
                        break
                
                return ", ".join(formatted_langs)
            else:
                return ""
        except Exception as e:
            print(f"Error fetching languages for {owner}/{repo}: {str(e)}")
            return ""
    
    def get_issues(self, owner: str, repo: str, max_issues: int = 500) -> List[IssueData]:
        """Fetch repository issues (both open and closed, sorted by creation date)."""
        issues = []
        per_page = 100
        max_pages = (max_issues + per_page - 1) // per_page
        
        # First, collect all open issues
        open_issues = self._collect_issues_by_state(owner, repo, 'open', max_issues // 2)
        issues.extend(open_issues)
        
        # Then, collect recent closed issues
        remaining_slots = max_issues - len(open_issues)
        if remaining_slots > 0:
            closed_issues = self._collect_issues_by_state(owner, repo, 'closed', remaining_slots)
            issues.extend(closed_issues)
        
        print(f"  Collected {len([i for i in issues if i.state == 'open'])} open issues and {len([i for i in issues if i.state == 'closed'])} closed issues")
        return issues
    
    def _collect_issues_by_state(self, owner: str, repo: str, state: str, max_issues: int) -> List[IssueData]:
        """Collect issues by state (open or closed)."""
        issues = []
        per_page = 100
        max_pages = (max_issues + per_page - 1) // per_page
        
        for page in range(1, max_pages + 1):
            issues_url = f'{self.base_url}/repos/{owner}/{repo}/issues'
            params = {
                'state': state,
                'sort': 'created',
                'direction': 'desc',
                'per_page': per_page,
                'page': page
            }
            
            try:
                response = requests.get(issues_url, headers=self.headers, params=params)
                
                if response.status_code == 429:
                    print(f"Rate limit exceeded. Waiting 60 seconds...")
                    time.sleep(60)
                    response = requests.get(issues_url, headers=self.headers, params=params)
                
                if response.status_code != 200:
                    print(f"Error fetching {state} issues for {owner}/{repo}: Status {response.status_code}")
                    break
                
                page_issues = response.json()
                
                if not page_issues:
                    break
                
                for issue_data in page_issues:
                    # Skip pull requests
                    if 'pull_request' in issue_data:
                        continue
                    
                    labels = [label['name'] for label in issue_data.get('labels', [])]
                    
                    issue = IssueData(
                        number=issue_data['number'],
                        title=issue_data['title'],
                        state=issue_data['state'],
                        labels=labels,
                        comments=issue_data.get('comments', 0),
                        created_at=issue_data['created_at'],
                        updated_at=issue_data['updated_at'],
                        body=issue_data.get('body', ''),
                        author=issue_data['user']['login'] if issue_data.get('user') else None
                    )
                    issues.append(issue)
                    
                    if len(issues) >= max_issues:
                        return issues[:max_issues]
                
                time.sleep(0.5)
                
            except Exception as e:
                print(f"Error fetching {state} issues page {page} for {owner}/{repo}: {str(e)}")
                break
        
        return issues
    
    def get_issue_details(self, owner: str, repo: str, issue_number: int) -> Optional[Dict[str, Any]]:
        """Fetch detailed information for a specific issue."""
        issue_url = f'{self.base_url}/repos/{owner}/{repo}/issues/{issue_number}'
        
        try:
            response = requests.get(issue_url, headers=self.headers)
            
            if response.status_code == 404:
                print(f"Issue {owner}/{repo}#{issue_number} not found (404)")
                return None
            elif response.status_code == 429:
                print(f"Rate limit exceeded. Waiting 60 seconds...")
                time.sleep(60)
                return self.get_issue_details(owner, repo, issue_number)
            elif response.status_code != 200:
                print(f"Error fetching issue {owner}/{repo}#{issue_number}: Status {response.status_code}")
                return None
            
            return response.json()
            
        except Exception as e:
            print(f"Error fetching issue {owner}/{repo}#{issue_number}: {str(e)}")
            return None
    
    def get_issue_comments(self, owner: str, repo: str, issue_number: int) -> List[Dict[str, Any]]:
        """Fetch all comments for a specific issue."""
        comments = []
        page = 1
        per_page = 100
        
        while True:
            comments_url = f'{self.base_url}/repos/{owner}/{repo}/issues/{issue_number}/comments'
            params = {
                'per_page': per_page,
                'page': page
            }
            
            try:
                response = requests.get(comments_url, headers=self.headers, params=params)
                
                if response.status_code == 429:
                    print(f"Rate limit exceeded. Waiting 60 seconds...")
                    time.sleep(60)
                    continue
                elif response.status_code != 200:
                    print(f"Error fetching comments for {owner}/{repo}#{issue_number}: Status {response.status_code}")
                    break
                
                page_comments = response.json()
                
                if not page_comments:
                    break
                
                comments.extend(page_comments)
                
                # Check if there are more pages
                if len(page_comments) < per_page:
                    break
                
                page += 1
                time.sleep(0.5)  # Be respectful to the API
                
            except Exception as e:
                print(f"Error fetching comments for {owner}/{repo}#{issue_number}: {str(e)}")
                break
        
        return comments