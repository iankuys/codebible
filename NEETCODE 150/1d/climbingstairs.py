# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        dict = {}
        return self.dfs(n, dict)

    def dfs(self, n, dict):
        
        if n in dict:
            return dict[n]
        if n == 0:
            return 1
        if n < 0:
            return 0
        
        # add number of paths of n into dictionary
        if n not in dict:
            dict[n] = self.dfs(n-1,dict) + self.dfs(n-2,dict)
            return dict[n]