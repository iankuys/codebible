# Link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
#117. Populating Next Right Pointers in Each Node II

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        node = root
        while node:
            #reset our level linkedlist every level iterated
            cur = dummy = Node(0)
            while node:
                if node.left:
                    cur.next = node.left
                    cur = cur.next
                if node.right:
                    cur.next = node.right
                    cur = cur.next
                # this checks whether it has another node beside it on the same level
                node = node.next
            # this will move on to the next level
            node = dummy.next
                
        return root