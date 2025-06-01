# Given a string s, return the number of palindromic substrings in it.

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
        