class Solution:
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
        