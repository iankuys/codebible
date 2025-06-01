#!/usr/bin/env python3
"""
Script to add LeetCode links to Python files that contain LeetCode problems.
"""

import os
import re
import glob
from pathlib import Path

def extract_problem_number_from_content(content):
    """Extract problem number from file content."""
    # Look for patterns like "123. Problem Name" or "123 - Problem Name"
    patterns = [
        r'^(\d+)\.\s+(.+)$',  # "123. Problem Name"
        r'^(\d+)\s*[-–]\s*(.+)$',  # "123 - Problem Name"
        r'^(\d+)\s+(.+)$',  # "123 Problem Name"
    ]
    
    lines = content.strip().split('\n')
    for line in lines[:10]:  # Check first 10 lines
        line = line.strip().lstrip('#').strip()
        for pattern in patterns:
            match = re.match(pattern, line)
            if match:
                try:
                    num = int(match.group(1))
                    title = match.group(2).strip()
                    return num, title
                except ValueError:
                    continue
    return None, None

def extract_problem_number_from_filename(filename):
    """Extract problem number from filename."""
    # Look for patterns like "123-problem" or "123.problem"
    patterns = [
        r'^(\d+)[-\.]',  # "123-" or "123."
        r'(\d+)[-\.]'    # any "123-" or "123." in filename
    ]
    
    for pattern in patterns:
        match = re.search(pattern, filename)
        if match:
            try:
                return int(match.group(1))
            except ValueError:
                continue
    return None

def generate_leetcode_url(problem_number, title=None):
    """Generate LeetCode URL from problem number and title."""
    if title:
        # Convert title to URL slug
        slug = title.lower()
        slug = re.sub(r'[^\w\s-]', '', slug)  # Remove special chars except spaces and hyphens
        slug = re.sub(r'[-\s]+', '-', slug)   # Replace spaces/hyphens with single hyphen
        slug = slug.strip('-')                # Remove leading/trailing hyphens
        return f"https://leetcode.com/problems/{slug}/"
    else:
        # For files without title, we'll use a generic approach
        return f"# LeetCode Problem {problem_number}: https://leetcode.com/problems/"

def has_leetcode_link(content):
    """Check if file already has a LeetCode link."""
    return 'leetcode.com' in content.lower()

def add_link_to_file(filepath, problem_number, title=None):
    """Add LeetCode link to the beginning of a file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if has_leetcode_link(content):
            print(f"✓ {filepath} already has LeetCode link")
            return
        
        # Generate the link
        if title:
            slug = title.lower()
            slug = re.sub(r'[^\w\s-]', '', slug)
            slug = re.sub(r'[-\s]+', '-', slug)
            slug = slug.strip('-')
            link = f"# Link: https://leetcode.com/problems/{slug}/"
        else:
            link = f"# LeetCode Problem {problem_number}: https://leetcode.com/problems/"
        
        # Find where to insert the link
        lines = content.split('\n')
        insert_pos = 0
        
        # Skip any existing filepath comments
        for i, line in enumerate(lines):
            if line.strip().startswith('# filepath:'):
                insert_pos = i + 1
                break
        
        # Insert the link
        if insert_pos < len(lines) and lines[insert_pos].strip() == '':
            lines[insert_pos] = link
        else:
            lines.insert(insert_pos, link)
        
        # Write back to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        
        print(f"✓ Added link to {filepath}")
        
    except Exception as e:
        print(f"✗ Error processing {filepath}: {e}")

def process_files():
    """Process all Python files in the workspace."""
    base_path = Path("c:/Users/ianku/Projects/codebible")
    python_files = list(base_path.glob("**/*.py"))
    
    print(f"Found {len(python_files)} Python files")
    processed_count = 0
    added_count = 0
    
    for filepath in python_files:
        try:
            # Skip the script itself
            if filepath.name == "add_leetcode_links.py":
                continue
                
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            processed_count += 1
            
            # Skip if already has link
            if has_leetcode_link(content):
                print(f"✓ {filepath.name} already has LeetCode link")
                continue
            
            # Try to extract problem number from content first
            problem_num, title = extract_problem_number_from_content(content)
            
            # If not found in content, try filename
            if problem_num is None:
                problem_num = extract_problem_number_from_filename(filepath.name)
            
            # If we found a problem number, add the link
            if problem_num is not None:
                add_link_to_file(str(filepath), problem_num, title)
                added_count += 1
            else:
                print(f"- {filepath.name} - no problem number found")
            
        except Exception as e:
            print(f"✗ Error reading {filepath}: {e}")
    
    print(f"\nSummary: Processed {processed_count} files, added links to {added_count} files")

if __name__ == "__main__":
    process_files()
