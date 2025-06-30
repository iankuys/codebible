"""
34. Find First and Last Position of Element in Sorted Array
Solved
Medium
Topics
conpanies icon
Companies
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
"""

# more intuitive solution, find the left most index and right most index of the target using binary search
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeftMostIndex():
            left, right = 0, len(nums) - 1
            leftMostIndex = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    leftMostIndex = mid
                    right = mid - 1
            return leftMostIndex

        def findRightMostIndex():
            left, right = 0, len(nums) - 1
            rightMostIndex = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    rightMostIndex = mid
                    left = mid + 1
            return rightMostIndex

        return [findLeftMostIndex(), findRightMostIndex()]

# mine but less intuitive essentially the left and right bound have to be on top of the target to find the first and last index
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def findLeft():
            left = 0
            right = len(nums) - 1

            while (left <= right):
                mid = (left + right) // 2

                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return left

        def findRight():
            left = 0
            right = len(nums) - 1

            while (left <= right):
                mid = (left + right) // 2

                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return right

        leftIdx, rightIdx = findLeft(), findRight()

        if leftIdx <= rightIdx:
            return [leftIdx, rightIdx]
        else:
            return [-1, -1]