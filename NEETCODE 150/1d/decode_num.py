# A message containing letters from A-Z can be encoded into numbers using the following mapping:
# Link: https://leetcode.com/problems/decode-ways/

# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

# Given a string s containing only digits, return the number of ways to decode it.

# The test cases are generated so that the answer fits in a 32-bit integer.

# Example 1:

# Input: s = "12"
# Output: 2
# Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

class Solution:
    # Time Complexity:
    #   Best case: O(n) - linear operation
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(1)
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}  # base case: empty string has 1 valid decoding

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0  # cannot decode strings starting with 0

            # Try decoding one character
            res = dfs(i + 1)

            # Try decoding two characters if valid (10-26)
            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                res += dfs(i + 2)

            dp[i] = res
            return res

        return dfs(0)