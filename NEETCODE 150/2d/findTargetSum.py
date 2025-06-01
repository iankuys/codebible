# You are given an integer array nums and an integer target.

# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.

# use brute force then caching.

class Solution:
    # Time Complexity:
    #   Best case: O(1) - hash table operations
    #   Average case: O(1)
    #   Worst case: O(n)
    # Space Complexity: O(1)
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo = {}

        def dfs(index, total, memo):
            if (index, total) in memo:
                return memo[(index, total)]
            if index == len(nums):
                if total == target:
                    return 1
                else:
                    return 0 
            
            num_ways = dfs(index + 1, total + nums[index], memo) + dfs(index + 1, total - nums[index], memo)

            memo[(index, total)] = num_ways

            return memo[(index, total)]
            
        return dfs(0,0, memo)