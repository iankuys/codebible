# LeetCode Problem 205: https://leetcode.com/problems/
#  if one-to-one mapping is possible for every character of the first string to 
# every character of the second string. For example, consider the two strings: “ACAB” and “XCXY”
#isomorphic strings
def isIsomorphic(self, s: str, t: str) -> bool:
        
        dict1 = {}
        dict2 = {}
        
        for key in range(len(s)):
            if (s[key] in dict1 and dict1[s[key]] != t[key]) or (t[key] in dict2 and dict2[t[key]] != s[key]):
                return False
            elif (s[key] not in dict1) and (t[key] not in dict2):
                dict1[s[key]] = t[key] 
                dict2[t[key]] = s[key]
            else:
                print("do nothing")
                
        return True