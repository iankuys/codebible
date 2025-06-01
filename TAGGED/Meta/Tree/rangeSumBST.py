# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# this uses properties of bst (mine)
# Time Complexity:
#   Best case: O(log n) - when range is very small or outside tree bounds, minimal traversal
#   Average case: O(k + log n) - where k is nodes in range, log n for navigation
#   Worst case: O(n) - when range covers entire tree (e.g., low=1, high=infinity)
# Space: O(h) where h is height of tree (recursion stack)
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.res = 0
        def recurse(cur):
            if not cur:
                return
            if cur.val < low:
                recurse(cur.right)
            elif cur.val > high:
                recurse(cur.left)
            else:  # low <= cur.val <= high
                self.res += cur.val
                recurse(cur.left)
                recurse(cur.right)

        recurse(root)
        return self.res

# this brute forces all nodes to check if it can find the value within range 
# Time Complexity:
#   Best case: O(n) - must visit every node regardless
#   Average case: O(n) - must visit every node regardless  
#   Worst case: O(n) - must visit every node regardless
# Space: O(h) where h is height of tree (recursion stack)
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.res = 0
        def recurse(cur):
            if not cur:
                return
            if low <= cur.val <= high:
                self.res += cur.val
            recurse(cur.left)
            recurse(cur.right)

        recurse(root)
        return self.res