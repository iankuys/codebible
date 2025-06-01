# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# We will rely upon the invariant of the BST to solve the exercise. 

# works for both BST and BT
class Solution:
    # Time Complexity:
    #   Best case: O(n) - tree traversal where h is height
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(h)
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.ans = None

        def recurse(cur):
            if not cur:
                return False

            left = recurse(cur.left)
            right = recurse(cur.right)
            mid = cur.val == p.val or cur.val == q.val

            if left + right + mid >= 2:
                self.ans = cur
            
            return mid or left or right
        
        recurse(root)
        return self.ans
    
# using BST property
class Solution:
    # Time Complexity:
    #   Best case: O(n) - tree traversal where h is height
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(h)
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def recurse(cur):
            if not cur:
                return None
            if p.val > cur.val and q.val > cur.val:
                return recurse(cur.right)
            elif p.val < cur.val and q.val < cur.val:
                return recurse(cur.left)
            else:
                return cur

        return recurse(root)

class Solution:
    # Time Complexity:
    #   Best case: O(n) - tree traversal where h is height
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(h)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        while True:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root