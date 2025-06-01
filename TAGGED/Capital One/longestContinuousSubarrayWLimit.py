# Link: https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
"""
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
Attempted
Medium
Topics
Companies
Hint
Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

 

Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2 
Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.
"""

# Leetcode min Heap max Heap
class Solution:
    def longestSubarray(self, nums, limit):
        max_heap = []
        min_heap = []

        left = 0
        max_length = 0

        for right in range(len(nums)):
            heapq.heappush(max_heap, (-nums[right], right))
            heapq.heappush(min_heap, (nums[right], right))

            # Check if the absolute difference between the maximum and minimum values in the current window exceeds the limit
            while -max_heap[0][0] - min_heap[0][0] > limit:
                # Move the left pointer to the right until the condition is satisfied.
                # This ensures we remove the element causing the violation
                left = min(max_heap[0][1], min_heap[0][1]) + 1

                # Remove elements from the heaps that are outside the current window
                while max_heap[0][1] < left:
                    heapq.heappop(max_heap)
                while min_heap[0][1] < left:
                    heapq.heappop(min_heap)

            # Update max_length with the length of the current valid window
            max_length = max(max_length, right - left + 1)

        return max_length
    
# Leetcode 2 dequeus
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = deque()
        min_deque = deque()
        left = 0
        max_length = 0

        for right in range(len(nums)):
            # Maintain the max_deque in decreasing order
            while max_deque and max_deque[-1] < nums[right]:
                max_deque.pop()
            max_deque.append(nums[right])

            # Maintain the min_deque in increasing order
            while min_deque and min_deque[-1] > nums[right]:
                min_deque.pop()
            min_deque.append(nums[right])

            # Check if the current window exceeds the limit
            while max_deque[0] - min_deque[0] > limit:
                # Remove the elements that are out of the current window
                if max_deque[0] == nums[left]:
                    max_deque.popleft()
                if min_deque[0] == nums[left]:
                    min_deque.popleft()
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
    
# NOT WORKING
# mine 55 / 63 testcases passed :( 
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        length = 0
        memo = {}

        def dfs(i, j, maximum, minimum):
            nonlocal length
            if i == len(nums):
                return
            maximum = max(maximum, nums[j])
            minimum = min(minimum, nums[j])
            abs_diff = abs(maximum - minimum)
            
            if abs_diff <= limit:
                length = max(length, j - i + 1)

            if j + 1 < len(nums):
                j += 1
                dfs(i, j, maximum, minimum)
            else:
                i += 1
                j = i
                dfs(i, j, 0, float('infinity'))

        dfs(0, 0, 0, float('infinity'))

        return length