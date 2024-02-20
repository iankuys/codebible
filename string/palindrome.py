
# function which return reverse of a string
 
def isPalindrome(s):
    return s == s[::-1]
 
 
# Driver code
s = "malayalam"
 
if ans := isPalindrome(s):
    print("Yes")
else:
    print("No")
