"""
3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without duplicate characters.
 
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3
Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dup = {}
        max_len = 0
        start = 0

        for i, char in enumerate(s):
            # we check if the character is already in the dictionary
            # and if its index is greater than or equal to the start index
            # the reason we don't want to update the start if the last duped char is outside of the current window
            # for eg, if abba, when we are at the second b then a, 'ba' is a valid substring, even though a is a duplicate but it
            # is outside of the current substring window
            if char in dup and dup[char] >= start:
                start = dup[char] + 1
            max_len = max(max_len, i - start + 1)
            dup[char] = i

        return max_len