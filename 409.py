#longest palindrome

def longestPalindrome(self, s: str) -> int:
    
    odd = set()
    
    for i in s:
        if i not in odd:
            odd.add(i)
        else:
            odd.remove(i)
        
    return len(s)-len(odd)+1 if len(odd)>0 else len(s)