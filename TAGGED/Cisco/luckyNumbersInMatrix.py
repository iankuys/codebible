"""
1380. Lucky Numbers in a Matrix
Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

Example 1:
Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 2:

Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 3:

Input: matrix = [[7,8],[1,2]]
Output: [7]
Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.
"""

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        # min in row
        resRow = [0] * m
        for i in range(m):
            resRow[i] = min(matrix[i])
        
        # max in col
        resCol = [0] * n
        for j in range(n):
            for i in range(m):
                resCol[j] = max(resCol[j], matrix[i][j])

        luckyNumbers = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == resRow[i] and matrix[i][j] == resCol[j]:
                    luckyNumbers.append(matrix[i][j])
        
        return luckyNumbers