# You are climbing a staircase. It takes n steps to reach the top.
# Link: https://leetcode.com/problems/climbing-stairs/

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    # Time Complexity:
    #   Best case: O(1) - hash table operations
    #   Average case: O(1)
    #   Worst case: O(n)
    # Space Complexity: O(1)
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
    
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dfs(n):
            if n == 0:
                return 1
            if n < 0:
                return 0
            if n in memo:
                return memo[n]
            
            memo[n] = dfs(n - 1) + dfs(n - 2)
            return memo[n]

        return dfs(n)