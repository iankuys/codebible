# LeetCode Problem 2: https://leetcode.com/problems/
# Given an integer array nums that may contain duplicates, return all possible 
# subsets
#  (the power set).
# # The solution set must not contain duplicate subsets. Return the solution in any order.
# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

# my solution but optimizied
class Solution:
    # Time Complexity:
    #   Best case: O(n log n) - sorting operation
    #   Average case: O(n log n)
    #   Worst case: O(n log n)
    # Space Complexity: O(1)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []
        cur = []

        def dfs(cur, i):
            if i >= len(nums):
                res.append(cur.copy())
                return

            cur.append(nums[i])
            dfs(cur, i + 1)

            cur.pop()
            # this while loop checks if the future elements are duplicated, if it is we just gonna count the duplicated values as one subset so we dont have to go into dp again.
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            dfs(cur, i + 1)

        dfs(cur, 0)
        return res
    
# my solution but slow
class Solution:
    # Time Complexity:
    #   Best case: O(n log n) - sorting operation
    #   Average case: O(n log n)
    #   Worst case: O(n log n)
    # Space Complexity: O(1)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []
        cur = []

        def dfs(cur, i):
            if i >= len(nums):
                if cur not in res:
                    res.append(cur.copy())
                return
            if cur not in res:
                res.append(cur.copy())
            cur.append(nums[i])
            print(1, cur)
            dfs(cur, i + 1)
            cur.pop()
            print(2, cur)

            dfs(cur, i + 1)

        dfs(cur, 0)
        return res