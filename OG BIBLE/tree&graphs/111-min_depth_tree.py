# LeetCode Problem 111: https://leetcode.com/problems/
# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.
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
    def minDepth(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            if not root:
                return 0

            depth = 0
            current_level = [root]

            while current_level:
                depth += 1
                next_level = []
                for node in current_level:
                    left = node.left
                    right = node.right
                    if not left and not right:
                        return depth
                    if left:
                        next_level.append(left)
                    if right:
                        next_level.append(right)
                current_level = next_level
            return depth


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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 1) if root else 0

    def dfs(self, root, depth):
        left = None
        right = None
        ans = None
        if root.right is None and root.left is None:
            return depth
        if root.left and not root.right:
            left = self.dfs(root.left, depth+1)
        if root.right and not root.left:
            right = self.dfs(root.right, depth+1)
        if root.left and root.right:
            ans = min(self.dfs(root.left, depth+1),self.dfs(root.right, depth+1))
        
        if not ans:
            if left and not right:
                return left
            elif right and not left:
                return right
            return min(left,right)
        else:
            return ans