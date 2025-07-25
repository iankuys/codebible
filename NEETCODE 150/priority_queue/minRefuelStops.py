# Link: https://leetcode.com/problems/minimum-number-of-refueling-stops/
"""
871. Minimum Number of Refueling Stops
A car travels from a starting position to a destination which is target miles east of the starting position.
There are gas stations along the way. The gas stations are represented as an array stations where stations[i] = [positioni, fueli] indicates that the ith gas station is positioni miles east of the starting position and has fueli liters of gas.
The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it. It uses one liter of gas per one mile that it drives. When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.
Return the minimum number of refueling stops the car must make in order to reach its destination. If it cannot reach the destination, return -1.
Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there. If the car reaches the destination with 0 fuel left, it is still considered to have arrived.

Example 1:

Input: target = 1, startFuel = 1, stations = []
Output: 0
Explanation: We can reach the target without refueling.
Example 2:

Input: target = 100, startFuel = 1, stations = [[10,100]]
Output: -1
Explanation: We can not reach the target (or even the first gas station).
Example 3:

Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
Output: 2
Explanation: We start with 10 liters of fuel.
We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
We made 2 refueling stops along the way, so we return 2.
"""
# Heap solution
import heapq


class Solution(object):
    # Time Complexity: O(n log n)
    # Space Complexity: O(n)
    def minRefuelStops(self, target, tank, stations):
        # Max-heap to store fuel capacities of passed stations
        # (use negative values to simulate max-heap in Python)
        max_heap = []

        # Append a dummy station at the target so we always process the final leg
        stations.append((target, float('inf')))

        # Initialize: total number of refuels, and the previous station's location
        refuels = 0
        prev_location = 0

        for location, capacity in stations:
            # Distance traveled since last station; subtract fuel used
            tank -= location - prev_location

            # While we don't have enough fuel to reach this station
            # refuel using the largest available fuel from previous stations
            while max_heap and tank < 0:
                tank += -heapq.heappop(max_heap)  # pop the largest fuel
                refuels += 1

            # If we still can't reach this station, it's impossible
            if tank < 0:
                return -1

            # Store the current station's fuel in heap (for possible future use)
            heapq.heappush(max_heap, -capacity)

            # Update previous station location
            prev_location = location

        # If we reach the end of loop, we’ve reached the target
        return refuels

# DFS but not efficient enough
class Solution:
    # Time Complexity:
    #   Best case: O(n) - linear scan
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(1)
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        minStops = float('inf')
        n = len(stations)

        def dfs(position, fuel, idx, stops):
            nonlocal minStops
            if position + fuel >= target:
                minStops = min(minStops, stops)
                return

            for i in range(idx, n):
                station_pos, station_fuel = stations[i]
                distance = station_pos - position
                if distance > fuel:
                    break  # Can't reach this station
                # Travel to the station and refuel
                dfs(station_pos, fuel - distance + station_fuel, i + 1, stops + 1)

        dfs(0, startFuel, 0, 0)
        return minStops if minStops != float('inf') else -1
