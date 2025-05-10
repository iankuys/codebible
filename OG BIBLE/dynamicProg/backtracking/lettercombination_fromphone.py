# use dictionary structure to store the available letters of each number
# using backtracking recursion to get the combination of letters of every digit starting from the first digit
# iterate through all the letters for digit in dictionary and when the length of the combination and the digits are the same, we will append it into our result

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_letters = {
            "1": [],
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z']
        }
         
        def backtracking(digits, number_index, combination):
            if len(digits) == 0:
                return
            if len(combination) == len(digits):
                result.append(combination)
                return
            current_digit = digits[number_index]
            for letter in digit_to_letters[current_digit]:
                backtracking(digits, number_index + 1, combination + letter)
        
        result = []
        combination = ""  
        backtracking(digits, 0, combination) 
        return result
            