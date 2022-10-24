from operator import index
memo = {}

def countConstruct(target, word_bank):
    if target in memo: return memo[target]
    if target == '': return 1
    total_count = 0
    
    for word in word_bank:
        try:
            index_value = target.index(word)
        except ValueError:
            index_value = -1
            
        if (index_value == 0):
            suffix = target[len(word): len(target)] #we are slicing the prefix from the string
            num_ways = countConstruct(suffix, word_bank)
            if (num_ways > 0):
                total_count = total_count + num_ways

    memo[target]= total_count
    return total_count

print(countConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(countConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(countConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', 
                   ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee', 'eeeeeee']))