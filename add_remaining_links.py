#!/usr/bin/env python3
"""
Script to add LeetCode links to remaining files based on problem titles and patterns.
"""

import os
import re
from pathlib import Path

# Map common file names to their LeetCode problem URLs
PROBLEM_MAPPING = {
    # 1D DP problems
    'climbingstairs.py': 'https://leetcode.com/problems/climbing-stairs/',
    'canPartition.py': 'https://leetcode.com/problems/partition-equal-subset-sum/',
    'count_pal_substr.py': 'https://leetcode.com/problems/palindromic-substrings/',
    'decode_num.py': 'https://leetcode.com/problems/decode-ways/',
    'houseRobber2.py': 'https://leetcode.com/problems/house-robber-ii/',
    'long_pal_substr.py': 'https://leetcode.com/problems/longest-palindromic-substring/',
    'min_cost_climbingStairs.py': 'https://leetcode.com/problems/min-cost-climbing-stairs/',
    'palindromicSubstr.py': 'https://leetcode.com/problems/palindromic-substrings/',
    'subArraySum.py': 'https://leetcode.com/problems/subarray-sum-equals-k/',
    'wordBreak.py': 'https://leetcode.com/problems/word-break/',
    'buySellStockWCooldown.py': 'https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/',
    'edit_dist.py': 'https://leetcode.com/problems/edit-distance/',
    'findTargetSum.py': 'https://leetcode.com/problems/target-sum/',
    'longestComSubsq.py': 'https://leetcode.com/problems/longest-common-subsequence/',
    'uniquePath.py': 'https://leetcode.com/problems/unique-paths/',
    
    # Array problems
    'anagram.py': 'https://leetcode.com/problems/valid-anagram/',
    'containsdup.py': 'https://leetcode.com/problems/contains-duplicate/',
    'group_anagrams.py': 'https://leetcode.com/problems/group-anagrams/',
    'longestConsecutiveSub.py': 'https://leetcode.com/problems/longest-consecutive-sequence/',
    'productExceptSelf.py': 'https://leetcode.com/problems/product-of-array-except-self/',
    'topkfreq.py': 'https://leetcode.com/problems/top-k-frequent-elements/',
    'twosum.py': 'https://leetcode.com/problems/two-sum/',
    'validSudoku.py': 'https://leetcode.com/problems/valid-sudoku/',
    
    # Backtracking
    'permutation.py': 'https://leetcode.com/problems/permutations/',
    
    # Binary Search
    'find_min_rotated_arr.py': 'https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/',
    
    # Graph problems
    'numberOfIslands.py': 'https://leetcode.com/problems/number-of-islands/',
    'pacific_alantic_flow.py': 'https://leetcode.com/problems/pacific-atlantic-water-flow/',
    'surrounded_regions.py': 'https://leetcode.com/problems/surrounded-regions/',
    
    # Greedy
    'hands_of_straight.py': 'https://leetcode.com/problems/hand-of-straights/',
    'jumpgame.py': 'https://leetcode.com/problems/jump-game/',
    
    # Intervals
    'insertInterval.py': 'https://leetcode.com/problems/insert-interval/',
    
    # Sliding Window
    'longestRepeatingCharRep.py': 'https://leetcode.com/problems/longest-repeating-character-replacement/',
    
    # Stack
    'daily_temperature.py': 'https://leetcode.com/problems/daily-temperatures/',
    'generate_parantheses.py': 'https://leetcode.com/problems/generate-parentheses/',
    'reverse_polish.py': 'https://leetcode.com/problems/evaluate-reverse-polish-notation/',
    
    # Tree
    'balancedtree.py': 'https://leetcode.com/problems/balanced-binary-tree/',
    'count_good_nodes.py': 'https://leetcode.com/problems/count-good-nodes-in-binary-tree/',
    'diameterBtree.py': 'https://leetcode.com/problems/diameter-of-binary-tree/',
    'lca.py': 'https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/',
    'maxDedpthBTree.py': 'https://leetcode.com/problems/maximum-depth-of-binary-tree/',
    'max_area_island.py': 'https://leetcode.com/problems/max-area-of-island/',
    'same_tree.py': 'https://leetcode.com/problems/same-tree/',
    
    # Two Pointers
    '2sum_array_sorted.py': 'https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/',
    '3sum.py': 'https://leetcode.com/problems/3sum/',
    'containerWMostWater.py': 'https://leetcode.com/problems/container-with-most-water/',
    'trap.py': 'https://leetcode.com/problems/trapping-rain-water/',
    'validpalindrome.py': 'https://leetcode.com/problems/valid-palindrome/',
    
    # Matrix problems
    'setzeroes.py': 'https://leetcode.com/problems/set-matrix-zeroes/',
    'rotate-matrix.py': 'https://leetcode.com/problems/rotate-image/',
    'set-matrix-zero.py': 'https://leetcode.com/problems/set-matrix-zeroes/',
    
    # Linked List
    'linked_list.py': 'https://leetcode.com/problems/reverse-linked-list/',
    'rotate_list.py': 'https://leetcode.com/problems/rotate-list/',
    
    # String
    'palindrome.py': 'https://leetcode.com/problems/valid-palindrome/',
    
    # Tree specific
    'rangeSumBST.py': 'https://leetcode.com/problems/range-sum-of-bst/',
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

def process_remaining_files():
    """Process files that still need LeetCode links."""
    base_path = Path("c:/Users/ianku/Projects/codebible")
    
    added_count = 0
    processed_count = 0
    
    for filename, url in PROBLEM_MAPPING.items():
        # Find files matching this name pattern
        matching_files = list(base_path.glob(f"**/{filename}"))
        
        for filepath in matching_files:
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check if it has class Solution (LeetCode file)
                if 'class Solution' in content:
                    processed_count += 1
                    if add_link_to_file(str(filepath), url):
                        print(f"✓ Added link to {filepath}")
                        added_count += 1
                    else:
                        print(f"- {filepath} already has link")
                        
            except Exception as e:
                print(f"Error reading {filepath}: {e}")
    
    print(f"\nSummary: Processed {processed_count} files, added links to {added_count} files")

if __name__ == "__main__":
    process_remaining_files()
