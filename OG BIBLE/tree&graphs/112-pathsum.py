# LeetCode Problem 112: https://leetcode.com/problems/
class Solution:
    # Time Complexity:
    #   Best case: O(n) - tree traversal where h is height
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(h)
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        return self.dfs(root, targetSum)
    
    def dfs(self, root, target):
        
        # BASE CASES
        if not root:
            return False
       
        # BASE CASES
        if (root.left is None and root.right is None) and target == root.val:
            return True
            
        if root:
        
            return self.dfs(root.left, target-root.val) or self.dfs(root.right, target-root.val)