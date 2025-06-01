class Solution:
    # Time Complexity:
    #   Best case: O(n) - linear scan
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(1)
    def removeDuplicates(self, nums: List[int]) -> int:
        repeated = {}
        i = 0

        while i < len(nums):
            if nums[i] not in repeated:
                repeated[nums[i]] = 1
                i += 1
            elif nums[i] in repeated and repeated[nums[i]] < 2:
                repeated[nums[i]] += 1
                i += 1
            else:
                del nums[i]
        
        return len(nums)
        