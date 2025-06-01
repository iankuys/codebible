# Link: https://leetcode.com/problems/binary-search/
# 704. Binary Search
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.
from typing import List

class Solution:
    # Time Complexity:
    #   Best case: O(1) - binary search
    #   Average case: O(log n)
    #   Worst case: O(log n)
    # Space Complexity: O(1)
    def search(self, nums: List[int], target: int) -> int:
        
        high = len(nums) - 1
        low = 0
        mid = 0
        while (low <= high):
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
          return -1

class Solution:
    # Time Complexity:
    #   Best case: O(1) - binary search
    #   Average case: O(log n)
    #   Worst case: O(log n)
    # Space Complexity: O(1)
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1

        while (left <= right):
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
            
        return -1