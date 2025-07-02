# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

 

# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1

        # goal is to find inflection point
        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                # Min is to the right
                l = mid + 1
            else:
                # Min is at mid or to the left
                r = mid

        return nums[l]
class Solution:
    # Time Complexity:
    #   Best case: O(1) - binary search
    #   Average case: O(log n)
    #   Worst case: O(log n)
    # Space Complexity: O(1)
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                # Min is to the right
                l = mid + 1
            else:
                # Min is at mid or to the left
                r = mid

        return nums[l]