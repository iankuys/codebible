from typing import List

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        array = []

        for i in range(len(grid[0])):
            array.append(self.dfs(grid, 0, i))

        return array
    
    def dfs(self, grid, r, c):

        if (r == len(grid)):
            return c
        nextCol = c + grid[r][c]
        if (nextCol < 0 or nextCol > len(grid[0]) - 1 or grid[r][c] != grid[r][nextCol]):
            return -1

        return self.dfs(grid, r+1, nextCol)

# my solution
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        array = []

        for i in range(len(grid[0])):
            array.append(self.dfs(grid, 0, i, False))

        return array
    
    def dfs(self, grid, r, c, isOpp):

        if (r == len(grid)):
            return c
        # ball cant go anywhere when its "\" and next to wall
        if grid[r][c] == 1 and c == len(grid[0]) - 1:
            return -1
        # ball cant go anywhere when its "/" and next to wall
        if grid[r][c] == -1 and c == 0:
            return -1
        # ball cant go anywhere when its "\/" and next to wall
        if (grid[r][c] == 1 and grid[r][c+1] == -1):
            return -1
        # ball cant go anywhere when its "/\" and next to wall
        if (grid[r][c] == -1 and grid[r][c-1] == 1):
            return -1

        if grid[r][c] == 1:
            return self.dfs(grid, r+1, c+1, False)
        else:
            return self.dfs(grid, r+1, c-1, True)

obj = Solution()
matrix = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]

print(obj.findBall(matrix))