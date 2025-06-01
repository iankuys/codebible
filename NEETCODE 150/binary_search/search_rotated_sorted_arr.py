from typing import List
# 33. Search in Rotated Sorted Array
# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.
# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

# 2025 solution
class Solution:
    # Time Complexity:
    #   Best case: O(1) - target found immediately
    #   Average case: O(log n)
    #   Worst case: O(log n)
    # Space Complexity: O(1)
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        # base case if last actually bigger than first O(1) then its not rotated?
        if nums[right] > nums[left]:
            return nums[left]

        # get first and last element to do soemthing?
        # binary search then compare the value to first or last
        while (left < right):
            mid = (left + right) // 2

            # its in the left half of the array
            if nums[mid] < nums[right]:
                right = mid
            # its on the right half of the array
            elif nums[mid] > nums[right]:
                left = mid + 1
            
        return nums[left]

class Solution:
    # Time Complexity:
    #   Best case: O(1) - target found immediately  
    #   Average case: O(log n)
    #   Worst case: O(log n)
    # Space Complexity: O(1)
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while l <= r:

            m = (l + r) // 2
            
            if target == nums[m]:
                return m
                
            # if target > nums[r] then we look at the left hand side
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            # if target < nums[r] then we look at the right hand side
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1

