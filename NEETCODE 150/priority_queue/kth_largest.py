# Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
# 215. Kth Largest Element in an Array
# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?
# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        reveresed_arr = [-1 * num for num in nums]
        heapq.heapify(reveresed_arr)

        while k > 0:
            value = heapq.heappop(reveresed_arr)
            k -= 1

        return -1 * value