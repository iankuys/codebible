"""
347. Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []
        hashmap = Counter(nums)
        res = []

        for key in hashmap.keys():
            heapq.heappush(maxHeap, (-1 * hashmap[key], key))

        heapq.heapify(maxHeap)
        while k > 0:
            res.append(heapq.heappop(maxHeap)[1])
            k-=1

        return res