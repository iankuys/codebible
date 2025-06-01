# Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/
"""
1650. Lowest Common Ancestor of a Binary Tree III
Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

Each node will have a reference to its parent node. The definition for Node is below:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)."
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    # Time Complexity:
    #   Best case: O(n) - linear operation
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(1)
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p1 = p
        p2 = q

        # If the two pointers meet, they are at the lowest common ancestor.
        # If one pointer reaches the end, switch it to the parent of the other node.
        # This way, both pointers will traverse the same number of nodes.
        # Similar to the intersection of two linked lists.
        while (p1 != p2):
            p1 = p1.parent if p1.parent else q
            p2 = p2.parent if p2.parent else p

        return p1