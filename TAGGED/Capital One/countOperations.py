# Link: https://leetcode.com/problems/count-operations-to-obtain-zero/
"""
2169. Count Operations to Obtain Zero
You are given two non-negative integers num1 and num2.

In one operation, if num1 >= num2, you must subtract num2 from num1, otherwise subtract num1 from num2.

For example, if num1 = 5 and num2 = 4, subtract num2 from num1, thus obtaining num1 = 1 and num2 = 4. However, if num1 = 4 and num2 = 5, after one operation, num1 = 4 and num2 = 1.
Return the number of operations required to make either num1 = 0 or num2 = 0.

Example 1:
Input: num1 = 2, num2 = 3
Output: 3
Explanation: 
- Operation 1: num1 = 2, num2 = 3. Since num1 < num2, we subtract num1 from num2 and get num1 = 2, num2 = 3 - 2 = 1.
- Operation 2: num1 = 2, num2 = 1. Since num1 > num2, we subtract num2 from num1.
- Operation 3: num1 = 1, num2 = 1. Since num1 == num2, we subtract num2 from num1.
Now num1 = 0 and num2 = 1. Since num1 == 0, we do not need to perform any further operations.
So the total number of operations required is 3.
"""

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0

        while (num1 and num2):

            if num1 > num2:
                num1 -= num2
            else:
                num2 -= num1
            count += 1

        return count
   
# Potential Question
from typing import List

def collect_sticks(sticks: List[int]) -> List[int]:
    n = len(sticks)
    pos = sticks.index(0)
    left = pos - 1
    right = pos + 1
    total = 0
    turn = 0  # 0 means right, 1 means left
    result = []

    while total < 100 and (left >= 0 or right < n):
        if turn % 2 == 0:  # right turn
            if right < n:
                total += sticks[right]
                result.append(right)
                right += 1
        else:  # left turn
            if left >= 0:
                total += sticks[left]
                result.append(left)
                left -= 1
        turn += 1

    return result
