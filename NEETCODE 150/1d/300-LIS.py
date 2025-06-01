# LeetCode Problem 300: https://leetcode.com/problems/
#Given an integer array nums, return the length of the longest strictly increasing 
# subsequence.
# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

class Solution:
    # Time Complexity:
    #   Best case: O(n²) - nested iteration
    #   Average case: O(n²)
    #   Worst case: O(n²)
    # Space Complexity: O(1)
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        
        for i in range(len(nums)-1, -1,-1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1+LIS[j])
                    
        return max(LIS)