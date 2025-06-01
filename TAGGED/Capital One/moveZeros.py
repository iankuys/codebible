# Link: https://leetcode.com/problems/move-zeroes/
"""
283. Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
"""
# way better soluton
class Solution:
    # Time Complexity:
    #   Best case: O(n²) - nested iteration
    #   Average case: O(n²)
    #   Worst case: O(n²)
    # Space Complexity: O(1)
    def moveZeroes(self, nums: List[int]) -> None:
        insert_pos = 0

        # Move non-zeroes forward
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1

        # Fill remaining with zeroes
        for i in range(insert_pos, len(nums)):
            nums[i] = 0

# mine but not efficient
class Solution:
    # Time Complexity:
    #   Best case: O(n²) - nested iteration
    #   Average case: O(n²)
    #   Worst case: O(n²)
    # Space Complexity: O(1)
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0

        while (i < len(nums)):
            
            j = i
            if nums[i] == 0:
                while (nums[j] == 0):
                    if j + 1 < len(nums):
                        j += 1
                    # if at the end of the array and everything is still 0? means its completed
                    else:
                        return
                temp = nums[j]
                nums[i] = nums[j]
                nums[j] = 0
            i += 1