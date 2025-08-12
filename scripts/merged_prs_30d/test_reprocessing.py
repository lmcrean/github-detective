"""Test the reprocessing functionality with a small sample."""

import sys
import os

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Add parent directory to path for imports  
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from scripts.merged_prs_30d.fetch_merged_prs import MergedPRsFetcher
from scripts.merged_prs_30d.identify_failed_repos import get_failed_repos_for_reprocessing


def test_token_and_api():
    """Test that the GitHub token is working and API is accessible."""
    print("Testing GitHub API access...")
    
    fetcher = MergedPRsFetcher()
    
    if not fetcher.token:
        print("[ERROR] No GitHub token found!")
        print("Please check that API_GITHUB_TOKEN is set in your .env file")
        return False
    
    print(f"[OK] Token found: {fetcher.token[:8]}...")
    
    # Test with a simple, well-known repository
    test_org = "stripe"
    test_repo = "stripe-python"
    
    print(f"Testing API call with {test_org}/{test_repo}...")
    
    try:
        count = fetcher.get_merged_prs_count(test_org, test_repo, 30)
        
        if count == -1:
            print("[ERROR] API call failed with rate limiting or error")
            return False
        else:
            print(f"[OK] API call successful! Found {count} merged PRs")
            return True
            
    except Exception as e:
        print(f"[ERROR] API call failed with exception: {str(e)}")
        return False


def test_small_sample():
    """Test reprocessing with a small sample of failed repositories."""
    print("\nTesting with small sample of failed repositories...")
    
    # Get a few failed repos from Stripe (smaller org)
    failed_repos = get_failed_repos_for_reprocessing("stripe")
    
    if not failed_repos:
        print("[ERROR] No failed repositories found for testing")
        return False
    
    # Take just the first 3 for testing
    test_repos = failed_repos[:3]
    print(f"Testing with {len(test_repos)} repositories:")
    for repo in test_repos:
        print(f"  - {repo['org_name']}/{repo['repo_name']}")
    
    # Test with very conservative settings
    fetcher = MergedPRsFetcher()
    results = fetcher.get_batch_merged_prs(
        test_repos, 
        days=30, 
        batch_size=1,  # One at a time
        batch_delay=10  # 10 second delay
    )
    
    # Analyze results
    successful = sum(1 for v in results.values() if v != -1)
    failed = sum(1 for v in results.values() if v == -1)
    
    print(f"\nTest results:")
    print(f"  Successful: {successful}")
    print(f"  Still failed: {failed}")
    print(f"  Success rate: {(successful/len(test_repos))*100:.1f}%")
    
    # Show detailed results
    print(f"\nDetailed results:")
    for key, count in results.items():
        status = "[OK]" if count != -1 else "[FAIL]"
        print(f"  {status} {key}: {count}")
    
    return successful > 0


def main():
    """Run tests to verify the reprocessing functionality."""
    print("TESTING REPROCESSING FUNCTIONALITY")
    print("=" * 50)
    
    # Test 1: API access
    if not test_token_and_api():
        print("\n[ERROR] API access test failed. Cannot proceed with reprocessing.")
        print("\nTroubleshooting:")
        print("1. Check that API_GITHUB_TOKEN is set in .env file")
        print("2. Verify token has proper permissions") 
        print("3. Check internet connection")
        return 1
    
    # Test 2: Small sample reprocessing
    if test_small_sample():
        print("\n[SUCCESS] Small sample test passed! The reprocessing should work.")
        print("\nYou can now run the full reprocessing with:")
        print("python scripts/merged_prs_30d/reprocess_failed_repos.py")
    else:
        print("\n[ERROR] Small sample test failed. There may be issues with rate limiting.")
        print("\nRecommendations:")
        print("1. Wait longer between API calls")
        print("2. Check if there are ongoing rate limit issues")
        print("3. Try running the test again in a few minutes")
        return 1
    
    return 0


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)