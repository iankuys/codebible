# LeetCode Problem 100: https://leetcode.com/problems/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        array1 = []
        array2 = []
        self.dfs(p, array1)
        self.dfs(q, array2)
        
        return (array1 == array2)
        
    def dfs(self, root, array):
        if root:
            array.append(root.val)
            self.dfs(root.left, array)
            self.dfs(root.right, array)
        else:
            array.append(None)