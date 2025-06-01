# Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
"""
102. Binary Tree Level Order Traversal
Given a binary tree root, return the level order traversal of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree, from left to right.

Example 1:
Input: root = [1,2,3,4,5,6,7]

Output: [[1],[2,3],[4,5,6,7]]
"""

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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        queue = []
        queue.append(root)

        #bfs
        while queue:
            # the length of the new queue is the number of children of the last node
            qLen = len(queue)
            level = []

            for i in range(qLen):
                cur = queue.pop(0)
                if cur:
                    level.append(cur.val)
                    queue.append(cur.left)
                    queue.append(cur.right)
                
            if level:
                res.append(level)

        return res
        
            