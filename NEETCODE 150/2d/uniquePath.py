# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.

 
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid_dict = {}
        return self.gridTraveler(m, n, grid_dict)

    def gridTraveler(self, m, n, grid_dict):
        key = str(m) + ',' + str(n)

        if key in grid_dict:
            return grid_dict[key]
        if m == 1 and n == 1:
            return 1
        if m == 0 or n == 0:
            return 0
        grid_dict[key] = self.gridTraveler(m-1, n, grid_dict) + self.gridTraveler(m, n-1, grid_dict)
        return grid_dict[key]
