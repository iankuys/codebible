# LeetCode Problem 392: https://leetcode.com/problems/
str1 = "abc"
str2 = "ahbbgdc"

def test(s, t):
        index = 0
        
        for i in range(len(s)):
            
            try:
                
                if(t.index(s[i]) >= index and s.count(s[i]) <= 1 and t.count(s[i]) <= 1):
                    index = t.index(s[i])
                elif (t.index(s[i], index+1) >= index):
                    print(t.index(s[i], index+1))
                    print(f'from: {index}')
                    index = t.index(s[i], index+1)
                else:
                    return False
                
            except:
                return False
                
        return True

print(test(str1, str2))
