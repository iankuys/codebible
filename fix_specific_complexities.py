#!/usr/bin/env python3

import os
import re
from typing import List

def fix_house_robber_files():
    """Fix house robber files that incorrectly show O(n²) instead of O(n)."""
    fixed_files = []
    
    # Files to check
    house_robber_files = [
        "NEETCODE 150/1d/198-houseRobber.py",
        "OG BIBLE/dynamicProg/1d/198-houseRobber.py"
    ]
    
    for file_path in house_robber_files:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Check if this uses inefficient O(n²) nested loop approach
                if 'for j in range(i+2, len(nums))' in content:
                    # This is indeed O(n²) - keep as is but fix description
                    content = content.replace(
                        '# Time Complexity:\n#   Best case: O(n²) - nested iteration\n#   Average case: O(n²)\n#   Worst case: O(n²)',
                        '# Time Complexity:\n#   Best case: O(n²) - inefficient nested loop approach\n#   Average case: O(n²)\n#   Worst case: O(n²)'
                    )
                    if content != original_content:
                        print(f"  Updated description for inefficient house robber: {file_path}")
                
                # Check for standard DP approach that should be O(n)
                elif ('dp[i] = max(dp[i-1], dp[i-2]' in content or 
                      'rob1, rob2 = ' in content or 
                      'prev1, prev2' in content):
                    content = content.replace(
                        '# Time Complexity:\n#   Best case: O(n²) - nested iteration\n#   Average case: O(n²)\n#   Worst case: O(n²)',
                        '# Time Complexity:\n#   Best case: O(n) - linear DP\n#   Average case: O(n)\n#   Worst case: O(n)'
                    )
                    if content != original_content:
                        print(f"  Fixed standard house robber DP: {file_path}")
                
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    fixed_files.append(file_path)
                        
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
    
    return fixed_files

def fix_coin_change_files():
    """Fix coin change files with incorrect complexity."""
    fixed_files = []
    
    coin_change_files = [
        "OG BIBLE/dynamicProg/322-coinchange2.py"
    ]
    
    for file_path in coin_change_files:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Fix coin change complexity
                content = content.replace(
                    '# Time Complexity:\n#   Best case: O(n²) - nested iteration\n#   Average case: O(n²)\n#   Worst case: O(n²)',
                    '# Time Complexity:\n#   Best case: O(amount × coins) - DP with nested loops\n#   Average case: O(amount × coins)\n#   Worst case: O(amount × coins)'
                )
                
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    fixed_files.append(file_path)
                    print(f"  Fixed coin change complexity: {file_path}")
                        
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
    
    return fixed_files

def fix_palindrome_files():
    """Fix longest palindromic substring files."""
    fixed_files = []
    
    palindrome_files = [
        "NEETCODE 150/1d/long_pal_substr.py"
    ]
    
    for file_path in palindrome_files:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Fix expand-around-center palindrome complexity
                if 'detectPalindrome' in content and 'while l>=0 and r<len(s)' in content:
                    content = content.replace(
                        '# Time Complexity:\n#   Best case: O(n) - linear scan\n#   Average case: O(n)\n#   Worst case: O(n)',
                        '# Time Complexity:\n#   Best case: O(n) - all characters same\n#   Average case: O(n²)\n#   Worst case: O(n²)'
                    )
                    
                    if content != original_content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(content)
                        fixed_files.append(file_path)
                        print(f"  Fixed palindrome expand-around-center: {file_path}")
                        
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
    
    return fixed_files

def fix_consecutive_sequence_space():
    """Fix longest consecutive sequence space complexity."""
    fixed_files = []
    
    consecutive_files = [
        "NEETCODE 150/array/longestConsecutiveSub.py"
    ]
    
    for file_path in consecutive_files:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Fix space complexity - uses hash set
                if 'set(nums)' in content or 'unique_nums = set' in content:
                    content = content.replace(
                        '# Space Complexity: O(1)',
                        '# Space Complexity: O(n)'
                    )
                    
                    if content != original_content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(content)
                        fixed_files.append(file_path)
                        print(f"  Fixed consecutive sequence space complexity: {file_path}")
                        
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
    
    return fixed_files

def main():
    print("Fixing specific algorithm complexity errors...")
    
    all_fixed = []
    
    # Fix different categories
    all_fixed.extend(fix_house_robber_files())
    all_fixed.extend(fix_coin_change_files())  
    all_fixed.extend(fix_palindrome_files())
    all_fixed.extend(fix_consecutive_sequence_space())
    
    print(f"\nFixed {len(all_fixed)} files with incorrect complexity analysis:")
    for file_path in all_fixed:
        print(f"  - {file_path}")
    
    if not all_fixed:
        print("No files needed complexity fixes.")

if __name__ == "__main__":
    main()
