"""
22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        
        # we generate as many open parantheses first then
        # we backtrack and add close parentheses
        def dfs(s, open_b, close_b):
            if len(s) == n * 2:
                res.append(s)
                return
            
            # if we can still add an open parenthesis
            if open_b:
                dfs(s + "(", open_b - 1, close_b)
            # if we can still add a close parenthesis
            if close_b > open_b:
                dfs(s + ")", open_b, close_b - 1)

        dfs("", n, n)
        return res
