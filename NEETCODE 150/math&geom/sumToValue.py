# Python3 program to find the smallest
# number whose sum of digits is also N
 
# Write a function, given integer n, that returns the smallest non-negative integer whose digits sum to n.

# Test Cases:
# Input: 16
# Output: 79
# Explanation: There are many numbers whose digits sum to 16 (i.e. 79, 97, 808, 5551, 22822), The smallest is 79.

# Input: 19
# Output: 199

# Input: 7
# Output: 7

# Constraints:
# 0 <= n <= 50

# Function to get sum of digits
def getSum(n):
 
    sum1 = 0
    while (n != 0):
        sum1 = sum1 + n % 10
        n = n // 10
     
    return sum1
 
# Function to find the smallest
# number whose sum of digits is also N
def smallestNumber(N):
 
    i = 1
    while (1):
        # Checking if number has
        # sum of digits = N
        if (getSum(i) == N):
            print(i)
            break
         
        i += 1
     
# Driver code
N = 10
smallestNumber(N)