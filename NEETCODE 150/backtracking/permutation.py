class Solution:
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
