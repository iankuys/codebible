#121. Best Time to Buy and Sell Stock
#Subarray solution
  def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        curProf = 0
        
        for i in range(1, len(prices)):
            curProf = max(0, curProf + (prices[i]-prices[i-1]))
            print(curProf)
            maxProf = max(maxProf, curProf)
            
        return maxProf   
    
#linear comparison(remember that arrays are iterated in one direction):
def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        cheapestPrice = 100000000000000000000000000000000000000000
        
        for i in range(len(prices)):
            if (prices[i]< cheapestPrice):
                cheapestPrice = prices[i]
            elif (prices[i]-cheapestPrice > maxProf):
                maxProf = prices[i]-cheapestPrice
        return maxProf   