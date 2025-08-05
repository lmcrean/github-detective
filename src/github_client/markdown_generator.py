"""Generate markdown documentation from collected GitHub repository statistics."""

import os
import pandas as pd
from typing import Dict, List
from datetime import datetime


class MarkdownGenerator:
    """Generates markdown documentation from repository statistics CSV."""
    
    def __init__(self, csv_path: str, output_dir: str = "docs"):
        """Initialize generator with CSV path and output directory."""
        self.csv_path = csv_path
        self.output_dir = output_dir
        self.df = None
    
    def load_data(self) -> None:
        """Load repository data from CSV."""
        self.df = pd.read_csv(self.csv_path)
        print(f"Loaded {len(self.df)} repositories from {self.csv_path}")
    
    def generate_markdown_files(self) -> None:
        """Generate markdown files for each category."""
        if self.df is None:
            self.load_data()
        
        # Ensure output directory exists
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Group by field/category
        grouped = self.df.groupby('Field')
        
        for field, group_df in grouped:
            # Sort by stars descending
            sorted_df = group_df.sort_values('Stars', ascending=False)
            
            # Generate filename (kebab-case)
            filename = self._generate_filename(field)
            filepath = os.path.join(self.output_dir, filename)
            
            # Generate markdown content
            content = self._generate_markdown_content(field, sorted_df)
            
            # Write to file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"Generated {filepath}")
    
    def _generate_filename(self, field: str) -> str:
        """Convert field name to kebab-case filename."""
        # Handle special cases
        if field == "AI/ML":
            return "ai-ml.md"
        elif field == "C# ASP.NET":
            return "csharp-aspdotnet.md"
        
        # General case: lowercase and replace spaces/underscores with hyphens
        return field.lower().replace(' ', '-').replace('_', '-') + '.md'
    
    def _generate_markdown_content(self, field: str, df: pd.DataFrame) -> str:
        """Generate markdown content for a category."""
        total_stars = df['Stars'].sum()
        total_repos = len(df)
        
        # Start with header
        lines = [
            f"# {field} Repositories",
            "",
            f"**Total Repositories:** {total_repos}  ",
            f"**Total Stars:** {total_stars:,}",
            "",
            f"*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*",
            "",
            "## Repository Statistics",
            "",
            "| Rank | Repository | Stars | Forks | Contributors | Open Issues | Open PRs | Last Active | Top Languages |",
            "|------|------------|-------|-------|--------------|-------------|----------|-------------|---------------|"
        ]
        
        # Add each repository as a table row
        for rank, (_, row) in enumerate(df.iterrows(), 1):
            repo_name = row['Name']
            repo_link = f"[{repo_name}](https://github.com/{repo_name})"
            
            # Format contributors and PRs (handle -1 as N/A)
            contributors = "N/A" if row['Contributors'] == -1 else str(row['Contributors'])
            open_prs = "N/A" if row['Open Pull Requests'] == -1 else str(row['Open Pull Requests'])
            
            # Format languages (truncate if too long)
            languages = row['Top Languages'] if pd.notna(row['Top Languages']) else "N/A"
            if len(languages) > 50:
                languages = languages[:47] + "..."
            
            # Format date
            last_active = row['Last Active'].split('T')[0] if 'T' in str(row['Last Active']) else row['Last Active']
            
            line = f"| {rank} | {repo_link} | {row['Stars']:,} | {row['Forks']:,} | {contributors} | {row['Open Issues']:,} | {open_prs} | {last_active} | {languages} |"
            lines.append(line)
        
        return '\n'.join(lines)