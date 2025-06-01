# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

class Solution:
    # Time Complexity:
    #   Best case: O(n) - linear operation
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(1)
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def dfs(cur, used):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return

            for i in range(len(nums)):

                if used[i]:
                    continue

                cur.append(nums[i])
                used[i] = True
                dfs(cur, used)
                
                cur.pop()
                used[i] = False
                
        dfs([], [False] * len(nums))
        return res
