# Link: https://leetcode.com/problems/maximal-square/
"""
221. Maximal Square
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
"""
class Solution:
    # Time Complexity:
    #   Best case: O(m × n) - dynamic programming with memoization
    #   Average case: O(m × n)
    #   Worst case: O(m × n)
    # Space Complexity: O(m × n)
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dynamic programming: bottom up
        # recursive: top down
        m, n= len(matrix), len(matrix[0])
        cache = {} # map each (r, c) -> maxLength of square

        def helper(r, c):
            if r >= m or c >= n:
                return 0
            if (r, c) not in cache:
                down = helper(r + 1, c)
                right = helper(r, c + 1)
                diag = helper(r + 1, c + 1)

                cache[(r, c)] = 0
                if matrix[r][c] == "1":
                    cache[(r, c)] = 1 + min(down, right, diag)

            return cache[(r, c)]

        helper(0, 0)
        
        return max(cache.values()) ** 2