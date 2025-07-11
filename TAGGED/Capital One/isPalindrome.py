# Link: https://leetcode.com/problems/palindrome-number/
"""
9. Palindrome Number
Solved
Easy
Topics
Companies
Hint
Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""

class Solution:
    # Time Complexity:
    #   Best case: O(n) - linear operation
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(1)
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]