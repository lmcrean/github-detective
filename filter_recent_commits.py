import pandas as pd
from datetime import datetime

# Read the CSV file
df = pd.read_csv('data/repos/big_three_last_commits.csv', delimiter=';')

# Convert last_commit to datetime
df['last_commit'] = pd.to_datetime(df['last_commit'])

# Define the cutoff date (July 18, 2025)
cutoff_date = datetime(2025, 7, 18)

# Filter repositories with last commit on or after July 18, 2025
filtered_df = df[df['last_commit'] >= cutoff_date]

# Save to a sibling file
output_file = 'data/repos/big_three_recent_commits.csv'
filtered_df.to_csv(output_file, sep=';', index=False)

print(f"Original repositories: {len(df)}")
print(f"Filtered repositories (last commit >= 2025-07-18): {len(filtered_df)}")
print(f"Filtered data saved to: {output_file}")