# 1046. Last Stone Weight

# You are given an array of integers stones where stones[i] is the weight of the ith stone.

# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.

# Return the weight of the last remaining stone. If there are no stones left, return 0.
# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation: 
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
# https://leetcode.com/problems/last-stone-weight/description/

class Solution:
    # Time Complexity:
    #   Best case: O(n) - linear scan
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(1)
    def lastStoneWeight(self, stones: List[int]) -> int:
        negated_stones = [-1 * stone for stone in stones]
        heapq.heapify(negated_stones)
        
        while (len(negated_stones) > 1):
            first_heaviest = -1 * heapq.heappop(negated_stones)

            sec_heaviest = -1 * heapq.heappop(negated_stones)

            result = first_heaviest - sec_heaviest

            heapq.heappush(negated_stones, -1 * result)

        return -1 * heapq.heappop(negated_stones)
