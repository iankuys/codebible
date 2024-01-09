# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.
# Example 1:

# Input: nums = [2,2,1]
# Output: 1
# https://leetcode.com/problems/single-number/description/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR solution since Xor of any two num gives the difference of bit as 1 and same bit as 0.
        # Thus, using this we get 1 ^ 1 == 0 because the same numbers have same bits.
        xor = 0
        for num in nums:
            xor ^= num

        return xor