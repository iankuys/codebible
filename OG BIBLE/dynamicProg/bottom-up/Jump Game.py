# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.
# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        # Initialize a boolean array to store whether each index is reachable
        reachable = [False] * n
        reachable[0] = True

        for i in range(1, n):
            # Check if any previous reachable index can reach the current index
            for j in range(i - 1, -1, -1):
                if reachable[j] and j + nums[j] >= i:
                    reachable[i] = True
                    break

        return reachable[n - 1]
