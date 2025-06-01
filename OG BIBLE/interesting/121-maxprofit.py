# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
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
    
prices = [7,1,5,19,8,7,25]
maxprof = maxProfit(prices)

#linear comparison(remember that arrays are iterated in one direction):
def maxProfit(prices: List[int]) -> int:
        maxProf = 0
        cheapestPrice = 100000000000000000000000000000000000000000
        
        for i in range(len(prices)):
            if (prices[i]< cheapestPrice):
                cheapestPrice = prices[i]
            elif (prices[i]-cheapestPrice > maxProf):
                maxProf = prices[i]-cheapestPrice
        return maxProf   

