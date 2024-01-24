# 74. Search a 2D Matrix
# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# https://leetcode.com/problems/search-a-2d-matrix/description/
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        low = 0
        high = len(matrix) - 1

        while (low <= high):

            row = (low + high) // 2

            if target > matrix[row][-1]:
                low = row + 1
            elif target < matrix[row][0]:
                high = row - 1
            else:
                break

        if not (low <= high):
            return False

        row = (low + high) // 2
        low = 0
        high = len(matrix[0]) - 1
        while (low <= high):
            
            mid = (low + high) // 2

            if target > matrix[row][mid]:
                low = mid + 1
            elif target < matrix[row][mid]:
                high = mid - 1
            else:        
                return True

        return False