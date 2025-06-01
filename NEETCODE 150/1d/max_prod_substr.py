# Link: https://leetcode.com/problems/maximum-product-subarray/
# 152. Maximum Product Subarray

# Given an integer array nums, find a 
# subarray
#  that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.
# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

class Solution:
    # Time Complexity:
    #   Best case: O(n) - linear scan
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(1)
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        minCur, maxCur = 1, 1 # min is for negative numbers

        for n in nums:
            if n == 0:
                minCur, maxCur = 1, 1
                continue
            tmp = maxCur * n
            maxCur = max(maxCur * n, minCur * n, n)
            minCur = min(tmp, minCur * n, n)
            res = max(maxCur, res)

        return res