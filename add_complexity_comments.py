#!/usr/bin/env python3
"""
Script to add time complexity comments to LeetCode Python solutions.
"""

import os
import re
import ast
from pathlib import Path

# Common time complexity patterns for different algorithms
COMPLEXITY_PATTERNS = {
    # Array/String operations
    'two_pointers': 'O(n)',
    'sliding_window': 'O(n)',
    'prefix_sum': 'O(n)',
    
    # Tree operations
    'tree_traversal': 'O(n)',
    'tree_dfs': 'O(n)',
    'tree_bfs': 'O(n)',
    'binary_search_tree': 'O(log n)',
    
    # Graph operations
    'dfs': 'O(V + E)',
    'bfs': 'O(V + E)',
    'dijkstra': 'O(V log V + E)',
    'union_find': 'O(α(n))',
    
    # Sorting
    'merge_sort': 'O(n log n)',
    'quick_sort': 'O(n log n) average, O(n²) worst',
    'heap_sort': 'O(n log n)',
    'counting_sort': 'O(n + k)',
    
    # Dynamic Programming
    'dp_1d': 'O(n)',
    'dp_2d': 'O(n * m)',
    'knapsack': 'O(n * capacity)',
    
    # Binary Search
    'binary_search': 'O(log n)',
    
    # Heap operations
    'heap_push_pop': 'O(log n)',
    'heap_build': 'O(n)',
    
    # Hash operations
    'hash_lookup': 'O(1) average',
    
    # Backtracking
    'backtrack': 'O(2^n)',
    'permutation': 'O(n!)',
    
    # Default for unknown
    'unknown': 'O(?)'
}

def analyze_code_complexity(code_content, filename):
    """Analyze code to determine likely time complexity."""
    code_lower = code_content.lower()
    filename_lower = filename.lower()
    
    # Check for specific patterns in filename
    if 'two' in filename_lower and ('pointer' in filename_lower or 'sum' in filename_lower):
        return 'O(n)', 'O(1)'
    
    if 'sliding' in filename_lower or 'window' in filename_lower:
        return 'O(n)', 'O(1)'
    
    if 'binary' in filename_lower and 'search' in filename_lower:
        return 'O(log n)', 'O(1)'
    
    if 'tree' in filename_lower or 'bst' in filename_lower:
        if 'range' in filename_lower:
            return 'O(n)', 'O(h) where h is height of tree'
        return 'O(n)', 'O(h) where h is height of tree'
    
    if 'graph' in filename_lower or 'island' in filename_lower or 'course' in filename_lower:
        return 'O(V + E)', 'O(V + E)'
    
    if 'dp' in filename_lower or 'dynamic' in filename_lower or 'coin' in filename_lower:
        if '2d' in filename_lower:
            return 'O(n * m)', 'O(n * m)'
        return 'O(n)', 'O(n)'
    
    if 'heap' in filename_lower or 'priority' in filename_lower:
        return 'O(n log n)', 'O(n)'
    
    if 'sort' in filename_lower:
        return 'O(n log n)', 'O(1) or O(n)'
    
    if 'palindrome' in filename_lower:
        return 'O(n)', 'O(1)'
    
    if 'permutation' in filename_lower or 'combination' in filename_lower:
        return 'O(n!)', 'O(n)'
    
    if 'subset' in filename_lower:
        return 'O(2^n)', 'O(n)'
    
    # Code pattern analysis
    nested_loops = len(re.findall(r'for.*for.*:', code_content, re.DOTALL))
    single_loops = len(re.findall(r'for\s+\w+\s+in', code_content))
    while_loops = len(re.findall(r'while\s+', code_content))
    
    if nested_loops >= 2:
        return 'O(n²)', 'O(1)'
    elif nested_loops == 1:
        return 'O(n²)', 'O(1)'
    elif single_loops >= 1 or while_loops >= 1:
        return 'O(n)', 'O(1)'
    
    # Check for recursion
    if 'def ' in code_content and ('recurse' in code_content or 'dfs' in code_content or 'helper' in code_content):
        if 'tree' in filename_lower:
            return 'O(n)', 'O(h) where h is height of tree'
        elif 'graph' in filename_lower:
            return 'O(V + E)', 'O(V)'
        else:
            return 'O(n)', 'O(n)'
    
    # Default case
    return 'O(n)', 'O(1)'

def has_complexity_comment(code_content):
    """Check if the code already has time complexity comments."""
    complexity_patterns = [
        r'#.*[Tt]ime.*[Cc]omplexity.*O\(',
        r'#.*[Tt]ime.*O\(',
        r'#.*[Ss]pace.*[Cc]omplexity.*O\(',
        r'#.*[Ss]pace.*O\(',
        r'# Time:.*O\(',
        r'# Space:.*O\(',
    ]
    
    for pattern in complexity_patterns:
        if re.search(pattern, code_content):
            return True
    return False

def add_complexity_comment(filepath):
    """Add time and space complexity comments to a Python file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if has_complexity_comment(content):
            print(f"✓ {filepath.name} already has complexity comments")
            return
        
        # Analyze the code
        time_complexity, space_complexity = analyze_code_complexity(content, filepath.name)
        
        lines = content.split('\n')
        modified = False
        
        # Find class definitions and add comments
        for i, line in enumerate(lines):
            if line.strip().startswith('class Solution'):
                # Look for the method definition
                method_line_idx = None
                for j in range(i + 1, min(i + 10, len(lines))):
                    if 'def ' in lines[j] and not lines[j].strip().startswith('#'):
                        method_line_idx = j
                        break
                
                if method_line_idx is not None:
                    # Get indentation of the method
                    method_indent = len(lines[method_line_idx]) - len(lines[method_line_idx].lstrip())
                    comment_indent = ' ' * (method_indent + 4)  # Add 4 spaces for method body indent
                    
                    # Insert complexity comments before the method
                    complexity_comment = f"{' ' * method_indent}# Time: {time_complexity}, Space: {space_complexity}"
                    lines.insert(method_line_idx, complexity_comment)
                    modified = True
                    break
        
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines))
            print(f"✓ Added complexity comments to {filepath.name}")
        else:
            print(f"- Could not find suitable location in {filepath.name}")
            
    except Exception as e:
        print(f"✗ Error processing {filepath}: {e}")

def process_all_files():
    """Process all Python files in the workspace."""
    base_path = Path("c:/Users/ianku/Projects/codebible")
    python_files = []
    
    # Get all Python files
    for pattern in ["**/*.py"]:
        python_files.extend(base_path.glob(pattern))
    
    # Filter out the script itself and non-LeetCode files
    leetcode_files = []
    for filepath in python_files:
        if filepath.name in ['add_leetcode_links.py', 'add_complexity_comments.py']:
            continue
        
        # Check if it's likely a LeetCode file (has class Solution or problem number)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                if 'class Solution' in content or re.search(r'\d+\.', content) or 'leetcode' in content.lower():
                    leetcode_files.append(filepath)
        except:
            continue
    
    print(f"Found {len(leetcode_files)} LeetCode files")
    
    processed_count = 0
    added_count = 0
    
    for filepath in leetcode_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            processed_count += 1
            
            if has_complexity_comment(content):
                print(f"✓ {filepath.name} already has complexity comments")
                continue
            
            add_complexity_comment(filepath)
            added_count += 1
            
        except Exception as e:
            print(f"✗ Error processing {filepath}: {e}")
    
    print(f"\nSummary: Processed {processed_count} files, added complexity comments to {added_count} files")

if __name__ == "__main__":
    process_all_files()
