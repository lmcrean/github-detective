"""Quick test to verify shopify/cli counts."""

from fix_github_counts_accurate import AccurateGitHubClient

# Test shopify/cli
client = AccurateGitHubClient()
print("Testing shopify/cli...")
issues, prs = client.get_accurate_counts('shopify', 'cli')

print(f"\nResults:")
print(f"  Open Issues (excluding PRs): {issues}")
print(f"  Open Pull Requests: {prs}")

if issues == 43 and prs == 46:
    print("\n[SUCCESS] Values match expected (43 issues, 46 PRs)!")
else:
    print(f"\n[MISMATCH] Expected 43 issues and 46 PRs, got {issues} issues and {prs} PRs")