class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        result = ""
        for i in range(len(s)):
            # detect odd and even and find the longest of them all
            result = max(self.detectPalindrome(s,i,i), self.detectPalindrome(s,i,i+1), result, key=len)
        
        return result
            
    def detectPalindrome(self, s, l, r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        
        return s[l+1:r]
            