sum_dict = {}

def how_sum(targetSum, numbers):
    if targetSum == 0: return []
    if targetSum < 0: return None
    if targetSum in sum_dict: return sum_dict[targetSum]
    
    for number in numbers:
        remainder = targetSum - number
        result = how_sum(remainder, numbers)
        if (result != None):
            result.append(number)
            sum_dict[targetSum] = result
            return sum_dict[targetSum]

    sum_dict[targetSum] = None
    return None

# m = target sum
# n = len(numbers)
# Brute Force
# time: O(n^m * m)
# space: O(m)

# Memoized
# time: O(n * m^2)
# space: O(m*m)

print(how_sum(7, [2,3]))
print(how_sum(7, [5,3,4,7]))
sum_dict = {}
print(how_sum(7, [2,4]))
print(how_sum(8, [2,3,5]))
sum_dict = {}
#memoization example
print(how_sum(300, [7,14]))
