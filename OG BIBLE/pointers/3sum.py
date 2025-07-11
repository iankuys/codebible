"""
# Link: https://leetcode.com/problems/3sum/
3Sum
Solved 
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:

Input: nums = [0,1,1]

Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]

Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""

class Solution:
    # Time Complexity:
    #   Best case: O(n²) - sorting + two pointers nested loops
    #   Average case: O(n²)
    #   Worst case: O(n²)
    # Space Complexity: O(1)
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # sorted nums will look like [-4,-1,-1,0,1,2]
        sorted_nums = sorted(nums)
        i = 0
        res = []

        # similar to twosum? two pointers?

        # [-4,-1,-1,0,1,2]
        #  i  k      j
        # nums[i] = -(nums[j] + nums[k])
        while (i < len(sorted_nums) - 2):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                i += 1
                continue

            target = sorted_nums[i]
            j = len(sorted_nums) - 1
            k = i + 1

            while (k < j):
                if target == -(sorted_nums[j] + sorted_nums[k]):
                    res.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])

                    # Skip duplicates for k
                    while k < j and sorted_nums[k] == sorted_nums[k + 1]:
                        k += 1

                    # Skip duplicates for j
                    while k < j and sorted_nums[j] == sorted_nums[j - 1]:
                        j -= 1
                    k += 1
                    j -= 1
                elif target < -(sorted_nums[j] + sorted_nums[k]):
                    k += 1
                else:
                    j -= 1
            i += 1

        return res

class Solution:
    # Time Complexity:
    #   Best case: O(n²) - sorting + two pointers nested loops
    #   Average case: O(n²)
    #   Worst case: O(n²)
    # Space Complexity: O(1)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        i = 0
        res = []

        while i < len(sorted_nums) - 2:
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                i += 1
                continue

            j = len(sorted_nums) - 1
            k = i + 1

            while k < j:
                total = sorted_nums[i] + sorted_nums[k] + sorted_nums[j]

                if total == 0:
                    res.append([sorted_nums[i], sorted_nums[k], sorted_nums[j]])

                    while k < j and sorted_nums[k] == sorted_nums[k + 1]:
                        k += 1
                    while k < j and sorted_nums[j] == sorted_nums[j - 1]:
                        j -= 1

                    k += 1
                    j -= 1
                elif total < 0:
                    k += 1
                else:
                    j -= 1

            i += 1

        return res
