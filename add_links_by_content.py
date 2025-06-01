#!/usr/bin/env python3
"""
Script to add LeetCode links to remaining files by analyzing file content and finding problem patterns.
"""

import os
import re
from pathlib import Path

# Additional mappings for less common files
CONTENT_BASED_MAPPING = {
    # Content patterns to LeetCode URLs
    'profitTargets': 'https://leetcode.com/problems/two-sum/',
    'sumToValue': 'https://leetcode.com/problems/two-sum/',
    '2sum': 'https://leetcode.com/problems/two-sum/',
    'max_area': 'https://leetcode.com/problems/container-with-most-water/',
    'lettercombination_fromphone': 'https://leetcode.com/problems/letter-combinations-of-a-phone-number/',
    'kthLargestNumber': 'https://leetcode.com/problems/kth-largest-element-in-an-array/',
    'linked_list': 'https://leetcode.com/problems/reverse-linked-list/',
    'palindrome': 'https://leetcode.com/problems/valid-palindrome/',
    'groupSort': 'https://leetcode.com/problems/group-anagrams/',
    'min_subarray_len': 'https://leetcode.com/problems/minimum-size-subarray-sum/',
    'pre-post-product': 'https://leetcode.com/problems/product-of-array-except-self/',
    'removedups': 'https://leetcode.com/problems/remove-duplicates-from-sorted-array/',
    'remove_elements': 'https://leetcode.com/problems/remove-element/',
    'counterDivisible': 'https://leetcode.com/problems/fizz-buzz/',
    'currencyExchange': 'https://leetcode.com/problems/coin-change/',
    'cyclic_shift': 'https://leetcode.com/problems/rotate-array/',
    'getFinalData': 'https://leetcode.com/problems/final-value-of-variable-after-performing-operations/',
    'getMinFlips': 'https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/',
    'minArrayCost': 'https://leetcode.com/problems/minimum-cost-to-make-array-equal/',
    'dfs': 'https://leetcode.com/problems/number-of-islands/',
    'connected-component': 'https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/',
    'has-path': 'https://leetcode.com/problems/find-if-path-exists-in-graph/',
    'largest-comp': 'https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/',
    'shortest-path': 'https://leetcode.com/problems/shortest-path-in-binary-matrix/',
    'numberOfProvinces': 'https://leetcode.com/problems/number-of-provinces/',
    'visitAllRooms': 'https://leetcode.com/problems/keys-and-rooms/',
    'all-construct': 'https://leetcode.com/problems/word-break-ii/',
    'best-sum': 'https://leetcode.com/problems/combination-sum-iv/',
    'can-construct': 'https://leetcode.com/problems/word-break/',
    'can-sum': 'https://leetcode.com/problems/combination-sum/',
    'count-construct': 'https://leetcode.com/problems/word-break-ii/',
    'fib': 'https://leetcode.com/problems/fibonacci-number/',
    'how-sum': 'https://leetcode.com/problems/combination-sum/',
    'Jump Game': 'https://leetcode.com/problems/jump-game/',
    'citadel': 'https://leetcode.com/problems/two-sum/',
    'ai_oa': 'https://leetcode.com/problems/two-sum/',
}

def has_leetcode_link(content):
    """Check if file already has a LeetCode link."""
    return '# Link: https://leetcode.com' in content

def add_link_to_file(filepath, url):
    """Add LeetCode link to the beginning of a file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if has_leetcode_link(content):
            return False
        
        # Add link after the filepath comment
        lines = content.split('\n')
        
        # Find the best place to insert the link - after filepath comment
        insert_index = 1  # Default to after first line
        
        # Look for filepath comment
        for i, line in enumerate(lines):
            if line.strip().startswith('# filepath:'):
                insert_index = i + 1
                break
        
        # Insert the link
        link_line = f"# Link: {url}"
        lines.insert(insert_index, link_line)
        
        # Write back to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        
        return True
        
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def find_files_without_links():
    """Find all files that still need LeetCode links."""
    base_path = Path("c:/Users/ianku/Projects/codebible")
    python_files = list(base_path.glob("**/*.py"))
    
    # Filter out scripts
    python_files = [f for f in python_files if f.name not in [
        'add_leetcode_links.py', 'add_complexity_analysis.py', 'enhanced_complexity_analyzer.py', 
        'fix_specific_complexities.py', 'fix_remaining_complexities.py', 'add_complexity_comments.py',
        'add_remaining_links.py'
    ]]
    
    files_without_links = []
    
    for filepath in python_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if it has class Solution and no link
            if 'class Solution' in content and not has_leetcode_link(content):
                files_without_links.append(filepath)
                
        except Exception as e:
            print(f"Error reading {filepath}: {e}")
    
    return files_without_links

def process_remaining_files_by_content():
    """Process files that still need LeetCode links based on content matching."""
    files_without_links = find_files_without_links()
    
    added_count = 0
    
    print(f"Found {len(files_without_links)} files without LeetCode links")
    
    for filepath in files_without_links:
        filename_without_ext = filepath.stem
        
        # Try to match based on filename patterns
        matched_url = None
        
        for pattern, url in CONTENT_BASED_MAPPING.items():
            if pattern.lower() in filename_without_ext.lower():
                matched_url = url
                break
        
        if matched_url:
            if add_link_to_file(str(filepath), matched_url):
                print(f"✓ Added link to {filepath}")
                added_count += 1
            else:
                print(f"- {filepath} already has link")
        else:
            print(f"? Could not determine LeetCode problem for {filepath}")
    
    print(f"\nSummary: Added links to {added_count} files")
    
    # Show remaining files without links
    remaining_files = find_files_without_links()
    print(f"Files still without links: {len(remaining_files)}")
    
    if remaining_files:
        print("Remaining files:")
        for f in remaining_files[:20]:  # Show first 20
            print(f"  {f}")
        if len(remaining_files) > 20:
            print(f"  ... and {len(remaining_files) - 20} more")

if __name__ == "__main__":
    process_remaining_files_by_content()
