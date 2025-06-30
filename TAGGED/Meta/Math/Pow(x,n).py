"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return self.binaryExp(x, n)
        
    def binaryExp(self, x, n):
        if n == 0:
            return 1

        # Handle case where, n < 0
        if n < 0:
            return 1.0 / self.binaryExp(x, -1 * n)

        # Perform Binary Exponentation
        # If 'n' is odd we performa Binary Exponentation on 'n - 1' and multiply
        # result with 'x'

        if n % 2 == 1:
            return x * self.binaryExp(x * x, (n - 1) // 2)
        # Otherwise we calculate result by performing Binary Exponentation on 'n'
        else:
            return self.binaryExp(x * x, n // 2)