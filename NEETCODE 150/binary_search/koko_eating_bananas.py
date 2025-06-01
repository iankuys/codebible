# 875. Koko Eating Bananas
# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# Return the minimum integer k such that she can eat all the bananas within h hours.

# Example 1:
# Input: piles = [3,6,7,11], h = 8
# Output: 4
# https://leetcode.com/problems/koko-eating-bananas/description/

# 2025 solution
class Solution:
    # Time Complexity:
    #   Best case: O(1) - binary search
    #   Average case: O(log n)
    #   Worst case: O(log n)
    # Space Complexity: O(1)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        rates = range(1, max(piles) + 1)

        minRate = float('infinity')
        left = 0 
        right = len(rates) - 1

        while (left <= right):
            middle = (left + right) // 2
            totalHours = 0
            rate = rates[middle]

            for pile in piles:
                totalHours += math.ceil(pile / rate)
            
            if totalHours <= h:
                minRate = min(minRate, rate)
                right = middle - 1
            else:
                left = middle + 1

        return minRate
    
class Solution:
    # Time Complexity:
    #   Best case: O(1) - binary search
    #   Average case: O(log n)
    #   Worst case: O(log n)
    # Space Complexity: O(1)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # the larger the faster
        # if h == len(piles):
        # the solution has the be max in piles

        # if h > len(piles)
        # 
        bot = 1
        top = max(piles)
        res = top

        while (bot <= top):
            hours = 0
            k = (bot + top) // 2
            # calculate k (time it takes to eat) by dividing by piles
            for pile in piles:
                hours += math.ceil(pile / k)
            
            # if the time is fast, that means we can go slower
            if hours <= h:
                res = min(res, k)
                top = k - 1
            else:
                # if time k is more than height, it means the mid is too low
                bot = k + 1
        
        return res
