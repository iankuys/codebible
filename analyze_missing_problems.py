#!/usr/bin/env python3
"""
Script to analyze all LeetCode problems in the workspace and identify missing ones from README.
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple

def extract_leetcode_link_from_file(content: str) -> str:
    """Extract LeetCode link from file content."""
    patterns = [
        r'# Link: (https://leetcode\.com/problems/[^/]+/)',
        r'# LeetCode Problem \d+: (https://leetcode\.com/problems/[^/]+/)',
        r'(https://leetcode\.com/problems/[^/\s\)]+)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, content)
        if match:
            return match.group(1)
    return None

def extract_problem_title_from_file(content: str) -> str:
    """Extract problem title from file content."""
    lines = content.strip().split('\n')
    for line in lines[:15]:  # Check first 15 lines
        line = line.strip().lstrip('#').strip()
        
        # Look for patterns like "123. Problem Name" 
        match = re.match(r'^(\d+)\.\s+(.+)$', line)
        if match:
            return match.group(2).strip()
        
        # Look for problem titles in comments
        if line and not line.startswith('filepath:') and not line.startswith('Link:'):
            # Skip if it looks like a URL or common comment
            if not any(x in line.lower() for x in ['http', 'leetcode', 'example', 'input:', 'output:']):
                if len(line.split()) >= 2 and len(line) < 100:
                    return line
    
    return None

def get_all_leetcode_problems() -> Dict[str, Dict[str, str]]:
    """Get all LeetCode problems from the workspace."""
    base_path = Path("c:/Users/ianku/Projects/codebible")
    python_files = list(base_path.glob("**/*.py"))
    
    # Filter out scripts
    exclude_files = {
        'add_leetcode_links.py', 'add_complexity_analysis.py', 'enhanced_complexity_analyzer.py',
        'fix_specific_complexities.py', 'fix_remaining_complexities.py', 'add_complexity_comments.py',
        'add_remaining_links.py', 'add_links_by_content.py', 'analyze_missing_problems.py'
    }
    
    problems = {}
    
    for filepath in python_files:
        if filepath.name in exclude_files:
            continue
            
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if it's a LeetCode file
            if 'class Solution' not in content:
                continue
                
            link = extract_leetcode_link_from_file(content)
            title = extract_problem_title_from_file(content)
            
            if link:
                problem_slug = link.split('/')[-2] if link.endswith('/') else link.split('/')[-1]
                problems[problem_slug] = {
                    'title': title or 'Unknown Title',
                    'link': link,
                    'file_path': str(filepath.relative_to(base_path)),
                    'full_path': str(filepath)
                }
                
        except Exception as e:
            print(f"Error processing {filepath}: {e}")
    
    return problems

def get_readme_problems() -> Set[str]:
    """Extract all LeetCode problem slugs mentioned in README."""
    readme_path = Path("c:/Users/ianku/Projects/codebible/README.md")
    
    if not readme_path.exists():
        return set()
    
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading README: {e}")
        return set()
    
    # Extract all LeetCode links from README
    pattern = r'https://leetcode\.com/problems/([^/\)\s]+)'
    matches = re.findall(pattern, content)
    
    return set(matches)

def categorize_missing_problems(all_problems: Dict[str, Dict[str, str]], readme_problems: Set[str]) -> Dict[str, List[str]]:
    """Categorize missing problems by folder structure."""
    missing_by_category = {}
    
    for slug, info in all_problems.items():
        if slug not in readme_problems:
            # Extract category from file path
            path_parts = info['file_path'].split('/')
            
            if 'NEETCODE 150' in path_parts:
                idx = path_parts.index('NEETCODE 150')
                if idx + 1 < len(path_parts):
                    category = f"NEETCODE 150/{path_parts[idx + 1]}"
                else:
                    category = "NEETCODE 150/misc"
            elif 'TAGGED' in path_parts:
                idx = path_parts.index('TAGGED')
                if idx + 1 < len(path_parts):
                    category = f"TAGGED/{path_parts[idx + 1]}"
                else:
                    category = "TAGGED/misc"
            elif 'OG BIBLE' in path_parts:
                idx = path_parts.index('OG BIBLE')
                if idx + 1 < len(path_parts):
                    category = f"OG BIBLE/{path_parts[idx + 1]}"
                else:
                    category = "OG BIBLE/misc"
            elif 'OAs' in path_parts:
                category = "OAs"
            else:
                category = "Other"
            
            if category not in missing_by_category:
                missing_by_category[category] = []
            
            missing_by_category[category].append({
                'slug': slug,
                'title': info['title'],
                'link': info['link'],
                'file_path': info['file_path']
            })
    
    return missing_by_category

def generate_readme_entries(missing_by_category: Dict[str, List[str]]) -> str:
    """Generate README entries for missing problems."""
    output = []
    
    for category, problems in sorted(missing_by_category.items()):
        if not problems:
            continue
            
        output.append(f"\n### {category}")
        output.append(f"Found {len(problems)} missing problems:")
        
        for problem in sorted(problems, key=lambda x: x['title']):
            title = problem['title']
            link = problem['link']
            file_path = problem['file_path']
            
            # Format for README
            readme_entry = f"- [{title}]({link}) | [Solution]({file_path})"
            output.append(readme_entry)
    
    return '\n'.join(output)

def main():
    print("Analyzing LeetCode problems in workspace...")
    
    # Get all problems from files
    all_problems = get_all_leetcode_problems()
    print(f"Found {len(all_problems)} LeetCode problems in workspace")
    
    # Get problems mentioned in README
    readme_problems = get_readme_problems()
    print(f"Found {len(readme_problems)} problems mentioned in README")
    
    # Find missing problems
    missing_slugs = set(all_problems.keys()) - readme_problems
    print(f"Found {len(missing_slugs)} problems missing from README")
    
    if not missing_slugs:
        print("All problems are already documented in README!")
        return
    
    # Categorize missing problems
    missing_by_category = categorize_missing_problems(all_problems, readme_problems)
    
    # Generate README entries
    readme_entries = generate_readme_entries(missing_by_category)
    
    # Save to file
    output_file = "missing_problems_for_readme.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Missing LeetCode Problems from README\n")
        f.write(f"Total missing: {len(missing_slugs)} problems\n")
        f.write(readme_entries)
    
    print(f"\nSaved missing problems analysis to: {output_file}")
    
    # Print summary
    print("\nSummary by category:")
    for category, problems in sorted(missing_by_category.items()):
        print(f"  {category}: {len(problems)} problems")

if __name__ == "__main__":
    main()
