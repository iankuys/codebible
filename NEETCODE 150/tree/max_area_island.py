# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# Link: https://leetcode.com/problems/max-area-of-island/

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

class Solution:
    # Time Complexity:
    #   Best case: O(V + E) - graph traversal
    #   Average case: O(V + E)
    #   Worst case: O(V + E)
    # Space Complexity: O(m × n)
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_area = 0

        def dfs(i, j, visited, count):
            if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0 or grid[i][j] == 0 or (i,j) in visited:
                return
            
            visited.add((i,j))
            count[0] += 1

            dfs(i+1, j, visited, count)
            dfs(i, j+1, visited, count)
            dfs(i-1, j, visited, count)
            dfs(i, j-1, visited, count)

            return

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                count_arr = [0]
                if grid[i][j] != 0:
                    dfs(i,j, visited, count_arr)
                    max_area = max(max_area, count_arr[0])

        return max_area