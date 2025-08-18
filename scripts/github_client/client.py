"""Refactored GitHub API client for repository statistics."""

import requests
import re
from typing import Optional, Dict, Any, List
from ..models.github_models import RepositoryStats, IssueData
from .auth import GitHubAuth
from .rate_limiter import RateLimiter
from .exceptions import GitHubAPIError, RateLimitError, RepositoryNotFoundError, AccessDeniedError


class GitHubClient:
    """GitHub API client with rate limiting and error handling."""
    
    def __init__(self, token: Optional[str] = None):
        """Initialize client with optional authentication token."""
        self.auth = GitHubAuth(token)
        self.rate_limiter = RateLimiter()
        self.base_url = 'https://api.github.com'
    
    def _make_request(self, url: str, params: Dict[str, Any] = None) -> requests.Response:
        """
        Make authenticated request with rate limiting.
        
        Args:
            url: API endpoint URL
            params: Optional query parameters
        
        Returns:
            HTTP response
        
        Raises:
            GitHubAPIError: For various API errors
        """
        self.rate_limiter.wait_if_needed()
        
        try:
            response = requests.get(url, headers=self.auth.get_headers(), params=params)
            
            # Handle rate limiting
            if response.status_code == 429:
                self.rate_limiter.handle_rate_limit_response(response)
                # Retry after waiting
                response = requests.get(url, headers=self.auth.get_headers(), params=params)
            
            return response
            
        except requests.exceptions.RequestException as e:
            raise GitHubAPIError(f"Request failed: {str(e)}")
    
    def get_repo_stats(self, owner: str, repo: str) -> Optional[RepositoryStats]:
        """Fetch complete repository statistics."""
        repo_url = f'{self.base_url}/repos/{owner}/{repo}'
        
        try:
            response = self._make_request(repo_url)
            
            if response.status_code == 404:
                print(f"Warning: Repository {owner}/{repo} not found (404)")
                return None
            elif response.status_code == 403:
                print(f"Warning: Access denied to {owner}/{repo} (403 - private repo?)")
                return None
            
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
            response = self._make_request(contributors_url)
            
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
                        last_response = self._make_request(last_page_url)
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
            response = self._make_request(search_url)
            
            if response.status_code == 200:
                data = response.json()
                return data.get('total_count', 0)
            
            # Fallback to pulls endpoint with pagination
            prs_url = f'{self.base_url}/repos/{owner}/{repo}/pulls?state=open&per_page=100'
            response = self._make_request(prs_url)
            
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
                        last_response = self._make_request(last_page_url)
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
            response = self._make_request(languages_url)
            
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
                    formatted_langs.append(f"{lang} ({percentage:.1f}%)")
                    
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
                response = self._make_request(issues_url, params)
                
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
                
            except Exception as e:
                print(f"Error fetching {state} issues page {page} for {owner}/{repo}: {str(e)}")
                break
        
        return issues
    
    def get_issue_details(self, owner: str, repo: str, issue_number: int) -> Optional[Dict[str, Any]]:
        """Fetch detailed information for a specific issue."""
        issue_url = f'{self.base_url}/repos/{owner}/{repo}/issues/{issue_number}'
        
        try:
            response = self._make_request(issue_url)
            
            if response.status_code == 404:
                print(f"Issue {owner}/{repo}#{issue_number} not found (404)")
                return None
            elif response.status_code != 200:
                print(f"Error fetching issue {owner}/{repo}#{issue_number}: Status {response.status_code}")
                return None
            
            return response.json()
            
        except Exception as e:
            print(f"Error fetching issue {owner}/{repo}#{issue_number}: {str(e)}")
            return None
    
    def get_org_repositories(self, org: str, per_page: int = 100) -> List[Dict[str, Any]]:
        """
        Fetch all public repositories for an organization.
        
        Args:
            org: Organization name
            per_page: Number of repositories per page (max 100)
        
        Returns:
            List of repository data dictionaries
        """
        repositories = []
        page = 1
        
        while True:
            org_repos_url = f'{self.base_url}/orgs/{org}/repos'
            params = {
                'type': 'public',  # Only public repositories
                'sort': 'updated',
                'direction': 'desc',
                'per_page': per_page,
                'page': page
            }
            
            try:
                response = self._make_request(org_repos_url, params)
                
                if response.status_code == 404:
                    print(f"Organization {org} not found (404)")
                    break
                elif response.status_code != 200:
                    print(f"Error fetching repositories for org {org}: Status {response.status_code}")
                    break
                
                page_repos = response.json()
                
                if not page_repos:
                    break  # No more repositories
                
                repositories.extend(page_repos)
                
                # If we got fewer results than per_page, we've reached the end
                if len(page_repos) < per_page:
                    break
                
                page += 1
                
                # Safety limit to prevent infinite loops
                if len(repositories) > 5000:
                    print(f"Warning: Reached safety limit of 5000 repositories for {org}")
                    break
                    
            except Exception as e:
                print(f"Error fetching repositories for org {org} page {page}: {str(e)}")
                break
        
        return repositories