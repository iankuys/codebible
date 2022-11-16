# the proper way with hast set
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
