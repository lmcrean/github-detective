import pandas as pd

# Input and output file paths
input_file = r"C:\Projects\github-library\data\repos\batch_Aug28\ftse100_active_repos_with_metrics.csv"
output_file = r"C:\Projects\github-library\data\repos\batch_Aug28\ftse100_active_repos_sorted_by_health.csv"

# Read the CSV
df = pd.read_csv(input_file)

# Sort by repo_health_score in descending order
df_sorted = df.sort_values('repo_health_score', ascending=False)

# Save to new CSV file
df_sorted.to_csv(output_file, index=False)

print(f"Sorted data saved to: {output_file}")
print(f"\nTop 10 repositories by health score:")
print("-" * 60)

# Display top 10
for idx, row in df_sorted.head(10).iterrows():
    print(f"{row['org']}/{row['repo']}: {row['repo_health_score']:.1f} (commits: {row['commits_last_30d']}, merges: {row['merges_last_30d']})")