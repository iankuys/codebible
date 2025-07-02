# Given a string s, return the number of palindromic substrings in it.
# Link: https://leetcode.com/problems/palindromic-substrings/

# A string is a palindrome when it reads the same backward as forward.

# A substring is a contiguous sequence of characters within the string.

# Example 1:

# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:

# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

# Soln : same as longest palindromic string, each char in str as middle and expand outwards, do same for pali of even len; maybe read up on manachers alg

class Solution:
    # Time Complexity:
    #   Best case: O(n) - linear scan
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(1)
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            r = l = i

            while l >= 0 and r < len(s) and s[r] == s[l]:
                res += 1
                l -= 1
                r += 1
            
            l = i
            r = i + 1
            
            while l >= 0 and r < len(s) and s[r] == s[l]:
                res += 1
                l -= 1
                r += 1
            
        return res

# Dynamic Programming Approach
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0

        if n == 0:
            return ans

        dp = [[0 for _ in range(n)] for _ in range(n)]

        # Base case: single letter substr
        for i in range(n):
            dp[i][i] = True
            ans += dp[i][i]

        # Base case: double letter substr
        for i in range(n - 1):
            dp[i][i + 1] = (s[i] == s[i + 1])
            ans += dp[i][i + 1]

        # All other cases: substrings of length 3 to n
        for length in range(3, n + 1):  # lengths from 3 to n
            for i in range(n - length + 1):  # ensure j < n
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans += 1

        return ans

        