"""
Generate Parentheses
Solved 
You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.

Example 1:

Input: n = 1

Output: ["()"]
Example 2:

Input: n = 3

Output: ["((()))","(()())","(())()","()(())","()()()"]
You may return the answer in any order.
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        solutions = []
        target = n
        
        # i to track cur index
        # track number of open brackets with stack
        def recursion(s, i, n, c):
            # base case when stack is the size of 2*n
            if n == c == target:
                return solutions.append(s)
            if n < target:
                # we can either pop one and finish one bracket
                recursion(s + "(", i + 1, n + 1, c)
            if c < n:
                # or end early
                recursion(s + ")", i + 1, n, c + 1)
            
        recursion("", 0, 0, 0)
        return solutions