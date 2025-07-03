"""
110. Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true
"""

# Given a binary tree, determine if it is 
# Link: https://leetcode.com/problems/balanced-binary-tree/
# height-balanced.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# much more intuitive solution (solved by myself)
class Solution:
    # Time Complexity:
    #   Best case: O(n) - tree traversal where h is height
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(h)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        def recurse(cur):

            if not cur:
                return 0 

            left = recurse(cur.left)
            right = recurse(cur.right)

            self.res = self.res and abs(left - right) <= 1

            return 1 + max(left, right)

        recurse(root)
        return self.res
    
class Solution:
    # Time Complexity:
    #   Best case: O(n) - tree traversal where h is height
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(h)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(root):
            if not root:
                return 0
            
            left_height, right_height = height(root.left), height(root.right)

            if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1:
                return -1
            
            return 1 + max(left_height, right_height)
        
        if (height(root) >= 0):
            return True

        return False