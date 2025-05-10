# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        sorted_nums = sorted(set(nums))

        i = 0
        j= 0
        max_len = 0

        while i < len(sorted_nums):
            if i + 1 < len(sorted_nums) and abs(sorted_nums[i + 1] - sorted_nums[i]) == 1:
                i += 1
            else:
                max_len  = max(max_len, i - j + 1)
                i += 1
                j = i

        return max_len
    
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        i = 0
        k = 0
        longest = 0

        sorted_nums = sorted(set(nums))
        if not nums:
            return 0

        for j in range(1, len(sorted_nums)):
            if sorted_nums[j] - sorted_nums[k] == 1:
                longest = max(longest, j - i + 1)
                k += 1
            else:
                i = j
                k = j
        
        if longest:
            return longest
        else:
            return 1
    
#faster soluton on leet code ig
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)

        for n in num_set:
            if (n-1) not in num_set:
                length = 1
                while (n+length) in num_set:
                    length += 1
                longest = max(longest, length)
        
        return longest

# i mean it works
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        sorted_unique_nums = sorted(unique_nums)
        sorted_unique_list = list(sorted_unique_nums)

        length_arr = []
        length = 1
        prev = None
        
        for i in range(len(sorted_unique_list)):
            if prev is not None:
                if sorted_unique_list[i] - prev == 1:
                    length += 1
                else:
                    length = 1
            length_arr.append(length)
            prev = sorted_unique_list[i]

        return max(length_arr) if length_arr else 0
