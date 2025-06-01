# Link: https://leetcode.com/problems/sum-root-to-leaf-numbers/
# 129. Sum Root to Leaf Numbers
# You are given the root of a binary tree containing digits from 0 to 9 only.
# Each root-to-leaf path in the tree represents a number.
# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

# A leaf node is a node with no children.

# Example 1:
# Input: root = [1,2,3]
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sum_str = ""
        sum_arr = []

        self.dfs(root, sum_str, sum_arr)
        return sum(sum_arr)  # Sum the values in the array to get the total sum

    def dfs(self, root, sum_str, sum_arr):
        if root is None:
            return
        elif not root.left and not root.right:
            sum_str += str(root.val)
            sum_arr.append(int(sum_str))
        else:
            sum_str += str(root.val)
            sum_str_copy = sum_str[::]
            self.dfs(root.left, sum_str, sum_arr)
            self.dfs(root.right, sum_str_copy, sum_arr)