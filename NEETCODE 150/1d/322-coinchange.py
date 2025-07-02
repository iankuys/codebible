# LeetCode Problem 322: https://leetcode.com/problems/
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1
    
from typing import List

class Solution:
    # Time Complexity:
    #   Best case: O(n) - linear scan
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(1)
    def coinChange(self, coins: List[int], amount: int) -> int:
        dict = {}
        coins.sort()
        print(coins)
        ans = self.recursive(coins, amount, 0, dict)
        # for key,value in dict.items():
        #     if value > -1:
        #         print(key, value)
        return ans
    
    def recursive(self, coins, amount, count, dict):
        
        if amount in dict:
            return dict[amount]
        if amount == 0:
            print(count)
            return count
        if amount < 0:
            return -1
        for coin in (coins[::-1]):
            way = self.recursive(coins, amount-coin, count+1, dict)
            if amount not in dict:
                dict[amount] = way
            if way != -1 and dict[amount] == -1:
                dict[amount] = way
            if way != -1 and way < dict[amount]:
                dict[amount] = way
            
        return dict[amount]

s1 = Solution()
s1.coinChange([186,419,83,408], 6249)