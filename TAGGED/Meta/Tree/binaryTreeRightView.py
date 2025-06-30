"""
199. Binary Tree Right Side View
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example 1:

Input: root = [1,2,3,null,5,null,4]

Output: [1,3,4]

Explanation:
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# bfs similar to level order traversal, but only appending the last node of each layer
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return res

        queue = []
        queue.append(root)

        while queue:
            layer_len = len(queue)

            for i in range(layer_len):
                node = queue.pop(0)
                if i + 1 == layer_len:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return res

# dfs example that tracks the level of the tree with the length of rightside at every recursion
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # dfs
        if not root:
            return []

        rightSide = []

        def helper(cur, level):
            if level == len(rightSide):
                rightSide.append(cur.val)
            
            for node in [cur.right, cur.left]:
                if node:
                    helper(node, level + 1)

        helper(root, 0)
        return rightSide
