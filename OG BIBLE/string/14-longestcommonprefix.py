# LeetCode Problem 14: https://leetcode.com/problems/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for i in range(len(strs)):
            # or checks only if one side is True so strs[i].index will not throw an exception
            while(prefix not in strs[i] or strs[i].index(prefix) != 0):
                prefix = prefix[0:len(prefix)-1]
                if len(prefix) == 0:
                    return ""
        return prefix