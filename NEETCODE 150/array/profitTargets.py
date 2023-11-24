#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'stockPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY stocksProfit
#  2. LONG_INTEGER target
#

def stockPairs(stocksProfit, target):
    # Write your code here
    seen_profits = set()
    pairs = set()
    count = 0
    
    for profit in stocksProfit:
        complement = target - profit
        
        seen_tuple = (profit, complement) if profit < complement else (complement, profit)
        if complement in seen_profits and seen_tuple not in pairs:
            pairs.add(seen_tuple)
            count += 1
                
        seen_profits.add(profit)
        
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    stocksProfit_count = int(input().strip())

    stocksProfit = []

    for _ in range(stocksProfit_count):
        stocksProfit_item = int(input().strip())
        stocksProfit.append(stocksProfit_item)

    target = int(input().strip())

    result = stockPairs(stocksProfit, target)

    fptr.write(str(result) + '\n')

    fptr.close()
