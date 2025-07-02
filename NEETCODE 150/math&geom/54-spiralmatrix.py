"""
54. Spiral Matrix
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

# latest dfs from me
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        visited = {}
        res = []

        def travel(i, j, isReverse):
            if i < 0 or j < 0 or i >= m or j >= n or (i, j) in visited:
                return
            visited[(i, j)] = 1
            res.append(matrix[i][j])

            if not isReverse:
                travel(i, j + 1, False)
                travel(i + 1, j, False)
                travel(i, j - 1, False)
                travel(i - 1, j, True)
            else:
                travel(i - 1, j, True)
                travel(i, j + 1, False)
            
        travel(0, 0, False)
        return res
    
class Solution:
    # Time Complexity:
    #   Best case: O(m × n) - visit each matrix cell once
    #   Average case: O(m × n)
    #   Worst case: O(m × n)
    # Space Complexity: O(m × n)
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        seen = set()
        def dfs(row,col, isUp):
            if row < len(matrix) and row >= 0 and col < len(matrix[0]) and col >= 0 and (row,col) not in seen:
                seen.add((row,col))
                ans.append(matrix[row][col])
                if isUp:
                    dfs(row-1,col,True)
                dfs(row,col+1,False)
                dfs(row+1,col,False)
                dfs(row,col-1,False)
                dfs(row-1,col,True)
        dfs(0,0, False)
        return ans

