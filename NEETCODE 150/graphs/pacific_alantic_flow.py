# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.
# Link: https://leetcode.com/problems/pacific-atlantic-water-flow/
# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
class Solution:
    # Time Complexity:
    #   Best case: O(V + E) - graph traversal
    #   Average case: O(V + E)
    #   Worst case: O(V + E)
    # Space Complexity: O(1)
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]: return []
        m, n = len(heights), len(heights[0])
        visited_p = set()
        visited_a = set()

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(row, col, visited):
            visited.add((row, col))

            for dx, dy in directions:
                new_r, new_c = row + dx, col + dy

                # we are doing dfs from left to right/ or bottom to top
                if m>new_r >= 0 and n>new_c>= 0 and heights[new_r][new_c] >= heights[row][col] and (new_r, new_c) not in visited:
                    dfs(new_r, new_c, visited)

        # from left to right border
        for i in range(m):
            dfs(i, 0, visited_p)
            dfs(i, n-1, visited_a)
        # from top to bottom border
        for j in range(n):
            dfs(0, j, visited_p)
            dfs(m-1, j, visited_a)

        return list(visited_p.intersection(visited_a))