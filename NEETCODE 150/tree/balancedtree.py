# Given a binary tree, determine if it is 
# height-balanced.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
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