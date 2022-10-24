from operator import index
memo = {}

def canConstruct(target, word_bank):
    if target in memo: return memo[target]
    if (target == ''): return True
    
    for word in word_bank:
        try:
            index_value = target.index(word)
        except ValueError:
            index_value = -1
            
        if (index_value == 0):
            suffix = target[len(word): len(target)] #we are slicing the prefix from the string
            if (canConstruct(suffix, word_bank) == True):
                memo[target] = True
                return True
            
    memo[target] = False
    return False
    
print(canConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(canConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', 
                   ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee', 'eeeeeee']))