# 97. Interleaving String
# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

# An interleaving of two strings s and t is a configuration where s and t are divided into n and m 
# substrings
#  respectively, such that:

# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...

# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# Explanation: One way to obtain s3 is:
# Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
# Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
# Since s3 can be obtained by interleaving s1 and s2, we return true.
# https://leetcode.com/problems/interleaving-string/description/

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True 

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
            
        return dp[0][0]
    
# memoization solution
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        cache = {}
        if len(s1) + len(s2) != len(s3):
            return False 
            
        def dfs(i, j):
            if i >= len(s1) and j >= len(s2):
                return True
            
            if (i, j) in cache:
                return cache[(i, j)]
            # i + j is the third pointer for s3
            if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
                return True
            
            if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
                return True

            cache[(i, j)] = False
            return False

        return dfs(0, 0)

