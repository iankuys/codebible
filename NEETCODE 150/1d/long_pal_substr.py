# Given a string s, return the longest 
# palindromic
 
# substring
#  in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        result = ""
        for i in range(len(s)):
            # detect odd and even
            result = max(self.detectPalindrome(s,i,i), self.detectPalindrome(s,i,i+1), result, key=len)
        
        return result
            
        
    def detectPalindrome(self, s, l, r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        
        return s[l+1:r]
            