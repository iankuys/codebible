# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
# Link: https://leetcode.com/problems/subarray-sum-equals-k/

# A subarray is a contiguous non-empty sequence of elements within an array.
# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2
 
class Solution:
    # Time Complexity:
    #   Best case: O(n) - linear scan
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(1)
    def subarraySum(self, nums: List[int], k: int) -> int:

        ans = 0
        prefsum = 0
        d = {0:1}
        # subarray is continguous

        for num in nums:
            prefsum += num
            if prefsum - k in d:
                # d contain the sum of differnt index, if one of index
                # in d plus k is the current sum, 
                # means there exit a subarray
                # from that index to current index, sum equals k
                ans += d[prefsum - k]
            if prefsum in d:
                d[prefsum] += 1
            else:
                d[prefsum] = 1
        return ans

