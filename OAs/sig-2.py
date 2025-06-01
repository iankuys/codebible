# LeetCode Problem 2: https://leetcode.com/problems/
# Sudoku checker

def solution(board):
    dict = {}
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (board[i][j] not in dict):
                dict[board[i][j]] = 1
            else:
                return False
                
        dict = {}
    
    for i in range(len(board[0])):
        for j in range(len(board)):
            if (board[j][i] not in dict):
                dict[board[j][i]] = 1
            else:
                return False
                
        dict = {}
        
    for i in range(len(board)//3):
        for j in range(len(board[0])//3):
            for k in range(i*3, i*3+3):
                for l in range(j*3, j*3+3):
                    if (board[k][l] not in dict):
                        dict[board[k][l]] = 1
                    else:
                        return False
            dict = {}
                
        
    return True

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
class Solution:
    # Time Complexity:
    #   Best case: O(n²) - nested iteration
    #   Average case: O(n²)
    #   Worst case: O(n²)
    # Space Complexity: O(1)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]
        return len(res) == len(set(res))