fib_dict = {}

#The dict is for memoization 
def fib(n):
    if (n <= 2): return 1
    if (n not in fib_dict):
        fib_dict[n] = fib(n-1) + fib(n-2)
    return fib_dict[n]

print(fib(50))
