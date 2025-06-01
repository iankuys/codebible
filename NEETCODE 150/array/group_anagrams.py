# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

class Solution:
    # Time Complexity:
    #   Best case: O(n) - linear scan
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(1)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_dict = defaultdict(list)

        for str in strs:
            sorted_str = ''.join(sorted(str))
            anagram_dict[sorted_str].append(str)

        return list(anagram_dict.values())

class Solution:
    # Time Complexity:
    #   Best case: O(n) - linear scan
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(1)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        output = []

        for i, s in enumerate(strs):
            sorted_s = "".join(sorted(s))
            if sorted_s in hashMap:
                hashMap[sorted_s].append(s)
                continue
            hashMap[sorted_s] = [s]

        for key, value in hashMap.items():
            output.append(value)

        return output