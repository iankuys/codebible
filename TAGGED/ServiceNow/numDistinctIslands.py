"""
694. Number of Distinct Islands
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Return the number of distinct islands.

Example 1:
Input: grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
Output: 1

Example 2:
Input: grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
Output: 3
"""

# my dfs
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        def dfs(i, j):
            if i >= m or j >= n or i < 0 or j < 0:
                return
            if grid[i][j] == 0:
                return
            if (i, j) in seen:
                return

            seen[(i, j)] = 1
            current_island.append((i - row_origin, j - col_origin))
            dfs(i, j + 1)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i - 1, j)

        m = len(grid)
        n = len(grid[0])
        seen = {}
        unique_islands = []

        for r in range(m):
            for c in range(n):
                if grid[r][c] != 0 and (r, c) not in seen:
                    current_island = []
                    row_origin = r
                    col_origin = c
                    dfs(r, c)
                    if not current_island or current_island in unique_islands:
                        continue
                    unique_islands.append(current_island)

        return len(unique_islands)

# super efficient tried arriving to this but copied from someone
class Solution:
    def numDistinctIslands(self, grid):
        islands = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    islands.add(self.dfs(grid, i, j, "s"))

        return len(islands)

    def dfs(self, g, i, j, path):
        if i < 0 or j < 0 or i >= len(g) or j >= len(g[i]) or g[i][j] == 0:
            return ""

        g[i][j] = 0

        # "u", "d", etc. suffixes: Marks that you're backtracking from a move.
        return path \
               + self.dfs(g, i+1, j, "d") + "u" \
               + self.dfs(g, i-1, j, "u") + "d" \
               + self.dfs(g, i, j+1, "r") + "l" \
               + self.dfs(g, i, j-1, "l") + "r"
    
# frozen set with dfs
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        def dfs(i, j):
            if i >= m or j >= n or i < 0 or j < 0:
                return
            if grid[i][j] == 0:
                return
            if (i, j) in seen:
                return

            seen[(i, j)] = 1
            current_island.add((i - row_origin, j - col_origin))
            dfs(i, j + 1)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i - 1, j)

        m = len(grid)
        n = len(grid[0])
        seen = {}
        unique_islands = set()

        for r in range(m):
            for c in range(n):
                if grid[r][c] != 0 and (r, c) not in seen:
                    current_island = set()
                    row_origin = r
                    col_origin = c
                    dfs(r, c)
                    if not current_island:
                        continue
                    unique_islands.add(frozenset(current_island))

        return len(unique_islands)