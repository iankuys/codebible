# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.
class Solution:
    # Time Complexity:
    #   Best case: O(1) - binary search
    #   Average case: O(log n)
    #   Worst case: O(log n)
    # Space Complexity: O(1)
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        max_area = 0
        left = 0
        right = n-1
        while left < right:
            width = right - left
            h = min(height[left], height[right])
            max_area = max(max_area, width * h)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
    
class Solution:
    # Time Complexity:
    #   Best case: O(1) - binary search
    #   Average case: O(log n)
    #   Worst case: O(log n)
    # Space Complexity: O(1)
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        area = 0

        while (i < j):
            cur = min(heights[i], heights[j]) * (j - i)
            area = max(area, cur)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
                
        return area
