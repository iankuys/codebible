# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# https://leetcode.com/problems/word-search/description/

class Solution:
    # Time Complexity:
    #   Best case: O(m × n × 4^L) - backtracking DFS on grid (L = word length)
    #   Average case: O(m × n × 4^L)
    #   Worst case: O(m × n × 4^L)
    # Space Complexity: O(L)
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = set()

        def dfs(row, col, index):
            if index == len(word):
                return True
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[index] or (row, col) in visited:
                return False

            visited.add((row, col))
            res = (dfs(row + 1, col, index + 1) or 
                dfs(row, col + 1, index + 1) or 
                dfs(row - 1, col, index + 1) or 
                dfs(row, col - 1, index + 1))

            # remove node from visited since we are backtracking now
            visited.remove((row, col))            
            return res

        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True
        
        return False