# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# Link: https://leetcode.com/problems/product-of-array-except-self/
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# What helped me was imagining a generic example without numbers.
# nums = [a, b, c, d]
# Each item in the list below is the pre and post values ​​multiplied by the list sol in each round.
# pre = [1, 1a, 1ab, 1abc]
# pos = [1bcd, 1cd, 1d, 1]
# Multiplying pre and post item by item:
# pre*pro = [1bcd, 1acd, 1abd, 1abc] -> Solution

from typing import List

class Solution:
    # Time Complexity:
    #   Best case: O(n²) - nested iteration
    #   Average case: O(n²)
    #   Worst case: O(n²)
    # Space Complexity: O(1)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # First pass: calculate product of all elements before the current index
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # Second pass: multiply with product of all elements after the current index
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res

class Solution:
    # Time Complexity:
    #   Best case: O(n²) - nested iteration
    #   Average case: O(n²)
    #   Worst case: O(n²)
    # Space Complexity: O(1)
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # could technically find the product of everything before
        # at every loop
        # so like for [1,2,4,6]
        # it will be like [1,1,2,8]

        # then do it in reverse?
        # so like [48,24,6,1]
        # but then how do we get that? do we reverse the nums?
        #so [6,4,2,1]
        product_before = []
        product_after = []

        for i in range(len(nums)):
            if i == 0:
                product_before.append(1)
            else:
                product_before.append(product_before[i - 1] * nums[i - 1])

        nums_reversed = nums[::-1]
        for j in range(len(nums_reversed)):
            if j == 0:
                product_after.append(1)
            else:
                product_after.append(product_after[j-1] * nums_reversed[j- 1])
        product_after = product_after[::-1]

        res = []
        for k in range(len(product_before)):
            res.append(product_before[k] * product_after[k])
        
        return res
        
