class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # this finds out how many rotations we actually need
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]