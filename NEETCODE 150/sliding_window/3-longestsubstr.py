# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. 

class Solution:
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
            