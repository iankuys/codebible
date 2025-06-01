#!/usr/bin/env python3
"""
Enhanced complexity analysis script with improved pattern recognition.
Handles more algorithmic patterns for accurate complexity analysis.
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple, Optional

class EnhancedComplexityAnalyzer:
    def __init__(self):
        # Enhanced algorithm patterns with more precise complexity analysis
        self.patterns = {
            # Sorting patterns
            'quickselect': {
                'pattern': r'(partition|pivot.*left.*right)',
                'best': 'O(n)',
                'avg': 'O(n)',
                'worst': 'O(n²)',
                'space': 'O(log n)',
                'description': 'quickselect algorithm'
            },
            'merge_sort': {
                'pattern': r'(merge.*sort|divide.*conquer.*merge)',
                'best': 'O(n log n)',
                'avg': 'O(n log n)',
                'worst': 'O(n log n)',
                'space': 'O(n)',
                'description': 'merge sort'
            },
            'built_in_sort': {
                'pattern': r'(\.sort\(\)|sorted\()',
                'best': 'O(n log n)',
                'avg': 'O(n log n)',
                'worst': 'O(n log n)',
                'space': 'O(1)' if 'sort()' in r'(\.sort\(\)|sorted\())' else 'O(n)',
                'description': 'built-in sorting'
            },
            
            # Two pointers patterns
            'two_pointers_sorted': {
                'pattern': r'(sorted.*left.*right|left.*right.*while.*<)',
                'best': 'O(n log n)',
                'avg': 'O(n log n)',
                'worst': 'O(n log n)',
                'space': 'O(1)',
                'description': 'two pointers on sorted array (sort dominates)'
            },
            'two_pointers_linear': {
                'pattern': r'(left.*=.*0.*right.*=.*len|while.*left.*<.*right)',
                'best': 'O(n)',
                'avg': 'O(n)',
                'worst': 'O(n)',
                'space': 'O(1)',
                'description': 'two pointers technique'
            },
            
            # Sliding window patterns
            'sliding_window': {
                'pattern': r'(window|start.*end|left.*right.*expand|shrink)',
                'best': 'O(n)',
                'avg': 'O(n)',
                'worst': 'O(n)',
                'space': 'O(k)',
                'description': 'sliding window'
            },
            
            # Tree patterns - more nuanced
            'tree_bfs': {
                'pattern': r'(queue.*level|level.*order|bfs)',
                'best': 'O(n)',
                'avg': 'O(n)',
                'worst': 'O(n)',
                'space': 'O(w)',
                'description': 'tree BFS where w is maximum width'
            },
            'tree_dfs': {
                'pattern': r'(def.*dfs|recursive.*left.*right)',
                'best': 'O(n)',
                'avg': 'O(n)',
                'worst': 'O(n)',
                'space': 'O(h)',
                'description': 'tree DFS where h is height'
            },
            'bst_operations': {
                'pattern': r'(if.*val.*<.*left|if.*val.*>.*right|binary.*search.*tree)',
                'best': 'O(log n)',
                'avg': 'O(log n)',
                'worst': 'O(n)',
                'space': 'O(log n)',
                'description': 'BST operations - balanced vs skewed'
            },
            
            # Graph patterns
            'graph_dfs_bfs': {
                'pattern': r'(visited.*set|adjacency|neighbors|graph)',
                'best': 'O(V + E)',
                'avg': 'O(V + E)',
                'worst': 'O(V + E)',
                'space': 'O(V)',
                'description': 'graph traversal'
            },
            'dijkstra': {
                'pattern': r'(dijkstra|shortest.*path.*priority|min.*distance)',
                'best': 'O((V + E) log V)',
                'avg': 'O((V + E) log V)',
                'worst': 'O((V + E) log V)',
                'space': 'O(V)',
                'description': 'Dijkstra algorithm'
            },
            
            # Dynamic Programming patterns
            'dp_1d_linear': {
                'pattern': r'dp\[i\].*dp\[i-1\]|memo\[.*\].*=',
                'best': 'O(n)',
                'avg': 'O(n)',
                'worst': 'O(n)',
                'space': 'O(n)',
                'description': '1D DP'
            },
            'dp_2d': {
                'pattern': r'dp\[i\]\[j\].*dp\[i-1\]\[j\]|matrix.*dp',
                'best': 'O(m × n)',
                'avg': 'O(m × n)',
                'worst': 'O(m × n)',
                'space': 'O(m × n)',
                'description': '2D DP'
            },
            'dp_memoization': {
                'pattern': r'@lru_cache|functools.*cache|memoization',
                'best': 'O(n)',
                'avg': 'O(n)',
                'worst': 'O(n)',
                'space': 'O(n)',
                'description': 'memoized recursion'
            },
            
            # Heap patterns - more specific
            'heap_k_closest': {
                'pattern': r'heappush.*if.*len.*>.*k.*heappop',
                'best': 'O(n log k)',
                'avg': 'O(n log k)',
                'worst': 'O(n log k)',
                'space': 'O(k)',
                'description': 'k-closest with bounded heap'
            },
            'heap_all_elements': {
                'pattern': r'heapify.*while.*heappop',
                'best': 'O(n + k log n)',
                'avg': 'O(n + k log n)',
                'worst': 'O(n + k log n)',
                'space': 'O(n)',
                'description': 'heapify + k extractions'
            },
            'heap_stream': {
                'pattern': r'class.*heap.*add.*remove',
                'best': 'O(log n)',
                'avg': 'O(log n)',
                'worst': 'O(log n)',
                'space': 'O(n)',
                'description': 'heap stream operations'
            },
            
            # Backtracking patterns
            'backtracking': {
                'pattern': r'(backtrack|permutation|combination|subset)',
                'best': 'O(2ⁿ)',
                'avg': 'O(2ⁿ)',
                'worst': 'O(2ⁿ)',
                'space': 'O(n)',
                'description': 'backtracking (exponential)'
            },
            'n_queens': {
                'pattern': r'(queens|board.*valid|row.*col.*diagonal)',
                'best': 'O(n!)',
                'avg': 'O(n!)',
                'worst': 'O(n!)',
                'space': 'O(n)',
                'description': 'n-queens problem'
            },
            
            # String patterns
            'string_kmp': {
                'pattern': r'(kmp|failure.*function|pattern.*matching)',
                'best': 'O(n + m)',
                'avg': 'O(n + m)',
                'worst': 'O(n + m)',
                'space': 'O(m)',
                'description': 'KMP string matching'
            },
            'string_sliding': {
                'pattern': r'substring.*window|anagram.*permutation',
                'best': 'O(n)',
                'avg': 'O(n)',
                'worst': 'O(n)',
                'space': 'O(k)',
                'description': 'string sliding window'
            },
            
            # Binary search patterns
            'binary_search_basic': {
                'pattern': r'left.*right.*mid.*=.*\(left.*\+.*right\).*//.*2',
                'best': 'O(1)',
                'avg': 'O(log n)',
                'worst': 'O(log n)',
                'space': 'O(1)',
                'description': 'binary search'
            },
            'binary_search_2d': {
                'pattern': r'matrix.*binary.*search|search.*2d.*matrix',
                'best': 'O(1)',
                'avg': 'O(log(m × n))',
                'worst': 'O(log(m × n))',
                'space': 'O(1)',
                'description': '2D binary search'
            },
            
            # Union-Find patterns
            'union_find': {
                'pattern': r'(union.*find|disjoint.*set|parent.*array)',
                'best': 'O(α(n))',
                'avg': 'O(α(n))',
                'worst': 'O(α(n))',
                'space': 'O(n)',
                'description': 'union-find with path compression'
            },
            
            # Trie patterns
            'trie': {
                'pattern': r'(class.*Trie|children.*dict|is_word)',
                'best': 'O(L)',
                'avg': 'O(L)',
                'worst': 'O(L)',
                'space': 'O(ALPHABET_SIZE × N × L)',
                'description': 'trie operations where L is word length'
            }
        }

    def analyze_specific_patterns(self, code: str, func_name: str) -> Optional[Dict[str, str]]:
        """Analyze code for specific algorithmic patterns."""
        
        # Check for 3Sum pattern (sort + two pointers)
        if re.search(r'sorted.*nums.*for.*i.*while.*left.*<.*right', code, re.DOTALL):
            return {
                'best': 'O(n²)',
                'avg': 'O(n²)',
                'worst': 'O(n²)',
                'space': 'O(1)',
                'description': '3Sum: sort O(n log n) + nested two pointers O(n²)'
            }
        
        # Check for matrix traversal
        if re.search(r'for.*i.*range.*len.*matrix.*for.*j.*range.*len.*matrix\[0\]', code, re.DOTALL):
            return {
                'best': 'O(m × n)',
                'avg': 'O(m × n)',
                'worst': 'O(m × n)',
                'space': 'O(1)',
                'description': 'matrix traversal'
            }
        
        # Check for palindrome checking
        if re.search(r'left.*right.*while.*left.*<.*right.*s\[left\].*s\[right\]', code, re.DOTALL):
            return {
                'best': 'O(1)',
                'avg': 'O(n)',
                'worst': 'O(n)',
                'space': 'O(1)',
                'description': 'palindrome check with two pointers'
            }
        
        # Check for subset generation
        if re.search(r'for.*i.*range.*len.*nums.*backtrack.*nums\[i\]', code, re.DOTALL):
            return {
                'best': 'O(2ⁿ)',
                'avg': 'O(2ⁿ)',
                'worst': 'O(2ⁿ)',
                'space': 'O(n)',
                'description': 'subset generation (exponential)'
            }
        
        return None

    def analyze_function(self, code: str, func_name: str) -> Dict[str, str]:
        """Enhanced function analysis with better pattern recognition."""
        
        # First check for specific patterns
        specific_analysis = self.analyze_specific_patterns(code, func_name)
        if specific_analysis:
            return specific_analysis
        
        # Check against enhanced patterns
        for pattern_name, pattern_info in self.patterns.items():
            if re.search(pattern_info['pattern'], code, re.DOTALL | re.IGNORECASE):
                return {
                    'best': pattern_info['best'],
                    'avg': pattern_info['avg'],
                    'worst': pattern_info['worst'],
                    'space': pattern_info['space'],
                    'description': pattern_info['description']
                }
        
        # Fallback analysis based on loop structure
        loop_count = len(re.findall(r'for.*in.*:', code))
        nested_loops = len(re.findall(r'for.*in.*:.*for.*in.*:', code, re.DOTALL))
        
        if nested_loops > 0:
            return {
                'best': 'O(n²)',
                'avg': 'O(n²)',
                'worst': 'O(n²)',
                'space': 'O(1)',
                'description': 'nested iteration'
            }
        elif loop_count > 0:
            return {
                'best': 'O(n)',
                'avg': 'O(n)',
                'worst': 'O(n)',
                'space': 'O(1)',
                'description': 'linear iteration'
            }
        
        # Default
        return {
            'best': 'O(1)',
            'avg': 'O(1)',
            'worst': 'O(1)',
            'space': 'O(1)',
            'description': 'constant time operation'
        }
    
    def has_complexity_comment(self, content: str) -> bool:
        """Check if the content already has time complexity comments."""
        return bool(re.search(r'# Time Complexity:', content, re.IGNORECASE))
    
    def analyze_code_complexity(self, content: str, filepath: str) -> Optional[Dict[str, str]]:
        """Analyze code and determine the correct complexity based on enhanced patterns."""
          # Special patterns for specific algorithms
        
        # 3Sum pattern: Sort + nested loops with two pointers = O(n²)
        if ('threeSum' in content or '3sum' in filepath.lower()) and 'sorted(' in content:
            if re.search(r'while.*<.*:.*while.*<.*:', content, re.DOTALL):
                return {
                    'best': 'O(n²)',
                    'avg': 'O(n²)', 
                    'worst': 'O(n²)',
                    'space': 'O(1)',
                    'description': 'sorting + two pointers nested loops'
                }
        
        # Sliding window patterns should be O(n)
        if any(pattern in filepath.lower() for pattern in ['sliding_window', 'window']):
            if re.search(r'(left|start).*right|while.*<.*len', content):
                return {
                    'best': 'O(n)',
                    'avg': 'O(n)',
                    'worst': 'O(n)', 
                    'space': 'O(1)',
                    'description': 'sliding window technique'
                }
        
        # Word Search in grid - backtracking DFS
        if 'word_search' in filepath.lower() or ('exist' in content and 'board' in content and 'word' in content):
            return {
                'best': 'O(m × n × 4^L)',
                'avg': 'O(m × n × 4^L)',
                'worst': 'O(m × n × 4^L)',
                'space': 'O(L)',
                'description': 'backtracking DFS on grid (L = word length)'
            }
        
        # Spiral matrix patterns - visit each cell once
        if 'spiral' in filepath.lower() and 'matrix' in content:
            return {
                'best': 'O(m × n)',
                'avg': 'O(m × n)',
                'worst': 'O(m × n)',
                'space': 'O(m × n)',
                'description': 'visit each matrix cell once'
            }
        
        # Matrix rotation - transpose + reflect operations
        if ('rotate' in filepath.lower() and 'matrix' in content) or 'transpose' in content:
            return {
                'best': 'O(n²)',
                'avg': 'O(n²)',
                'worst': 'O(n²)',
                'space': 'O(1)',
                'description': 'matrix transpose and reflection'
            }
        
        # Set matrix zeros - two passes through matrix
        if 'setZeroes' in content or 'set.*zero' in filepath.lower():
            return {
                'best': 'O(m × n)',
                'avg': 'O(m × n)',
                'worst': 'O(m × n)',
                'space': 'O(m + n)',
                'description': 'two-pass matrix traversal'
            }
        
        # Maximal square DP - recursive with memoization  
        if 'maximalSquare' in content and 'cache' in content:
            return {
                'best': 'O(m × n)',
                'avg': 'O(m × n)',
                'worst': 'O(m × n)',
                'space': 'O(m × n)',
                'description': 'dynamic programming with memoization'
            }
        
        # Binary search patterns
        if 'binary_search' in filepath.lower() or re.search(r'left.*right.*mid.*=.*\(left.*\+.*right\).*//.*2', content):
            return {
                'best': 'O(1)',
                'avg': 'O(log n)',
                'worst': 'O(log n)',
                'space': 'O(1)',
                'description': 'binary search'
            }
        
        # Backtracking patterns - exponential complexities
        if 'backtracking' in filepath.lower():
            if 'combinationSum' in content:
                return {
                    'best': 'O(2^n)',
                    'avg': 'O(2^n)',
                    'worst': 'O(2^n)',
                    'space': 'O(target/min_candidate)',
                    'description': 'backtracking exploration of all combinations'
                }
            elif 'permutation' in content.lower() or 'permutation' in filepath.lower():
                return {
                    'best': 'O(n!)',
                    'avg': 'O(n!)',
                    'worst': 'O(n!)',
                    'space': 'O(n)',
                    'description': 'backtracking to generate all permutations'
                }
            elif 'subset' in content.lower() or 'subset' in filepath.lower():
                return {
                    'best': 'O(2^n)',
                    'avg': 'O(2^n)',
                    'worst': 'O(2^n)',
                    'space': 'O(n)',
                    'description': 'backtracking to generate all subsets'
                }
            elif 'letter' in content.lower() and 'combination' in content.lower():
                return {
                    'best': 'O(4^n)',
                    'avg': 'O(4^n)',
                    'worst': 'O(4^n)',
                    'space': 'O(n)',
                    'description': 'backtracking phone letter combinations'
                }
        
        # Apply general patterns if no specific pattern matched
        for pattern_name, pattern_info in self.patterns.items():
            if re.search(pattern_info['pattern'], content, re.MULTILINE | re.DOTALL):
                return pattern_info
        
        return None
    
    def update_complexity_comments(self, content: str, new_analysis: Dict[str, str]) -> str:
        """Update existing complexity comments with new analysis."""
        
        # Pattern to match existing complexity comments
        pattern = r'(    # Time Complexity:\s*\n    #   Best case: O\([^)]+\)[^\n]*\n    #   Average case: O\([^)]+\)[^\n]*\n    #   Worst case: O\([^)]+\)[^\n]*\n    # Space Complexity: O\([^)]+\)[^\n]*)'
        
        # Create new complexity comment
        new_comment = f"""    # Time Complexity:
    #   Best case: {new_analysis['best']} - {new_analysis['description']}
    #   Average case: {new_analysis['avg']}
    #   Worst case: {new_analysis['worst']}
    # Space Complexity: {new_analysis['space']}"""
        
        # Replace the existing comment
        updated_content = re.sub(pattern, new_comment, content, flags=re.MULTILINE)
        
        return updated_content

def update_complexity_analysis():
    """Update files that need better complexity analysis."""
    analyzer = EnhancedComplexityAnalyzer()
      # Files that likely need updates based on algorithmic patterns
    candidates = [
        "NEETCODE 150/two pointers/3sum.py",
        "OG BIBLE/pointers/3sum.py",
        "NEETCODE 150/sliding_window/3-longestsubstr.py",
        "NEETCODE 150/sliding_window/minWindowSubstr.py",
        "NEETCODE 150/sliding_window/permutationInString.py",
        "NEETCODE 150/backtracking/combinationsum.py",
        "NEETCODE 150/backtracking/combinationsum2.py",
        "NEETCODE 150/backtracking/letter_combination.py",
        "NEETCODE 150/backtracking/subset.py",
        "NEETCODE 150/backtracking/permutation.py",
        "NEETCODE 150/backtracking/word_search.py",
        "NEETCODE 150/math&geom/54-spiralmatrix.py",
        "NEETCODE 150/math&geom/setzeroes.py",
        "NEETCODE 150/2d/maximalSquare.py",
        "NEETCODE 150/binary_search/binary_search.py",
        "TAGGED/Capital One/spiralOrder.py",
        "TAGGED/Capital One/rotateImage.py",
        "OG BIBLE/array-matrix/rotate_matrix.py",
        "OG BIBLE/array-matrix/54-spiralmatrix.py"
    ]
    
    base_path = Path("c:/Users/ianku/Projects/codebible")
    files_updated = 0
    
    for candidate in candidates:
        filepath = base_path / candidate
        if filepath.exists():
            print(f"Analyzing: {candidate}")
            
            # Read the current file content
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if it has complexity comments
            if analyzer.has_complexity_comment(content):
                # Analyze and get new complexity
                new_analysis = analyzer.analyze_code_complexity(content, str(filepath))
                
                if new_analysis:
                    # Update the complexity comments
                    updated_content = analyzer.update_complexity_comments(content, new_analysis)
                    
                    if updated_content != content:
                        # Write the updated content back
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(updated_content)
                        print(f"  ✅ Updated complexity analysis")
                        files_updated += 1
                    else:
                        print(f"  ✓ Complexity analysis already correct")
                else:
                    print(f"  ⚠️ Could not determine complexity")
            else:
                print(f"  ⚠️ No existing complexity comments found")
        else:
            print(f"  ❌ File not found: {candidate}")
    
    print(f"\nEnhanced complexity analysis complete! Updated {files_updated} files.")

if __name__ == "__main__":
    update_complexity_analysis()
