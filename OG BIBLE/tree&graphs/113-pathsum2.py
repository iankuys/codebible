# 113. Path Sum II
#Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        list = []
        result = []
        self.dfs(root, targetSum, list, result)
        return result
            
    def dfs(self, root, target, ls, res):
        
        if root:
            if not root.left and not root.right and target == root.val:
                ls.append(root.val)
                res.append(ls)
            self.dfs(root.left, target-root.val, ls+[root.val], res)
            self.dfs(root.right, target-root.val, ls+[root.val], res)