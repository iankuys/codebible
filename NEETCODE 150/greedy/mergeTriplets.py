# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/
# A triplet is an array of three integers. You are given a 2D integer array triplets, where triplets[i] = [ai, bi, ci] describes the ith triplet. You are also given an integer array target = [x, y, z] that describes the triplet you want to obtain.

# To obtain target, you may apply the following operation on triplets any number of times (possibly zero):

# Choose two indices (0-indexed) i and j (i != j) and update triplets[j] to become [max(ai, aj), max(bi, bj), max(ci, cj)].
# For example, if triplets[i] = [2, 5, 3] and triplets[j] = [1, 7, 5], triplets[j] will be updated to [max(2, 1), max(5, 7), max(3, 5)] = [2, 7, 5].
# way better solution and clear
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        a, b, c = 0, 0, 0
        for i, (x, y, z) in enumerate(triplets):
                if not(  x > target[0] or y > target[1] or z > target[2]):
                     a, b, c = max(a, x), max(b, y), max(c, z)
                        
        return [a, b, c] == target

# works but not efficient and clear
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cur_i, cur_j, cur_k = 0, 0, 0
        count = 0

        for i, j, k in triplets:
            newCount = 0
            max_i = max(cur_i, i)
            max_j = max(cur_j, j)
            max_k = max(cur_k, k)

            if (max_i == target[0] and max_j == target[1] and max_k == target[2]):
                return True
            if max_i == target[0]:
                newCount += 1
            if max_j == target[1]:
                newCount += 1 
            if max_k == target[2]:
                newCount += 1

            if count < newCount and max_i <= target[0] and max_j <= target[1] and max_k <= target[2]:
                cur_i = max_i
                cur_j = max_j
                cur_k = max_k
                count = newCount

        return False
