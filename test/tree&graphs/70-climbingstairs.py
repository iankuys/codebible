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
            # sum the number of total paths
            dict[n] = self.dfs(n-1,dict) + self.dfs(n-2,dict)
            return dict[n]