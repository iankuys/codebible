# LeetCode Problem 1: https://leetcode.com/problems/
# new hash map 

def solution(queryType, query):
    hashMap = {}
    sumArray = []
    
    for i in range(len(queryType)):
        
        if queryType[i] == "insert":
            key = query[i][0]
            value = query[i][1]
            
            if key not in hashMap:
                hashMap[key] = value    
                       
        elif queryType[i] == "addToKey":
            addition = int(query[i][0])
            newHashMap = {}
            for k, v in hashMap.items():
                old_key = k
                value = v
                newHashMap[old_key+addition] = value  
            hashMap = newHashMap 
            
        elif queryType[i] == "addToValue":
            addition = int(query[i][0])
            for k, v in hashMap.items():
                hashMap[k] = v + addition
                
        else:
            sumArray.append(hashMap[query[i][0]])
    
    return sum(sumArray)
    

