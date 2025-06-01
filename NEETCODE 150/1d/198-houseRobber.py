# LeetCode Problem 198: https://leetcode.com/problems/
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

class Solution:
    def rob(self, nums: List[int]) -> int:
        largest = [0] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            largest[i] = nums[i]
            for j in range(i+2, len(nums)):
                if largest[j] != nums[j]:
                    largest[i] = max(largest[i], nums[i]+largest[j])
                else:
                    largest[i] = max(largest[i], nums[i]+nums[j])
        
        return max(largest)
