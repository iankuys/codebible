from multiprocessing import reduction


sum_dict = {}
 
def can_sum(targetSum, numbers):
    if (targetSum == 0): return True
    if (targetSum < 0): return False
    if (targetSum in sum_dict): return sum_dict[targetSum]
    
    for number in numbers:
        remainder = targetSum - number
        if (can_sum(remainder, numbers)):
            sum_dict[targetSum] = True
            return sum_dict[targetSum]
    
    sum_dict[targetSum] = False
    return False

print(can_sum(7, [2, 3]))
print(can_sum(7, [5, 3, 4, 7]))

#memoization example
print(can_sum(300, [7, 14]))