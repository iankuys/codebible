# Link: https://leetcode.com/problems/two-sum/
"""
1. Two Sum
Solved
Easy
Topics
Companies
Hint
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

class Solution:
    # Time Complexity:
    #   Best case: O(n) - linear scan
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(1)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            sub = target - num
            if sub not in hashmap:
                hashmap[num] = i
            else:
                return [i, hashmap[sub]]