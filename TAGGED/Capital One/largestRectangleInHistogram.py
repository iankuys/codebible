# Link: https://leetcode.com/problems/largest-rectangle-in-histogram/
"""
84. Largest Rectangle in Histogram
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
"""

class Solution:
    # Time Complexity:
    #   Best case: O(n²) - nested iteration
    #   Average case: O(n²)
    #   Worst case: O(n²)
    # Space Complexity: O(1)
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea