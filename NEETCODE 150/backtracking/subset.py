# https://leetcode.com/problems/subsets/description/

# neetcode easier to undersand
class Solution:
    # Time Complexity:
    #   Best case: O(2^n) - backtracking to generate all subsets
    #   Average case: O(2^n)
    #   Worst case: O(2^n)
    # Space Complexity: O(n)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subsets = []

        def dfs(i):

            if i >= len(nums):
                res.append(subsets.copy())
                return
            
            # subset incluidng itself
            subsets.append(nums[i])
            dfs(i + 1)

            # subset of []
            subsets.pop()
            dfs(i + 1)

        dfs(0)
        return res
    
class Solution:
    # Time Complexity:
    #   Best case: O(2^n) - backtracking to generate all subsets
    #   Average case: O(2^n)
    #   Worst case: O(2^n)
    # Space Complexity: O(n)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i+1, path+[nums[i]], res)
