# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        return sorted_s == sorted_t