"""
Valid Sudoku
Solved 
You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.
"""

class Solution:
    # Time Complexity:
    #   Best case: O(n²) - nested iteration
    #   Average case: O(n²)
    #   Worst case: O(n²)
    # Space Complexity: O(1)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        col_dup = {}
        row_dup = {}
        box_dup = {}

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row_dup:
                    print("returning row")
                    return False
                else:
                    row_dup[board[i][j]] = True
            row_dup = {}

        for j in range(len(board[0])):
            for i in range(len(board)):
                if board[i][j] == ".":
                    continue
                if board[i][j] in col_dup:
                    print("returning col")
                    return False
                else:
                    col_dup[board[i][j]] = True
            col_dup = {}
        
        for i in range(len(board) // 3):
            for j in range(len(board[0]) // 3):
                for k in range(i * 3, 3 + i * 3):
                    for l in range(j * 3, 3 + j * 3):
                        if board[k][l] == ".":
                            continue    
                        if board[k][l] in box_dup:
                            print("returning here")
                            return False
                        else:
                            box_dup[board[k][l]] = True
                box_dup = {}

        return True
