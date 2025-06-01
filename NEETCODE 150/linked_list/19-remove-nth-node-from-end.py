# LeetCode Problem 19: https://leetcode.com/problems/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        newHead = ListNode(0)
        newHead.next = self.reverseLinkedList(head)
        dummy = newHead
        count = 0
        
        while newHead:
            if count == n:
                if count == 1 and head.next is None:
                    newHead.next = None
                    return newHead.next
                elif count == 1:
                    dummy.next = newHead.next
                    break
                else:
                    oldHead.next = newHead.next
            oldHead = newHead
            count+=1
            newHead = newHead.next
        
        return self.reverseLinkedList(dummy.next)
            
        
    def reverseLinkedList(self, head):
        dummy = ListNode()
        tail = dummy
        
        while head:
            if not tail:
                tail.next = head
                head = head.next
            else:
                dum2 = ListNode(head.val, tail.next)
                tail.next = dum2
                head = head.next
        
        return dummy.next