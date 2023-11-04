#Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
# conditions for an island to exist, top down left right are land
# once we have neighbors that are not 1 then we stop
# boundary conditions are the length of the grid and each element

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    self.dfs(grid, i ,j)
        return count

    def dfs(self, grid, row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == "0":
            return 

        grid[row][col] = "0"

        self.dfs(grid, row, col+1)
        self.dfs(grid, row, col-1)
        self.dfs(grid, row+1, col)
        self.dfs(grid, row-1, col)