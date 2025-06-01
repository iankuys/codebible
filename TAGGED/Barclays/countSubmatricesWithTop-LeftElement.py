# Link: https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-equals-k/
"""
3070. Count Submatrices with Top-Left Element and Sum Less Than Equals k
You are given a 0-indexed integer matrix grid and an integer k.

Return the number of submatrices that contain the top-left element of the grid, and have a sum less than or equal to k.

Example 1:
Input: grid = [[7,6,3],[6,6,1]], k = 18
Output: 4
Explanation: There are only 4 submatrices, shown in the image above, that contain the top-left element of grid, and have a sum less than or equal to 18.
"""

class Solution:
    # Time Complexity:
    #   Best case: O(n²) - nested iteration
    #   Average case: O(n²)
    #   Worst case: O(n²)
    # Space Complexity: O(1)
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0

        for i in range(m):
            for j in range(n):
                # Add the prefix sum of the cell just above and left to it.
                # Subtract the prefix sum of the cell on the top-left diagonal cell. 
                # We do this because we have added this prefix sum in each of the top and left cell of the given cell. 
                # Therefore, we have to subtract it once.
                if i > 0:
                    grid[i][j] += grid[i - 1][j]
                if j > 0:
                    grid[i][j] += grid[i][j - 1]
                if i > 0 and j > 0:
                    grid[i][j] -= grid[i - 1][j - 1]

        for i in range(m):
            for j in range(n):
                if grid[i][j] <= k:
                    count += 1

        return count

