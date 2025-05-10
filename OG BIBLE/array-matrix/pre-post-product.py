# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
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

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sol = [1] * n
        pre = 1
        post = 1 

        for i in range(n):
            sol[i] *= pre
            pre *= nums[i]
            sol[n - i - 1] *= post
            post = post * nums[n - i -1]
        return sol