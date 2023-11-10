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

# Better solution
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cntr, w = Counter(s1), len(s1)   

        for i in range(len(s2)):
            if s2[i] in cntr: 
                cntr[s2[i]] -= 1
            # this part resets the passed searched chars in dict to what it was
            if i >= w and s2[i-w] in cntr: 
                cntr[s2[i-w]] += 1

            if all([cntr[i] == 0 for i in cntr]): # see optimized code below
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

# my own
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        size = len(s1)

        i = 0
        j = size

        if size == 2:
            if (s2.find(s1) >= 0) or (s2.find(s1[::-1]) >= 0):
                return True
            return False
    
        while (j <= len(s2)):
            
            substr = s2[i:j]

            if sorted(substr) == sorted(s1):
                return True
            
            i += 1
            j += 1

        return False
    