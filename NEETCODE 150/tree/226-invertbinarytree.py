# LeetCode Problem 226: https://leetcode.com/problems/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time Complexity:
    #   Best case: O(n) - tree traversal where h is height
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(h)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #base case
        if not root:
            return
        
        temp = root.right
        root.right = root.left
        root.left = temp
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
    
class Solution:
    # Time Complexity:
    #   Best case: O(n) - tree traversal where h is height
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(h)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root:
            temp = root.left
            root.left = root.right
            root.right = temp

            self.invertTree(root.left)
            self.invertTree(root.right)  

        return root    

