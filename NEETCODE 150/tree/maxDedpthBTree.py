# Given the root of a binary tree, return its maximum depth.
# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

class Solution:
    # Time Complexity:
    #   Best case: O(n) - tree traversal where h is height
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(h)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, depth):

            if not root:
                return depth

            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))

        return dfs(root, 0)
    
class Solution:
    # Time Complexity:
    #   Best case: O(n) - tree traversal where h is height
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(h)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxim = 0
        depth = 0
        return self.dfs(root, depth, maxim)
    
    def dfs(self, root, depth, maxim):
        if root:
            maxim = max(self.dfs(root.left, depth+1, maxim), maxim)
            maxim = max(self.dfs(root.right, depth+1, maxim), maxim)
        # find max after the last leaf node (base case)
        else:
            maxim = max(maxim, depth)

        return maxim