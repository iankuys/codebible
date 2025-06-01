# LeetCode Problem 54: https://leetcode.com/problems/
class Solution:
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

# doesnt work 17/23 passed
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()
        array = []

        self.dfs(matrix, 0, 0, visited, array, False)
        return array
        
    def dfs(self, matrix, row, col, visited, array, isUp):

        temp = len(array)
        if col >= len(matrix[0]):
            row += 1
            col -= 1
        if col < 0:
            row -= 1
            col += 1
        if row < 0:
            col += 1
            row += 1
        if row >= len(matrix):
            col -= 1
            row -= 1
        if (row, col) not in visited and (col >= 0 and col < len(matrix[0]) and (row >= 0 and row < len(matrix))):
            array.append(matrix[row][col])
            visited.add((row,col))
        print(isUp)
        print(row,col)
        if temp == len(array):
            return
        if isUp and (row, col) in visited:
            self.dfs(matrix, row, col-1, visited, array, True)
        
        self.dfs(matrix, row, col+1, visited, array, False)
        self.dfs(matrix, row, col-1, visited, array, True)


