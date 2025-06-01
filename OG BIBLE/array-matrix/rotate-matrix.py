class Solution:
# Link: https://leetcode.com/problems/rotate-image/
    # Time Complexity:
    #   Best case: O(n) - linear operation
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(1)
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # this finds out how many rotations we actually need
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]