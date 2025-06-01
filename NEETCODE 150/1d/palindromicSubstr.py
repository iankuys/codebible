# Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.

# Example 1:
# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".

# Example 2:

# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

class Solution:    
    # Time Complexity:
    #   Best case: O(n) - linear scan
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(1)
    def expandAndCountPallindromes(self, i, j, s):
        '''Counts the number of pallindrome substrings from a given center i,j        
        1. when i=j, it's an odd-lengthed pallindrome string. 
            eg: for string "aba", i=j=1.
        2. when i+1=j, it's an even-lengthed pallindrome string. 
            eg: for string "abba", i=1, j=2.
        
        Parameters:
            i,j - centers from which the code will expand to find number of pallindrome substrings.
            s - the string in which the code needs to find the pallindrome substrings. 
        
        Returns:
            cnt - The number of pallindrome substrings from the given center i,j       
        '''
        
        length=len(s)
        cnt=0
        
        while 0<=i and j<length and s[i]==s[j]:
            i-=1
            j+=1
            cnt+=1
        
        return cnt
        
    def countSubstrings(self, s: str) -> int:
        
        return sum(self.expandAndCountPallindromes(i,i,s) + self.expandAndCountPallindromes(i,i+1,s) for i in range(len(s)))
        