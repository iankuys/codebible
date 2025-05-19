"""
121. Best Time to Buy and Sell Stock
Solved
Easy
Topics
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

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        i = 0
        j = i + 1
        max_profit = 0

        while (j < len(prices)):
            # if price cur day is higher than later day, then we move on
            # move to the new minimum whenever we can
            # if there is a larger maximum later on the new min will be better for it anyway
            profit = prices[j] - prices[i]
            if profit < 0:
                i += 1
                j = i + 1
            else:
                max_profit = max(max_profit, profit)
                j += 1

        return max_profit