class Solution:
    # Time Complexity:
    #   Best case: O(n) - linear operation
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(1)
    def removeElement(self, nums: List[int], val: int) -> int:

        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
                i -= 1
            i += 1
            
        return len(nums)
