import copy #LOL WHAT

sum_dict = dict()

def best_sum(targetSum, numbers):
    if (targetSum in sum_dict): return sum_dict[targetSum]
    if (targetSum == 0): return []
    if (targetSum < 0): return None
    
    shortest_combo = None
    
    for number in numbers:
        remainder = targetSum - number
        if (remainder_combination := best_sum(remainder, numbers)) != None:
            remainder_combination_copy = copy.deepcopy(remainder_combination)
            remainder_combination_copy.append(number) 
            combination = remainder_combination_copy
            # check combination is shorter than the current shortest
            if (shortest_combo == None or len(combination) < len(shortest_combo)):
                shortest_combo = combination
            
            
    sum_dict[targetSum] = shortest_combo
    return shortest_combo


# m = target sum
# n = len(numbers)
# Brute Force
# time: O(n^m * m) --> n^m means tree nodes per child
# space: O(m^2)

# Memoized
# time: O(n * m^2)
# space: O(m*m)

print(best_sum(7, [5, 3, 4, 7]))
print(best_sum(8, [2, 3, 5]))
print(best_sum(8, [1, 4, 5]))
print(best_sum(100, [1, 2, 5, 25]))
