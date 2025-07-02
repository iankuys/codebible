"""
206. Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        cur = head

        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        return prev

# recursive
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if (not head) or (not head.next):
            # return the last node
            return head
        
        p = self.reverseList(head.next)
        
        # After backtracking, head.next is the next node, head.next.next is which node the child is pointing to
        # since we are trying to reverse the linkedlist
        # we want our child to point back to us or the current node.
        # so from 5 -> 1 -> None, we change it to 1 -> 5 -> None
        head.next.next = head
        head.next = None
        return p