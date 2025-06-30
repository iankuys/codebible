"""
560. Subarray Sum Equals K
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = { 0: 1 }
        roll_sum = 0
        res = 0

        for i, num in enumerate(nums):
            roll_sum += num
            diff = roll_sum - k

            if diff in hashmap:
                res += hashmap[diff]
            
            hashmap[roll_sum] = 1 + hashmap.get(roll_sum, 0)

        return res