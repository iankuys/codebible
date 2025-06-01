# Link: https://leetcode.com/problems/candy-crush/
"""
723. Candy Crush

Given an m x n integer array board representing the grid of candy where board[i][j] represents the type of candy. A value of board[i][j] == 0 represents that the cell is empty.

The given board represents the state of the game following the player's move. Now, you need to restore the board to a stable state by crushing candies according to the following rules:

If three or more candies of the same type are adjacent vertically or horizontally, crush them all at the same time - these positions become empty.
After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, then these candies will drop until they hit a candy or bottom at the same time. No new candies will drop outside the top boundary.
After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.
If there does not exist more candies that can be crushed (i.e., the board is stable), then return the current board.
You need to perform the above rules until the board becomes stable, then return the stable board.
"""
class Solution:
    # Time Complexity:
    #   Best case: O(n²) - nested iteration
    #   Average case: O(n²)
    #   Worst case: O(n²)
    # Space Complexity: O(1)
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        done = True
        m = len(board)
        n = len(board[0])
        
        # row crunch
        for row in range(m):
            for col in range(n - 2):
                first = abs(board[row][col])
                second = abs(board[row][col + 1])
                third = abs(board[row][col + 2])

                if first == second == third and first != 0:
                    board[row][col] = -1 * first
                    board[row][col + 1] = -1 * second
                    board[row][col + 2] = -1 * third
                    done = False

        # col crunch
        for col in range(n):
            for row in range(m - 2):
                first = abs(board[row][col])
                second = abs(board[row + 1][col])
                third = abs(board[row + 2][col])

                if first == second == third and first != 0:
                    board[row][col] = -1 * first
                    board[row + 1][col] = -1 * second
                    board[row + 2][col] = -1 * third
                    done = False

        # gravity this is very similar to move zeros on leetcode
        if not done:
            for col in range(n):
                idx = m - 1
                for row in range(m - 1, -1, -1):
                    if board[row][col] > 0:
                        board[idx][col] = board[row][col]
                        idx -= 1

                for row in range(idx, -1, -1):
                    board[row][col] = 0

        return board if done else self.candyCrush(board)
                


# 12/24 i give up
class Solution:
    # Time Complexity:
    #   Best case: O(n²) - nested iteration
    #   Average case: O(n²)
    #   Worst case: O(n²)
    # Space Complexity: O(1)
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:

        explored = {}

        def dfs_verti(i, j, count, value):
            if i >= len(board):
                return count >= 3
            if board[i][j] != value:
                return count >= 3

            explored[(i, j)] = 1
            vert = dfs_verti(i + 1, j, count + 1, value)

            if vert:
                board[i][j] = "x"
            
            return vert

        def dfs_hori(i, j, count, value):
            if j >= len(board[0]):
                return count >= 3
            if board[i][j] != value:
                return count >= 3

            explored[(i, j)] = 1
            hori = dfs_hori(i, j + 1, count + 1, value)

            if hori:
                board[i][j] = "x"
            
            return hori
        
        not_stable = True

        while (not_stable):
            not_stable = False
            temp_explored = {}  # Reset for each iteration
            # identify and mark pairs with x
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] in explored or board[i][j] == "x" or board[i][j] == 0:
                        continue
                    if dfs_verti(i, j, 0, board[i][j]) or dfs_hori(i, j, 0, board[i][j]):
                        not_stable = True

            # remove the marked pairs and shift array down
            for j in range(len(board[0])):
                # Start from the bottom of each column
                write_pos = len(board) - 1
                
                # Move from bottom to top
                for i in range(len(board)-1, -1, -1):
                    if board[i][j] != "x":
                        # Move candy down to write position
                        board[write_pos][j] = board[i][j]
                        write_pos -= 1
                
                # Fill the top with zeros
                for i in range(write_pos, -1, -1):
                    board[i][j] = 0

                print(board)

        return board

# potential OA
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
