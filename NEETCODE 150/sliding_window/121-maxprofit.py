# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
121. Best Time to Buy and Sell Stock
Solved
Easy
Topics
conpanies icon
Companies
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

# Subarray solution (Kadane's Algorithm)
from typing import List

def maxProfit(prices: List[int]) -> int:
        maxProf = 0
        curProf = 0
        
        for i in range(1, len(prices)):
            curProf = max(0, curProf + (prices[i]-prices[i-1]))
            maxProf = max(maxProf, curProf)
            
        return maxProf   
    
class Solution:
    # Time Complexity:
    #   Best case: O(n) - linear operation
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = i + 1
        profit = 0

        while (j < len(prices)):
            profit = max(profit, prices[j] - prices[i])

            if prices[j] - prices[i] < 0:
                i += 1
            else:
                j += 1

        return profit
            