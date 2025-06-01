# Link: https://leetcode.com/problems/maximum-subarray/
"""
53. Maximum Subarray
Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = max_sum = nums[0]

        for num in nums[1:]:
            # track the current sum, if the current number if higher than the previous sum, we move on
            cur_sum = max(num, cur_sum + num)
            # track the sum of the max_sum, if the current sum is smaller than max_sum, replace max_sum
            max_sum = max(max_sum, cur_sum)

        return max_sum

        