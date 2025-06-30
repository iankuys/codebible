"""
41. First Missing Positive
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Example 2:
Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        contains_1 = False

        # Replace negative numbers, zeros,
        # and numbers larger than n with 1s.
        # After this nums contains only positive numbers.
        for i in range(n):
            # Check whether 1 is in the original array
            if nums[i] == 1:
                contains_1 = True
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        if not contains_1:
            return 1

        # Mark whether integers 1 to n are in nums
        # Use index as a hash key and negative sign as a presence detector.
        for i in range(n):
            value = abs(nums[i])
            # If you meet number a in the array - change the sign of a-th element.
            # Be careful with duplicates : do it only once.
            if value == n:
                nums[0] = -abs(nums[0])
            else:
                nums[value] = -abs(nums[value])

        # First positive in nums is smallest missing positive integer
        for i in range(1, n):
            if nums[i] > 0:
                return i

        # nums[0] stores whether n is in nums
        if nums[0] > 0:
            return n

        # If nums contained all elements 1 to n
        # the smallest missing positive number is n + 1
        return n + 1

# With my own comments
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        size = len(nums)
        contains_one = False

        # convert all irrelevant numbers to 1
        # irrelevant numbers include numbers bigger than the length of nums, or negative numbers
        for i in range(size):
            if nums[i] == 1:
                contains_one = True
            elif nums[i] > size or nums[i] <= 0:
                nums[i] = 1
        
        # if there are no ones, then the smaller positive number is 1
        if not contains_one:
            return 1

        # track if a number exists in the array by negating the value in the index
        for i in range(size):
            value = abs(nums[i])
            # if the value is same as size, since its impossible to have a index of size
            # we use the first element to determine whether it exists
            if value == size:
                nums[0] = -abs(nums[0])
            else:
                nums[value] = -abs(nums[value])

        # first number thats positive is
        for i in range(1, size):
            if nums[i] > 0:
                return i

        # since we couldnt find anything pos from 1 to size
        # we look in the first value to see if value of size n exists
        if nums[0] > 0:
            return size

        # if none applied, then the next smalles pos number is size + 1
        return size + 1