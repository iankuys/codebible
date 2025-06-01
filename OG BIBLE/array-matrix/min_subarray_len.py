# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.


class Solution:
    # Time Complexity:
    #   Best case: O(n) - linear scan
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(1)
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_len = float('inf')
        window_start = 0
        window_sum = 0

        for window_end in range(n):
            window_sum += nums[window_end]

            while window_sum >= target:
                min_len = min(min_len, window_end - window_start + 1)
                window_sum -= nums[window_start]
                window_start += 1

        return 0 if min_len == float('inf') else min_len

from typing import List

# my own solution but doesnt work
class Solution:
    # Time Complexity:
    #   Best case: O(n) - linear scan
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(1)
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_len = 99999999
        memo = {}

        for i in range(n):
            result = self.dfs(nums, target, i, 0, memo)
            if result != -1:
                min_len = min(min_len, result)

        return 0 if min_len == 99999999 else min_len

    def dfs(self, nums, target, index, depth, memo):
        if (index, target) in memo:
            return memo[(index, target)]
        if target <= 0:
            return depth
        if index >= len(nums):
            return -1

        memo[(index, target)] = self.dfs(nums, target - nums[index], index + 1, depth + 1, memo)

        return memo[(index, target)]