# 74. Search a 2D Matrix
# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# https://leetcode.com/problems/search-a-2d-matrix/description/

# new and better solution by me 2025
class Solution:
    # Time Complexity:
    #   Best case: O(1) - target found immediately
    #   Average case: O(log(m × n))
    #   Worst case: O(log(m × n))
    # Space Complexity: O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        down = len(matrix) - 1

        while (top <= down):
            middleRow = (top + down) // 2

            # bigger than first element of row, then check the row before
            if matrix[middleRow][0] > target:
                down = middleRow - 1
            # if its target is bigger than the last element of row, then check the next row
            elif matrix[middleRow][-1] < target:
                top = middleRow + 1
            # if they are both not true, then we know that it is in this row
            else:
                row = matrix[middleRow]
                left = 0
                right = len(row) - 1

                while (left <= right):
                    middleCol = (left + right) // 2

                    if row[middleCol] < target:
                        left = middleCol + 1
                    elif row[middleCol] > target:
                        right = middleCol - 1
                    else:
                        return True

                return False  # target not found in the row, exit as soon as we have checked the row

        return False # target not found in any row
    
class Solution:
    # Time Complexity:
    #   Best case: O(1) - target found immediately
    #   Average case: O(log(m × n))
    #   Worst case: O(log(m × n))
    # Space Complexity: O(1)
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
    
