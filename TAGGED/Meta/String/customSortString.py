"""
791. Custom Sort String
You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.
Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.
Return any permutation of s that satisfies this property.

Example 1:
Input: order = "cba", s = "abcd"
Output: "cbad"
Explanation: "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".

Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.
"""

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        freq = {}
        res = ""

        for c in enumerate(s):
            freq[c] = 1 + freq.get(c, 0)

        # Iterate through the order string and append characters from s in the order specified
        for c in order:
            if c in freq:
                while freq[c] > 0:
                    res += c
                    freq[c] -= 1
        
        # Append remaining characters that were not in the order string   
        for key, value in freq.items():
            while value > 0:
                res += key 
                value -= 1

        return res