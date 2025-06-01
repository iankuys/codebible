# 973. K Closest Points to Origin
# Companies
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
# https://leetcode.com/problems/k-closest-points-to-origin/description/

import math 
from collections import defaultdict 

class Solution:
    # Time Complexity:
    #   Best case: O(n²) - nested iteration
    #   Average case: O(n²)
    #   Worst case: O(n²)
    # Space Complexity: O(1)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        origin = (0,0)
        arr = []
        res = []
        hmap = defaultdict(list)

        for point in points:
            distance = math.sqrt((point[0] - origin[0]) ** 2 + (point[1] - origin[1]) ** 2)
            hmap[distance].append(point)
            arr.append(distance)

        heapq.heapify(arr)

        while k > 0:
            highest = heapq.heappop(arr)
            for point in hmap[highest]:
                res.append(point)
                k -= 1

        return res

