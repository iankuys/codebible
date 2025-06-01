# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
# Link: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Return the number of good nodes in the binary tree.
# Example 1:
# Input: root = [3,1,4,3,null,1,5]
# Output: 4
# Explanation: Nodes in blue are good.
# Root Node (3) is always a good node.
# Node 4 -> (3,4) is the maximum value in the path starting from the root.
# Node 5 -> (3,4,5) is the maximum value in the path
# Node 3 -> (3,1,3) is the maximum value in the path.


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
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, value):
            count = 0

            if root:
            
                if root.val >= value:
                    count += 1

                count += dfs(root.left, max(value, root.val))
                count += dfs(root.right, max(value, root.val))

            return count

        return dfs(root, root.val)
                
            
