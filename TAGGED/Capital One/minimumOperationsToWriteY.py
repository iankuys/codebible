# Link: https://leetcode.com/problems/minimum-operations-to-write-the-letter-y-on-a-grid/
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
    # Time Complexity:
    #   Best case: O(n²) - nested iteration
    #   Average case: O(n²)
    #   Worst case: O(n²)
    # Space Complexity: O(1)
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
    
# Potential OA version
from typing import List

class Solution:
    # Time Complexity:
    #   Best case: O(n²) - nested iteration
    #   Average case: O(n²)
    #   Worst case: O(n²)
    # Space Complexity: O(1)
    def diagonalPop(self, board: List[List[int]]) -> List[List[int]]:
        m, n = len(board), len(board[0])
        done = True
        to_crush = [[False] * n for _ in range(m)]

        # Diagonal top-left to bottom-right and top-right to bottom-left
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        # May need to negate the board[i][j] to avoid confusion with 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 0:
                    continue
                color = abs(board[i][j])
                for dx, dy in directions:
                    x1, y1 = i + dx, j + dy
                    x2, y2 = i + 2 * dx, j + 2 * dy
                    if 0 <= x1 < m and 0 <= y1 < n and 0 <= x2 < m and 0 <= y2 < n:
                        if abs(board[x1][y1]) == color and abs(board[x2][y2]) == color:
                            to_crush[i][j] = True
                            to_crush[x1][y1] = True
                            to_crush[x2][y2] = True
                            done = False

        # Mark cells to be crushed
        for i in range(m):
            for j in range(n):
                if to_crush[i][j]:
                    board[i][j] = -abs(board[i][j])

        # Gravity step (same as Candy Crush)
        for col in range(n):
            idx = m - 1
            for row in range(m - 1, -1, -1):
                if board[row][col] > 0:
                    board[idx][col] = board[row][col]
                    idx -= 1
            for row in range(idx, -1, -1):
                board[row][col] = 0

        return board if done else self.diagonalPop(board)
