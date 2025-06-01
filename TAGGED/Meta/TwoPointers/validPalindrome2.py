# Link: https://leetcode.com/problems/valid-palindrome-ii/
"""
680. Valid Palindrome II
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:
Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
"""

class Solution:
    # Time Complexity:
    #   Best case: O(n) - linear operation
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(1)
    def validPalindrome(self, s: str) -> bool:
        
        def checkPalindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        i = 0
        j = len(s) - 1

        # For our purposes, we can basically pretend that matched characters no longer exist. 
        # For example, after verifying that the first and last characters of 'racecar' match, 
        # we can reframe the problem as checking if 'aceca' can be a palindrome with at most one deletion.
        while i < j:
            if s[i] != s[j]:
                return checkPalindrome(s, i + 1, j) or checkPalindrome(s, i, j - 1)
            i += 1
            j -= 1

        return True