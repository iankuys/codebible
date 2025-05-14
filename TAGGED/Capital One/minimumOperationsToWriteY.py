"""
3071. Minimum Operations to Write the Letter Y on a Grid
Solved
Medium
Topics
Companies
You are given a 0-indexed n x n grid where n is odd, and grid[r][c] is 0, 1, or 2.

We say that a cell belongs to the Letter Y if it belongs to one of the following:

The diagonal starting at the top-left cell and ending at the center cell of the grid.
The diagonal starting at the top-right cell and ending at the center cell of the grid.
The vertical line starting at the center cell and ending at the bottom border of the grid.
The Letter Y is written on the grid if and only if:

All values at cells belonging to the Y are equal.
All values at cells not belonging to the Y are equal.
The values at cells belonging to the Y are different from the values at cells not belonging to the Y.
Return the minimum number of operations needed to write the letter Y on the grid given that in one operation you can change the value at any cell to 0, 1, or 2.
"""

class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        y_counter = {}
        not_y_counter = {}
        m = len(grid)
        n = len(grid[0])
        num_y = 0
        num_non_y = 0

        # how to determine that i and j is in Y
        for i in range(m):
            for j in range(n):
                if (i == j and i < m // 2) or (j == m - i - 1 and i < m // 2) or (i >= m // 2 and j == n // 2):
                    num_y += 1
                    y_counter[grid[i][j]] = 1 + y_counter.get(grid[i][j], 0)
                else:
                    num_non_y += 1
                    not_y_counter[grid[i][j]] = 1 + not_y_counter.get(grid[i][j], 0)
        
        operation = float('infinity')

        # use for non y
        for a in [0, 1, 2]:
            # use for y
            for b in [0, 1, 2]:
                if a == b:
                    continue
                op = num_non_y - not_y_counter.get(a, 0) + num_y - y_counter.get(b, 0)
                operation = min(operation, op)

        return operation