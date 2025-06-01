# Link: https://leetcode.com/problems/30-99-60-5-10/
from typing import List

"""
5 30 99 60 5 10
114

becuase ian picks from the 1st(5), 3rd(99) and 6th(10) jars
"""
def pick_chocolates(jars: List[int], i: int) -> int:
    if i >= len(jars):
        return 0
    
    pick_i = jars[i] + pick_chocolates(jars, i+2)
    skip_i = pick_chocolates(jars, i+1)
    
    return max(pick_i, skip_i)

print(pick_chocolates([5,30,99,60,5,10],0))
print(pick_chocolates([1,7,3,91,12,66,54,60],0))