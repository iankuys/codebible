# Link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
# 116. Populating Next Right Pointers in Each Node

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        return self.bfs(root)
        
    def bfs(self, root):
        discovered = [root]
        multiplier = 0
        counter = 1
        node = discovered.pop(0)
        
        while node:
            if node.left:
                discovered.append(node.left)
            if node.right:
                discovered.append(node.right)
            
            if discovered:
                new_node = discovered.pop(0)
            else:
                break
                            
            if pow(2, multiplier) == counter:
                multiplier = multiplier + 1
                node.next = None
                counter = 1
            else:
                node.next = new_node
                counter = counter + 1  
            node = new_node
        
        return root