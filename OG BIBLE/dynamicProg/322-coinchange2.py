# Link: https://leetcode.com/problems/coin-change/
from typing import List

class Solution:
    # Time Complexity:
    #   Best case: O(amount × coins) - DP with nested loops
    #   Average case: O(amount × coins)
    #   Worst case: O(amount × coins)
    # Space Complexity: O(amount)
    def coinChange(self, coins: 'List[int]', amount: 'int') -> 'int':
        dp = [0] + [float('inf') for i in range(amount)]
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        if dp[-1] == float('inf'):
            return -1
        return dp[-1]

