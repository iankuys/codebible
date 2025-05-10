# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Example 1:
# Input: s = "()"
# Output: true
# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        
        bracket_rule = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        stack = []

        for bracket in s:
            if bracket in bracket_rule.keys():
                stack.append(bracket)
            elif bracket in bracket_rule.values():
                if stack:
                    init_bracket = stack.pop()
                    if bracket_rule[init_bracket] != bracket:
                        return False
                else:
                    return False

        if not stack:
            return True
        return False
    
class Solution:
    def isValid(self, s: str) -> bool:
        openbrack = []
        parantheses = {'(': ')', '{': '}', '[': ']'}

        for char in s:
            if char in parantheses:
                openbrack.append(char)
            elif char in parantheses.values():
                # handles close brackets
                if not openbrack:
                    return False
                else:
                    last_bracket = openbrack.pop()
                    if parantheses[last_bracket] != char:
                        return False
        
        # if there are still open brackets return false
        if openbrack: return False

        return True

