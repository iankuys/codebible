# Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
"""
215. Kth Largest Element in an Array
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""

class Solution:
    # Time Complexity:
    #   Best case: O(n) - linear scan
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(1)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [ -1 * num for num in nums]
        heapq.heapify(heap)

        while k > 0:
            val = heapq.heappop(heap)
            k -= 1

        return -1 * val