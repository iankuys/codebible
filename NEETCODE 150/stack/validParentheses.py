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