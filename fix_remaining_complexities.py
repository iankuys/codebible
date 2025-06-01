#!/usr/bin/env python3
"""
Script to fix remaining incorrect complexity classifications in Python files.
"""

import os
import re
from typing import List, Dict

def fix_two_pointer_algorithms():
    """Fix two-pointer algorithms incorrectly labeled as binary search."""
    fixed_files = []
    
    two_pointer_files = [
        "OG BIBLE/pointers/trap.py",
        "NEETCODE 150/two pointers/trap.py", 
        "OG BIBLE/pointers/max_area.py",
        "NEETCODE 150/two pointers/maxArea.py"
    ]
    
    for file_path in two_pointer_files:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Fix trapping rain water - two pointers, not binary search
                if 'trap' in file_path.lower() and 'while l < r' in content:
                    content = re.sub(
                        r'# Time Complexity:\s*\n\s*#\s*Best case: O\(1\) - binary search\s*\n\s*#\s*Average case: O\(log n\)\s*\n\s*#\s*Worst case: O\(log n\)',
                        '# Time Complexity:\n#   Best case: O(n) - two pointers scan\n#   Average case: O(n)\n#   Worst case: O(n)',
                        content
                    )
                
                # Fix container with most water - two pointers, not binary search
                if 'max_area' in file_path.lower() or 'maxArea' in file_path:
                    content = re.sub(
                        r'# Time Complexity:\s*\n\s*#\s*Best case: O\(1\) - binary search\s*\n\s*#\s*Average case: O\(log n\)\s*\n\s*#\s*Worst case: O\(log n\)',
                        '# Time Complexity:\n#   Best case: O(n) - two pointers scan\n#   Average case: O(n)\n#   Worst case: O(n)',
                        content
                    )
                    
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    fixed_files.append(file_path)
                    print(f"  Fixed two-pointer algorithm: {file_path}")
                    
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
    
    return fixed_files

def fix_dijkstra_algorithm():
    """Fix Dijkstra's algorithm complexity."""
    fixed_files = []
    
    dijkstra_files = [
        "NEETCODE 150/graphs/network_delay_time.py"
    ]
    
    for file_path in dijkstra_files:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Fix Dijkstra's algorithm - uses min heap with edges
                if 'minHeap' in content and 'heappop' in content and 'heappush' in content:
                    content = re.sub(
                        r'# Time Complexity:\s*\n\s*#\s*Best case: O\(n²\) - nested iteration\s*\n\s*#\s*Average case: O\(n²\)\s*\n\s*#\s*Worst case: O\(n²\)\s*\n\s*# Space Complexity: O\(1\)',
                        '# Time Complexity:\n#   Best case: O((V + E) log V) - Dijkstra with min heap\n#   Average case: O((V + E) log V)\n#   Worst case: O((V + E) log V)\n# Space Complexity: O(V)',
                        content
                    )
                    
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    fixed_files.append(file_path)
                    print(f"  Fixed Dijkstra algorithm: {file_path}")
                    
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
    
    return fixed_files

def fix_topological_sort():
    """Fix topological sort complexity."""
    fixed_files = []
    
    topo_files = [
        "OG BIBLE/tree&graphs/210-courseschedule2.py"
    ]
    
    for file_path in topo_files:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Fix course schedule - topological sort, not linear
                if 'findOrder' in content and 'dfs' in content:
                    content = re.sub(
                        r'# Time Complexity:\s*\n\s*#\s*Best case: O\(n\) - linear scan\s*\n\s*#\s*Average case: O\(n\)\s*\n\s*#\s*Worst case: O\(n\)\s*\n\s*# Space Complexity: O\(1\)',
                        '# Time Complexity:\n#   Best case: O(V + E) - topological sort with DFS\n#   Average case: O(V + E)\n#   Worst case: O(V + E)\n# Space Complexity: O(V)',
                        content
                    )
                    
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    fixed_files.append(file_path)
                    print(f"  Fixed topological sort: {file_path}")
                    
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
    
    return fixed_files

def fix_binary_search_files():
    """Fix binary search files with missing or incorrect complexity."""
    fixed_files = []
    
    binary_search_files = [
        "NEETCODE 150/binary_search/search_2d.py",
        "NEETCODE 150/binary_search/koko_eating_bananas.py"
    ]
    
    for file_path in binary_search_files:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Fix 2D matrix search - binary search on both dimensions
                if 'search_2d' in file_path and 'matrix' in content:
                    # Check if complexity comment already exists
                    if '# Time Complexity:' not in content:
                        # Find the class definition and add complexity comment
                        content = re.sub(
                            r'(class Solution:\s*\n\s*)(def )',
                            r'\1# Time Complexity:\n    #   Best case: O(1) - target found immediately\n    #   Average case: O(log(m × n))\n    #   Worst case: O(log(m × n))\n    # Space Complexity: O(1)\n    \2',
                            content
                        )
                
                # Fix Koko eating bananas - binary search with validation loop
                if 'koko_eating_bananas' in file_path and 'math.ceil' in content:
                    content = re.sub(
                        r'# Time Complexity:\s*\n\s*#\s*Best case: O\(1\) - binary search\s*\n\s*#\s*Average case: O\(log n\)\s*\n\s*#\s*Worst case: O\(log n\)',
                        '# Time Complexity:\n#   Best case: O(n log max_pile) - binary search with pile validation\n#   Average case: O(n log max_pile)\n#   Worst case: O(n log max_pile)',
                        content
                    )
                    
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    fixed_files.append(file_path)
                    print(f"  Fixed binary search: {file_path}")
                    
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
    
    return fixed_files

def fix_tree_space_complexity():
    """Fix tree algorithms with incorrect space complexity."""
    fixed_files = []
    
    tree_files = [
        "TAGGED/Meta/Tree/binaryTreeVerticalOrder.py",
        "OG BIBLE/linked_list/876-middlenode.py"
    ]
    
    for file_path in tree_files:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Fix binary tree vertical order - BFS with queue storage
                if 'verticalOrder' in content and 'queue' in content:
                    content = re.sub(
                        r'# Space Complexity: O\(h\)',
                        '# Space Complexity: O(n)',
                        content
                    )
                
                # Fix middle node - should be O(1) space for two pointers
                if 'middleNode' in content and 'slow = fast = head' in content:
                    content = re.sub(
                        r'# Time Complexity:\s*\n\s*#\s*Best case: O\(n\) - tree traversal where h is height\s*\n\s*#\s*Average case: O\(n\)\s*\n\s*#\s*Worst case: O\(n\)\s*\n\s*# Space Complexity: O\(h\)',
                        '# Time Complexity:\n#   Best case: O(n) - two pointers scan\n#   Average case: O(n)\n#   Worst case: O(n)\n# Space Complexity: O(1)',
                        content
                    )
                    
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    fixed_files.append(file_path)
                    print(f"  Fixed tree/linked list: {file_path}")
                    
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
    
    return fixed_files

def fix_climbing_stairs():
    """Fix climbing stairs memoization complexity."""
    fixed_files = []
    
    stairs_files = [
        "OG BIBLE/tree&graphs/70-climbingstairs.py"
    ]
    
    for file_path in stairs_files:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Fix climbing stairs - memoized recursion is O(n), not O(1)
                if 'climbStairs' in content and 'dict' in content and 'dfs' in content:
                    content = re.sub(
                        r'# Time Complexity:\s*\n\s*#\s*Best case: O\(1\) - hash table operations\s*\n\s*#\s*Average case: O\(1\)\s*\n\s*#\s*Worst case: O\(n\)\s*\n\s*# Space Complexity: O\(1\)',
                        '# Time Complexity:\n#   Best case: O(n) - memoized recursion\n#   Average case: O(n)\n#   Worst case: O(n)\n# Space Complexity: O(n)',
                        content
                    )
                    
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    fixed_files.append(file_path)
                    print(f"  Fixed climbing stairs: {file_path}")
                    
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
    
    return fixed_files

def fix_maximal_rectangle():
    """Fix maximal rectangle complexity."""
    fixed_files = []
    
    rect_files = [
        "NEETCODE 150/2d/maximalRectangle.py"
    ]
    
    for file_path in rect_files:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Fix maximal rectangle - should be O(m × n) time, O(n) space
                if 'maximalRectangle' in content:
                    content = re.sub(
                        r'# Time Complexity:\s*\n\s*#\s*Best case: O\(n²\) - nested iteration\s*\n\s*#\s*Average case: O\(n²\)\s*\n\s*#\s*Worst case: O\(n²\)\s*\n\s*# Space Complexity: O\(1\)',
                        '# Time Complexity:\n#   Best case: O(m × n) - process each cell with histogram\n#   Average case: O(m × n)\n#   Worst case: O(m × n)\n# Space Complexity: O(n)',
                        content
                    )
                    
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    fixed_files.append(file_path)
                    print(f"  Fixed maximal rectangle: {file_path}")
                    
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
    
    return fixed_files

def fix_walls_and_gates():
    """Fix walls and gates space complexity."""
    fixed_files = []
    
    walls_files = [
        "NEETCODE 150/graphs/walls_and_gates.py"
    ]
    
    for file_path in walls_files:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Fix walls and gates - BFS uses queue space
                if 'walls_and_gates' in content and 'deque' in content:
                    content = re.sub(
                        r'# Space Complexity: O\(1\)',
                        '# Space Complexity: O(m × n)',
                        content
                    )
                    
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    fixed_files.append(file_path)
                    print(f"  Fixed walls and gates: {file_path}")
                    
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
    
    return fixed_files

def fix_max_area_island():
    """Fix max area of island space complexity."""
    fixed_files = []
    
    island_files = [
        "NEETCODE 150/tree/max_area_island.py"
    ]
    
    for file_path in island_files:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Fix max area of island - DFS uses call stack space
                if 'maxAreaOfIsland' in content:
                    content = re.sub(
                        r'# Space Complexity: O\(1\)',
                        '# Space Complexity: O(m × n)',
                        content
                    )
                    
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    fixed_files.append(file_path)
                    print(f"  Fixed max area island: {file_path}")
                    
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
    
    return fixed_files

def main():
    """Main function to run all fixes."""
    print("Starting complexity fixes for remaining incorrect classifications...")
    print(f"Current working directory: {os.getcwd()}")
    
    all_fixed_files = []
    
    print("\n1. Fixing two-pointer algorithms...")
    all_fixed_files.extend(fix_two_pointer_algorithms())
    
    print("\n2. Fixing Dijkstra's algorithm...")
    all_fixed_files.extend(fix_dijkstra_algorithm())
    
    print("\n3. Fixing topological sort...")
    all_fixed_files.extend(fix_topological_sort())
    
    print("\n4. Fixing binary search files...")
    all_fixed_files.extend(fix_binary_search_files())
    
    print("\n5. Fixing tree space complexity...")
    all_fixed_files.extend(fix_tree_space_complexity())
    
    print("\n6. Fixing climbing stairs...")
    all_fixed_files.extend(fix_climbing_stairs())
    
    print("\n7. Fixing maximal rectangle...")
    all_fixed_files.extend(fix_maximal_rectangle())
    
    print("\n8. Fixing walls and gates...")
    all_fixed_files.extend(fix_walls_and_gates())
    
    print("\n9. Fixing max area island...")
    all_fixed_files.extend(fix_max_area_island())
    
    print(f"\n✅ Complexity fixes completed!")
    print(f"📊 Total files updated: {len(all_fixed_files)}")
    
    if all_fixed_files:
        print("\n📝 Updated files:")
        for file_path in all_fixed_files:
            print(f"  - {file_path}")
    else:
        print("\n💡 No files needed complexity updates.")

if __name__ == "__main__":
    main()
