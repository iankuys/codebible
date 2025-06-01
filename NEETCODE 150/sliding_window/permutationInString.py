# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
# https://leetcode.com/problems/permutation-in-string/solutions/1761953/python3-sliding-window-optimized-explained/

# my own O(N^2)
class Solution:
    # Time Complexity:
    #   Best case: O(n log n) - built-in sorting
    #   Average case: O(n log n)
    #   Worst case: O(n log n)
    # Space Complexity: O(n)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # window size will be size of s1
        sorted_s1 = sorted(s1)

        for i in range(len(s2) - len(s1) + 1):
            substr = sorted(s2[i:i+len(s1)])
            if (substr == sorted_s1):
                return True

        return False

# optimized (read and uinderstand pls)
# Optimized:
# We can use an auxiliary variable to count a number of characters whose frequency gets to zero during window sliding. That helps us to avoid iterating over the hashmap for every cycle tick to check whether frequencies turned into zero.
def checkInclusion(self, s1: str, s2: str) -> bool:
	cntr, w, match = Counter(s1), len(s1), 0     

	for i in range(len(s2)):
		if s2[i] in cntr:
			if not cntr[s2[i]]: match -= 1
			cntr[s2[i]] -= 1
			if not cntr[s2[i]]: match += 1

		if i >= w and s2[i-w] in cntr:
			if not cntr[s2[i-w]]: match -= 1
			cntr[s2[i-w]] += 1
			if not cntr[s2[i-w]]: match += 1

		if match == len(cntr):
			return True

	return False

            
from collections import Counter

# chatgpt solution easy to follow with counter class and just compare the dictionary
class Solution:
    # Time Complexity:
    #   Best case: O(n log n) - built-in sorting
    #   Average case: O(n log n)
    #   Worst case: O(n log n)
    # Space Complexity: O(n)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = Counter(s1)
        window_count = Counter(s2[:len(s1)])

        if s1_count == window_count:
            return True

        for i in range(len(s1), len(s2)):
            window_count[s2[i]] += 1
            window_count[s2[i - len(s1)]] -= 1

            if window_count[s2[i - len(s1)]] == 0:
                del window_count[s2[i - len(s1)]]

            if s1_count == window_count:
                return True

        return False

