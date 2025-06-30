"""
227. Basic Calculator II
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.
You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:
Input: s = "3+2*2"
Output: 7

Example 2:
Input: s = " 3/2 "
Output: 1

Example 3:
Input: s = " 3+5 / 2 "
Output: 5
"""

class Solution:
    def calculate(self, s: str) -> int:
        s = "".join(s.split())
        stack = []
        num = 0
        sign = '+'
        i = 0

        while i < len(s):
            c = s[i]
            if c.isdigit():
                num = num * 10 + int(c)
            # Check if the character is an operator or if we are at the end of the string
            if c in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    prev = stack.pop()
                    # Python division truncates toward negative infinity for ints, so we fix that:
                    stack.append(int(prev / num))
                sign = c
                num = 0
            i += 1

        return sum(stack)
