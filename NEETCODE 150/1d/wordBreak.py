# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# Example 1:

# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:

# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.

# same as canConstruct

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        hmap = {} 
        def dfs(target):

            if target in hmap:
                return hmap[target]
            if target == "":
                return True
                
            for word in wordDict:

                try:
                    index_val = target.index(word)
                except ValueError:
                    index_val = -1

                if index_val == 0:
                    suffix = target[len(word):len(target)]
                    res = dfs(suffix)
                    if res:
                        hmap[target] = True
                        return hmap[target]

            hmap[target] = False
            return hmap[target]

        return dfs(s)