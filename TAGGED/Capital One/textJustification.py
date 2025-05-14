"""
68. Text Justification
Solved
Hard
Topics
Companies
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
 

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
"""

from typing import List
import math

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        i = 0
        res = []

        while i < len(words):
            j = i
            line_length = 0
            
            # Step 1: Find how many words fit from i to j
            while j < len(words) and line_length + len(words[j]) + (j - i) <= maxWidth:
                line_length += len(words[j])
                j += 1

            num_words = j - i
            total_spaces = maxWidth - line_length
            line = ""

            # Step 2: If it's the last line or only one word — left justify
            if j == len(words) or num_words == 1:
                for k in range(i, j):
                    line += words[k]
                    if k < j - 1:
                        line += " "
                line += " " * (maxWidth - len(line))
            else:
                # Step 3: Full justify
                space_between_words, extra = divmod(total_spaces, num_words - 1)
                for k in range(i, j - 1):
                    line += words[k]
                    line += " " * (space_between_words + (1 if k - i < extra else 0))
                line += words[j - 1]  # last word, no space after

            res.append(line)
            i = j  # move to next group of words

        return res
