# Link: https://leetcode.com/problems/palindrome-partitioning/
# 131. Palindrome Partitioning
# Given a string s, partition s such that every 
# substring
#  of the partition is a 
# palindrome
# . Return all possible palindrome partitioning of s.

# Given a string s, partition s such that every 
# substring
#  of the partition is a 
# palindrome
# . Return all possible palindrome partitioning of s.
# Example 1:

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# fastest solution
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def detectPalindrome(s):
            if len(s) != 0 :
                return s == s[::-1]
            
            else: return False
        
        res = []
        cache = {}

        # literally same solution but different tree setup
        def backtrack(cur, pos):
            if pos >= len(s):
                res.append(cur.copy())
                return
            for i in range(pos, len(s)):
                if detectPalindrome(s[pos:i + 1]):
                    cur.append(s[pos: i + 1])
                    backtrack(cur, i + 1)
                    cur.pop()

        backtrack([], 0)
        return res

# fixed of original solution (86 % faster)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def detectPalindrome(s):
            if len(s) != 0 :
                return s == s[::-1]
            
            else: return False
        
        res = []
        cache = {}
        def backtrack(cur, pos):
            if len("".join(cur)) == len(s):    
                res.append(cur.copy())
                return
            if pos >= len(s):
                return
            for i in range(pos, len(s)):
                if detectPalindrome(s[pos:i + 1]):
                    cur.append(s[pos:i + 1])
                    backtrack(cur, i + 1)

                    cur.pop()

            return
        
        backtrack([], 0)
        return res
    
# passed 31/32 ran out of time
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def detectPalindrome(s):
            if len(s) != 0 :
                return s == s[::-1]
            
            else: return False
        
        res = []
        cache = {}
        def backtrack(cur, pos):
            if len("".join(cur)) == len(s):    
                res.append(cur.copy())
                cache[tuple(cur)] = True
                return
            if tuple(cur) in cache:
                return
            if pos >= len(s):
                return
            for i in range(pos, len(s)):
                if detectPalindrome(s[pos:i + 1]):
                    cur.append(s[pos:i + 1])
                    backtrack(cur, i + 1)

                    cur.pop()
                    # we do not need this line with the for loop
                    backtrack(cur, i + 1)

            return
        
        backtrack([], 0)
        return res