# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
# Link: https://leetcode.com/problems/min-cost-climbing-stairs/
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.

# Example 1:

# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.
class Solution:
    # Time Complexity:
    #   Best case: O(n) - linear scan
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(1)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp = [float("inf")] * (len(cost) + 1)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost) + 1):
            if i < len(cost):
                dp[i] = cost[i] + min(dp[i-1], dp[i-2])
            else:
                dp[i] = min(dp[i-1], dp[i-2])
        
        return dp[-1]
