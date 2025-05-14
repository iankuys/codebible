"""
200. Number of Islands
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Time Complexity: O(m * n)
Every cell in the grid is visited once.

The dfs function only recurses into cells that are '1' and haven't been marked yet.

Since each cell is marked as 'x' the first time it's visited, and never visited again, the total number of recursive DFS calls across the entire grid is bounded by m * n.
"""
# MINE Accepted 49 / 49 testcases passed
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = {}
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            if i >= m or j >= n or i < 0 or j < 0:
                return
            if grid[i][j] == "0" or grid[i][j] == "x":
                return

            grid[i][j] = "x"
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1

        return count