# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# Link: https://leetcode.com/problems/set-matrix-zeroes/

# You must do it in place.
class Solution:
    # Time Complexity:
    #   Best case: O(m × n) - two-pass matrix traversal
    #   Average case: O(m × n)
    #   Worst case: O(m × n)
    # Space Complexity: O(m + n)
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i_zero = set()
        j_zero = set()

        m = len(matrix[0])
        n = len(matrix)

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    i_zero.add(i)
                    j_zero.add(j)
        
        for i in range(n):
            for j in range(m):
                if i in i_zero or j in j_zero:
                    matrix[i][j] = 0
