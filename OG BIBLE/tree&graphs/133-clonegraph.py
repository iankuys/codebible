# LeetCode Problem 133: https://leetcode.com/problems/
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    # Time Complexity:
    #   Best case: O(n) - tree traversal where h is height
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(h)
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        dup = {node.val: Node(node.val, [])}
        queue = [node]
        
        while queue:
            cur = queue.pop(0)
            cur_clone = dup[cur.val]
            for j in cur.neighbors:
                if j.val not in dup:
                    dup[j.val] = Node(j.val, [])
                    queue.append(j)
                cur_clone.neighbors.append(dup[j.val])
            
        return dup[node.val]
            
                            