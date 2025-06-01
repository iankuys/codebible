# LeetCode Problem 513: https://leetcode.com/problems/
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
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        
        for node in queue:
            if node.right:
                queue += [node.right]
            if node.left:
                queue += [node.left]
            
        return node.val