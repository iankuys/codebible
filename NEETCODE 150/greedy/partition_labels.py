# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

# Return a list of integers representing the size of these parts.

# Example 1:

# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

# https://leetcode.com/problems/partition-labels/description/
class Solution:
    # Time Complexity:
    #   Best case: O(n²) - nested iteration
    #   Average case: O(n²)
    #   Worst case: O(n²)
    # Space Complexity: O(1)
    def partitionLabels(self, s: str) -> List[int]:
        hmap = {}
        # end tracks whne the last index ends and will partition when end == i
        length = 0
        end = 0
        res = []

        # find the last index of each character
        for i,c in enumerate(s):
            hmap[c] = i

        for i in range(len(s)):
            end = max(end, hmap[s[i]])
            length += 1

            print(end)
            if i == end:
                res.append(length)
                length = 0
        
        return res
                
