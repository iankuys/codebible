# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/
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
