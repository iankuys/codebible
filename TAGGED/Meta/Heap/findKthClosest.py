# Link: https://leetcode.com/problems/k-closest-points-to-origin/
"""
973. K Closest Points to Origin
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Example 1:

Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
"""
import math
import heapq

# max_heap more efficient as we remove the farthest point when heap size exceeds k
class Solution:
    # Time Complexity:
    #   Best case: O(n log k) - heap operations for each point, heap size limited to k
    #   Average case: O(n log k)
    #   Worst case: O(n log k)
    # Space Complexity: O(k)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x, y in points:
            dist = -(x * x + y * y)
            heapq.heappush(maxHeap, (dist, [x, y]))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        return [coord for (_, coord) in maxHeap]


# min_heap less efficient
class Solution:
    # Time Complexity:
    #   Best case: O(n + k log n) - heapify O(n) + k heap pops O(k log n)
    #   Average case: O(n + k log n)
    #   Worst case: O(n + k log n)
    # Space Complexity: O(n)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []

        for x, y in points:
            distance = math.sqrt(x ** 2 + y ** 2)
            minHeap.append((distance, [x,y]))

        heapq.heapify(minHeap)

        while k > 0:
            d, coords = heapq.heappop(minHeap)
            res.append(coords)
            k -= 1

        return res
