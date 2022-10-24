class Solution:
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