"""
198. House Robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""

# DP tables O(n) time, O(1) space
class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0

        N = len(nums)

        # Base case:
        # at the last house, there will be no house left to rob
        # second to last will have one house left to rob
        rob_next_plus_one = 0
        rob_next = nums[N - 1]
        
        for i in range(N - 2, -1, -1):
            # if you rob i + 1 means u cant rob cur house
            # whereas if you rob i + 2 then u can rob cur house
            current = max(rob_next, nums[i] + rob_next_plus_one)

            # Update the variables
            rob_next_plus_one = rob_next
            rob_next = current

        return rob_next

# DP tables O(n) time, O(n) space
class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0

        maxRobbedAmount = [None for _ in range(len(nums) + 1)]
        N = len(nums)

        # Base case:
        # at the last house, there will be no house left to rob
        # second to last will have one house left to rob
        maxRobbedAmount[N], maxRobbedAmount[N - 1] = 0, nums[N - 1]

        for i in range(N - 2, -1, -1):
            # if you rob i + 1 means u cant rob cur house
            # whereas if you rob i + 2 then u can rob cur house
            maxRobbedAmount[i] = max(maxRobbedAmount[i + 1], nums[i] + maxRobbedAmount[i + 2])

        return maxRobbedAmount[0]
    
# Recursion with memoization
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]

            memo[i] = max(dfs(i + 2) + nums[i], dfs(i + 1))
            return memo[i]

        return dfs(0)
