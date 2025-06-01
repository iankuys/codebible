# Link: https://leetcode.com/problems/number-of-black-blocks/
"""
2768. Number of Black Blocks
Attempted
Medium
Topics
Companies
Hint
You are given two integers m and n representing the dimensions of a 0-indexed m x n grid.

You are also given a 0-indexed 2D integer matrix coordinates, where coordinates[i] = [x, y] indicates that the cell with coordinates [x, y] is colored black. All cells in the grid that do not appear in coordinates are white.

A block is defined as a 2 x 2 submatrix of the grid. More formally, a block with cell [x, y] as its top-left corner where 0 <= x < m - 1 and 0 <= y < n - 1 contains the coordinates [x, y], [x + 1, y], [x, y + 1], and [x + 1, y + 1].

Return a 0-indexed integer array arr of size 5 such that arr[i] is the number of blocks that contains exactly i black cells.

"""
# optimized chatgpt solution
from collections import defaultdict

class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        blacks = defaultdict(int)
        
        for row, col in coordinates:
            for dx in [0, -1]:
                for dy in [0, -1]:
                    x, y = row + dx, col + dy
                    if 0 <= x < m - 1 and 0 <= y < n - 1:
                        blacks[(x, y)] = 1 + blacks.get((x, y), 0)

        res = [0] * 5
        res[0] = (m - 1) * (n - 1)

        for black in blacks.values():
            res[black] += 1
            res[0] -= 1

        return res
    
# redo with comments
class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        block_count = defaultdict(int)
        
        for black_cell in coordinates:
            for dx in [0, -1]:
                for dy in [0, -1]:
                    # we are only calculating the blocks that will exist in every black cell
                    r, c = black_cell
                    nx, ny = r + dy, c + dx
                    if 0 <= nx < m - 1 and 0 <= ny < n - 1:
                        # add to that block hash map so the next time the block is the same, we will add to it again
                        block_count[(nx, ny)] += 1

        res = [0] * 5
        res[0] = (m - 1) * (n - 1)
        for value in block_count.values():
            res[value] += 1
            res[0] -= 1

        return res
    
class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        block_count = defaultdict(int)

        for r, c in coordinates:
            # A black cell can be part of up to 4 different 2x2 blocks
            for dr in [0, -1]:
                for dc in [0, -1]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m - 1 and 0 <= nc < n - 1:
                        block_count[(nr, nc)] += 1

        res = [0] * 5
        for count in block_count.values():
            res[count] += 1

        # Total number of possible 2x2 blocks is (m - 1) * (n - 1)
        total_blocks = (m - 1) * (n - 1)
        res[0] = total_blocks - sum(res[1:])

        return res


# my solution but Time Limit Exceeded 2103 / 2145 testcases passed
class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        
        res = [0] * 5
        matrix = [[0] * n for _ in range(m)]

        for coordinate in coordinates:
            row = coordinate[0]
            col = coordinate[1]
            matrix[row][col] = 1

        # traverse matrix in block fashion, maybe reiterate among smaller blocks?
        # how inefficient will that be it would that be?
        # each block is a 2 by 2

        for i in range(m - 1):
            for j in range(n - 1):
                # loop within the block?
                black = 0

                if matrix[i][j] == 1:
                    black += 1
                if matrix[i + 1][j] == 1:
                    black += 1
                if matrix[i][j + 1] == 1:
                    black += 1
                if matrix[i + 1][j + 1] == 1:
                    black += 1

                res[black] += 1

        return res