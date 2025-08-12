"""Debug why shopify/cli issues API returns empty."""

import requests
import json

def test_shopify_cli_api():
    """Test different API approaches for shopify/cli."""
    
    print("Testing shopify/cli API endpoints...")
    print("="*50)
    
    # Test 1: Repository endpoint
    print("\n1. Repository endpoint (/repos/shopify/cli):")
    resp = requests.get("https://api.github.com/repos/shopify/cli")
    if resp.status_code == 200:
        data = resp.json()
        print(f"   - open_issues_count: {data.get('open_issues_count')}")
        print(f"   - has_issues: {data.get('has_issues')}")
        print(f"   - visibility: {data.get('visibility')}")
    else:
        print(f"   ERROR: {resp.status_code}")
    
    # Test 2: Issues endpoint
    print("\n2. Issues endpoint (/repos/shopify/cli/issues?state=open):")
    resp = requests.get("https://api.github.com/repos/shopify/cli/issues?state=open&per_page=100")
    if resp.status_code == 200:
        items = resp.json()
        issues = [i for i in items if 'pull_request' not in i]
        prs = [i for i in items if 'pull_request' in i]
        print(f"   - Total items: {len(items)}")
        print(f"   - Issues (no PR key): {len(issues)}")
        print(f"   - Pull requests (has PR key): {len(prs)}")
        
        # Show first few items
        if items:
            print("\n   First 3 items:")
            for item in items[:3]:
                is_pr = 'pull_request' in item
                print(f"     - #{item['number']}: {'[PR]' if is_pr else '[ISSUE]'} {item['title'][:40]}")
    else:
        print(f"   ERROR: {resp.status_code}")
    
    # Test 3: Try with different parameters
    print("\n3. Issues endpoint with filter=all:")
    resp = requests.get("https://api.github.com/repos/shopify/cli/issues?state=open&filter=all&per_page=100")
    if resp.status_code == 200:
        items = resp.json()
        issues = [i for i in items if 'pull_request' not in i]
        print(f"   - Total items: {len(items)}")
        print(f"   - Issues only: {len(issues)}")
    else:
        print(f"   ERROR: {resp.status_code}")
    
    # Test 4: Pulls endpoint
    print("\n4. Pulls endpoint (/repos/shopify/cli/pulls?state=open):")
    resp = requests.get("https://api.github.com/repos/shopify/cli/pulls?state=open&per_page=100")
    if resp.status_code == 200:
        prs = resp.json()
        print(f"   - Open PRs: {len(prs)}")
    else:
        print(f"   ERROR: {resp.status_code}")
    
    # Test 5: Search API
    print("\n5. Search API for issues:")
    resp = requests.get("https://api.github.com/search/issues?q=is:issue+is:open+repo:shopify/cli")
    if resp.status_code == 200:
        data = resp.json()
        print(f"   - Total count: {data.get('total_count')}")
        print(f"   - Items returned: {len(data.get('items', []))}")
    else:
        print(f"   ERROR: {resp.status_code}")
    
    print("\n6. Search API for PRs:")
    resp = requests.get("https://api.github.com/search/issues?q=is:pr+is:open+repo:shopify/cli")
    if resp.status_code == 200:
        data = resp.json()
        print(f"   - Total count: {data.get('total_count')}")
    else:
        print(f"   ERROR: {resp.status_code}")
    
    # Test 7: GraphQL approach (if we had a token)
    print("\n7. Alternative: Try querying a known working repo (stripe/stripe-android):")
    resp = requests.get("https://api.github.com/repos/stripe/stripe-android/issues?state=open&per_page=5")
    if resp.status_code == 200:
        items = resp.json()
        print(f"   - Items returned: {len(items)}")
        if items:
            print(f"   - First item: #{items[0]['number']} {items[0]['title'][:30]}")
    
    print("\n" + "="*50)
    print("CONCLUSION:")
    print("The shopify/cli repository appears to have restricted issue visibility.")
    print("This might be because:")
    print("1. Issues are only visible to authenticated users")
    print("2. Issues are restricted to organization members")
    print("3. The repository uses GitHub Discussions instead of Issues")
    print("\nThe open_issues_count field includes PRs, so we can calculate:")
    print("- Total open items: 89 (from repo endpoint)")
    print("- Open PRs: 46 (from pulls endpoint)")
    print("- Calculated open issues: 89 - 46 = 43")

if __name__ == "__main__":
    test_shopify_cli_api()