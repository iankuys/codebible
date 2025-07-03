# You are climbing a staircase. It takes n steps to reach the top.
# Link: https://leetcode.com/problems/climbing-stairs/

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# my own dp
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)

        # 1 way to stay at step 0 (do nothing)
        dp[0] = 1

        # 1 way to reach step 1 (one single step)
        dp[1] = 1

        for i in range(2, n + 1):
            # Ways to reach step i = ways to reach (i-1) + ways to reach (i-2)
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]

# more intuitive with actually step 2
class Solution:
    def climbStairs(self, n: int) -> int:
        # Handle small cases directly
        if n == 0 or n == 1:
            return 1
        if n == 2:
            return 2

        dp = [0] * (n + 1)
        dp[0] = 1  # 1 way to stay at step 0 (do nothing)
        dp[1] = 1  # 1 way to reach step 1
        dp[2] = 2  # 2 ways to reach step 2: (1+1) or (2)

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

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