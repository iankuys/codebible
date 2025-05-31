"""
670. Maximum Swap
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

 

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.
"""

"""
Backwards, find the max, if the current value less than max, it will be our candidate. If the current value bigger than max, we update max. 
If the current val equals to max, do nothing, because switch a number to the last occurance of max will maximize the results, since that number is less than max. 
If later another number less than max, we update our candidate, because switch at the front will give bigger result. Done!
"""
class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = [int(x) for x in str(num)]
        max_idx = len(num) - 1
        xi = yi = 0
        for i in range(len(num) - 1, -1, -1):
            if num[i] > num[max_idx]:
                max_idx = i
            elif num[i] < num[max_idx]:
                xi = i
                yi = max_idx
        num[xi], num[yi] = num[yi], num[xi]
        return int(''.join([str(x) for x in num]))