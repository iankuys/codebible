# LeetCode Problem 3: https://leetcode.com/problems/
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. 

class Solution:
    # Time Complexity:
    #   Best case: O(n) - linear scan
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(1)
    def lengthOfLongestSubstring(self, s: str) -> int:
        # dictionary for repeating characters
        dictionary = {}
        # array to store all the substrings
        max_len = 0
        start = 0
        
        if len(s) == 0:
            return len(s)
        
        for i, c in enumerate(s):
            if c in dictionary and start <= dictionary[c]:
                # this will set the start of the search from the next char after the last time the same character was found
                start = dictionary[c] + 1
            else:
                max_len = max(max_len, i-start+1)
            
            # instantiate the dictionary or updates the dictionary whenever the same char is found
            dictionary[c] = i
            
        return max_len
            
# 2025 solution
class Solution:
    # Time Complexity:
    #   Best case: O(n) - linear scan
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(1)
    def lengthOfLongestSubstring(self, s: str) -> int:
        repeat = {}
        start = 0
        longest = 0

        for i, char in enumerate(s):
            # need to check repeat[char] >= start to ensure the repeated character is within the current window.
            # case like abba where the last a is in the new window
            if char in repeat and repeat[char] >= start:
                start = repeat[char] + 1
            repeat[char] = i
            longest = max(longest, i - start + 1)
        
        return longest
