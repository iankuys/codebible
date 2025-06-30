"""
42. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
"""
# Two Pointers
class Solution:
    def trap(self, height):
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        res = 0

        while (left < right):
            # if the height on the left is lower
            # explore left since there could be a valley
            # whichever direction with the shortest bound will be the bound of valley
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                res += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                res += right_max - height[right]
                right -= 1

        return res
    
# DP because we use the last max height from left and right to calculate the water trapped at each index.
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        ans = 0
        size = len(height)

        left_max, right_max = [0] * size, [0] * size
        # Initialize first height into left max
        left_max[0] = height[0]

        for i in range(1, size):
            # update left max with current max
            left_max[i] = max(height[i], left_max[i - 1])

        # Initialize last height into right max
        right_max[size - 1] = height[size - 1]

        for i in range(size - 2, -1, -1):
            # update right max with current max
            right_max[i] = max(height[i], right_max[i + 1])

        # Calculate the trapped water
        for i in range(1, size - 1):
            ans += min(left_max[i], right_max[i]) - height[i]

        return ans

# Stack
class Solution:
    def trap(self, height):
        ans = 0                 # Final result: total trapped water
        current = 0             # Pointer to iterate over 'height'
        st = []                 # Monotonic stack to store indices

        while current < len(height):
            # Essentially everytime we found some bigger than the last height, there could be a valley
            while len(st) != 0 and height[current] > height[st[-1]]:
                top = st[-1]         # Index of the last element in the stack (potential "valley")
                st.pop()
                
                if len(st) == 0:
                    break            # No left boundary, can't trap water

                # Calculate the distance between current and the new top
                distance = current - st[-1] - 1
                
                # Find the bounded height, the top will be the height of the valley
                # current height is right boundary and st[-1] is the left boundary
                bounded_height = min(height[current], height[st[-1]]) - height[top]
                
                # Accumulate trapped water
                ans += distance * bounded_height

            st.append(current)       # Push current index to stack
            current += 1             # Move forward

        return ans


# Brute Force Solution
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        size = len(height)
        memo = {}

        for i in range(1, size - 1):

            left = 0
            right = 0

            for j in range(i, -1, -1):
                left = max(left, height[j]) 
            for j in range(i, size):
                right = max(right, height[j])

            ans += min(left, right) - height[i]
        
        return ans