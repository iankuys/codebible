# LeetCode Problem 513: https://leetcode.com/problems/
# Definition for a binary tree node. (DOESNT WORK)
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
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        result = tuple()
        array = []
        if not root.left and not root.right:
            return root.val
        if not root.left:
            result = self.dfs(root.right, 0, True, array)
        else:
            result = self.dfs(root, 0, False, array)
        return result[1]
    
    def dfs(self, root, count, is_left, array):

        left = tuple()
        right = tuple()
        if not root.left and not root.right and is_left:
            print("done")
            return (count, root.val)
        
        if root.left:
            left = self.dfs(root.left, count+1, True, array)
            print(left)
            
        if root.right:
            right = self.dfs(root.right, count+1, False, array)
        
        if left and right:
            if left[0] > right[0]:
                return left
            return right
        elif left:
            return left
        elif right:
            return right
        else:
            return None