# Link: https://leetcode.com/problems/gas-station/
# 134. Gas Station
# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique
# Example 1:
# Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# Output: 3
# Explanation:
# Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 4. Your tank = 4 - 1 + 5 = 8
# Travel to station 0. Your tank = 8 - 2 + 1 = 7
# Travel to station 1. Your tank = 7 - 3 + 2 = 6
# Travel to station 2. Your tank = 6 - 4 + 3 = 5
# Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
# Therefore, return 3 as the starting index.
# smart solution
class Solution:
    # Time Complexity:
    #   Best case: O(n) - linear scan
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(1)
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gain = 0    # Tracks overall net gas after completing the full loop
        curr_gain = 0     # Tracks net gas from the current starting station
        answer = 0        # Index of the candidate starting station

        for i in range(len(gas)):
            gain = gas[i] - cost[i]  # Net gas gained or lost at this station
            total_gain += gain       # Add to total gain across the whole trip
            curr_gain += gain        # Add to current path's gain

            # If current gain drops below zero, we can't reach the next station
            # from the current starting point. So, try starting from the next station.
            if curr_gain < 0:
                curr_gain = 0        # Reset current gain since we're starting fresh
                answer = i + 1       # Mark the next station as the new starting point

        # If total gain is negative, it's impossible to complete the circuit
        return answer if total_gain >= 0 else -1


# 33/40 passed bruh ran out of time (shoudl be useful for traversing arrays in cycles)
class Solution:
    # Time Complexity:
    #   Best case: O(n) - linear scan
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(1)
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        def dfs(remain_gas, index, visited):
            if remain_gas < 0:
                return False
            if len(visited) == len(gas):
                return True
            if index >= len(gas):
                index = 0
            visited.add(index)
            if len(visited) == 1:
                remaining_tank = remain_gas - cost[index]
            else:
                remaining_tank = remain_gas - cost[index] + gas[index]
            return dfs(remaining_tank, index+1, visited)
        
        for i in range(len(gas)):
            starting_gas = gas[i]
            visited = set()
            if (dfs(starting_gas, i, visited)):
                print("found")
                return i

        return -1