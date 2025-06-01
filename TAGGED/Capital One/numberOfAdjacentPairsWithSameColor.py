# Link: https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/
"""
2672. Number of Adjacent Elements With the Same Color
You are given an integer n representing an array colors of length n where all elements are set to 0's meaning uncolored. You are also given a 2D integer array queries where queries[i] = [indexi, colori]. For the ith query:

Set colors[indexi] to colori.
Count the number of adjacent pairs in colors which have the same color (regardless of colori).
Return an array answer of the same length as queries where answer[i] is the answer to the ith query.

 

Example 1:

Input: n = 4, queries = [[0,2],[1,2],[3,1],[1,1],[2,1]]

Output: [0,1,1,0,2]

Explanation:

Initially array colors = [0,0,0,0], where 0 denotes uncolored elements of the array.
After the 1st query colors = [2,0,0,0]. The count of adjacent pairs with the same color is 0.
After the 2nd query colors = [2,2,0,0]. The count of adjacent pairs with the same color is 1.
After the 3rd query colors = [2,2,0,1]. The count of adjacent pairs with the same color is 1.
After the 4th query colors = [2,1,0,1]. The count of adjacent pairs with the same color is 0.
After the 5th query colors = [2,1,1,1]. The count of adjacent pairs with the same color is 2.
"""

class Solution:
    # Time Complexity:
    #   Best case: O(n) - linear scan
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(1)
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        colors = [0] * n
        res = []
        count = 0

        for pos, color in queries:
            if colors[pos] != 0:
                if pos > 0 and colors[pos - 1] == colors[pos]:
                    count -= 1

                if pos < n - 1 and colors[pos + 1] == colors[pos]:
                    count -= 1

            colors[pos] = color

            if colors[pos] != 0:
                if pos > 0 and colors[pos - 1] == colors[pos]:
                    count += 1

                if pos < n - 1 and colors[pos + 1] == colors[pos]:
                    count += 1

            res.append(count)

        return res
