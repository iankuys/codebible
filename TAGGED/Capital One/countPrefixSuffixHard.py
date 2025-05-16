"""
3045. Count Prefix and Suffix Pairs II
You are given a 0-indexed string array words.

Let's define a boolean function isPrefixAndSuffix that takes two strings, str1 and str2:

isPrefixAndSuffix(str1, str2) returns true if str1 is both a prefix and a suffix of str2, and false otherwise.
For example, isPrefixAndSuffix("aba", "ababa") is true because "aba" is a prefix of "ababa" and also a suffix, but isPrefixAndSuffix("abc", "abcd") is false.

Return an integer denoting the number of index pairs (i, j) such that i < j, and isPrefixAndSuffix(words[i], words[j]) is true.

Example 1:

Input: words = ["a","aba","ababa","aa"]
Output: 4
Explanation: In this example, the counted index pairs are:
i = 0 and j = 1 because isPrefixAndSuffix("a", "aba") is true.
i = 0 and j = 2 because isPrefixAndSuffix("a", "ababa") is true.
i = 0 and j = 3 because isPrefixAndSuffix("a", "aa") is true.
i = 1 and j = 2 because isPrefixAndSuffix("aba", "ababa") is true.
Therefore, the answer is 4.
"""
# korean chicls solution
class Trie:
    def __init__(self):
        self.root = {}
        
    def insert(self, w, reverse=False):
        cur = self.root
        indices = set()
        for c in w:
            if c in cur:
                cur = cur[c]
            else:
                cur[c] = {}
                cur = cur[c]
            if 'end' in cur:
                indices.add(cur['end'])
        # tracking the end of word
        cur['end'] = w[::-1] if reverse else w
        return indices

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        pref = Trie()
        suf = Trie()
        ct = defaultdict(int)
        res = 0
        for w in words:
            # Insert w in prefix trie and get matching previous words
            indices1 = pref.insert(w)
            rw = w[::-1]

            # Insert reversed w in suffix trie and get matching previous words
            indices2 = suf.insert(rw, True)
            print(indices1, indices2)

            # len(indices1) and len(indices2) are bounded by len(w)
            for j in indices1:
                if j in indices2:
                    res += ct[j]
            ct[w] += 1
        return res

# traditional trie implementation not as efficient
from typing import List
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, reverse=False):
        node = self.root
        prefix = ""
        seen = set()

        for c in word:
            prefix += c
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            if node.endOfWord:
                seen.add(prefix[::-1]) if reverse else seen.add(prefix) # remember this is prefix suffix not palindrome
        
        node.endOfWord = True
        return seen

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        prefixTrie = Trie()
        suffixTrie = Trie()
        countMap = defaultdict(int)
        count = 0

        for word in words:
            prefixMatches = prefixTrie.insert(word)
            suffixMatches = suffixTrie.insert(word[::-1], reverse=True)

            for w in prefixMatches:
                if w in suffixMatches:
                    count += countMap[w]

            countMap[word] += 1

        return count
