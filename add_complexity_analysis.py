#!/usr/bin/env python3
"""
Script to add comprehensive time complexity analysis to all LeetCode solutions.
Analyzes code patterns and adds best/average/worst case complexity comments.
"""

import os
import re
import ast
from pathlib import Path
from typing import Dict, List, Tuple, Optional

class ComplexityAnalyzer:
    def __init__(self):
        # Common algorithm patterns and their complexities
        self.patterns = {
            # Array/List patterns
            'single_loop': {
                'pattern': r'for.*in.*:',
                'best': 'O(n)',
                'avg': 'O(n)', 
                'worst': 'O(n)',
                'description': 'single pass through array'
            },
            'nested_loops': {
                'pattern': r'for.*in.*:\s*.*for.*in.*:',
                'best': 'O(n²)',
                'avg': 'O(n²)',
                'worst': 'O(n²)',
                'description': 'nested loops'
            },
            'binary_search': {
                'pattern': r'(left.*right|mid.*=|while.*left.*<=.*right)',
                'best': 'O(1)',
                'avg': 'O(log n)',
                'worst': 'O(log n)',
                'description': 'binary search pattern'
            },
            'sorting': {
                'pattern': r'(\.sort\(\)|sorted\()',
                'best': 'O(n log n)',
                'avg': 'O(n log n)',
                'worst': 'O(n log n)',
                'description': 'sorting operation'
            },
            # Tree patterns
            'tree_traversal': {
                'pattern': r'(def.*\(.*root.*\)|\.left|\.right)',
                'best': 'O(n)',
                'avg': 'O(n)',
                'worst': 'O(n)',
                'description': 'tree traversal'
            },
            'bst_search': {
                'pattern': r'(if.*val.*<.*:|if.*val.*>.*:)',
                'best': 'O(log n)',
                'avg': 'O(log n)',
                'worst': 'O(n)',
                'description': 'BST operations'
            },
            # Graph patterns
            'dfs_bfs': {
                'pattern': r'(queue|deque|stack|visited)',
                'best': 'O(V + E)',
                'avg': 'O(V + E)',
                'worst': 'O(V + E)',
                'description': 'graph traversal'
            },
            # Dynamic Programming
            'dp_1d': {
                'pattern': r'dp\[.*\].*=',
                'best': 'O(n)',
                'avg': 'O(n)',
                'worst': 'O(n)',
                'description': '1D dynamic programming'
            },
            'dp_2d': {
                'pattern': r'dp\[.*\]\[.*\].*=',
                'best': 'O(n²)',
                'avg': 'O(n²)',
                'worst': 'O(n²)',
                'description': '2D dynamic programming'
            },
            # Hash table patterns
            'hash_operations': {
                'pattern': r'(dict\(\)|{}|\[.*\].*in.*dict)',
                'best': 'O(1)',
                'avg': 'O(1)',
                'worst': 'O(n)',
                'description': 'hash table operations'
            },            # Heap patterns
            'heap_operations': {
                'pattern': r'(heapq\.|heappush|heappop)',
                'best': 'O(log n)',
                'avg': 'O(log n)',
                'worst': 'O(log n)',
                'description': 'heap operations'
            },
            'k_closest_max_heap': {
                'pattern': r'(heappush.*heappop.*len.*>.*k|if.*len.*>.*k.*heappop)',
                'best': 'O(n log k)',
                'avg': 'O(n log k)',
                'worst': 'O(n log k)',
                'description': 'k-closest with max heap'
            },
            'heapify_pattern': {
                'pattern': r'heapify',
                'best': 'O(n)',
                'avg': 'O(n)',
                'worst': 'O(n)',
                'description': 'heap creation'
            }
        }
      def analyze_function(self, code: str, func_name: str) -> Dict[str, str]:
        """Analyze a function and determine its complexity."""
        # Count loops and nesting
        loop_count = len(re.findall(r'for.*in.*:', code))
        while_count = len(re.findall(r'while.*:', code))
        
        # Special case: K closest points with max heap pattern
        if re.search(r'heappush.*heappop.*len.*>.*k|if.*len.*>.*k.*heappop', code, re.DOTALL):
            return {
                'best': 'O(n log k)',
                'avg': 'O(n log k)',
                'worst': 'O(n log k)',
                'space': 'O(k)',
                'description': 'heap operations for each point, heap size limited to k'
            }
        
        # Special case: Min heap with heapify + k pops
        if re.search(r'heapify.*while.*k.*>.*0|heapify.*for.*range.*k', code, re.DOTALL):
            return {
                'best': 'O(n + k log n)',
                'avg': 'O(n + k log n)',
                'worst': 'O(n + k log n)',
                'space': 'O(n)',
                'description': 'heapify O(n) + k heap pops O(k log n)'
            }
        
        # Check for specific patterns
        for pattern_name, pattern_info in self.patterns.items():
            if re.search(pattern_info['pattern'], code, re.DOTALL | re.IGNORECASE):
                # Customize based on specific algorithms
                if 'tree' in func_name.lower() or 'node' in code.lower():
                    if 'bst' in func_name.lower() or re.search(r'val.*<|val.*>', code):
                        return {
                            'best': 'O(log n)',
                            'avg': 'O(log n)', 
                            'worst': 'O(n)',
                            'space': 'O(h)',
                            'description': 'BST operations - balanced vs skewed tree'
                        }
                    else:
                        return {
                            'best': 'O(n)',
                            'avg': 'O(n)',
                            'worst': 'O(n)',
                            'space': 'O(h)',
                            'description': 'tree traversal where h is height'
                        }
                
                # For array operations
                if loop_count >= 2:
                    return {
                        'best': 'O(n²)',
                        'avg': 'O(n²)',
                        'worst': 'O(n²)',
                        'space': 'O(1)',
                        'description': 'nested iteration'
                    }
                elif loop_count == 1 or while_count == 1:
                    if 'binary' in func_name.lower() or re.search(r'left.*right|mid.*=', code):
                        return {
                            'best': 'O(1)',
                            'avg': 'O(log n)',
                            'worst': 'O(log n)',
                            'space': 'O(1)',
                            'description': 'binary search'
                        }
                    else:
                        return {
                            'best': 'O(n)',
                            'avg': 'O(n)',
                            'worst': 'O(n)',
                            'space': 'O(1)',
                            'description': 'linear scan'
                        }
                
                return {
                    'best': pattern_info['best'],
                    'avg': pattern_info['avg'],
                    'worst': pattern_info['worst'],
                    'space': 'O(1)',
                    'description': pattern_info['description']
                }
        
        # Default complexity
        return {
            'best': 'O(n)',
            'avg': 'O(n)',
            'worst': 'O(n)',
            'space': 'O(1)',
            'description': 'linear operation'
        }

    def extract_functions(self, code: str) -> List[Tuple[str, str, int]]:
        """Extract all Solution class methods from the code."""
        functions = []
        lines = code.split('\n')
        
        in_solution_class = False
        current_func = None
        func_start_line = 0
        func_lines = []
        indent_level = 0
        
        for i, line in enumerate(lines):
            stripped = line.strip()
            
            # Check if we're entering a Solution class
            if re.match(r'class Solution', stripped):
                in_solution_class = True
                continue
            
            # Check if we're leaving the current class
            if in_solution_class and stripped.startswith('class ') and 'Solution' not in stripped:
                in_solution_class = False
                continue
            
            if in_solution_class:
                # Check for method definition
                if re.match(r'def \w+', stripped):
                    # Save previous function if exists
                    if current_func and func_lines:
                        func_code = '\n'.join(func_lines)
                        functions.append((current_func, func_code, func_start_line))
                    
                    # Start new function
                    current_func = re.search(r'def (\w+)', stripped).group(1)
                    func_start_line = i
                    func_lines = [line]
                    indent_level = len(line) - len(line.lstrip())
                elif current_func:
                    # Continue collecting function lines
                    current_line_indent = len(line) - len(line.lstrip()) if line.strip() else indent_level + 4
                    if line.strip() == '' or current_line_indent > indent_level:
                        func_lines.append(line)
                    else:
                        # Function ended, save it
                        func_code = '\n'.join(func_lines)
                        functions.append((current_func, func_code, func_start_line))
                        current_func = None
                        func_lines = []
        
        # Don't forget the last function
        if current_func and func_lines:
            func_code = '\n'.join(func_lines)
            functions.append((current_func, func_code, func_start_line))
        
        return functions

    def generate_complexity_comment(self, complexity: Dict[str, str]) -> str:
        """Generate a formatted complexity comment."""
        comment = "# Time Complexity:\n"
        comment += f"#   Best case: {complexity['best']} - {complexity['description']}\n"
        comment += f"#   Average case: {complexity['avg']}\n"
        comment += f"#   Worst case: {complexity['worst']}\n"
        comment += f"# Space Complexity: {complexity['space']}"
        return comment

def has_complexity_comment(code: str) -> bool:
    """Check if code already has time complexity comments."""
    return 'time complexity' in code.lower() or 'best case' in code.lower()

def add_complexity_to_file(filepath: str, analyzer: ComplexityAnalyzer):
    """Add complexity analysis to a single file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if has_complexity_comment(content):
            print(f"✓ {Path(filepath).name} already has complexity analysis")
            return False
        
        lines = content.split('\n')
        new_lines = []
        modified = False
        
        # Extract functions and their complexities
        functions = analyzer.extract_functions(content)
        
        if not functions:
            print(f"- {Path(filepath).name} - no Solution class methods found")
            return False
        
        i = 0
        while i < len(lines):
            line = lines[i]
            
            # Check if this line starts a Solution class method
            if re.match(r'\s*class Solution', line.strip()):
                new_lines.append(line)
                i += 1
                
                # Look for the next method definition
                while i < len(lines):
                    line = lines[i]
                    if re.match(r'\s*def \w+', line.strip()):
                        # Find the matching function
                        func_name = re.search(r'def (\w+)', line.strip()).group(1)
                        
                        # Find complexity for this function
                        for fname, fcode, _ in functions:
                            if fname == func_name:
                                complexity = analyzer.analyze_function(fcode, fname)
                                complexity_comment = analyzer.generate_complexity_comment(complexity)
                                
                                # Add complexity comment before method
                                for comment_line in complexity_comment.split('\n'):
                                    new_lines.append(' ' * (len(line) - len(line.lstrip())) + comment_line)
                                modified = True
                                break
                        
                        new_lines.append(line)
                        i += 1
                        break
                    else:
                        new_lines.append(line)
                        i += 1
            else:
                new_lines.append(line)
                i += 1
        
        if modified:
            # Write back to file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write('\n'.join(new_lines))
            print(f"✓ Added complexity analysis to {Path(filepath).name}")
            return True
        else:
            print(f"- {Path(filepath).name} - no modifications needed")
            return False
            
    except Exception as e:
        print(f"✗ Error processing {filepath}: {e}")
        return False

def process_all_files():
    """Process all Python files in the workspace."""
    base_path = Path("c:/Users/ianku/Projects/codebible")
    python_files = list(base_path.glob("**/*.py"))
    
    # Filter out our own scripts
    python_files = [f for f in python_files 
                   if f.name not in ["add_leetcode_links.py", "add_complexity_analysis.py"]]
    
    analyzer = ComplexityAnalyzer()
    
    print(f"Found {len(python_files)} Python files to analyze")
    
    modified_count = 0
    processed_count = 0
    
    for filepath in python_files:
        try:
            processed_count += 1
            print(f"Processing: {filepath.name}")
            if add_complexity_to_file(str(filepath), analyzer):
                modified_count += 1
        except Exception as e:
            print(f"Error with {filepath}: {e}")
    
    print(f"\nSummary: Processed {processed_count} files, added complexity analysis to {modified_count} files")

if __name__ == "__main__":
    process_all_files()
