

# working but very inefficient
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        cache = {}
        res = []

        def dfs(i, cur):
            if sum(cur) == target:
                if cur not in res:
                    res.append(cur.copy())
                return
            if tuple(cur) in cache:
                return
            if sum(cur) > target:
                return
            if i >= len(candidates):
                return

            cur.append(candidates[i])
            # either we take the next val
            dfs(i + 1, cur)

            cur.pop()
            # we dont take next val
            dfs(i + 1, cur)

            if tuple(cur) not in cache:
                cache[tuple(cur)] = cur

            return

        dfs(0, [])
        return res