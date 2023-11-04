# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

# the proper way with hash set
class Solution:
    def isHappy(self, n: int) -> bool:
        
        def nextNum(n):
            sum = 0
            while n > 0:
                n, digit = divmod(n,10)
                sum += digit ** 2
            
            return sum

        cycle_set = set()
        
        while n != 1 and n not in cycle_set:
            cycle_set.add(n)
            n = nextNum(n)

        return n == 1


# recursion solution with lucky base case
class Solution:
    def isHappy(self, n: int) -> bool:
        sum = 0
        if n == 1:
            return True
        # why less than 5 LMAO
        if n < 5:
            return False
        for digit in str(n):
            sum += (int(digit)*int(digit))

        if sum == 1:
            return True
        
        return self.isHappy(sum)
