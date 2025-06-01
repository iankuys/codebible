# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# Link: https://leetcode.com/problems/valid-anagram/

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

class Solution:
    # Time Complexity:
    #   Best case: O(n log n) - sorting operation
    #   Average case: O(n log n)
    #   Worst case: O(n log n)
    # Space Complexity: O(1)
    def isAnagram(self, s: str, t: str) -> bool:
        
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        return sorted_s == sorted_t