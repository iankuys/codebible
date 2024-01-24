# use dictionary structure to store the available letters of each number
# using backtracking recursion to get the combination of letters of every digit starting from the first digit
# iterate through all the letters for digit in dictionary and when the length of the combination and the digits are the same, we will append it into our result
# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

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
            
# # my own solution
# Approach
# Find all combinations via DFS and then store combinations of length equivalent to digits to an array.

# Complexity
# The code uses a depth-first search (DFS) algorithm to generate all possible combinations of letters for a given input of digits. For each digit, there are at most 4 possible letters (except for digits 7 and 9 which have 4 letters each). Therefore, the number of recursive calls in the DFS function is at most 4^n, where n is the length of the input digits. Each recursive call takes constant time to append a letter to the current combination and update the position. Hence, the overall time complexity is O(4^n).

# Time complexity: O(4 ^ n)
# The space complexity of the function is O(n), where n is the length of the input string digits. This is because the space used by the function is proportional to the recursion depth, which is at most n in this case.

# Space complexity: O(n)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        dc_map = { "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8":"tuv", "9": "wxyz"}
        res = []

        def dfs(s, cur, pos):
            if len(s) == len(digits):
                res.append(s)
                return
            if pos >= len(digits):
                return
            cur_digit = dc_map[digits[pos]]
            for i in range(len(cur_digit)):
                dfs(s + cur_digit[i], cur + [cur_digit[i]], pos + 1)
            return

        dfs("", [], 0)
        return res if len(digits) != 0 else []