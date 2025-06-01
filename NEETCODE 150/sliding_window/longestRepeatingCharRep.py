# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
# Link: https://leetcode.com/problems/longest-repeating-character-replacement/

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.


# brute force first then optimize it
class Solution:
    # Time Complexity:
    #   Best case: O(n) - linear scan
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(1)
    def characterReplacement(self, s: str, k: int) -> int:

        # every window look for the most common char, replace the chars with the most common
        # window size? would it be a sliding window that checks for the most common char 
        # in every interval then it adds the k value? 
        # SHRINK THE WINDOW
        count = {}
        res = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            # get most frequent char found and deduct the window to check if k fits
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
    
# more efficient
class Solution:
    # Time Complexity:
    #   Best case: O(n) - linear scan
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(1)
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {}
        res = 0

        l = 0
        maxf = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0) # if char doesnt exist just return default value of 0 (SMART)
            maxf = max(maxf, count[s[r]]) 
            
            while (r - l + 1) - maxf > k: # SMART as well LOL
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        
        return res