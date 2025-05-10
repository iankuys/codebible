#121. Best Time to Buy and Sell Stock
#Subarray solution
from typing import List

def maxProfit(prices: List[int]) -> int:
        maxProf = 0
        curProf = 0
        
        for i in range(1, len(prices)):
            curProf = max(0, curProf + (prices[i]-prices[i-1]))
            print(curProf)
            maxProf = max(maxProf, curProf)
            
        return maxProf   
    
class Solution:
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
            